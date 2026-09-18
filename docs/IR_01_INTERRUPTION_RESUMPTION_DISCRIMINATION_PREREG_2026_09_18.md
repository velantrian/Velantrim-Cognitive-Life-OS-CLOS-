# 🧠🪢 IR-01 — Interruption / Resumption Information-Class Discrimination

**Date:** 2026-09-18  
**Status:** `PREREGISTRATION DRAFT · RESEARCH ONLY · NO EXECUTION AUTHORIZATION`  
**Owner surface:** CLOS research methodology  
**Related owners:** Mentaury Soul cognition/orientation research; Continuum continuity/handoff research  
**Architecture consequence:** `NONE`

## 0. Purpose

IR-01 operationalizes one bounded question left by the donor reconciliation cycle:

> After an interruption, which information classes materially improve correct resumption when the fixture-level world/reference state is fixed and non-target information, surface format, and payload budget are controlled?

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

C, G, X and R are **experimental information classes**, not latent cognitive modules. In particular, R is named only `RATIONALE` in the experiment. A later result may motivate discussion of a *candidate orientation-relevant information class*, but IR-01 does not treat R, or the bundle G/X/R, as an `Orientation` construct.

## 2. Primary null

The minimum-complexity null is:

> **C alone is sufficient for the tested resumption tasks; adding G, X, or R does not produce a material improvement in prespecified resumption outcomes.**

A null-preserving result is a successful research result.

IR-01 gives no prior credit to richer state packages.

For IR-01, `C-only` means CONTENT plus the arm-invariant common non-target harness material defined below. It does **not** include semantic labels or placeholders that reveal that Goal, Context or Rationale were withheld.

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

### 3.1. Fixture-level atomic proposition ledger

Before arm rendering, every fixture must define one arm-invariant atomic proposition ledger:

```text
P = {p1, p2, ... pn}

For each task-material proposition pi:
CLASS(pi) ∈ {C, G, X, R, N}

N = common non-target information
```

The same fixture-level ledger governs every arm. The default rule is **exclusive semantic assignment**: a task-material proposition may not be silently duplicated or paraphrased into another target class merely to make a richer arm easier.

Required construction checks:

- task-material CONTENT must not restate the current Goal;
- CONTENT must not silently encode currentness/scope that is assigned to Context;
- CONTENT must not silently carry the documented grounds assigned to Rationale;
- Rationale must not merely restate Goal;
- Rationale must not silently duplicate Context applicability conditions;
- Context must not silently restate Goal;
- common non-target information `N` must be identical across compared arms.

Natural semantic overlap may make perfect separation impossible. Such overlap must be recorded explicitly in a fixture-level overlap map:

```text
OVERLAP(pi, pj) = documented semantic dependence / entailment
```

If an omitted factor is materially reconstructable from another retained target class because of such overlap, the affected single-factor contrast for that fixture is:

```text
NOT_IDENTIFIABLE
→ report UNKNOWN for that factor contrast
→ do not use that fixture as confirmatory evidence for that factor
```

The fixture may still be usable for other factor contrasts.

### 3.2. One reference state → arm-specific visible subsets

The preregistered data relationship is:

```text
ONE FIXTURE WORLD / REFERENCE STATE
        ↓
ONE ARM-INVARIANT GOLD
        ↓
ONE ATOMIC PROPOSITION LEDGER
        ↓
ARM-SPECIFIC VISIBLE SUBSETS
```

Gold truth does not change by arm. Only model-visible experimental information changes.

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

Arm names are experimental labels only; they are not architectural state names and must never be shown to the tested successor model.

## 5. Matching / anti-confound controls

The intended contrast is semantic information class, not prompt quality.

The matching claim is deliberately limited:

```text
FIXED FIXTURE WORLD / REFERENCE STATE
+ MATCHED NON-TARGET INFORMATION
+ MATCHED MODEL-VISIBLE FORMAT / BUDGET
≠ IDENTICAL SEMANTIC INFORMATION
```

