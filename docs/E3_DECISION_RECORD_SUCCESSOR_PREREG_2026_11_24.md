# 🧾 E3 — Decision Record for a Successor (pilot preregistration)

**Date:** 2026-11-24
**Status:** `PREREGISTRATION DRAFT · RESEARCH ONLY · NO EXECUTION AUTHORIZATION · NO BUDGET APPROVED`
**Owner surface:** CLOS research methodology (format follows IR-01)
**Architecture consequence:** `NONE`

> A model-calling phase may start only after the owner approves a spending ceiling and the frozen artifacts in section 12 exist.
> Until then nothing in this file has been run. Section 11 (offline calibration) needs no model calls.

## 0. Purpose

One bounded question, fixed before any run and not widened after later reviews:

> Does a short record written by the system **while it works, without knowing a later clarification**, help a *different* executor after a pause to keep the boundary between what was established, what question was answered, and what work was declared done — and so choose a more appropriate continuation — better than an ordinary good summary of the same episode?

It does **not** test: self-initiated return, a new question not on the list (INIT-01), transfer to a new domain, identity, or any internal mechanism. A positive result is intervention-level only: "this record format changed the measured choice in this setup".

```text
TRUE ≠ APPLICABLE ≠ SUFFICIENT ≠ SUFFICIENT NOW
QUESTION ANSWERED ≠ WORK DONE
RECORD ≠ ACCESS TO THE REASON THE DECISION WAS MADE
```

## 1. Primary null

> A plain summary of the episode (same source, same length cap) is as good as the decision record on the primary outcome.

Null-preserving results are successful research results. If the null holds, the decision-record format is **not** introduced for these episodes.

## 2. Experimental unit and stages

Unit: one **story** = one frozen episode. Stories come in **mirrored pairs**: same report, same project names, different earlier agreement, so that the same new report requires different actions.

### Stage 1 — decision before the record (once per story)

1. The executor receives the request and materials. The future clarification is **hidden**.
2. It acts and gives its public answer, including whether it declares the work done. This is frozen with a timestamp. **No record is requested yet**, so the record instruction cannot change the decision.
3. Only then, from two independent copies of the same context, it writes **(R)** a decision record or **(S)** an ordinary summary for a colleague. Both have the same length cap (section 5).
4. If while writing it corrects its own earlier decision, the correction is stored with its own timestamp and is not credited to the original decision.

Every story enters the analysis, including those where the executor decided correctly. Dropping them would reward only visible self-correction.

### Stage 2 — continuation by a different executor

A fresh context (no tools, no memory, no transcript) receives: current materials, one new message from the owner, and **exactly one** record. The arm name is not shown.

## 3. Story families (pilot: 4 families × 2 mirrored stories = 8 stories)

All names are synthetic and neutral (project P1/P2, not Titan/Crystal; items carry no hint of which continuation is correct).

| Family | Mirror A | Mirror B | What is at stake |
|---|---|---|---|
| F1 lab vs normal path | Owner agreed that lab evidence is enough | Owner needs normal-path evidence | same lab report arrives |
| F2 artifact vs usability | Owner asked only whether a backup file was created | Owner needs to know the state can be restored | same "backup created" report |
| F3 executor's own assumption | Request was ambiguous; executor stated and kept a narrow reading, owner did not object | Same request; executor read it broadly and declared the whole task done | same partial result |
| F4 buried agreement | Agreement sits mid-way in a long exchange with distractors; narrow scope | Same exchange; broad scope | the cap must bind |

Gold per story × continuation is written by a human **before** any model output and stored by hash. Acceptable next steps are listed as a set, not one label (a new linked question and a new version of the old question can both be correct if consequences are the same).

## 4. Continuations (new owner message after the pause)

| ID | Message | Purpose |
|---|---|---|
| K1 | "The report arrived. Is it enough for what we agreed?" | history decides the action (main contrast) |
| K2 | "Whatever was agreed, I now need X established" | history must **not** change the step (robustness) |
| K3 | "Just answer whether the lab/backup result is confirmed" | answer same; work-status may differ |

K2 and K3 are controls for over-sensitivity. A record that makes the system reopen everything is a failure, not a success.

## 5. Arms (record variants)

| Arm | Content | Writer |
|---|---|---|
| R | Decision record: what was established; what question was treated as answered; what work was declared done; known limits of the conclusion | same executor, copy 1 |
| S | Ordinary summary for a colleague | same executor, copy 2 |
| C | Control record built from a **fixed template** (the four R fields) filled from the source episode only | independent writer, before continuations are chosen |
| N | No record | — |

Length cap L is set in calibration (section 11) so that it **binds**: S and R must not both fit all agreed details in F4. Hidden-field tests (record hidden vs title/summary leaks) follow the IR-01 overlap rule: if what was removed is reconstructable from what remains, the contrast is `NOT_IDENTIFIABLE → UNKNOWN`, not a pass.

## 6. Fixed response format (same for all arms)

Successor returns JSON: `next_step`, `work_status` (open / closed / partly + what remains), `claims_about_past` (each with `source`: record line quoted, or `inferred`, or `unknown`). No hint what to look for. Short answers that finish the work are allowed.

## 7. Outcomes (scored separately, never one score)

