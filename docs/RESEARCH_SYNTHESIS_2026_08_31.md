# 🔬 CLOS External Memory Research Synthesis — 2026-08-31

```text
Status: SUPPORTING RESEARCH SYNTHESIS
Canon: NO
Runtime authorization: NONE
Architecture adoption: NONE
New memory organ: NONE
```

## 0. 2026-09-01 bounded re-analysis update

A fresh live re-analysis did not establish a new memory architecture. It narrowed the remaining uncertainty.

Verified current heads used by this update:

```text
CLOS main:   5f3e5bb73d375fb544020e5656720d551da340b0 before this documentation sync
Crystal:     7509be14c274cdc83e8e00287f46a78f8ee33696
Titan:       78be30a89eb0ad698af1f4f3884db6728d076c06
```

The main corrections to the older 2026-08-31 wording are:

1. Broad `REACH → USE` is now too coarse. Current research distinguishes `R → S → T → U → A`.
2. Titan has bounded evidence for `R/S/T`; `S → T` can be lossy; `T → U` and `U → A` remain `NOT_ESTABLISHED`.
3. Crystal Phase-0 can close as a bounded owner review. `SOURCE → REPRESENTATION COVERAGE` remains genuinely `NOT_ESTABLISHED`, but exact replay, version invalidation/history preservation, bounded reread and authority firewalls are established in scope.
4. The highest-information reopen residual is no longer capability. It is **later-task task-conditioned sufficiency/reopen policy**.
5. No implementation gap is established by these residuals.
6. Current disposition remains `NO NEW CONSTRUCT`.

Current highest-information formulation:

```text
OLD COMPACT REPRESENTATION SUFFICIENT FOR T1
+ GENUINELY LATER TASK T2
→ does the system detect insufficiency for T2?
→ does it recover the correct source/version/span?
→ does it reopen boundedly when justified?
→ otherwise does it return safe UNKNOWN / REPRESENTATION_INSUFFICIENT?
```

```text
REOPEN CAPABILITY ≠ REOPEN POLICY
SAME-RUN REOPEN POLICY ≠ LATER-TASK REOPEN POLICY
NOT REPRESENTED ≠ ABSENT
```

Next bounded step: inspect Titan only for an already-existing later-task/cross-session reuse+reopen path. Do not create F2 or any new mechanism without separate Operator GO.

---

## 1. Why this research line was opened

The research question was not which external memory framework Velantrim should copy.

The question was whether current external memory systems and benchmarks exposed a real semantic or architectural gap in Velantrim, or whether they were better treated as donors of phenomena and discriminating tests for existing owners.

The investigation focused on:

- source vs representation loss;
- selection / representation coverage;
- retrieval reachability;
- currentness / supersession / historical truth;
- provenance and source lineage;
- use of retrieved evidence;
- the boundary between relevant memory and decision authority.

## 2. Research path

### NexusMem

Useful donor for:

- raw source vs derived essence/summary;
- provenance separated from trust;
- supersede / stale semantics;
- failure → fix history.

Disposition: reference donor, not architecture import.

### locomo-recordari

Used as a negative / empirical donor.

Useful findings included:

- coarse whole-session source expansion;
- selection / coverage loss hidden behind compact extraction;
- overloaded provenance/semantic relation vocabulary;
- mutation of supposedly verbatim source text;
- aggregate score hiding gained/lost churn;
- unconditional one-hop expansion without relation/sufficiency gates.

Disposition: `TEST EXISTING` / negative donor.

### Microsoft Memora, MemORAI, Structural Memory

These sharpened representation/granularity questions.

The durable result is not that one granularity is universally best. Instead:

```text
REPRESENTATION RICHNESS / GRANULARITY
↔
TASK DEPENDENCE / CONTEXT COST / RETRIEVAL BEHAVIOUR
```

A monotonic rule such as `span > turn > segment > session` is not established.

### From Recall to Forgetting / FAMA, ForgetEval, Supersede, STALE, A-TMA