The semantic presence/absence of G, X and R is the manipulated variable.

### 5.1. Common controls

Across compared arms for the same fixture:

- identical fixture-level world/reference state and atomic proposition ledger;
- identical common non-target set `N`;
- identical continuation prompt;
- identical system prompt, stop conditions, hidden harness context and tool policy;
- identical model/provider/settings within a declared run family;
- fresh isolated successor context for every arm;
- no access to prior arm outputs;
- no tools, retrieval, memory connectors, hidden transcript access or benchmark-side memory unless separately preregistered for **all** compared arms;
- no provider conversation/session reuse across arms;
- cache behavior must be disabled/isolated where technically possible, otherwise declared before evidence and treated as a possible limitation;
- no arm-specific hints such as "the missing goal is important".

### 5.2. Condition-blind model-visible packet

The tested model must not see:

- arm IDs such as `C000` / `C111`;
- G/X/R factor names as packet headers;
- filenames or metadata that encode condition;
- semantic absence labels;
- `MASKED_FOR_IR01` or equivalent factor-revealing markers;
- Gold, evaluator labels, expected outcome, or condition-specific instructions.

Model-visible resume material must use a generic envelope with opaque/generic item slots. Experimental propositions and filler occupy those slots without model-visible class labels.

### 5.3. Budget and neutral filler

For each declared run family, the later Evidence Lock must freeze:

- one deterministic tokenizer / counting function;
- one serialized packet budget `B`;
- one versioned, condition-independent neutral filler pool;
- one deterministic packet serializer.

Primary compared arms for a fixture must have equal serialized packet token count under the frozen counting function:

```text
TOKENS(packet_arm) = B
```

Neutral filler:

- must contain no task-domain facts;
- must not mention Goal / Context / Rationale / missing information classes;
- must be drawn/generated by a rule independent of arm outcome;
- must not be selected after observing model behavior.

If exact equality cannot be achieved under the frozen counting function, that comparison is not evidence-eligible until the mismatch is resolved. Provider-reported token telemetry, when available, is recorded diagnostically; a systematic arm-dependent discrepancy that could explain the result downgrades the comparison to `UNKNOWN`.

### 5.4. Position / recency control

Experimental information must not be permanently bound to one ordinal position.

Design-level rule:

```text
G / X / R-bearing propositions and matched filler
→ preregistered counterbalancing / permutation
→ no factor always occupies the same early/late position
```

The exact permutation schedule may be generated later, but it must be frozen in the Evidence Lock before evidence execution.

### 5.5. Arm blinding and randomization

- the tested model is condition-blind except for the semantic information intentionally supplied;
- arm order and fixture order rules must be frozen before evidence execution;
- exact randomization seeds/schedule may be deferred to the Evidence Lock;
- any human or nondeterministic evaluator must be blind to arm identity until scoring is complete where technically possible.

Semantic content may itself reveal a Goal, Context or Rationale when that information is present. That is the intended manipulation. What is forbidden is revealing **which class was withheld** through labels, masks, metadata, position or harness differences.

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

IR-F3 is explicitly a bounded necessity/stress fixture. If X is intentionally the only source that disambiguates two valid next steps, an X effect demonstrates utility/necessity for that fixture construction; it does **not** establish general Context superiority or an Orientation construct.

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

For every fixture, one human-authored **arm-invariant Gold** record must be frozen before evidence execution.

The Gold describes the fixture-level world/reference truth. It must not encode a different truth for richer vs poorer arms.

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
- `forbidden_next_step_variants` where applicable;
- `forbidden_promotions`;
- `unknowns_that_must_remain_unknown`;
- fixture-specific scoring atoms for O1–O7;
- reference to the frozen atomic proposition ledger and overlap map.

Required invariant:

```text
ONE FIXTURE WORLD / REFERENCE STATE
→ ONE ARM-INVARIANT GOLD
→ ARM-SPECIFIC VISIBLE SUBSETS
```

