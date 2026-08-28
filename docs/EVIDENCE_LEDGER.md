# 📚 CLOS Evidence Ledger

```text
Status: SUPPORTING RESEARCH LEDGER
Canon: NO
Runtime authority: NONE
Purpose: preserve claim → evidence → limitation → disposition traceability
```

This ledger is deliberately smaller than the full research history in Notion / Google Docs. It records the evidence needed to understand why the current CLOS research families survived, what that evidence does **not** prove, and how the result is currently classified.

## Evidence classes

```text
DIRECT SUPPORT
STRUCTURAL ANALOGUE
COUNTEREXAMPLE
CONTESTED INTERPRETATION
INSPIRATION ONLY
NEGATIVE EVIDENCE / FAILED REPLICATION
LONGITUDINAL BEHAVIOURAL OBSERVATION
```

`MULTIPLE AI REPORTS AGREE ≠ INDEPENDENT REPLICATION`.

AI research passes are treated as synthesis/search assistance. Scientific support comes from the underlying literature or from explicitly bounded behavioural fixtures.

---

## 1. 🌍 Coverage / possibility-space adequacy

### CLOS claim under test

```text
UNCERTAINTY WITHIN THE REPRESENTED POSSIBILITY SPACE
≠
ADEQUACY OF THE REPRESENTED POSSIBILITY SPACE ITSELF
```

| Source / family | Class | Supports | Does **not** prove |
|---|---|---|---|
| Open-world / open-set recognition research, including Bendale & Boult, *Towards Open World Recognition* (CVPR 2015) | DIRECT SUPPORT for machine failure family | Closed-set confidence is insufficient when material inputs/classes may lie outside the represented set | A universal percentage of “world coverage” |
| Model misspecification / M-open statistical reasoning | DIRECT SUPPORT for distinction | Inference may be coherent conditional on a model family while the family itself is incomplete/wrong | A unique CLOS scalar or module |
| Unknown-unknown discovery work, including Lakkaraju et al. (AAAI 2017) | DIRECT SUPPORT for practical discovery failure | Important errors can sit outside the currently inspected/represented region | Exhaustive discovery of all unknown unknowns |
| Open-set/OOD detection | STRUCTURAL ANALOGUE / PARTIAL TOOL | Some novelty can be detected relative to a model/distribution | `OOD DETECTION = KNOWLEDGE OF HYPOTHESIS-SPACE COMPLETENESS` |

Disposition: `REFINE / CROSSWALK`.

No `Coverage Module` and no universal coverage scalar are established.

### Falsifier / downgrade condition

If all material failures attributed to coverage can be expressed without semantic loss by existing uncertainty/currentness/open-world qualifications, downgrade to `NO NEW CONSTRUCT`.

---

## 2. 💎 Lossy representation / candidate access

### CLOS claim under test

```text
SOURCE ≠ LOSSY DERIVED VIEW
NOT REPRESENTED ≠ ABSENT
NOT SURFACED AS A CANDIDATE ≠ IRRELEVANT
```

The strongest proposed failure is **candidate-space deformation**: a lossy representation controls what downstream reasoning ever gets to consider.

| Source / family | Class | Supports | Does **not** prove |
|---|---|---|---|
| Information Bottleneck / task-relative compression (Tishby, Pereira & Bialek, 1999) | STRUCTURAL ANALOGUE | Compression is meaningful relative to a preservation/relevance objective | A compressed view knows every future-relevant omitted fact |
| Rate-distortion theory | STRUCTURAL ANALOGUE | Lossy representation trades preserved information against resource/rate constraints | A universal CLOS distortion function |
| Search / diagnostic generation-vs-evaluation failures | DIRECT SUPPORT for pipeline failure family | An evaluator cannot evaluate an alternative that never enters the active set | Every candidate generator must be exhaustive |
| Retrieval / embedding-search practical failure modes | IMPLEMENTATION ANALOGUE | Approximate retrieval can suppress rare/differently expressed material before reasoning | Mandatory embeddings, RAG, GraphRAG or a specific fallback |
| Human gist / fuzzy-trace literature | STRUCTURAL ANALOGUE | Different representations preserve different information for later judgment | Mandatory digital gist/verbatim layers |