These sharpened the distinction between:

```text
PROVENANCE
≠ CURRENT VALIDITY
≠ SUPERSESSION
≠ HISTORICAL TRUTH
≠ REVOCATION / DELETION / EXPIRATION
```

They also reinforced that explicit update and implicit invalidation are different evaluation phenomena.

### MEMPROBE, the two MemTrace papers, HaluMem, MemOps, LongMemEval-V2, MemoryArena, MemTrapBench

These shifted the research from a single memory score to failure localization:

```text
STORED
≠ REPRESENTED
≠ REACHABLE
≠ SELECTED
≠ USED
≠ CORRECTLY RESOLVED
≠ SAFE TO LET CONTROL A DECISION
```

Final-answer accuracy alone is insufficient to diagnose a memory system.

## 3. Methodological contradictions resolved during review

Repeated multi-model review found several errors introduced by the review process itself.

Important corrections:

- There are two distinct systems/papers named **Memora** and two distinct papers named **MemTrace**; evidence identity must use canonical title/version/arXiv identity.
- Microsoft Memora `0.838/0.833` vs `0.831/0.823` was not an internal contradiction; the values belong to different Policy vs Semantic retriever blocks.
- LongMemEval-V2 `72.5` is the average of `74.9` and `70.1`, not version drift; `451` manually curated questions is supported by the primary source.
- RC-4 was incorrectly called a ghost component when the reviewer had not read live Crystal. Live Crystal contains RC-4.

Methodological rule reinforced:

```text
MODEL AGREEMENT ≠ INDEPENDENT EVIDENCE
PARTIAL REVIEW CONTEXT ≠ LIVE-SOURCE ABSENCE
```

## 4. Live Crystal crosswalk changed the question

The live Crystal read showed that several relevant mechanisms already exist:

- source URI + SHA identity;
- exact / structural source locators;
- no persistent source body inside Reader domain objects;
- RC-4 pre-admission proposition candidates;
- RC-5 relation candidates without truth adjudication;
- source-version invalidation while preserving historical artifacts;
- bounded targeted reread mechanics and product-bridge orchestration;
- retrieval diagnostics and explicit authority firewalls.

This moved the research from architecture search to residual-boundary verification.

Important limit:

```text
ADDRESSABILITY ≠ REPRESENTATION COVERAGE
```

A perfect locator for represented candidates does not establish that all materially relevant source content entered the candidate space.

Likewise:

```text
LOCATOR EXISTS ≠ SOURCE DETAIL WAS USED
RETRIEVAL MATCH ≠ EVIDENCE
RELEVANT MEMORY ≠ DECISION AUTHORITY
```

### 4.1 Crystal bounded Phase-0 closure — 2026-09-01

Fresh live verification supports:

```text
SOURCE → REPRESENTATION COVERAGE: NOT_ESTABLISHED
LOCATOR → EXACT SOURCE REPLAY: IMPLEMENTED + TESTED
VERSION → STALE / HISTORICAL PRESERVATION: IMPLEMENTED + TESTED
CANDIDATE → RELATION DISCRIMINATION: IMPLEMENTED + MEASURED GAP
NEEDS_REVIEW → BOUNDED REREAD: IMPLEMENTED + TESTED
CRYSTAL → AUTHORITY FIREWALL: EXPLICIT / IMPLEMENTED + LOCAL TEST COVERAGE
```

This is a review closure, not a completeness claim. Broad Crystal auditing should stop unless a concrete later evidence question returns ownership to Crystal.

## 5. Distinctions that survived repeated review

```text
SOURCE ≠ REPRESENTATION
NOT REPRESENTED ≠ ABSENT
ADDRESSABILITY ≠ REPRESENTATION COVERAGE
STORED ≠ REACHABLE ≠ USED
CURRENT ≠ HISTORICALLY TRUE
SUPERSEDED ≠ ERASED ≠ FALSE
RETRIEVAL ≠ EVIDENCE
RELEVANT MEMORY ≠ DECISION AUTHORITY
FINAL ANSWER ACCURACY ≠ MEMORY DIAGNOSIS
```

