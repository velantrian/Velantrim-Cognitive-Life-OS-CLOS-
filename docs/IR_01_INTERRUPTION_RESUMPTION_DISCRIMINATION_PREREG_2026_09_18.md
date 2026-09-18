# 🧠🪢 IR-01 — Interruption / Resumption Information-Class Discrimination

**Date:** 2026-09-18  
**Status:** `PREREGISTRATION DRAFT · RESEARCH ONLY · NO EXECUTION AUTHORIZATION`  
**Owner surface:** CLOS research methodology  
**Related owners:** Mentaury Soul cognition/orientation research; Continuum continuity/handoff research  
**Architecture consequence:** `NONE`

## 0. Purpose

IR-01 operationalizes one bounded question left by the donor reconciliation cycle:

> After an interruption, which information classes materially improve correct resumption when source facts, surface format, and payload budget are controlled?

The experiment does **not** assume that `orientation` is one latent module or one already-established empirical construct.

It tests observable consequences of supplying or withholding specific information classes.

```text
CONTENT CONTINUITY ≠ ORIENTATION CONTINUITY
= RESEARCH SYNTHESIS TO BE OPERATIONALIZED
≠ EMPIRICAL FACT ALREADY PROVEN
```

IR-01 is not TCE proof, EDCA proof, identity proof, or architecture selection.

## 1. Primary research question

Given the same interrupted work episode and the same underlying factual source material, how much does successful continuation depend on explicit availability of:

- **C — CONTENT:** task-relevant facts / artifacts / findings;
- **G — GOAL:** the currently active bounded objective;
- **X — CONTEXT:** scope, reference frame, current constraints, currentness qualifiers;
- **R — RATIONALE:** externally recorded grounds for the current position, including materially relevant rejected alternatives / scoped negatives.

`RATIONALE` here means **documented external rationale**, not hidden chain-of-thought.

```text
RATIONALE ≠ PRIVATE CHAIN OF THOUGHT
```

## 2. Primary null

The minimum-complexity null is:

> **C alone is sufficient for the tested resumption tasks; adding G, X, or R does not produce a material improvement in prespecified resumption outcomes.**

A null-preserving result is a successful research result.

IR-01 gives no prior credit to richer state packages.

## 3. Experimental unit

Each fixture contains one completed pre-interruption work episode with a human-authored reference state:

```text
SOURCE FACTS
ACTIVE GOAL
CURRENT CONTEXT / SCOPE
DOCUMENTED RATIONALE
REJECTED / DEFERRED ALTERNATIVES WHERE MATERIAL
CORRECT NEXT BOUNDED STEP
```

The interrupted successor receives only the arm-specific resume packet and the same continuation prompt.

No arm receives the original full conversation unless used as a separately labelled diagnostic reference.

## 4. Factorial arms

CONTENT is held present in every primary arm.

The three experimental factors are independently toggled:

```text
G ∈ {0,1}
X ∈ {0,1}
R ∈ {0,1}
```

This creates eight primary arms:

| Arm | Content | Goal | Context | Rationale |
|---|---:|---:|---:|---:|
| C000 | ✅ | ❌ | ❌ | ❌ |
| C100 | ✅ | ✅ | ❌ | ❌ |
| C010 | ✅ | ❌ | ✅ | ❌ |
| C001 | ✅ | ❌ | ❌ | ✅ |
| C110 | ✅ | ✅ | ✅ | ❌ |
| C101 | ✅ | ✅ | ❌ | ✅ |
| C011 | ✅ | ❌ | ✅ | ✅ |
| C111 | ✅ | ✅ | ✅ | ✅ |

Arm names are experimental labels only; they are not architectural state names.

## 5. Matching / anti-confound controls

The intended contrast is semantic information class, not prompt quality.

Across arms for the same fixture:

- identical underlying **source fact set**;
- identical continuation question;
- identical model/provider/settings within a run family;
- fresh isolated successor context for every arm;
- no access to prior arm outputs;
- no tools, retrieval, memory connectors, or hidden transcript access unless separately preregistered;
- same packet schema and field order;
- same maximum payload/token budget;
- format and verbosity matched as closely as possible;
- omitted experimental fields replaced by a fixed `MASKED_FOR_IR01` marker plus neutral padding outside task semantics when required for budget matching;
- no arm-specific hints such as "the missing goal is important";
- fixture order randomized where applicable.