Acceptable answer variants, forbidden variants and any qualitative rubric must be frozen before evidence outputs are observed.

The evaluated response-generating model must not:

- write, approve or revise its own Gold;
- score its own output;
- see evaluator-only metadata.

Evaluation must be performed by a separate evaluator process. If any evaluator judgment is nondeterministic or human-coded, arm identity must be hidden until scoring is complete where technically possible. The exact evaluator/rubric version must be frozen in the Evidence Lock.

## 8. Outcomes

Score outcomes separately. Do not collapse them into one weighted "continuity score".

Outcome roles are frozen as:

```text
O1 = PRIMARY task outcome
O2–O7 = SECONDARY / ERROR-ATOM outcomes
O8 = DIAGNOSTIC only
```

O2/O3 may causally contribute to O1 and are not independent confirmations of O1. O4/O5 are related but separately scored error atoms. O6/O7 may overlap in some responses but require separate fixture-level coding rules; they must not be counted as independent replications of one effect.

For every fixture, O1 must be scored against the preregistered `correct_next_step_class` plus frozen acceptable/forbidden variants as `PASS`, `FAIL`, or `UNKNOWN`. O2–O7 require fixture-specific observable scoring atoms frozen before evidence.

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

## 9. Model-visible response protocol

The successor must be externally scorable without requesting chain-of-thought, but the response format must not teach the experimental constructs.

The same neutral continuation instruction is used for every arm:

> Continue the interrupted work using only the supplied resume material. Give the next bounded step and only the qualifications needed to avoid an incorrect continuation. If the supplied material is insufficient, return `UNKNOWN` or request the minimal clarification needed. Do not provide private chain-of-thought.

The tested model is **not** given output fields named Goal, Context, Rationale, rejected routes or source/rationale status.

A separate evaluator extracts/scores O1–O7 from the bounded response using the frozen Gold/rubric.

If a structured parser becomes necessary later, any model-visible schema must remain factor-neutral and must be reviewed/frozen before evidence; it may not reintroduce semantic construct cues that distinguish G/X/R conditions.

Short externally reportable justification is allowed, but hidden reasoning traces are neither requested nor scored.

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

A fixture marked `NOT_IDENTIFIABLE` for a factor because of proposition overlap is excluded from that factor's confirmatory contrast and reported as `UNKNOWN` for that estimand.

IR-01 causal interpretation is intervention-level only:

```text
SUPPLYING INFORMATION CLASS X
→ changed measured output under the tested setup
```

It does not establish a latent human/AI cognitive mechanism, universal necessity, or architecture.

Results are bounded to the declared model/provider/run family unless independently replicated across separately declared model families.

## 11. PASS / FAIL / UNKNOWN and material-improvement rule

Before evidence execution, the Evidence Lock must freeze a **factor claim matrix** for each of G, X and R:

- eligible fixture families;
- target outcome(s);
- expected direction of effect;
- critical-error outcome(s) that must not materially regress;
- minimum decision criterion / threshold for the declared run family.

A general factor-level `PASS` requires:

1. same-direction improvement on the prespecified target outcome(s);
2. in at least **two prespecified eligible fixture families**;
3. meeting the frozen minimum decision criterion;
4. with no frozen material regression on critical-error outcomes.

If fewer than two suitable fixture families are preregistered for a factor at Evidence Lock, IR-01 may report only fixture-specific results for that factor; it may not promote them to a general factor-level `PASS`.

### PASS for a candidate information class

A class is provisionally useful only when the rule above is satisfied without merely increasing unsupported confidence, verbosity, prompt compliance or invented rationale.

### FAIL / no material gain

A richer packet fails to earn general complexity for the tested scope if:

- the corresponding class produces no reproducible improvement on the prespecified target outcomes;
- apparent gains are attributable to formatting, label leakage, position or budget artifacts;
- simpler arms perform equivalently on the relevant prespecified contrasts.

### TRADEOFF / UNKNOWN

