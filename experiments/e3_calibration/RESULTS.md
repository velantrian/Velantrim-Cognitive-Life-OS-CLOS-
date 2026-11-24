# E3 offline calibration: results

Date: 2026-11-24. Standard library only; no model calls. Records below are hand-written by the researcher and calibrate the stand, not executor behaviour.

## 0. Frozen artifacts (sha256)

- `continuations`: `554fdd379bb1c3b3f575ee540e6f5eda19228db0d6671ba7b894bf5a90d60856`
- `gold_and_rubric`: `0d4499f2fc497acf45e5ea187d032bdc629a5510146ab09c4edd699fcec52e84`
- `ledger`: `13ed42b2e9a270469a2ba8e516faa76495c5ce96e1562514ef88b573c9b7761f`
- `records`: `d675c5f20592804c325b4bf0556657592f6f5e12cdc5c104c5354cf0e522fea7`
- `stories`: `deec108be20504b27c40c72628998b0212a5372a2188cf7bc15f5c1318fdedce`

## 1. Structure checks

- F1: mirrors ['A', 'B'] OK
- F2: mirrors ['A', 'B'] OK
- F3: mirrors ['A', 'B'] OK
- F4: mirrors ['A', 'B'] OK
- F1: same report across mirrors=True; gold differs=True; K1 acceptable sets differ=True
- F2: same report across mirrors=True; gold differs=True; K1 acceptable sets differ=True
- F3: same report across mirrors=True; gold differs=True; K1 acceptable sets differ=True
- F4: same report across mirrors=True; gold differs=True; K1 acceptable sets differ=True
- all structure checks: PASS

## 2. Length cap and coverage

Cap per family (words): {'F1': 45, 'F2': 45, 'F3': 45, 'F4': 30}. Record, summary and control share the family cap.

| story | arm | words | within L | ledger facts present | key facts present |
|---|---|---|---|---|---|
| s01 | R | 38 | yes | 3/3 | 2/2 |
| s01 | S | 32 | yes | 2/3 | 1/2 |
| s01 | C | 36 | yes | 3/3 | 2/2 |
| s02 | R | 37 | yes | 3/3 | 2/2 |
| s02 | S | 29 | yes | 3/3 | 2/2 |
| s02 | C | 29 | yes | 3/3 | 2/2 |
| s07 | R | 28 | yes | 3/8 | 2/2 |
| s07 | S | 29 | yes | 7/8 | 1/2 |
| s07 | C | 22 | yes | 1/8 | 1/2 |
| s08 | R | 24 | yes | 3/8 | 2/2 |
| s08 | S | 30 | yes | 7/8 | 1/2 |
| s08 | C | 18 | yes | 2/8 | 2/2 |

What this table can and cannot show: all three texts per story are hand-written by the researcher, so 'S keeps the deciding fact' reflects the author, not a model. Whether a model-written S under this cap drops the deciding fact is **not decidable offline**. It needs a handful of real summaries (a small pre-pilot, see section 6).

## 3. Leak and overlap checks

- forbidden design words in records: none
- story ids neutral (s01..s08), project names P-numbers only: yes
- F1 arm R: word overlap between mirrors (Jaccard) = 0.50
- F1 arm S: word overlap between mirrors (Jaccard) = 0.41
- F1 arm C: word overlap between mirrors (Jaccard) = 0.54
- F4 arm R: word overlap between mirrors (Jaccard) = 0.54
- F4 arm S: word overlap between mirrors (Jaccard) = 0.76
- F4 arm C: word overlap between mirrors (Jaccard) = 0.44

Indistinguishability R vs S on the deciding fact (does S already carry it?):
- s01: deciding fact (the agreement itself) kept by R=True, S=True, C=True
- s02: deciding fact (the agreement itself) kept by R=True, S=True, C=True
- s07: deciding fact (the agreement itself) kept by R=True, S=True, C=False
- s08: deciding fact (the agreement itself) kept by R=True, S=True, C=True