These are evidence-backed research distinctions / evaluation concerns. This document does not promote them beyond their existing owner status.

### 5.1 Evidence-use refinement

Current bounded measurement vocabulary:

```text
R = retrieved
S = serialized
T = transmitted
U = demonstrably used
A = demonstrably answer-supporting
```

Titan evidence on 2026-09-01 establishes only bounded portions:

```text
R → S: ESTABLISHED for the measured Titan path
S → T: ESTABLISHED as potentially lossy
T → U: NOT_ESTABLISHED
U → A: NOT_ESTABLISHED
source_fact_ids membership → U/A: INSUFFICIENT EVIDENCE
```

Therefore:

```text
TRACE MEMBERSHIP ≠ SEMANTIC USE
SEMANTIC USE ≠ ANSWER SUPPORT
ANSWER SUPPORT ≠ DECISION AUTHORITY
```

No attribution engine follows.

## 6. How this work is intended to strengthen Velantrim

### Crystal

Preserve source/version/locator/provenance and expose representation/retrieval gaps without becoming a truth or decision engine.

### Titan

Inspect only where the unresolved boundary becomes retrieval use, source-reopen execution, context presentation or decision influence.

The next bounded Titan question is specifically whether a **later task / cross-session** path already exists that can detect that an older compact representation is no longer sufficient and recover/reopen the exact source region.

### Native Kernel

Inspect where the unresolved boundary concerns currentness, supersession, historical preservation or derived-view semantic invariants.

### CLOS

Maintain substrate-neutral distinctions around lossy representation, task-bounded sufficiency/stopping, UNKNOWN, currentness and authority ceilings.

### Graphiti / Continuum

Use only where the tested phenomenon actually intersects their existing project-local ownership. Do not assign them generic memory responsibilities by default.

## 7. Current disposition

```text
ARCHITECTURAL ADOPTION: NONE
NEW MEMORY ORGAN: NONE
BROAD MEMORY-FRAMEWORK HUNT: STOP
RECORDARI: REFERENCE / NEGATIVE DONOR
EXTERNAL MEMORY LITERATURE: EVIDENCE SOURCES, NOT AUTHORITIES
CURRENT MODE: BOUNDED OWNER LOCALIZATION / EVIDENCE HYGIENE
```

No `Memory OS`, FAMA engine, A-TMA overlay, cue-anchor layer, semantic Reader promotion, Recordari dependency, attribution service or new graph subsystem is authorized by this research.

## 8. Residual questions after 2026-09-01 localization

1. `SOURCE → REPRESENTATION COVERAGE` — genuinely `NOT_ESTABLISHED`; materially relevant content may fail to enter the candidate space.
2. `T → U → A` — actual semantic use and answer support remain unestablished beyond direct observations.
3. `LATER-TASK SUFFICIENCY / REOPEN` — highest-information current boundary: can a new task invalidate the sufficiency of an older compact view and trigger the correct bounded source reopen?
4. `CURRENT ↔ HISTORICAL RESOLUTION` — can current and historical queries preserve supersession without resurrection/erasure?
5. `MEMORY → DECISION AUTHORITY` — can relevant/correct memory influence decisions only within the permitted authority boundary?

These are crosswalk/test/contract candidates, not implementation instructions.

## 9. Stop rule

If an existing owner handles a bounded discriminating fixture without material semantic loss:

```text
DOCUMENT EVIDENCE
→ NO NEW CONSTRUCT
→ STOP
```

For the current later-task boundary, inspect existing Titan behaviour before proposing any fixture. If no behaviour is established, record `TEST GAP` or `CONTRACT GAP` first; do not infer an implementation gap.

This checkpoint records research history and rationale only. It does not change Canon, project-local authority, runtime authorization, Crystal V1 freeze, or sibling-project implementation status.