Rejected:

```text
LOSSY VIEW MAY NEVER EXCLUDE
```

Retained:

```text
LOSSY VIEW MAY SOMETIMES EXCLUDE WITHIN A JUSTIFIED, SCOPED SUFFICIENCY CONTRACT.
LOSSY OMISSION MUST NOT SILENTLY BECOME GLOBAL NEGATIVE EVIDENCE.
DECLARED LOSS ≠ COMPLETE KNOWLEDGE OF EVERYTHING OMITTED.
```

Disposition: `STRONGEST MATERIAL RESIDUAL CANDIDATE · REFINE / FIXTURE`.

### Falsifier / downgrade condition

If F2 Hidden Exception is handled entirely by existing Meaning Envelope, source lineage, currentness and UNKNOWN semantics, disposition becomes `MERGE / NO NEW CONSTRUCT`.

---

## 3. 🛑 Task-bounded sufficiency / reason-typed stopping

```text
STOP ≠ TRUTH ESTABLISHED
STOP ≠ SEARCH EXHAUSTED
JUSTIFIED STOP ≠ PERMANENT CLOSURE
```

| Source / family | Class | Supports | Does **not** prove |
|---|---|---|---|
| Herbert Simon — bounded rationality / satisficing | DIRECT SUPPORT for phenomenon | Decision systems often terminate without exhaustive optimization | A single quantitative CLOS stopping equation |
| Charnov, Marginal Value Theorem (1976) | STRUCTURAL ANALOGUE / FORMAL CASE | Leaving a search/foraging patch can be rational before exhaustion | A universal cognition law or truth criterion |
| Rational metareasoning / value-of-computation | DIRECT SUPPORT for one stopping basis | Further computation can be evaluated by expected decision value vs cost | Authority, prohibition, deadlines and irreducible uncertainty all reduce to one scalar |
| Animal uncertainty-response / opt-out work | STRUCTURAL ANALOGUE | Some systems change behaviour when basis is weak/uncertain | Human-like conscious metacognition or mandatory digital mechanism |

Minimum obligation:

```text
TERMINATION MUST NOT ERASE THE MATERIAL REASON AND STATUS UNDER WHICH COGNITION TERMINATED.
```

Disposition: `MERGE / REFINE`.

---

## 4. ⚖️ Endogenous state vs external-world evidence

```text
ENDOGENOUS SIGNAL ≠ EXTERNAL-WORLD EVIDENCE BY DEFAULT
```

| Source / family | Class | Supports | Does **not** prove |
|---|---|---|---|
| Illusory-truth / repetition-familiarity research | DIRECT SUPPORT for failure family | Repetition/familiarity can increase judged truth/confidence without new independent world evidence | Internal states can never be evidential |
| Information cascades / dependent social testimony | DIRECT SUPPORT for provenance problem | Agreement count may exceed independent evidence count | Consensus has zero value in all settings |
| Dataset shift / calibration drift | STRUCTURAL ANALOGUE | Internal confidence calibration can become stale under changed conditions | Universal drift detector or auto-correction rule |

Absolute claim rejected:

`INTERNAL STATE CAN NEVER BE EVIDENCE`.

A signal may have evidential role when a justified causal/provenance/calibration relation exists.

Disposition: `VERIFY / MERGE INTO EXISTING PROVENANCE + EPISTEMIC STATUS DISCIPLINE`.

---

## 5. ♻️ Retrieval / reconstruction / revision

| Source / family | Class | Supports | Does **not** prove |
|---|---|---|---|
| Nader, Schafe & LeDoux, Nature 2000 | DIRECT SUPPORT for bounded biological phenomenon | Reactivated memory can become labile under experimental conditions | `EVERY RETRIEVAL → REVISION` or required digital Reconsolidation Module |
| Reconsolidation boundary-condition literature | CONTESTED / CONDITIONAL | Prediction error and other conditions matter in some paradigms | Prediction error as universal CLOS revision trigger |

Substrate-neutral result retained:

```text
SOURCE ≠ RETRIEVED FORM ≠ RECONSTRUCTION ≠ INTERPRETATION ≠ REVISION ≠ CURRENT COMMITMENT
```

