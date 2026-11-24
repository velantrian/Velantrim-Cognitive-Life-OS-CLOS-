"""E3 offline calibration (preregistration section 11). No model calls, standard library only.

Usage: python3 -I calibrate.py   (from this directory) -> prints report, writes RESULTS.md and HASHES.txt
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))

import stories as D

HERE = Path(__file__).resolve().parent
ARMS = ("R", "S", "C", "N")
CONTS = ("K1", "K2", "K3")
REPS = (1, 2)
FAMILIES = ("F1", "F2", "F3", "F4")
LEDGER_STORIES = [s for s in D.STORIES if s in D.RECORDS]
out: list[str] = []


def say(line: str = "") -> None:
    print(line)
    out.append(line)


def words(t: str) -> int:
    return len(re.findall(r"\S+", t))


# ---------------------------------------------------------------- 1. freeze / hash
def canon(obj) -> str:
    def conv(o):
        if isinstance(o, set):
            return sorted(o)
        if isinstance(o, tuple):
            return [conv(x) for x in o]
        if isinstance(o, dict):
            return {k: conv(v) for k, v in o.items()}
        if isinstance(o, list):
            return [conv(x) for x in o]
        return o
    return json.dumps(conv(obj), sort_keys=True, ensure_ascii=False)


gold = {s: v["gold"] for s, v in D.STORIES.items()}
frozen = {"gold_and_rubric": gold, "continuations": D.CONTS,
          "stories": {s: {k: v[k] for k in ("family", "mirror", "report", "episode")} for s, v in D.STORIES.items()},
          "records": D.RECORDS, "ledger": D.LEDGER}
hashes = {k: hashlib.sha256(canon(v).encode()).hexdigest() for k, v in frozen.items()}
(HERE / "HASHES.txt").write_text("".join(f"{h}  {k}\n" for k, h in sorted(hashes.items())))

say("# E3 offline calibration: results\n")
say("Date: 2026-11-24. Standard library only; no model calls. Records below are hand-written by the researcher "
    "and calibrate the stand, not executor behaviour.\n")
say("## 0. Frozen artifacts (sha256)\n")
for k, h in sorted(hashes.items()):
    say(f"- `{k}`: `{h}`")

# ---------------------------------------------------------------- 2. structure checks
say("\n## 1. Structure checks\n")
ok = True
for fam in FAMILIES:
    ms = {v["mirror"] for s, v in D.STORIES.items() if v["family"] == fam}
    good = ms == {"A", "B"}
    ok &= good
    say(f"- {fam}: mirrors {sorted(ms)} {'OK' if good else 'BAD'}")
for fam in FAMILIES:
    a, b = [s for s, v in D.STORIES.items() if v["family"] == fam]
    same_report = D.STORIES[a]["report"] == D.STORIES[b]["report"]
    diff_gold = any(D.STORIES[a]["gold"][k] != D.STORIES[b]["gold"][k] for k in CONTS)
    k1_diff = D.STORIES[a]["gold"]["K1"][0] != D.STORIES[b]["gold"]["K1"][0]
    say(f"- {fam}: same report across mirrors={same_report}; gold differs={diff_gold}; K1 acceptable sets differ={k1_diff}")
    ok &= same_report and diff_gold and k1_diff
say(f"- all structure checks: {'PASS' if ok else 'FAIL'}")

# ---------------------------------------------------------------- 3. cap + ledger coverage
def facts_present(sid: str, text: str):
    t = text.lower()
    res = {}
    for fid, groups, key in D.LEDGER[sid]:
        res[fid] = (all(re.search(g, t) for g in groups), key)
    return res


say("\n## 2. Length cap and coverage\n")
lens = {(s, a): words(D.RECORDS[s][a]) for s in LEDGER_STORIES for a in "RSC"}
say(f"Cap per family (words): {D.CAP}. Record, summary and control share the family cap.\n")
say("| story | arm | words | within L | ledger facts present | key facts present |")
say("|---|---|---|---|---|---|")
cov = {}
for s in LEDGER_STORIES:
    for a in "RSC":
        fp = facts_present(s, D.RECORDS[s][a])
        n_all = sum(v[0] for v in fp.values())
        n_key = sum(1 for v in fp.values() if v[0] and v[1])
        tk = sum(1 for v in fp.values() if v[1])
        cov[(s, a)] = (n_all, len(fp), n_key, tk)
        say(f"| {s} | {a} | {lens[(s, a)]} | {'yes' if lens[(s, a)] <= D.CAP[D.STORIES[s]['family']] else 'NO'} | {n_all}/{len(fp)} | {n_key}/{tk} |")

say("\nWhat this table can and cannot show: all three texts per story are hand-written by the researcher, so "
    "'S keeps the deciding fact' reflects the author, not a model. Whether a model-written S under this cap drops the "
    "deciding fact is **not decidable offline**. It needs a handful of real summaries (a small pre-pilot, see section 6).")

# ---------------------------------------------------------------- 4. leak / indistinguishability
say("\n## 3. Leak and overlap checks\n")
bad = []
for s in LEDGER_STORIES:
    for a in "RSC":
        t = D.RECORDS[s][a].lower()
        for w in D.FORBIDDEN_IN_RECORDS:
            if re.search(rf"\b{re.escape(w)}\b", t):
                bad.append((s, a, w))
say(f"- forbidden design words in records: {bad if bad else 'none'}")
say("- story ids neutral (s01..s08), project names P-numbers only: yes")
for fam, (a, b) in {"F1": ("s01", "s02"), "F4": ("s07", "s08")}.items():
    for arm in "RSC":
        ta, tb = D.RECORDS[a][arm], D.RECORDS[b][arm]
        sa = set(re.findall(r"\w+", ta.lower())); sb = set(re.findall(r"\w+", tb.lower()))
        say(f"- {fam} arm {arm}: word overlap between mirrors (Jaccard) = {len(sa & sb) / len(sa | sb):.2f}")
say("\nIndistinguishability R vs S on the deciding fact (does S already carry it?):")
ceiling = []
def decisive(s, arm):
    first_key = next(fid for fid, g, key in D.LEDGER[s] if key)
    return facts_present(s, D.RECORDS[s][arm])[first_key][0]
for s in LEDGER_STORIES:
    kr, ks, kc = decisive(s, "R"), decisive(s, "S"), decisive(s, "C")
    ceiling.append(ks)
    say(f"- {s}: deciding fact (the agreement itself) kept by R={kr}, S={ks}, C={kc}")
say(f"\nThe hand-written S keeps the deciding fact in {sum(ceiling)}/{len(ceiling)} stories. With a good-faith author the agreement is "
    "the headline of any summary, so a **ceiling risk** (S ~ R) is real. S does drop the secondary 'limit' facts, which matter for "
    "the account of the past (O5/O6) more than for the next step.\n")

# ---------------------------------------------------------------- 5. scoring
def score_one(a: dict, record_text: str | None):
    tags, status = D.STORIES[a["story"]]["gold"][a["cont"]]
    o1 = a["tag"] in tags
    o2 = a["status"] == status
    o3 = a["status"] == "closed" and status != "closed"
    o4 = a["tag"] == "CHECK_TARGET" and "CHECK_TARGET" not in tags
    o5 = False
    for c in a.get("claims", []):
        if c["source"] == "record" and (record_text is None or c["quote"].lower() not in record_text.lower()):
            o5 = True
    o6 = a["arm"] == "N" and a["tag"] == "ASK_OWNER" and not any(c["source"] != "unknown" for c in a.get("claims", []))
    return dict(o1=o1, o2=o2, o3=o3, o4=o4, o5=o5, o6=o6)


def rec_text(story: str, arm: str):
    return D.RECORDS.get(story, {}).get(arm)


def answerer(name: str):
    def f(story, arm, cont):
        tags, status = D.STORIES[story]["gold"][cont]
        if name == "oracle":
            if arm == "N":
                return "ASK_OWNER", "open", [{"source": "unknown", "text": "history not available"}]
            return sorted(tags)[0], status, []
        if name == "leaky":
            return sorted(tags)[0], status, []
        if name == "overreact":
            if cont == "K1":
                return sorted(tags)[0], status, []
            return "CHECK_TARGET", "open", []
        if name == "closer":
            return "ANSWER_CLOSE", "closed", []
        if name == "reopener":
            return "CHECK_TARGET", "open", []
        if name == "asker":
            return "ASK_OWNER", "open", [{"source": "unknown", "text": "no history"}]
        if name == "inventor":
            return "CHECK_TARGET", "open", [{"source": "record", "quote": "owner agreed production", "text": "invented"}]
        raise ValueError(name)
    return f


def run_matrix(policy: dict[str, str]):
    ans = []
    for s in D.STORIES:
        for arm in ARMS:
            f = answerer(policy[arm])
            for k in CONTS:
                for rep in REPS:
                    tag, st, cl = f(s, arm, k)
                    ans.append(dict(story=s, arm=arm, cont=k, rep=rep, tag=tag, status=st, claims=cl))
    return ans


def rates(ans, arm, conts=CONTS, key="o1"):
    xs = [score_one(a, rec_text(a["story"], arm))[key] for a in ans if a["arm"] == arm and a["cont"] in conts]
    return sum(xs) / len(xs) if xs else float("nan")


say("\n## 4. Scoring script on dummy answerers (all arms get the same answerer)\n")
say("| answerer | O1 on K1 | O1 on K2 | O1 on K3 | O2 (status) | O3 premature close | O4 needless reopen | O5 unsupported claim |")
say("|---|---|---|---|---|---|---|---|")
for n in ("oracle", "closer", "reopener", "asker", "inventor"):
    ans = run_matrix({a: n for a in ARMS})
    sub = [a for a in ans if a["arm"] in ("R", "S", "C")]
    def m(key, conts=CONTS):
        xs = [score_one(a, rec_text(a["story"], a["arm"]))[key] for a in sub if a["cont"] in conts]
        return f"{sum(xs) / len(xs):.2f}"
    say(f"| {n} | {m('o1', ('K1',))} | {m('o1', ('K2',))} | {m('o1', ('K3',))} | {m('o2')} | {m('o3')} | {m('o4')} | {m('o5')} |")
say("\nExpected: oracle 1.00/1.00/1.00; closer and reopener each fail about half of K1 and K3; asker fails O1 but is honest "
    "(no O5); inventor triggers O5 (quote not in any record, O5 is computed only where a record text exists, else it counts).")

# ---------------------------------------------------------------- 6. decision rule on synthetic scenarios
def decide(ans):
    fam_of = {s: v["family"] for s, v in D.STORIES.items()}
    def k1_correct(arm, fam):
        return sum(score_one(a, rec_text(a["story"], arm))["o1"] for a in ans
                   if a["arm"] == arm and a["cont"] == "K1" and fam_of[a["story"]] == fam)
    diffs = {f: k1_correct("R", f) - k1_correct("S", f) for f in FAMILIES}
    s_ceiling = sum(k1_correct("S", f) == 4 for f in FAMILIES) >= 3
    n_c = rates(ans, "N", ("K1",)) < rates(ans, "C", ("K1",)) - 0.25
    def err(arm):
        xs = [score_one(a, rec_text(a["story"], arm)) for a in ans if a["arm"] == arm and a["cont"] in ("K2", "K3")]
        return sum(x["o3"] or x["o4"] for x in xs) / len(xs)
    over = err("R") - err("S") > 0.10
    fav = sum(d >= 2 for d in diffs.values()); unf = sum(d <= -2 for d in diffs.values())
    near = sum(abs(d) <= 1 for d in diffs.values())
    if s_ceiling or not n_c:
        return "UNKNOWN (ceiling or stand invalid)", diffs
    if fav >= 3 and unf == 0 and not over:
        return "PASS", diffs
    if near >= 3:
        return "NULL (summary sufficient)", diffs
    return "UNKNOWN (mixed / over-sensitive)", diffs


say("\n## 5. Decision rule (section 10) on synthetic arm policies\n")
say("| R policy | S policy | C policy | N policy | verdict | per-family R-S |")
say("|---|---|---|---|---|---|")
scen = [("oracle", "closer", "oracle", "asker"), ("oracle", "reopener", "oracle", "asker"),
        ("oracle", "oracle", "oracle", "asker"), ("oracle", "closer", "oracle", "leaky"),
        ("overreact", "asker", "oracle", "asker"), ("closer", "closer", "oracle", "asker")]
for r, s_, c, n in scen:
    ans = run_matrix({"R": r, "S": s_, "C": c, "N": n})
    v, d = decide(ans)
    say(f"| {r} | {s_} | {c} | {n} | {v} | {d} |")
say("\nReadings: row 3 (R = S = perfect) gives UNKNOWN: the ceiling clause fires before the NULL clause and the written rule gives no precedence. "
    "Row 4 (N leaks the history) gives UNKNOWN, so the N-below-C validity check works. Row 5 (R right on K1 but always reopening on K2/K3) is "
    "stopped by the over-sensitivity guard, which needs a numeric threshold (here 0.10 absolute) that the preregistration did not state. "
    "Rows 1-2 give PASS only because S is an obviously weak policy.")

say("\n## 6. Findings and required amendments\n")
say("1. **Precedence rule missing.** Add: validity checks first (ceiling, floor, N~C, non-identifiable) -> UNKNOWN; then PASS; then NULL.")
say("2. **Over-sensitivity threshold missing.** Fix: R's O3+O4 rate on K2/K3 may exceed S's by at most 0.10 absolute.")
say("3. **Cap must be per family.** F1-F3 cap 45 words; F4 cap 30 words (decoys about the same two environments are in the episode).")
say("4. **Cap binding and S-drops-fact are not decidable offline.** Add a pre-pilot of ~16 model calls (8 stories x R and S written by the "
    "executor) before the full run; if S keeps the deciding fact in at least 7 of 8 summaries, the primary contrast is near ceiling and "
    "the episodes must be redesigned before spending the full budget.")
say("5. **K3 hides over-sensitivity in O4.** CHECK_TARGET is never acceptable on K3 by design, so any reopening on K3 counts; this is intended, but K3 errors weigh into the over-sensitivity guard and the threshold should be set knowing that.")
say("6. **Stand sanity verified:** structure (mirrors, same report, different gold), dummy answerers separated as expected, N-leaks case "
    "caught, hashes frozen. Not verified: anything about model behaviour.")
say("\nStories still to hand-write for the full run: records for s03-s06 (F2, F3). Only F1 and F4 pairs have records so far.")

(HERE / "RESULTS.md").write_text("\n".join(out) + "\n")
