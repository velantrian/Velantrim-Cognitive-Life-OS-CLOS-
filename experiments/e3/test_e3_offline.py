#!/usr/bin/env python3
"""Offline checks for the E3 runner and scorer. Mock provider only; no network.

Run: python -I experiments/e3/test_e3_offline.py
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import runner  # noqa: E402
import score  # noqa: E402


def freeze_copy(tmp: Path, limit: int, status: str = "FROZEN") -> Path:
    fx = tmp / "fixtures"
    shutil.copytree(HERE / "fixtures", fx)
    for name in ("families.json", "prompts.json"):
        p = fx / name
        d = json.loads(p.read_text(encoding="utf-8"))
        d["status"] = status
        p.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    return fx


def test_fixtures_valid() -> None:
    fam, prm = runner.load_fixtures(HERE / "fixtures")
    assert fam["status"] in ("DRAFT_NOT_FROZEN", "FROZEN")
    for f in fam["families"]:
        # mirror invariant: materials shared, owner words differ (except family 4)
        a, b = f["stories"]["A"], f["stories"]["B"]
        if f["agreement_kind"] == "explicit_owner_words":
            assert a["owner_request"] != b["owner_request"]
    # every prompt template formats without KeyError
    f = fam["families"][0]
    runner.executor_messages(prm, f, "A")
    runner.successor_messages(fam, prm, f, "запись", "row1")
    runner.successor_messages(fam, prm, f, None, "row1")
    nb = "заметка"
    prm["record_authorial"].format(limit_words=100, episode_notes_block=nb)
    prm["record_summary"].format(limit_words=100, episode_notes_block=nb)
    prm["calibration_summary"].format(episode_notes_block=nb)
    prm["control_task"].format(limit_words=100, episode_notes_block=nb, owner_request="x", materials="y", decision="z", public_answer="w")


def test_owner_words_hidden_from_successor() -> None:
    fam, prm = runner.load_fixtures(HERE / "fixtures")
    for f in fam["families"]:
        for s in ("A", "B"):
            msgs = runner.successor_messages(fam, prm, f, None, "row1")
            blob = "\n".join(m["content"] for m in msgs)
            assert f["stories"][s]["owner_request"] not in blob


def test_episode_notes_hidden_from_successor() -> None:
    fam, prm = runner.load_fixtures(HERE / "fixtures")
    f4 = [f for f in fam["families"] if f["id"] == "F4"][0]
    notes = f4["stories"]["A"]["episode_notes"]
    assert notes and "ничего не написал" not in f4["materials"]
    assert notes in runner.notes_block(prm, f4, "A")  # record authors see it
    for rec in (None, "запись"):
        blob = "\n".join(m["content"] for m in runner.successor_messages(fam, prm, f4, rec, "row1"))
        assert "ничего не написал" not in blob and "не подтверждал" not in blob
    f1 = fam["families"][0]
    assert runner.notes_block(prm, f1, "A") == ""


def test_f3a_request_answerable_from_materials() -> None:
    fam, _ = runner.load_fixtures(HERE / "fixtures")
    f3 = [f for f in fam["families"] if f["id"] == "F3"][0]
    req = f3["stories"]["A"]["owner_request"]
    assert "точнее нашего" not in req and "распознал" in req and "задержка" in req
    assert "пробный пакет" in req  # boundary explicit: a sample, not the whole dump


def test_condition_blind_and_counts() -> None:
    fam, _ = runner.load_fixtures(HERE / "fixtures")
    jobs = runner.successor_jobs(fam, 2, fam["seed"])
    assert len(jobs) == 192
    assert len({j["job_id"] for j in jobs}) == 192
    assert jobs == runner.successor_jobs(fam, 2, fam["seed"])  # seeded
    assert runner.estimate_calls(fam, "episodes", 2) == 14
    assert runner.estimate_calls(fam, "pilot", 2) == 216


def test_draft_refused() -> None:
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        fx = freeze_copy(tmp, 80, status="DRAFT_NOT_FROZEN")
        rc = runner.main(["--stage", "episodes", "--provider", "mock", "--fixtures", str(fx), "--out", str(tmp / "ep")])
        assert rc == 0  # mock may use drafts
        fake = tmp / "frozen.json"
        ep = json.loads((tmp / "ep" / "episodes.json").read_text(encoding="utf-8"))
        ep.update(status="FROZEN", length_limit_words=80)
        fake.write_text(json.dumps(ep, ensure_ascii=False), encoding="utf-8")
        rc = runner.main(["--stage", "pilot", "--provider", "mock", "--fixtures", str(fx), "--frozen", str(fake),
                          "--out", str(tmp / "pilot")])
        assert rc == 1, "pilot must refuse DRAFT fixtures"


def test_end_to_end_mock() -> None:
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        fx = freeze_copy(tmp, 80)
        assert runner.main(["--stage", "episodes", "--provider", "mock", "--fixtures", str(fx),
                            "--out", str(tmp / "ep")]) == 0
        ep = json.loads((tmp / "ep" / "episodes.json").read_text(encoding="utf-8"))
        assert len(ep["episodes"]) == 8
        assert sum(e["decision_source"] == "scripted" for e in ep["episodes"]) == 2
        assert ep["calibration"]["proposed_length_limit_words"] % 10 == 0
        ep.update(status="FROZEN", length_limit_words=80)
        frozen = tmp / "frozen.json"
        frozen.write_text(json.dumps(ep, ensure_ascii=False), encoding="utf-8")

        out = tmp / "pilot"
        assert runner.main(["--stage", "pilot", "--provider", "mock", "--fixtures", str(fx),
                            "--frozen", str(frozen), "--out", str(out)]) == 0
        recs = runner.read_jsonl(out / "records.jsonl")
        assert len(recs) == 24
        succ = runner.read_jsonl(out / "successor.jsonl")
        assert len(succ) == 192
        # resume: second run makes no new calls
        before = (out / "successor.jsonl").read_text(encoding="utf-8")
        assert runner.main(["--stage", "pilot", "--provider", "mock", "--fixtures", str(fx),
                            "--frozen", str(frozen), "--out", str(out)]) == 0
        assert (out / "successor.jsonl").read_text(encoding="utf-8") == before
        # fixtures edited after episodes → pilot refuses
        fam_p = fx / "families.json"
        orig = fam_p.read_text(encoding="utf-8")
        fam_p.write_text(orig.replace("SMS-провайдер", "SMS-провайдер*"), encoding="utf-8")
        assert runner.main(["--stage", "pilot", "--provider", "mock", "--fixtures", str(fx),
                            "--frozen", str(frozen), "--out", str(tmp / "p2")]) == 1
        fam_p.write_text(orig, encoding="utf-8")

        assert score.main(["--run", str(out), "--fixtures", str(fx)]) == 0
        rep = json.loads((out / "score.json").read_text(encoding="utf-8"))
        assert rep["n_answers"] == 192
        assert rep["verdict"]["verdict"] == "NO VERDICT"
        assert (out / "annotation_blind.csv").exists()
        header = (out / "annotation_blind.csv").read_text(encoding="utf-8").splitlines()[0]
        assert "variant" not in header


def test_verdict_logic() -> None:
    th = {"summary_within_threshold_max_abs_diff": 0.1, "critical_error_regression_max": 0.0}
    def fam(a, s):
        z = {"premature_completion": 0, "unnecessary_check": 0}
        return {"authorial": dict(z, correct=a), "summary": dict(z, correct=s)}
    assert score.verdict({"F1": fam(1, .5), "F2": fam(1, .5), "F3": fam(.5, .5), "F4": fam(1, .5)}, th)["verdict"] == "PASS"
    assert score.verdict({"F1": fam(.5, .5), "F2": fam(.5, .5), "F3": fam(1, .5), "F4": fam(1, .5)}, th)["verdict"] == "FAIL"
    regress = fam(1, .5)
    regress["authorial"]["premature_completion"] = .3  # improvement, but with critical-error regression
    assert score.verdict({"F1": fam(1, .5), "F2": fam(.5, .5), "F3": regress, "F4": regress}, th)["verdict"] == "UNKNOWN"
    assert score.verdict({"F1": fam(1, 0)}, {"summary_within_threshold_max_abs_diff": None,
                                            "critical_error_regression_max": 0})["verdict"] == "NO VERDICT"


class _FakeResp:
    def __init__(self, finish: str, content: str):
        self._b = json.dumps({"choices": [{"finish_reason": finish, "message": {"content": content}}],
                              "usage": {}, "model": "m"}).encode()

    def read(self): return self._b
    def __enter__(self): return self
    def __exit__(self, *a): return False


def _client_with(responses: list, max_calls: int = 10):
    import os
    os.environ["DEEPSEEK_API_KEY"] = "test-key-not-real"
    it = iter(responses)
    orig = runner.urllib.request.urlopen
    runner.urllib.request.urlopen = lambda req, timeout=0: next(it)
    return runner.Client("deepseek", "m", max_calls, 16, 5), orig


def test_truncation_is_retried_not_recorded() -> None:
    c, orig = _client_with([_FakeResp("length", ""), _FakeResp("length", "{"), _FakeResp("stop", '{"a":1}')])
    try:
        r = c.chat([{"role": "user", "content": "x"}], "t")
    finally:
        runner.urllib.request.urlopen = orig
    assert r["ok"] and r["finish_reason"] == "stop" and r["content"] == '{"a":1}'
    assert c.calls == 3 and r["attempts"] == 3  # retries count against the call cap


def test_truncation_exhausted_is_failure() -> None:
    c, orig = _client_with([_FakeResp("length", "")] * 3)
    try:
        r = c.chat([{"role": "user", "content": "x"}], "t")
    finally:
        runner.urllib.request.urlopen = orig
    assert not r["ok"] and r["error"]["type"] == "Truncated"


def test_resume_regenerates_only_failed() -> None:
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        assert runner.main(["--stage", "episodes", "--provider", "mock", "--out", str(tmp / "e1")]) == 0
        ep = json.loads((tmp / "e1" / "episodes.json").read_text(encoding="utf-8"))
        victim = [e for e in ep["episodes"] if e["episode_id"] == "F3A"][0]
        victim["decision"] = {"decision": "format_error", "public_answer": ""}
        src = tmp / "partial.json"
        src.write_text(json.dumps(ep, ensure_ascii=False), encoding="utf-8")
        assert runner.failed_episode_ids(ep) == ["F3A"]
        assert runner.main(["--stage", "episodes", "--provider", "mock", "--resume-episodes", str(src),
                            "--out", str(tmp / "e2")]) == 0
        new = json.loads((tmp / "e2" / "episodes.json").read_text(encoding="utf-8"))
        assert new["reran_episodes"] == ["F3A"]
        by_new = {e["episode_id"]: e for e in new["episodes"]}
        by_old = {e["episode_id"]: e for e in ep["episodes"]}
        for eid, e in by_old.items():
            if eid != "F3A":
                assert by_new[eid]["decision"] == e["decision"]  # decisions stay fixed
        assert by_new["F3A"]["decision"]["decision"] == "complete"
        assert by_new["F3A"]["superseded"]["decision"]["decision"] == "format_error"
        # fixtures changed since that run -> refuse
        ep["fixtures_sha"]["families"] = "0" * 16
        src.write_text(json.dumps(ep, ensure_ascii=False), encoding="utf-8")
        assert runner.main(["--stage", "episodes", "--provider", "mock", "--resume-episodes", str(src),
                            "--out", str(tmp / "e3")]) == 1


def test_stale_history_is_refused_for_resume() -> None:
    """v0.2 history no longer matches fixtures v0.3: resuming it must be refused, not silently mixed."""
    hist_path = HERE / "history" / "episodes_v0.2_run45424109785.json"
    hist = json.loads(hist_path.read_text(encoding="utf-8"))
    assert runner.failed_episode_ids(hist) == ["F3A"]
    with tempfile.TemporaryDirectory() as t:
        rc = runner.main(["--stage", "episodes", "--provider", "mock", "--resume-episodes", str(hist_path),
                          "--out", str(Path(t) / "x")])
        assert rc == 1


def test_committed_frozen_episodes_match_fixtures() -> None:
    """Guard: editing fixtures after freezing makes this fail loudly (prereg: freeze before the run)."""
    path = HERE / "frozen" / "episodes.json"
    if not path.exists():
        return
    frozen = json.loads(path.read_text(encoding="utf-8"))
    fam, prm = runner.load_fixtures(HERE / "fixtures")
    assert runner.check_frozen(fam, prm, frozen) == 0
    assert frozen["length_limit_words"] == 200
    assert not runner.failed_episode_ids(frozen)


def test_paid_episodes_refused_when_frozen() -> None:
    with tempfile.TemporaryDirectory() as t:
        p = Path(t) / "episodes.json"
        assert runner.frozen_episodes_block(p, "deepseek") is None  # no frozen file yet
        p.write_text(json.dumps({"status": "UNREVIEWED"}), encoding="utf-8")
        assert runner.frozen_episodes_block(p, "deepseek") is None
        p.write_text(json.dumps({"status": "FROZEN"}), encoding="utf-8")
        assert "FROZEN" in runner.frozen_episodes_block(p, "deepseek")
        assert runner.frozen_episodes_block(p, "openrouter") is not None
        assert runner.frozen_episodes_block(p, "mock") is None  # offline tests stay free
    # the committed frozen file really blocks a paid episodes run
    assert runner.frozen_episodes_block(HERE / "frozen" / "episodes.json", "deepseek") is not None


def test_call_cap() -> None:
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        rc = runner.main(["--stage", "episodes", "--provider", "mock", "--max-calls", "3",
                          "--out", str(tmp / "ep")])
        assert rc == 3


def test_redaction() -> None:
    assert "sk-or-" not in runner.redact("key sk-or-v1-abcdefgh12345678")
    assert runner.parse_json_reply('```json\n{"action": "ASK_OWNER"}\n```') == {"action": "ASK_OWNER"}
    assert runner.parse_json_reply("не json") is None


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in tests:
        fn()
        print(f"ok  {fn.__name__}")
    print(f"{len(tests)} passed")
