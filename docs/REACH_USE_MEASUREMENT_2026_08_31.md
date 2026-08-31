# 🔬 CLOS Reach → Use Measurement Note — 2026-08-31

```text
Status: SUPPORTING RESEARCH NOTE
Canon: NO
Runtime authorization: NONE
Architecture adoption: NONE
New construct: NONE
```

## 1. Why this note exists

The external-memory review and bounded Titan crosswalk localized one residual question more precisely:

```text
REACHABLE / RETRIEVED
≠ SERIALIZED
≠ TRANSMITTED
≠ USED
≠ ANSWER-SUPPORTING
```

The distinction itself is mature enough to be expressed as a Cognitive OS semantic contract.

What remains research is **how to measure or prove the later stages**, especially `USED` and `ANSWER-SUPPORTING`, without overclaiming from mere context presence.

This note therefore narrows the research surface. It does not create a new architecture component.

## 2. Live bounded evidence that motivated the refinement

The 2026-08-31 Titan crosswalk established several different stages in the current system:

- retrieval can produce a rich `pipeline_facts` set;
- the legacy answer prompt serializes only a subset of each fact's structure;
- provider-specific packing can further alter or truncate transmitted context;
- downstream route/orientation logic can consume context while remaining intentionally shadow-only;
- the authoritative model answer path receives retrieved facts in its system prompt;
- actual semantic use of each fact by the model is not directly demonstrated;
- existing trace population can record available/retrieved fact IDs without proving that each fact materially supported the answer.

These observations refine the previous broad `REACH → USE` question into a stage-localized measurement problem.

## 3. Stable distinction vs research question

### Stable semantic distinction

```text
CONTEXT PRESENT ≠ CONTEXT USED
RETRIEVED EVIDENCE ≠ EVIDENCE USED
TRACE OF AVAILABLE EVIDENCE ≠ TRACE OF ACTUAL REASONING SUPPORT
```

This is not the unresolved part.

### Unresolved research questions

1. What observation is sufficient to classify an item as `USED`?
2. What observation is sufficient to classify an item as `ANSWER-SUPPORTING`?
3. How should the system distinguish merely present context from causally material context?
4. When provider packing removes or truncates an item, how should the system record that loss?
5. How should structured qualifiers, temporal scope, provenance and uncertainty be tested for survival into reasoning?
6. Can counterfactual removal or substitution demonstrate contribution reliably enough for bounded system tests?
7. When conflicting evidence is present, can the system demonstrate that the conflict affected the answer rather than merely appearing in context?
8. How should attribution behave when the model already knows the same information parametrically?

## 4. Candidate measurement vocabulary

For research and fixtures, distinguish at least four sets:

```text
R = retrieved item identifiers
S = serialized item identifiers
T = transmitted item identifiers
U = demonstrably used / answer-supporting item identifiers
```

Important:

```text
R != necessarily S
S != necessarily T
T != necessarily U
```

This notation is a measurement aid, not a required runtime schema.

## 5. Candidate fixture families

These are candidates only. No fixture is authorized by this document.

### F1 — Tail truncation

Place a uniquely necessary fact late enough that provider packing may remove it.

Measure whether:

- it is in `R`;
- it is in `S`;
- it survives into `T`;
- the answer changes when it is absent from `T`.

### F2 — Structured qualifier survival

Use a claim whose correctness depends on a qualifier, exception, temporal scope or uncertainty field that is not safely reducible to bare claim text.

Measure whether the structured distinction survives each stage.

### F3 — Counterfactual evidence removal

Hold task and model configuration fixed while removing one candidate item.

Observe whether answer content, uncertainty, route or decision-relevant output changes in the predicted direction.

Limitation: answer change alone does not prove internal causal mechanism; it is bounded behavioural evidence only.

### F4 — Conflicting evidence

Provide two materially conflicting source-linked items.

Measure whether the system:

- transmits both;
- surfaces conflict;
- avoids silently selecting one without justification;
- changes answer status or uncertainty appropriately.

### F5 — Parametric-knowledge confound

Use synthetic or freshly generated task-local facts that the model cannot plausibly know beforehand.

Purpose: reduce the confound where a correct answer is produced from prior model knowledge rather than supplied evidence.

## 6. Falsifiers / downgrade conditions

Downgrade or close this research line if bounded fixtures show that existing owners already expose sufficient stage provenance and no material semantic error occurs from collapsing later stages for the relevant task class.

Likewise, do not promote a universal attribution mechanism unless repeated evidence shows that a simpler owner-local contract is insufficient.

## 7. Owner boundary

### Cognitive OS

Owns the semantic distinction that pipeline presence is not equivalent to actual support.

### CLOS

Owns the substrate-neutral research question of how to measure `USED` / `ANSWER-SUPPORTING` without false attribution.

### Titan

May later host bounded implementation tests because current evidence localized concrete retrieval/serialization/transmission behavior there. This note does not authorize changes.

### Crystal

No change is required from this finding alone.

## 8. Anti-drift rule

```text
REAL MEASUREMENT GAP
≠ NEW MEMORY ORGAN
≠ NEW COGNITIVE MODULE
≠ UNIVERSAL ATTRIBUTION ENGINE
```

The preferred progression remains:

```text
semantic distinction
→ bounded measurement
→ owner-local fixture
→ evidence
→ smallest justified contract change, if any
```

If measurement shows no material residual failure:

```text
DOCUMENT EVIDENCE
→ NO NEW CONSTRUCT
→ STOP
```