Important qualification:

```text
MATCHED SOURCE FACTS + MATCHED FORMAT/BUDGET
≠ IDENTICAL SEMANTIC INFORMATION
```

The semantic presence/absence of G, X, and R is the manipulated variable.

## 6. Fixture families

IR-01 should begin with bounded fixtures that make different failure modes observable.

### IR-F1 — Scoped negative decision

A method/option was rejected **under a specific condition**, not universally.

Correct resumption must preserve:

- the rejection;
- its scope;
- the possibility of reopening if the condition changes.

Primary risk:
`REJECTED UNDER C` → `REJECTED ALWAYS`.

### IR-F2 — Current goal after revision

An earlier objective remains historically visible, but a newer objective is current.

Primary risk:
historical objective is resumed because it is more salient.

### IR-F3 — Same facts, different reference frame

The factual content is identical, but the correct next step changes with scope / audience / project phase / authorization boundary.

Primary risk:
content is preserved while applicability is lost.

### IR-F4 — Rejected alternative with surviving rationale

Two routes remain technically possible; one was rejected for a documented reason that still applies.

Primary risk:
successor reopens the rejected route without evidence that the rejection condition changed.

### IR-F5 — Rationale no longer applicable

The old rationale was valid under context X0; the resume packet reflects context X1 where it no longer applies.

Primary risk:
history is preserved but given permanent authority.

This fixture tests:

```text
PRESERVE HISTORY ≠ FREEZE HISTORY
```

## 7. Human-authored reference / Gold

For every fixture, a human-authored Gold record must be frozen before any evidence run.

Minimum Gold fields:

- `fixture_id`;
- `source_fact_ids`;
- `current_goal`;
- `current_context`;
- `documented_rationale`;
- `scoped_negative_decisions`;
- `reopen_conditions`;
- `correct_next_step_class`;
- `acceptable_next_step_variants`;
- `forbidden_promotions`;
- `unknowns_that_must_remain_unknown`.

The evaluated model must not write, approve, or revise its own Gold.

## 8. Primary outcomes

Score outcomes separately. Do not collapse them into one weighted "continuity score".

### O1 — Next-step correctness

Did the successor choose a Gold-consistent next bounded step?

### O2 — Goal continuity

Did it act on the current goal rather than a superseded/deferred one?

### O3 — Scope/context fidelity

Did it preserve the applicability conditions required for the next step?

### O4 — Scoped-negative preservation

Did it preserve a rejected/deferred route with the correct scope and reopen condition?

### O5 — Inappropriate reopening

Did it reopen a route while the original rejection condition still held?

### O6 — Invented rationale

Did it fabricate reasons not present in the supplied packet?

### O7 — Provenance/ownership error

Did it attribute a model inference, reviewer result, or inherited state as though it were the successor's own prior experience or verified evidence?

### O8 — Resume efficiency

Diagnostic only:

- turns to reach a Gold-consistent next step;
- clarification count;
- token use / latency where available.

Efficiency cannot override correctness.

## 9. Required response shape

Successor output must be externally scorable without chain-of-thought.

Minimum response:

```text
CURRENT GOAL:
CURRENT SCOPE / CONTEXT:
WHAT REMAINS OPEN:
NEXT BOUNDED STEP:
REOPENED OR REJECTED ROUTES:
CRITICAL UNKNOWN:
SOURCE / RATIONALE STATUS:
```

Short justification may cite supplied facts/rationale, but no hidden reasoning trace is requested.

## 10. Primary contrasts

The primary scientific object is not "which arm wins overall".

Compare the effect of each information class while holding the other factors fixed:

- **Goal effect:** G1 vs G0 at matched X/R;
- **Context effect:** X1 vs X0 at matched G/R;
- **Rationale effect:** R1 vs R0 at matched G/X.

Also inspect interactions:

- G × X;
- G × R;
- X × R;
- G × X × R.

No architectural meaning is attached to an interaction by itself.

## 11. PASS / FAIL / UNKNOWN

### PASS for a candidate information class

A class is provisionally useful only if its presence produces a reproducible improvement on prespecified outcomes across more than one fixture family **without** merely increasing unsupported confidence, verbosity, or invented rationale.

### FAIL / no material gain