Mixed benefit/harm is **not** silently converted into PASS.

Use `TRADEOFF` / `UNKNOWN` when, for example:

- a target outcome improves while a prespecified critical-error outcome materially regresses;
- benefit is fixture-specific and does not satisfy the general factor rule;
- fixture Gold is ambiguous;
- manipulated fields are not separable or a contrast is `NOT_IDENTIFIABLE`;
- budget/format matching fails materially;
- model/provider behavior is unstable;
- sample/run count is insufficient;
- the successor has unintended access to omitted information;
- multiple causal explanations remain observationally equivalent.

No weighted aggregate score may override a critical-error regression.

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
- using the same exact pilot wording as later evidence wording without an explicit contamination decision;
- exposing arm IDs, condition metadata, factor names, semantic mask labels, condition-bearing filenames or expected outcomes to the tested model;
- using a different system prompt, stop sequence, hidden harness context, conversation state, tool policy or model setting for selected arms;
- reusing provider conversation/session state or cross-arm cached conversational context;
- binding one factor permanently to one ordinal packet position;
- allowing the tested response generator to score its own output;
- revealing arm identity to a human/nondeterministic evaluator before scoring when blinding is technically possible.

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

The Evidence Lock must freeze at minimum:

- runs per arm;
- concrete fixture count and evidence variants;
- random seeds / randomization procedure where applicable;
- exact provider/model identifier and model settings for every declared run family;
- arm-order rule/schedule;
- fixture-order rule/schedule;
- exact field-position counterbalancing / permutation schedule;
- atomic proposition ledgers and overlap maps;
- arm-invariant Gold and acceptable/forbidden variants;
- factor claim matrix and material-improvement thresholds;
- system prompt and neutral continuation prompt;
- stop conditions and hidden harness context;
- tool/retrieval policy;
- conversation/session/cache isolation policy;
- packet serializer/schema;
- deterministic tokenizer/counting function and packet budget `B`;
- versioned neutral filler pool;
- evaluator implementation/rubric/version;
- pilot/evidence contamination partition.

The numerical values may be chosen later, but they must be frozen **before any evidence run**.

Evidence mode is fail-closed: if any required lock item is missing or differs from the locked value, the affected comparison is not evidence-eligible.

The design-level field-position rule is already frozen by §5.4; only the exact permutation schedule is deferred to the Evidence Lock.

## 14. Falsification rules

IR-01 must be capable of reducing, not only expanding, state requirements.

Examples:

- If C-only performs equivalently across diverse fixtures, do **not** add Goal/Context/Rationale requirements.
- If only X matters, do **not** infer a general Orientation object.
- If R helps only scoped-negative fixtures, keep the requirement fixture-/task-relative.
- If C111 improves performance but the causal contribution cannot be localized, record the result as a package-level effect, not proof of a latent orientation mechanism.
- If richer packets increase lock-in to obsolete history, treat that as evidence against unconditional history preservation.
- If no preregistered factor or interaction satisfies its frozen decision rule, do **not** rescue the hypothesis by redefining the null result as evidence for an emergent or hidden Orientation construct.
- If an interaction is observed without an identifiable component effect, report a bounded interaction/package effect only.
- If the effect appears only in one declared model/provider/run family, keep the conclusion model/run-family-bounded.
- If controls, separability or scoring are insufficient, `UNKNOWN` is a valid final result.

## 15. Relationship to existing research

IR-01 is adjacent to but distinct from:

- **CA-01 / CASE E:** history-conditioned cognitive availability under matched current task;
- **Cognitive Orientation View v0.1:** bounded Soul research representation;
- **Continuum E0-T:** minimum sufficient representation for functional transfer from an Oracle State.

IR-01 does not modify any of them.

Within IR-01 the experimental factor is named only `RATIONALE`. Any later phrase such as "orientation-relevant" is an interpretation layer applied **after** results and cannot convert an R, G, X or interaction effect into proof of a unitary Orientation construct.

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
