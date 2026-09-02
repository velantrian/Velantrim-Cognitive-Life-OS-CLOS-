# 🔬 F2 Post-#436 Evidence Checkpoint — 2026-09-02

```text
Status: SUPPORTING BOUNDED EVIDENCE CHECKPOINT
Canon: NO
Implementation authorization: NONE
Runtime authorization: NONE
Production authorization: NONE
```

This checkpoint records the bounded state reached after the Titan F2 / later-task reopen sequence through merged PR #436. It supersedes older CLOS wording that said later-task reopen planning/execution were entirely `NOT_ESTABLISHED`, but it does not erase those historical checkpoints.

## 1. Verified owner baseline

Titan owner repository:

`velantrian/Velantrim-ExoCortex-Titan@1996086ef12ea5922f89262177258070a361e9dc`

Merge sequence relevant to F2:

- #429 — bounded later-task Hidden Exception fixture;
- #431 — binds omitted source-linked X to existing `unsupported_source_claim_ids`;
- #430 — task-conditioned representation sufficiency contract;
- #434 — exact source/version/span addressability for the omitted T2-material claim;
- #435 — bounded explicit later-task reopen planning contract;
- #436 — bounded exact-span reopen execution capability.

## 2. What is established

The bounded sequence now supports:

```text
T1 COMPACT MAY OMIT X
→ X REMAINS SOURCE-LINKED
→ UNSUPPORTED X SIGNAL EXISTS
→ CALLER EXPLICITLY SELECTS T2-RELEVANT CLAIM ID
→ EXACT SOURCE / REVISION / SPAN IS VALIDATED
→ BOUNDED READY REOPEN PLAN
→ BOUNDED EXACT-SPAN READER EXECUTION
```

PR #436 additionally preserves accepted Reader provenance by validating slice-local spans and rebasing them into full-source coordinates before downstream exposure.

Its reviewed malformed duplicate-span case was fixed fail-closed: one `span_id` cannot silently identify two different immutable source payloads and produce a false complete execution.

## 3. What is not established

The following arrow remains open:

```text
GENUINELY NEW TASK T2
→ SYSTEM RECOGNIZES OLD COMPACT VIEW IS INSUFFICIENT
→ REAL QUERY / ANSWER CALLER SELECTS RELEVANT CLAIM
→ REOPEN PATH EXECUTES
→ REOPENED MATERIAL IS DEMONSTRABLY USED
→ REOPENED MATERIAL SUPPORTS THE ANSWER
```

Not established:

- automatic sufficiency detection;
- automatic task relevance inference;
- production/query-path caller wiring;
- durable cross-session source/result recovery;
- semantic use `U`;
- answer support `A`;
- evidence admission;
- decision authority;
- production authorization.

## 4. Authority ceiling

```text
REOPEN CAPABILITY ≠ REOPEN POLICY
PLANNING ≠ EXECUTION
EXECUTION ≠ EVIDENCE
REOPEN RESULT ≠ SEMANTIC USE
SEMANTIC USE ≠ ANSWER SUPPORT
ANSWER SUPPORT ≠ DECISION AUTHORITY
CAPABILITY ≠ PERMISSION
CI GREEN ≠ SEMANTIC PROOF
```

No Crystal V1 reopening, new memory organ, new scheduler, new authority owner, or universal attribution/relevance engine follows from this checkpoint.

## 5. Post-merge caller localization

A bounded live Titan code inspection after #436 searched for actual caller usage of the later-task request/planner/executor chain.

Observed:

- `LaterTaskReopenRequest` is owner-local and used by the planning contract/tests;
- `unsupported_source_claim_ids` is produced by `GlobalDocumentSynthesis` and used as the explicit unsupported-claim signal;
- `source_grounded_digest` is exposed by the Reader product/CLI path;
- no existing real query/answer caller was established that already composes a genuinely later task into explicit claim selection + planner + executor.

Therefore:

```text
NO REAL CALLER ESTABLISHED
≠ CALLER IMPOSSIBLE
≠ IMPLEMENTATION DEFECT PROVED
```

The evidence supports only a localized documented gap.

## 6. Current disposition

```text
DOCUMENTED GAP
→ NO NEW CONSTRUCT
→ STOP IMPLEMENTATION
```

Do not invent a runtime layer merely to make the research diagram continuous.

Implementation should resume only when a concrete owner-local caller/use-case exists. Then first localize the exact missing arrow and classify it as one of:

```text
TEST GAP
CONTRACT GAP
IMPLEMENTATION GAP
```

Only evidence should justify the third class.

## 7. F2 status

```text
F2 HIDDEN EXCEPTION PHENOMENON = ESTABLISHED IN BOUNDED FIXTURE
LATER-TASK PLANNING CAPABILITY = ESTABLISHED ON TITAN MAIN
EXACT-SPAN EXECUTION CAPABILITY = ESTABLISHED ON TITAN MAIN
REAL LATER-TASK POLICY = NOT_ESTABLISHED
REAL ANSWER-PATH WIRING = NOT_ESTABLISHED
DURABLE CROSS-SESSION RECOVERY = NOT_ESTABLISHED
U / A = NOT_ESTABLISHED
F2 END-TO-END = NOT_SOLVED
```

## 8. Safest next research move

Stop broad F2 implementation work unless a real caller appears.

The next high-information work may move to another bounded candidate such as F1 Missing Hypothesis, F3 Same Stop / Different Reason, F4 Endogenous Confidence, or ES-02, while preserving the same rule:

```text
FIXTURE BEFORE PRIMITIVE
EVIDENCE BEFORE DESIGN
NO NEW CONSTRUCT WHERE EXISTING SEMANTICS SUFFICE
```
