#!/usr/bin/env python3
"""E3 runner · journal record vs ordinary summary (RESEARCH ONLY).

Prereg: docs/E3_JOURNAL_RECORD_SUFFICIENCY_PREREG_2026_11_24.md

Two stages, run as separate, separately reviewed steps:

  episodes  Source episodes run once (prereg §3.2): the executor sees the owner's
            request and materials and fixes its completion decision and public
            answer. Family 4 decisions are scripted (prereg §3.1). Then one trial
            ordinary summary per episode, without a length limit, to calibrate the
            shared limit (prereg §3.4). Output: episodes.json with a proposed limit.
            The operator reviews it, sets the limit, and commits it as
            experiments/e3/frozen/episodes.json together with FROZEN fixtures.

  pilot     From the frozen episodes: authorial record and ordinary summary
            (same executor context, same limit, made after the decision), control
            record by an independent author on a fixed template (no access to
            continuations), plus the "no record" variant. Then successor answers:
            8 episodes × 4 variants × 3 continuations × repeats, each in a fresh
            context, condition-blind, in seeded random order.

Providers: deepseek (default), openrouter, mock (offline, no network, for tests).
The API key is read only at request time and is never printed or written.
Results are appended to JSONL as they arrive, so an interrupted run resumes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import re
import statistics
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent

PROVIDERS: dict[str, dict[str, str]] = {
    "deepseek": {
        "url": "https://api.deepseek.com/chat/completions",
        "key_env": "DEEPSEEK_API_KEY",
        "default_model": "deepseek-flash",
    },
    "openrouter": {
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "key_env": "OPENROUTER_API_KEY",
        "default_model": "deepseek/deepseek-chat",
    },
    "mock": {"url": "", "key_env": "", "default_model": "mock-1"},
}

VARIANTS = ["authorial", "summary", "control", "none"]
ROWS = ["row1", "row2", "row3"]
RETRY_STATUS = {429, 500, 502, 503, 504}
MAX_TRUNCATION_RETRIES = 2

KEY_PATTERNS = [
    re.compile(r"sk-or-[A-Za-z0-9_-]{8,}"),
    re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9]{16,}"),
]


# ---------------------------------------------------------------- utilities

def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _secrets() -> list[str]:
    return [v for v in (os.environ.get("DEEPSEEK_API_KEY"), os.environ.get("OPENROUTER_API_KEY")) if v]


def redact(text: str) -> str:
    out = str(text)
    for s in _secrets():
        out = out.replace(s, "[REDACTED]")
    for pat in KEY_PATTERNS:
        out = pat.sub("[REDACTED]", out)
    return out


def dump(obj: Any) -> str:
    return redact(json.dumps(obj, ensure_ascii=False, indent=2))


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump(obj) + "\n", encoding="utf-8")


def append_jsonl(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(redact(json.dumps(obj, ensure_ascii=False)) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text or ""))


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def parse_json_reply(text: str) -> dict | None:
    """Lenient: accepts a bare object or one wrapped in a ``` fence."""
    if not text:
        return None
    t = text.strip()
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", t, re.S)
    if m:
        t = m.group(1)
    else:
        start, end = t.find("{"), t.rfind("}")
        if start == -1 or end <= start:
            return None
        t = t[start : end + 1]
    try:
        obj = json.loads(t)
    except json.JSONDecodeError:
        return None
    return obj if isinstance(obj, dict) else None


# ---------------------------------------------------------------- client

class CallBudgetExceeded(RuntimeError):
    pass


class Client:
    def __init__(self, provider: str, model: str, max_calls: int, max_tokens: int, timeout_s: int):
        if provider not in PROVIDERS:
            raise SystemExit(f"unknown provider {provider!r}")
        self.provider = provider
        self.cfg = PROVIDERS[provider]
        self.model = model or self.cfg["default_model"]
        self.max_calls = max_calls
        self.max_tokens = max_tokens
        self.timeout_s = timeout_s
        self.calls = 0
        if provider != "mock" and not os.environ.get(self.cfg["key_env"]):
            raise SystemExit(f"{self.cfg['key_env']} is not set; refusing to start")

    def chat(self, messages: list[dict[str, str]], tag: str) -> dict[str, Any]:
        if self.calls >= self.max_calls:
            raise CallBudgetExceeded(f"call budget {self.max_calls} reached before {tag}")
        self.calls += 1
        if self.provider == "mock":
            return {"ok": True, "content": _mock_reply(messages, tag), "usage": {}, "model": self.model}
        payload = {"model": self.model, "messages": messages, "max_tokens": self.max_tokens, "stream": False}
        data = json.dumps(payload).encode("utf-8")
        last_err: dict[str, Any] = {}
        truncations = 0
        for attempt in range(6):
            req = urllib.request.Request(
                self.cfg["url"],
                data=data,
                method="POST",
                headers={
                    "Authorization": f"Bearer {os.environ[self.cfg['key_env']]}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
            )
            try:
                with urllib.request.urlopen(req, timeout=self.timeout_s) as resp:
                    body = json.loads(resp.read().decode("utf-8", errors="replace"))
            except urllib.error.HTTPError as exc:
                last_err = {"type": "HTTPError", "status": exc.code,
                            "body": redact(exc.read().decode("utf-8", errors="replace")[:2000])}
                if exc.code in RETRY_STATUS and attempt < 3:
                    time.sleep(2 ** (attempt + 1))
                    continue
                return {"ok": False, "error": last_err}
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                last_err = {"type": type(exc).__name__, "message": redact(str(exc))}
                if attempt < 3:
                    time.sleep(2 ** (attempt + 1))
                    continue
                return {"ok": False, "error": last_err}
            finally:
                req.headers = {}
            if isinstance(body, dict) and body.get("error"):
                return {"ok": False, "error": {"type": "ProviderError", "body": redact(json.dumps(body["error"], ensure_ascii=False)[:2000])}}
            choice = (body.get("choices") or [{}])[0] or {}
            if choice.get("finish_reason") == "length":
                # Output cut off (with thinking enabled, reasoning can use the whole budget).
                # A truncated answer is not data for this experiment: retry, counted in the call cap.
                truncations += 1
                if truncations <= MAX_TRUNCATION_RETRIES:
                    if self.calls >= self.max_calls:
                        raise CallBudgetExceeded(f"call budget {self.max_calls} reached retrying truncated {tag}")
                    self.calls += 1
                    continue
                return {"ok": False, "error": {"type": "Truncated", "message": "finish_reason=length after retries",
                                               "usage": body.get("usage") or {}}, "attempts": truncations}
            msg = choice.get("message") or {}
            content = msg.get("content")
            if isinstance(content, list):
                content = "".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in content)
            return {
                "ok": True,
                "content": content or "",
                "finish_reason": choice.get("finish_reason"),
                "attempts": truncations + 1,
                "usage": body.get("usage") or {},
                "model": body.get("model") or self.model,
                "id": body.get("id"),
            }
        return {"ok": False, "error": last_err}


def _mock_reply(messages: list[dict[str, str]], tag: str) -> str:
    """Deterministic offline replies shaped like real ones; content is meaningless."""
    h = int(sha(tag + messages[-1]["content"]), 16)
    last = messages[-1]["content"]
    if tag.startswith("executor"):
        return json.dumps({"decision": "complete", "public_answer": "Лабораторный обмен прошёл (mock)."}, ensure_ascii=False)
    if tag.startswith("successor"):
        labels = ["COMPLETE_WORK", "VERIFY_FURTHER", "ASK_OWNER", "DO_REQUESTED_STEP", "CONFIRM_ONLY", "CANNOT_DETERMINE"]
        reply = {
            "action": labels[h % len(labels)],
            "action_text": "ответ (mock)",
            "work_status": ["closed", "open", "unknown"][h % 3],
            "remaining": "",
            "past_claims": [{"claim": "лабораторный обмен прошёл", "source": ["record", "materials", "assumption"][h % 3]}],
        }
        text = json.dumps(reply, ensure_ascii=False)
        return f"```json\n{text}\n```" if h % 5 == 0 else text
    n = 40 + h % 60
    return " ".join(["слово"] * n) + (" (mock " + tag + ")" if "Шаблон" not in last else "")


# ---------------------------------------------------------------- fixtures

def load_fixtures(fixtures_dir: Path) -> tuple[dict, dict]:
    fam = json.loads((fixtures_dir / "families.json").read_text(encoding="utf-8"))
    prm = json.loads((fixtures_dir / "prompts.json").read_text(encoding="utf-8"))
    validate_fixtures(fam)
    return fam, prm


def validate_fixtures(fam: dict) -> None:
    labels = set(fam["action_labels"])
    assert set(fam["continuations"]) == set(ROWS), "continuations must be row1..row3"
    assert len(fam["families"]) == 4, "prereg: four families"
    for f in fam["families"]:
        assert set(f["stories"]) == {"A", "B"}, f"{f['id']}: two mirrored stories"
        exp = fam["expected"][f["id"]]
        for story in ("A", "B"):
            for row in ROWS:
                e = exp[story][row]
                assert e["correct"] and set(e["correct"]) <= labels, f"{f['id']}{story}{row}: bad labels"
                assert set(e["status"]) <= {"closed", "open", "unknown"}
        if f["agreement_kind"] == "executor_inference_unconfirmed":
            for story in ("A", "B"):
                assert "scripted_decision" in f["stories"][story], f"{f['id']}: family 4 needs scripted decisions"


def notes_block(prm: dict, f: dict, story: str) -> str:
    """Episode notes: shown to record authors only, never to the successor."""
    notes = f["stories"][story].get("episode_notes")
    return prm["episode_notes_block"].format(notes=notes) if notes else ""


def episodes_of(fam: dict) -> list[tuple[dict, str]]:
    return [(f, s) for f in fam["families"] for s in ("A", "B")]


def executor_messages(prm: dict, f: dict, story: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": prm["executor_system"]},
        {"role": "user", "content": prm["executor_task"].format(
            owner_request=f["stories"][story]["owner_request"], materials=f["materials"])},
    ]


# ---------------------------------------------------------------- stage: episodes

def failed_episode_ids(resume: dict) -> list[str]:
    return [e["episode_id"] for e in resume["episodes"]
            if e["decision"].get("decision") not in ("complete", "not_complete")]


def stage_episodes(client: Client, fam: dict, prm: dict, out: Path, resume: dict | None = None) -> int:
    episodes = []
    prev = {e["episode_id"]: e for e in resume["episodes"]} if resume else {}
    reran: list[str] = []
    for f, story in episodes_of(fam):
        eid = f"{f['id']}{story}"
        old = prev.get(eid)
        if old and old["decision"].get("decision") in ("complete", "not_complete"):
            episodes.append(old)  # decision stays fixed (prereg §3.2); not regenerated
            print(f"[{eid}] kept from earlier run: decision={old['decision']['decision']}")
            continue
        msgs = executor_messages(prm, f, story)
        scripted = f["stories"][story].get("scripted_decision")
        if scripted:
            decision_raw = json.dumps(scripted, ensure_ascii=False)
            decision, source, call_meta = scripted, "scripted", None
        else:
            r = client.chat(msgs, f"executor:{eid}")
            if not r["ok"]:
                print(f"[{eid}] executor call failed: {r['error']}", file=sys.stderr)
                return 1
            decision_raw = r["content"]
            decision = parse_json_reply(decision_raw)
            source, call_meta = "generated", {k: r.get(k) for k in ("model", "usage", "finish_reason", "id")}
            if not decision or decision.get("decision") not in ("complete", "not_complete"):
                print(f"[{eid}] executor reply is not the required JSON; stored as format_error", file=sys.stderr)
                decision = {"decision": "format_error", "public_answer": decision_raw}
        convo = msgs + [{"role": "assistant", "content": decision_raw}]
        cal = client.chat(convo + [{"role": "user", "content": prm["calibration_summary"].format(episode_notes_block=notes_block(prm, f, story))}], f"calibration:{eid}")
        if not cal["ok"]:
            print(f"[{eid}] calibration call failed: {cal['error']}", file=sys.stderr)
            return 1
        if old:
            reran.append(eid)
        episodes.append({
            "superseded": ({"decision": old["decision"], "calibration_summary": old["calibration_summary"],
                            "reason": "decision was format_error / truncated (infrastructure), regenerated"} if old else None),
            "episode_id": eid,
            "family": f["id"],
            "story": story,
            "decision_source": source,
            "decision": decision,
            "executor_conversation": convo,
            "executor_call": call_meta,
            "decided_at": now(),
            "calibration_summary": cal["content"],
            "calibration_words": word_count(cal["content"]),
        })
        print(f"[{eid}] decision={decision.get('decision')} calibration_words={episodes[-1]['calibration_words']}")
    words = [e["calibration_words"] for e in episodes]
    proposed = int(math.ceil(statistics.median(words) / 10.0) * 10)
    write_json(out / "episodes.json", {
        "kind": "e3_episodes",
        "fixture_version": fam["fixture_version"],
        "fixtures_sha": {"families": sha(json.dumps(fam, ensure_ascii=False, sort_keys=True)),
                         "prompts": sha(json.dumps(prm, ensure_ascii=False, sort_keys=True))},
        "provider": client.provider,
        "model": client.model,
        "created_at": now(),
        "calibration": {"words": words, "median": statistics.median(words),
                        "proposed_length_limit_words": proposed,
                        "rule": "медиана длины пробных сводок, округлённая вверх до десятка"},
        "reran_episodes": reran,
        "resumed_from_created_at": resume.get("created_at") if resume else None,
        "length_limit_words": None,
        "status": "UNREVIEWED",
        "episodes": episodes,
    })
    print(f"episodes.json written; proposed length limit = {proposed} words; calls used = {client.calls}")
    return 0


# ---------------------------------------------------------------- stage: pilot

def check_frozen(fam: dict, prm: dict, frozen: dict) -> int:
    problems = []
    if fam.get("status") != "FROZEN":
        problems.append("families.json status is not FROZEN")
    if prm.get("status") != "FROZEN":
        problems.append("prompts.json status is not FROZEN")
    if frozen.get("status") != "FROZEN":
        problems.append("frozen episodes status is not FROZEN")
    limit = frozen.get("length_limit_words")
    if not isinstance(limit, int) or limit <= 0:
        problems.append("frozen episodes have no length_limit_words")
    if frozen.get("fixtures_sha", {}).get("families") != sha(json.dumps(fam, ensure_ascii=False, sort_keys=True)) \
            or frozen.get("fixtures_sha", {}).get("prompts") != sha(json.dumps(prm, ensure_ascii=False, sort_keys=True)):
        problems.append("fixtures changed after the episodes stage (sha mismatch)")
    if {e["episode_id"] for e in frozen.get("episodes", [])} != {f"{f['id']}{s}" for f, s in episodes_of(fam)}:
        problems.append("frozen episodes do not cover all 8 episodes")
    for p in problems:
        print(f"pilot refused: {p}", file=sys.stderr)
    return 1 if problems else 0


def make_records(client: Client, fam: dict, prm: dict, frozen: dict, path: Path) -> dict[str, dict[str, str]] | None:
    limit = frozen["length_limit_words"]
    fams = {f["id"]: f for f in fam["families"]}
    done = {(r["episode_id"], r["variant"]): r for r in read_jsonl(path) if r.get("ok")}
    for ep in frozen["episodes"]:
        eid, f, story = ep["episode_id"], fams[ep["family"]], ep["story"]
        convo = ep["executor_conversation"]
        jobs = {
            "authorial": convo + [{"role": "user", "content": prm["record_authorial"].format(limit_words=limit, episode_notes_block=notes_block(prm, f, story))}],
            "summary": convo + [{"role": "user", "content": prm["record_summary"].format(limit_words=limit, episode_notes_block=notes_block(prm, f, story))}],
            "control": [
                {"role": "system", "content": prm["control_system"]},
                {"role": "user", "content": prm["control_task"].format(
                    limit_words=limit,
                    episode_notes_block=notes_block(prm, f, story),
                    owner_request=f["stories"][story]["owner_request"],
                    materials=f["materials"],
                    decision=ep["decision"].get("decision"),
                    public_answer=ep["decision"].get("public_answer", ""))},
            ],
        }
        for variant, msgs in jobs.items():
            if (eid, variant) in done:
                continue
            r = client.chat(msgs, f"record:{variant}:{eid}")
            rec = {"episode_id": eid, "variant": variant, "ok": r["ok"], "at": now()}
            if r["ok"]:
                rec.update(text=r["content"], words=word_count(r["content"]),
                           over_limit=word_count(r["content"]) > limit,
                           model=r.get("model"), usage=r.get("usage"), finish_reason=r.get("finish_reason"))
            else:
                rec["error"] = r["error"]
            append_jsonl(path, rec)
            if not r["ok"]:
                print(f"[{eid}/{variant}] record call failed: {r['error']}", file=sys.stderr)
                return None
            done[(eid, variant)] = rec
    records: dict[str, dict[str, str]] = {}
    for (eid, variant), rec in done.items():
        records.setdefault(eid, {})[variant] = rec["text"]
    return records


def successor_jobs(fam: dict, repeats: int, seed: int) -> list[dict]:
    jobs = [
        {"job_id": f"{f['id']}{s}-{v}-{row}-r{k}", "episode_id": f"{f['id']}{s}", "family": f["id"],
         "story": s, "variant": v, "row": row, "repeat": k}
        for f, s in episodes_of(fam) for v in VARIANTS for row in ROWS for k in range(1, repeats + 1)
    ]
    random.Random(seed).shuffle(jobs)
    for i, j in enumerate(jobs):
        j["order"] = i
    return jobs


def successor_messages(fam: dict, prm: dict, f: dict, record: str | None, row: str) -> list[dict[str, str]]:
    block = (prm["record_block_present"].format(record=record) if record is not None
             else prm["record_block_absent"])
    action_list = "\n".join(f"- {k}: {v}" for k, v in fam["action_labels"].items())
    return [
        {"role": "system", "content": prm["successor_system"]},
        {"role": "user", "content": prm["successor_task"].format(
            materials=f["materials"], record_block=block,
            message=fam["continuations"][row], action_list=action_list)},
    ]


def stage_pilot(client: Client, fam: dict, prm: dict, frozen: dict, repeats: int, out: Path) -> int:
    if check_frozen(fam, prm, frozen):
        return 1
    records = make_records(client, fam, prm, frozen, out / "records.jsonl")
    if records is None:
        return 1
    fams = {f["id"]: f for f in fam["families"]}
    path = out / "successor.jsonl"
    done = {r["job_id"] for r in read_jsonl(path)}
    jobs = successor_jobs(fam, repeats, fam["seed"])
    write_json(out / "plan.json", {"seed": fam["seed"], "repeats": repeats, "n_jobs": len(jobs), "jobs": jobs})
    failures = 0
    for job in jobs:
        if job["job_id"] in done:
            continue
        rec = None if job["variant"] == "none" else records[job["episode_id"]][job["variant"]]
        msgs = successor_messages(fam, prm, fams[job["family"]], rec, job["row"])
        r = client.chat(msgs, f"successor:{job['job_id']}")
        row = dict(job, at=now(), ok=r["ok"])
        if r["ok"]:
            parsed = parse_json_reply(r["content"])
            row.update(raw=r["content"], parsed=parsed, format_error=parsed is None,
                       model=r.get("model"), usage=r.get("usage"), finish_reason=r.get("finish_reason"))
        else:
            row["error"] = r["error"]
            failures += 1
        append_jsonl(path, row)
        print(f"[{job['order']:>3}] {job['job_id']} ok={r['ok']}")
    write_json(out / "run_meta.json", {
        "provider": client.provider, "model": client.model, "calls_this_session": client.calls,
        "repeats": repeats, "finished_at": now(), "failed_calls": failures,
        "fixture_version": fam["fixture_version"], "episodes_created_at": frozen.get("created_at"),
    })
    print(f"pilot finished; calls this session = {client.calls}; failed = {failures}")
    return 0 if failures == 0 else 2


# ---------------------------------------------------------------- main

def estimate_calls(fam: dict, stage: str, repeats: int) -> int:
    eps = episodes_of(fam)
    if stage == "episodes":
        generated = sum(1 for f, s in eps if "scripted_decision" not in f["stories"][s])
        return generated + len(eps)
    return 3 * len(eps) + len(eps) * len(VARIANTS) * len(ROWS) * repeats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", choices=["episodes", "pilot"], required=True)
    ap.add_argument("--provider", choices=sorted(PROVIDERS), default="deepseek")
    ap.add_argument("--model", default="")
    ap.add_argument("--fixtures", type=Path, default=HERE / "fixtures")
    ap.add_argument("--frozen", type=Path, default=HERE / "frozen" / "episodes.json")
    ap.add_argument("--repeats", type=int, default=2)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--max-tokens", type=int, default=16384,
                    help="with thinking enabled, 4096 let reasoning use the whole budget (F3 A, run 45424109785)")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--max-calls", type=int, default=0, help="hard cap; 0 = estimate + 10%%")
    ap.add_argument("--resume-episodes", type=Path, default=None,
                    help="episodes stage: keep valid decisions from this episodes.json, regenerate only failed ones")
    ap.add_argument("--allow-draft", action="store_true",
                    help="episodes stage only: allow DRAFT fixtures (pilot never allows it)")
    args = ap.parse_args(argv)

    fam, prm = load_fixtures(args.fixtures)
    if args.repeats < 1:
        raise SystemExit("--repeats must be >= 1")
    if args.stage == "episodes" and fam["status"] != "FROZEN" and not args.allow_draft and args.provider != "mock":
        print("episodes refused: fixtures are DRAFT; review them or pass --allow-draft explicitly", file=sys.stderr)
        return 1
    resume = None
    if args.resume_episodes:
        resume = json.loads(args.resume_episodes.read_text(encoding="utf-8"))
        cur = {"families": sha(json.dumps(fam, ensure_ascii=False, sort_keys=True)),
               "prompts": sha(json.dumps(prm, ensure_ascii=False, sort_keys=True))}
        if resume.get("fixtures_sha") != cur:
            print("resume refused: fixtures differ from the run being resumed (sha mismatch)", file=sys.stderr)
            return 1
        if args.stage != "episodes":
            print("--resume-episodes applies to the episodes stage only", file=sys.stderr)
            return 1
    est = estimate_calls(fam, args.stage, args.repeats)
    if resume is not None:
        est = 2 * len(failed_episode_ids(resume))
        if est == 0:
            print("nothing to resume: all decisions are valid")
            return 0
    cap = args.max_calls or int(math.ceil(est * 1.1))
    print(f"stage={args.stage} provider={args.provider} estimated_calls={est} cap={cap}")
    client = Client(args.provider, args.model, cap, args.max_tokens, args.timeout)
    args.out.mkdir(parents=True, exist_ok=True)
    try:
        if args.stage == "episodes":
            return stage_episodes(client, fam, prm, args.out, resume)
        frozen = json.loads(args.frozen.read_text(encoding="utf-8")) if args.frozen.exists() else {}
        if not frozen:
            print(f"pilot refused: {args.frozen} not found", file=sys.stderr)
            return 1
        return stage_pilot(client, fam, prm, frozen, args.repeats, args.out)
    except CallBudgetExceeded as exc:
        print(f"stopped: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