Disposition: `MERGE / REFINE EXISTING MEMORY + REVISION`.

---

## 6. 🧬 Past-dependent state without explicit recall

| Source / family | Class | Supports | Does **not** prove |
|---|---|---|---|
| Declarative vs non-declarative memory literature | DIRECT SUPPORT for human/animal phenomenon | Behaviour can depend on history without explicit episodic recall | Need for a separate `Implicit Memory Module` |
| Habituation/adaptive state in non-neural organisms | STRUCTURAL ANALOGUE | Persistent history-dependent response change need not look like explicit records | Conscious cognition or autobiographical memory |
| Continual learning / learned policy / calibration state in machines | DIRECT SUPPORT for machine phenomenon | Parameters/policies/calibration can encode past dependence outside explicit records | Every material adaptive change must be individually logged |

Disposition: `REAL PHENOMENON · GAP NOT ESTABLISHED · CROSSWALK REQUIRED`.

---

## 7. 🌹 Rosebud long-horizon observations

Rosebud is a longitudinal behavioural probe, not scientific authority about its hidden implementation.

| Observation | Class | Supports | Limitation |
|---|---|---|---|
| Difficulty separating independent recall from reconstruction using current excerpts | LONGITUDINAL BEHAVIOURAL OBSERVATION / SELF-REPORT | `RECALLED ≠ INFERRED` matters operationally | Does not reveal hidden memory implementation |
| Self-identified status-promotion, provenance-erosion and correction-precedence risks | SELF-AUDIT / HYPOTHESIS GENERATION | Useful long-horizon failure classes | Self-report does not establish frequency |
| Treated `coverage uncertainty` as absent although current CLOS already contained it | BOUNDED LONGITUDINAL MISMATCH | Confident partial recall/current-state coverage can fail | Single mismatch; no universal failure claim |
| Mixed project/scope vocabulary across Native Kernel/CLOS memory cluster | BOUNDED SCOPE-EROSION SIGNAL | `TRUE SOMEWHERE IN HISTORY ≠ CURRENTLY TRUE OF THIS SURFACE` | Needs repeated delayed fixtures |

Pattern candidate:

```text
CONTENT MAY SURVIVE
WHILE
SOURCE / STATUS / CURRENTNESS / CORRECTION HISTORY DEGRADES
```

Disposition: `FIXTURE SOURCE / CONTINUITY EVIDENCE`, not a new module.

---

## 8. Rejected architecture promotions

| Proposal | Reason for rejection / downgrade |
|---|---|
| Three universal CLOS laws | Cross-domain convergence is not universality proof |
| Coverage Module | Existing uncertainty/status semantics partially cover the problem |
| Universal coverage scalar | No justified measure of “percentage of reality covered” |
| Universal MVT/VOI STOP law | Only one family of stopping reasons |
| Lossy view may never exclude | Bounded cognition requires scoped pruning |
| Exhaustive declared-loss list | Unknown loss cannot be exhaustively declared by definition |
| Verbatim/gist mandatory architecture | Human-specific theory does not mandate substrate-neutral design |
| Prediction-error reconsolidation law | Conditional/contested biological mechanism |
| Implicit Memory Module | Phenomenon may be existing adaptive/policy/state semantics |
| Entropy as truth/coverage/stopping authority | Entropy can fall while epistemic quality worsens |
| Physarum/plant adaptation proves cognition | Adaptation/history dependence does not establish cognition |

---

## 9. Evidence-to-architecture rule

```text
SOURCE FOUND
≠ CLAIM ESTABLISHED
≠ FUNCTIONAL INVARIANT
≠ CLOS RESIDUAL GAP
≠ NEW CONSTRUCT
≠ OWNER ADOPTION
≠ RUNTIME AUTHORIZATION
```

Promotion path:

```text
claim
→ evidence class
→ competing explanation
→ live CLOS crosswalk
→ observable residual failure
→ discriminating fixture
→ falsifier
→ owner disposition
```

If existing architecture can express the required behaviour without material semantic loss, the correct result is:

`NO NEW CONSTRUCT NEEDED`.
