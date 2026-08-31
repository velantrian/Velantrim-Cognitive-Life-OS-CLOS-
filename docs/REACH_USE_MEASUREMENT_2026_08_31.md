# 🔬 CLOS Reach → Use Measurement Note — 2026-08-31

```text
Status: SUPPORTING RESEARCH NOTE
Canon: NO
Runtime authorization: NONE
Architecture adoption: NONE
New module: NONE
```

## 1. What is already stable

The following distinction is mature enough to be treated outside research as a Cognitive OS architectural invariant:

```text
RETRIEVED
≠ SERIALIZED
≠ TRANSMITTED
≠ USED
≠ ANSWER-SUPPORTING
≠ DECISION-AUTHORIZING
```

Research should therefore not spend effort re-proving that these stages are conceptually distinct.

## 2. What remains genuinely unresolved

The residual research question is narrower:

```text
HOW DO WE RELIABLY ESTABLISH ACTUAL USE / SUPPORT?
```

In particular:

- did an item survive retrieval-to-context serialization?
- did it survive provider-specific packing/truncation?
- did the reasoner actually rely on it?
- did it materially support the final answer?
- was it merely present but ignored?
- would removing or changing it alter the answer in a task-relevant way?

## 3. Measurement vocabulary

A useful measurement frame is:

```text
R = retrieved item IDs
S = serialized item IDs
T = transmitted item IDs
U = demonstrably used / answer-supporting item IDs
```

The research problem is not to assume these sets are equal, but to determine which transitions can be measured reliably enough for the task under test.

```text
R != necessarily S
S != necessarily T
T != necessarily U
```

## 4. Why this was localized from live Titan

A bounded Titan crosswalk showed two concrete phenomena without requiring a new architecture:

1. rich retrieved fact structures can be flattened by the legacy answer prompt builder before model use;
2. provider-specific packing can further truncate model-facing context.

Therefore:

```text
RETRIEVED ≠ ACTUALLY PRESENT AFTER PACKING
```

and mere presence in an earlier pipeline stage cannot justify a claim of answer support.

The same crosswalk also showed that current reasoning-trace population can represent available/retrieved fact IDs without proving actual semantic use. This is a measurement/semantic-contract question, not evidence for a new memory organ.

## 5. Candidate fixture family

Future bounded fixtures may test one or more of the following:

### A. Serialization survival
Given a known retrieved set, verify which items actually enter model-facing context.

### B. Transmission survival
Given serialized context, verify which items survive provider-specific packing/truncation.

### C. Counterfactual use
Remove or alter one discriminating item while holding the rest stable and test whether the answer changes in the predicted way.

### D. Qualifier / exception dependence
Provide an answer-critical qualifier, exception or temporal scope and test whether the final answer respects it.

### E. Conflict dependence
Inject a material conflict and test whether the answer changes from confident resolution to conflict/uncertainty handling.

## 6. What does not count as proof of use

By itself, none of the following establishes semantic use:

```text
retrieval rank
prompt presence
attention-like salience
model self-report
post-hoc citation generation
final-answer correctness
trace membership populated from retrieved facts
```

These may be signals or instrumentation, but stronger attribution claims require stronger evidence.

## 7. Research stopping rule

If a bounded fixture shows that an existing owner can measure or safely report the relevant transition without material semantic loss:

```text
DOCUMENT EVIDENCE
→ NO NEW CONSTRUCT
→ STOP
```

If exact semantic use cannot be established, the system may still safely report weaker observed stages such as `RETRIEVED`, `SERIALIZED` or `TRANSMITTED` rather than inventing `USED`.

## 8. Owner boundary

```text
Cognitive OS:
  owns the stable distinction / anti-overclaim contract

CLOS Research:
  studies how actual use/support can be measured

Titan:
  may later host implementation-specific instrumentation or fixtures
  only if separately authorized

Crystal:
  no change required by this note
```

This note records a residual measurement problem only. It does not authorize implementation, runtime change, new attribution service, new memory subsystem or new authority root.