A richer packet fails to earn its complexity if:

- the corresponding class produces no reproducible outcome improvement;
- apparent gains come only from verbosity / formatting / label leakage;
- the class increases false reopening, invented rationale, or provenance errors;
- simpler arms perform equivalently on the relevant fixture class.

### UNKNOWN / insufficient

Use UNKNOWN when:

- fixture Gold is ambiguous;
- manipulated fields are not separable;
- budget/format matching fails materially;
- model/provider behavior is unstable;
- sample/run count is insufficient;
- the successor has unintended access to omitted information;
- multiple causal explanations remain observationally equivalent.

## 12. Anti-cheat / contamination rules

Evidence interpretation is invalid if any compared arm differs in an uncontrolled way that could explain the result.

Forbidden:

- reusing one arm's output as another arm's context;
- tuning fixture wording after observing evidence-arm failures;
- changing Gold after model output;
- giving richer arms better instructions;
- using hidden evaluator labels in model prompts;
- silently changing model/provider/settings across compared arms;
- allowing tools/retrieval in only selected arms;
- treating model self-report ("I remembered...") as proof of mechanism;
- using the same exact pilot wording as later evidence wording without an explicit contamination decision.

## 13. Pilot vs evidence

First execution, if later authorized, must be:

```text
PILOT — NOT EVIDENCE
```

Pilot may discover:

- ambiguous Gold;
- packet-budget artifacts;
- label leakage;
- parser/evaluator defects;
- impossible fixture distinctions;
- unstable model settings.

Pilot results cannot support architecture conclusions.

Evidence execution requires a separate evidence lock and explicit authorization.

## 14. Falsification rules

IR-01 must be capable of reducing, not only expanding, state requirements.

Examples:

- If C-only performs equivalently across diverse fixtures, do **not** add Goal/Context/Rationale requirements.
- If only X matters, do **not** infer a general Orientation object.
- If R helps only scoped-negative fixtures, keep the requirement fixture-/task-relative.
- If C111 improves performance but the causal contribution cannot be localized, record the result as a package-level effect, not proof of a latent orientation mechanism.
- If richer packets increase lock-in to obsolete history, treat that as evidence against unconditional history preservation.

## 15. Relationship to existing research

IR-01 is adjacent to but distinct from:

- **CA-01 / CASE E:** history-conditioned cognitive availability under matched current task;
- **Cognitive Orientation View v0.1:** bounded Soul research representation;
- **Continuum E0-T:** minimum sufficient representation for functional transfer from an Oracle State.

IR-01 does not modify any of them.

Especially:

```text
IR-01 ≠ CONTINUUM EXPERIMENT 0
IR-01 ≠ TCE PASS
IR-01 ≠ EDCA PASS
IR-01 ≠ ORIENTATION MODULE TEST
IR-01 ≠ IDENTITY CONTINUITY TEST
```

Continuum Experiment 0 remains independently gated and must not be contaminated by IR-01 pilot/evidence material.

## 16. Owner routing

| Surface | IR-01 role | Not authorized |
|---|---|---|
| ⚗️ CLOS | preregistration, discriminating methodology, evidence classification | runtime / owner adoption |
| 🌀 Mentaury Soul | cognition-side interpretation of eventual results | new cognition module / persistence |
| 🌎 Continuum | future comparison only if separately adopted after its own gates | modification of E0 / Pilot authorization |
| 💠 Crystal | possible later provenance implication if a concrete result requires it | automatic schema/storage change |
| 🪁 Mentaury-Kernel | cross-domain preservation question only | new invariant without residual gap |

## 17. Stop condition for this preregistration phase

Stop after:

1. protocol review;
2. fixture-family review;
3. anti-confound review;
4. Gold schema review;
5. explicit decision: `FREEZE PREREGISTRATION` or `REVISE BEFORE FREEZE`.

Do **not** build a harness or run a pilot from this draft.

## 18. Current disposition

```text
IR-01 PREREGISTRATION = DRAFT
EXECUTION = NOT_AUTHORIZED
PILOT = NOT_AUTHORIZED
EVIDENCE = NOT_AUTHORIZED
EVIDENCE LOCK = NOT_CREATED
NEW PRIMITIVE / MODULE / OWNER = NONE
ARCHITECTURE CONSEQUENCE = NONE
```