The hand-written S keeps the deciding fact in 4/4 stories. With a good-faith author the agreement is the headline of any summary, so a **ceiling risk** (S ~ R) is real. S does drop the secondary 'limit' facts, which matter for the account of the past (O5/O6) more than for the next step.


## 4. Scoring script on dummy answerers (all arms get the same answerer)

| answerer | O1 on K1 | O1 on K2 | O1 on K3 | O2 (status) | O3 premature close | O4 needless reopen | O5 unsupported claim |
|---|---|---|---|---|---|---|---|
| oracle | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| closer | 0.38 | 0.00 | 0.38 | 0.25 | 0.75 | 0.00 | 0.00 |
| reopener | 0.50 | 1.00 | 0.00 | 0.50 | 0.00 | 0.50 | 0.00 |
| asker | 0.25 | 0.00 | 0.12 | 0.50 | 0.00 | 0.00 | 0.00 |
| inventor | 0.50 | 1.00 | 0.00 | 0.50 | 0.00 | 0.50 | 1.00 |

Expected: oracle 1.00/1.00/1.00; closer and reopener each fail about half of K1 and K3; asker fails O1 but is honest (no O5); inventor triggers O5 (quote not in any record, O5 is computed only where a record text exists, else it counts).

## 5. Decision rule (section 10) on synthetic arm policies

| R policy | S policy | C policy | N policy | verdict | per-family R-S |
|---|---|---|---|---|---|
| oracle | closer | oracle | asker | PASS | {'F1': 2, 'F2': 2, 'F3': 4, 'F4': 2} |
| oracle | reopener | oracle | asker | PASS | {'F1': 2, 'F2': 2, 'F3': 2, 'F4': 2} |
| oracle | oracle | oracle | asker | UNKNOWN (ceiling or stand invalid) | {'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0} |
| oracle | closer | oracle | leaky | UNKNOWN (ceiling or stand invalid) | {'F1': 2, 'F2': 2, 'F3': 4, 'F4': 2} |
| overreact | asker | oracle | asker | UNKNOWN (mixed / over-sensitive) | {'F1': 4, 'F2': 4, 'F3': 0, 'F4': 4} |
| closer | closer | oracle | asker | NULL (summary sufficient) | {'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0} |

Readings: row 3 (R = S = perfect) gives UNKNOWN: the ceiling clause fires before the NULL clause and the written rule gives no precedence. Row 4 (N leaks the history) gives UNKNOWN, so the N-below-C validity check works. Row 5 (R right on K1 but always reopening on K2/K3) is stopped by the over-sensitivity guard, which needs a numeric threshold (here 0.10 absolute) that the preregistration did not state. Rows 1-2 give PASS only because S is an obviously weak policy.

## 6. Findings and required amendments

1. **Precedence rule missing.** Add: validity checks first (ceiling, floor, N~C, non-identifiable) -> UNKNOWN; then PASS; then NULL.
2. **Over-sensitivity threshold missing.** Fix: R's O3+O4 rate on K2/K3 may exceed S's by at most 0.10 absolute.
3. **Cap must be per family.** F1-F3 cap 45 words; F4 cap 30 words (decoys about the same two environments are in the episode).
4. **Cap binding and S-drops-fact are not decidable offline.** Add a pre-pilot of ~16 model calls (8 stories x R and S written by the executor) before the full run; if S keeps the deciding fact in at least 7 of 8 summaries, the primary contrast is near ceiling and the episodes must be redesigned before spending the full budget.
5. **K3 hides over-sensitivity in O4.** CHECK_TARGET is never acceptable on K3 by design, so any reopening on K3 counts; this is intended, but K3 errors weigh into the over-sensitivity guard and the threshold should be set knowing that.
6. **Stand sanity verified:** structure (mirrors, same report, different gold), dummy answerers separated as expected, N-leaks case caught, hashes frozen. Not verified: anything about model behaviour.

Stories still to hand-write for the full run: records for s03-s06 (F2, F3). Only F1 and F4 pairs have records so far.