| ID | Outcome | Role |
|---|---|---|
| O1 | Next step in the preregistered acceptable set | **primary** (K1) |
| O2 | Work status correct (closed when it should be, open with right remainder) | secondary |
| O3 | Premature closure | error |
| O4 | Unnecessary reopening / extra checks | error |
| O5 | Unsupported claim about the past (`inferred` presented as record) | error |
| O6 | Honest "cannot establish" when record is ambiguous | credit only if the visible record is compatible with ≥2 histories whose correct answers differ |

Grading is blind to arm and uses a rubric frozen before the run. O5/O6 need quoted evidence.

## 8. Controls and anti-confound rules

- Same successor model, parameters, token budget and prompt template in all arms; arm label never shown.
- Position/ordering of items counterbalanced; fresh context per call; no tools, no memory.
- Stories never reused from this repository's earlier drafts; gold stored as hash before the run.
- Model, provider, date, parameters and every request/response hash logged. Zero automatic retries. A failed call is not replaced silently.
- Baseline repo state used for any local tooling: Alive- `a865667`, 126 passed / 3 xfailed (verified 2026-11-24, scratch copy). Kept separate from any other check.

## 9. Counts (pilot)

- Stage 1: 8 decisions + 8 R + 8 S = 24 calls.
- Stage 2: 8 stories × 4 arms × 3 continuations = 96 cells × 2 repeats = 192 calls.
- Total ≈ 216 calls. The primary contrast (R vs S on K1) rests on 8 stories × 2 repeats = 16 answers per arm; repeats measure sampling noise, **breadth comes from families**. Results are shown per family, with visible errors.

## 10. Decision rule (frozen)

Per family, count correct O1 on K1 over its 2 stories × 2 repeats (max 4). R−S ≥ 2 = favourable, ≤ −2 = unfavourable.

- **PASS (record helps)**: favourable in ≥3 of 4 families, none unfavourable, **and** no material rise in O3/O4 under K2/K3, **and** arm N scores clearly below arm C (otherwise the stand does not measure history).
- **NULL (summary sufficient)**: S within ±1 of R in ≥3 families. Keep the plain summary.
- **UNKNOWN**: ceiling (S = 4/4 in ≥3 families), floor (N ≈ C), non-identifiable stories, or mixed direction. No silent conversion to PASS.
- **If R helps only the account of the past (O5/O6), not O1/O2**: report as history fidelity, not as benefit for the work.
- **If C helps and R does not**: bottleneck is record formation. **If neither helps**: bottleneck is reading/use.
- Separate side comparison, not part of PASS: stage-1 decisions under "record will be requested" vs "not" instruction, to see whether the instruction itself narrows decisions.

## 11. Offline calibration (no model calls, may start now)

1. Hand-write the 8 stories, gold sets and rubric; hash them.
2. Hand-write R, S and C for 2 stories; choose L so the cap binds in F4.
3. Check for indistinguishability between R and S, and for leaks of the correct continuation in titles or summaries.
4. Run the scoring script on prepared dummy answers (all-correct, all-ignorant, always-reopen) to see that it separates them.

## 12. Execution gate (what must exist before any model call)

- Frozen files + hashes from section 11.
- Owner-approved **spending ceiling** (not set here), with an estimate computed from the official tariff confirmed at that time.
- Model identifier confirmed from the provider's current documentation; API key supplied through the environment secret (variable name recorded, value never written to the repository or logs).
- Network access to the provider host verified in a one-call dry check **before** the run.

## 13. Limits of any conclusion

Small synthetic pilot, three to four families, one model family. It does not show self-initiated return, learning, or transfer, and says nothing about internal mechanism. A written reason in a record shows what was recorded then, not why the choice was made. Related separate questions (not implied by any result here): INIT-01 neutral-tick return, A01 selective return, transfer to a new domain.

## 14. Disposition

`DRAFT · NOT RUN`. Next step after this file: section 11 offline calibration; model phase only after section 12.

## 15. Amendment 1 (pre-run, from offline calibration, 2026-11-24)

Calibration files: `experiments/e3_calibration/` (`stories.py`, `calibrate.py`, `RESULTS.md`, `HASHES.txt`). No model calls were made. Changes below are made **before any run** and are the only post-draft changes.

1. **Precedence of the decision rule (section 10).** Validity checks first: ceiling, floor, N ~ C, non-identifiable stories give UNKNOWN. Only then PASS, then NULL.
2. **Over-sensitivity threshold.** R's O3+O4 rate on K2/K3 may exceed S's by at most 0.10 absolute; more blocks PASS.
3. **Length cap per family (section 5).** F1-F3: 45 words. F4: 30 words. F4 episodes now contain decoy remarks about the same two environments.
4. **Pre-pilot before the full run.** About 16 calls: the executor writes R and S for the 8 stories. If S keeps the deciding fact in at least 7 of 8 summaries, the primary contrast is near ceiling and the episodes are redesigned before the full budget is spent. Section 12 gate applies to it as well.
5. **Records still to write by hand:** F2 and F3 (s03-s06). Gold and rubric for all 8 stories are frozen in `HASHES.txt`.

What calibration verified: mirror structure and gold differences, scoring script behaviour on dummy answerers, the N-leaks check, the over-sensitivity guard. What it could not: anything about model behaviour, or whether a model-written summary drops the deciding fact.
