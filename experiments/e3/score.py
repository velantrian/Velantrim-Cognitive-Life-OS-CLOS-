#!/usr/bin/env python3
"""E3 scorer (RESEARCH ONLY). Offline; no API calls.

Reads successor.jsonl from a pilot run and computes, per record variant
(prereg §4):

  - appropriateness of the next step (primary; row 1 is the main contrast);
  - premature completions;
  - unnecessary checks;
  - unsupported claims about the past (automatic part only);
  - honest gaps (ASK_OWNER / CANNOT_DETERMINE where not the expected step).

Historical accuracy is NOT scored automatically: a lucky guess must not earn
it (prereg §4). It is exported as a blind annotation sheet; the variant key is
written to a separate file.

A PASS / FAIL / UNKNOWN verdict is produced only when the operator has set
thresholds in fixtures/families.json before the run (prereg §5–6). Otherwise
the report states NO VERDICT.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
VARIANTS = ["authorial", "summary", "control", "none"]
GAP_LABELS = {"ASK_OWNER", "CANNOT_DETERMINE"}


def classify(row: dict, expected: dict) -> dict:
    p = row.get("parsed") or {}
    action = p.get("action")
    status = p.get("work_status")
    exp = expected[row["family"]][row["story"]][row["row"]]
    out = {
        "format_error": not row.get("ok") or row.get("format_error") or action is None,
        "action": action,
        "status": status,
        "correct": action in exp["correct"],
        "status_ok": status in exp["status"],
    }
    out["premature_completion"] = (
        (action == "COMPLETE_WORK" and not out["correct"])
        or (status == "closed" and "closed" not in exp["status"])
    )
    out["unnecessary_check"] = action == "VERIFY_FURTHER" and not out["correct"]
    out["honest_gap"] = action in GAP_LABELS and not out["correct"]
    claims = p.get("past_claims") if isinstance(p.get("past_claims"), list) else []
    out["claims"] = len(claims)
    out["unsupported_claims"] = sum(
        1 for c in claims if isinstance(c, dict) and (
            c.get("source") == "assumption"
            or (row["variant"] == "none" and c.get("source") == "record")
        )
    )
    return out


def rate(xs: list[bool]) -> float | None:
    return round(sum(xs) / len(xs), 3) if xs else None


def summarize(rows: list[dict]) -> dict:
    keys = ["correct", "status_ok", "premature_completion", "unnecessary_check", "honest_gap", "format_error"]
    res = {k: rate([r["c"][k] for r in rows]) for k in keys}
    res["n"] = len(rows)
    res["unsupported_claims_per_answer"] = (
        round(sum(r["c"]["unsupported_claims"] for r in rows) / len(rows), 3) if rows else None)
    return res


def verdict(per_family_row1: dict, thresholds: dict) -> dict:
    eps = thresholds.get("summary_within_threshold_max_abs_diff")
    reg = thresholds.get("critical_error_regression_max")
    if eps is None or reg is None:
        return {"verdict": "NO VERDICT", "reason": "thresholds not set before the run (prereg §5–6)"}
    improved, summary_ok = [], []
    for fid, by_v in per_family_row1.items():
        a, s = by_v.get("authorial"), by_v.get("summary")
        if not a or not s or a["correct"] is None or s["correct"] is None:
            continue
        diff = a["correct"] - s["correct"]
        crit_a = (a["premature_completion"] or 0) + (a["unnecessary_check"] or 0)
        crit_s = (s["premature_completion"] or 0) + (s["unnecessary_check"] or 0)
        if diff > eps and crit_a - crit_s <= reg:
            improved.append(fid)
        if diff <= eps:
            summary_ok.append(fid)
    if len(improved) >= 2 and len(summary_ok) < 2:
        v = "PASS"
    elif len(summary_ok) >= 2:
        v = "FAIL"
    else:
        v = "UNKNOWN"
    return {"verdict": v, "families_improved": improved, "families_summary_not_worse": summary_ok,
            "note": "Пилот, не доказательство (prereg §8). Историческая точность — отдельно, по ручной разметке."}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", type=Path, required=True, help="pilot output dir with successor.jsonl")
    ap.add_argument("--fixtures", type=Path, default=HERE / "fixtures")
    args = ap.parse_args(argv)

    fam = json.loads((args.fixtures / "families.json").read_text(encoding="utf-8"))
    rows = [json.loads(l) for l in (args.run / "successor.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    for r in rows:
        r["c"] = classify(r, fam["expected"])

    by_variant = {v: summarize([r for r in rows if r["variant"] == v]) for v in VARIANTS}
    by_variant_row = {v: {row: summarize([r for r in rows if r["variant"] == v and r["row"] == row])
                          for row in ("row1", "row2", "row3")} for v in VARIANTS}
    families = sorted({r["family"] for r in rows})
    per_family_row1 = {f: {v: summarize([r for r in rows if r["family"] == f and r["variant"] == v and r["row"] == "row1"])
                           for v in VARIANTS} for f in families}
    report = {
        "n_answers": len(rows),
        "by_variant": by_variant,
        "by_variant_row": by_variant_row,
        "row1_by_family": per_family_row1,
        "verdict": verdict(per_family_row1, fam["analysis"]["thresholds"]),
    }
    (args.run / "score.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Blind annotation sheet for historical accuracy: variant hidden, order shuffled.
    rng = random.Random(fam["seed"] + 1)
    sheet = [r for r in rows if r.get("parsed")]
    rng.shuffle(sheet)
    key = {}
    with (args.run / "annotation_blind.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["blind_id", "family", "story", "row", "action_text", "remaining", "past_claims",
                    "historical_accuracy(0/1/NA)", "note"])
        for i, r in enumerate(sheet):
            bid = f"E3-{i:04d}"
            key[bid] = {"job_id": r["job_id"], "variant": r["variant"]}
            p = r["parsed"]
            w.writerow([bid, r["family"], r["story"], r["row"], p.get("action_text", ""), p.get("remaining", ""),
                        json.dumps(p.get("past_claims", []), ensure_ascii=False), "", ""])
    (args.run / "annotation_key.json").write_text(json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({"by_variant": by_variant, "verdict": report["verdict"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
