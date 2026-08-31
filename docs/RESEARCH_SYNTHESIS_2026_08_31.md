# 🔬 CLOS External Memory Research Synthesis — 2026-08-31

```text
Status: SUPPORTING RESEARCH SYNTHESIS
Canon: NO
Runtime authorization: NONE
Architecture adoption: NONE
New memory organ: NONE
```

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

## 6. How this work is intended to strengthen Velantrim

### Crystal

Preserve source/version/locator/provenance and expose representation/retrieval gaps without becoming a truth or decision engine.

### Titan

Inspect only where the unresolved boundary becomes retrieval use, source-reopen execution, context presentation or decision influence.

### Native Kernel

Inspect where the unresolved boundary concerns currentness, supersession, historical preservation or derived-view semantic invariants.

### CLOS

Maintain substrate-neutral distinctions around lossy representation, task-bounded sufficiency/stopping, UNKNOWN, currentness and authority ceilings.

### Graphiti / Continuum

Use only where the tested phenomenon actually intersects their existing project-local ownership. Do not assign them generic memory responsibilities by default.

## 7. Current disposition — 2026-08-31

```text
ARCHITECTURAL ADOPTION: NONE
NEW MEMORY ORGAN: NONE
BROAD MEMORY-FRAMEWORK HUNT: STOP
RECORDARI: REFERENCE / NEGATIVE DONOR
EXTERNAL MEMORY LITERATURE: EVIDENCE SOURCES, NOT AUTHORITIES
CURRENT MODE: READ-ONLY OWNER CROSSWALK / EVIDENCE HYGIENE
```

No `Memory OS`, FAMA engine, A-TMA overlay, cue-anchor layer, semantic Reader promotion, Recordari dependency, or new graph subsystem is authorized by this research.

## 8. Residual questions

The remaining task is to establish whether these boundaries are real and untested in the existing owners:

1. `SOURCE → REPRESENTATION COVERAGE` — was materially relevant content represented at all?
2. `REACH → USE` — if evidence was reachable/replayed, was its detail/qualification/conflict actually used?
3. `NEEDS_REVIEW → EPISTEMIC SUFFICIENCY / REOPEN` — does bounded reread happen for the correct semantic reason and target?
4. `CURRENT ↔ HISTORICAL RESOLUTION` — can current and historical queries preserve supersession without resurrection/erasure?
5. `MEMORY → DECISION AUTHORITY` — can relevant/correct memory influence decisions only within the permitted authority boundary?

These are fixture/crosswalk candidates, not implementation instructions.

## 9. Stop rule

If an existing owner handles a bounded discriminating fixture without material semantic loss:

```text
DOCUMENT EVIDENCE
→ NO NEW CONSTRUCT
→ STOP
```

This checkpoint records research history and rationale only. It does not change Canon, project-local authority, runtime authorization, Crystal V1 freeze, or sibling-project implementation status.
