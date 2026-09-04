# 📚 CLOS Evidence Ledger

```text
Status: SUPPORTING RESEARCH LEDGER
Canon: NO
Runtime authority: NONE
Purpose: preserve claim → evidence → limitation → disposition traceability
```

This ledger is deliberately smaller than the full research history in Notion / Google Docs. It records the evidence needed to understand why the current CLOS research families survived, what that evidence does **not** prove, and how the result is currently classified.

## 2026-09-01 live owner-verification addendum

This addendum supersedes older fixture-order wording below where the two conflict. It records live owner evidence, not new architecture.

### 💠 Crystal bounded Phase-0 closure

Verified baseline: `velantrian/velantrim-exocortex-crystal@7509be14c274cdc83e8e00287f46a78f8ee33696`.

| Boundary | Current evidence status | Does **not** prove |
|---|---|---|
| `SOURCE → REPRESENTATION COVERAGE` | `NOT_ESTABLISHED` | That omitted material is absent from the source, or that a new subsystem is required |
| `LOCATOR → EXACT SOURCE REPLAY` | `IMPLEMENTED + TESTED` | That downstream reasoning actually used the replayed detail |
| `VERSION → STALE / HISTORICAL PRESERVATION` | `IMPLEMENTED + TESTED` | Full natural-language current-vs-historical resolution |
| `CANDIDATE → RELATION DISCRIMINATION` | `IMPLEMENTED + MEASURED GAP` | Truth adjudication or safe decision authority |
| `NEEDS_REVIEW → BOUNDED REREAD` | `IMPLEMENTED + TESTED` | A later task will know when an older compact view is insufficient |
| `CRYSTAL → AUTHORITY FIREWALL` | `EXPLICIT / IMPLEMENTED + LOCAL TEST COVERAGE` | System-wide production authorization |

Disposition: `CRYSTAL PHASE-0 BOUNDED REVIEW CLOSED`.

Closure means the owner boundary is localized. It does **not** mean all memory questions are solved. Broad Crystal auditing should stop unless a concrete evidence question returns ownership there.

### 🗿 Titan evidence-use localization

Verified baseline: `velantrian/Velantrim-ExoCortex-Titan@78be30a89eb0ad698af1f4f3884db6728d076c06`.

Current measurement vocabulary:

```text
R = retrieved
S = serialized
T = transmitted
U = demonstrably used
A = demonstrably answer-supporting
```

Bounded evidence:

- PR #426 / merge commit `43d03e02339ea820ade009ef552bd8f24615f76f`: bounded `R/S/T` measurement path;
- `R → S` is established for the measured path;
- `S → T` can be lossy under provider/message packing;
- PR #427 / Titan `main@78be30a89eb0ad698af1f4f3884db6728d076c06`: negative-authority fixture showing `source_fact_ids` / trace membership alone does not establish U or A;
- `T → U` remains `NOT_ESTABLISHED`;
- `U → A` remains `NOT_ESTABLISHED`.

```text
TRACE MEMBERSHIP ≠ SEMANTIC USE
SEMANTIC USE ≠ ANSWER SUPPORT
ANSWER SUPPORT ≠ DECISION AUTHORITY
```

Disposition: `MEASUREMENT / LOCALIZATION GAP · NO ATTRIBUTION ENGINE`.

### 🔁 Later-task sufficiency / reopen boundary

Live owner reading establishes:

```text
REOPEN CAPABILITY = IMPLEMENTED
SAME-RUN REOPEN POLICY = IMPLEMENTED
LATER-TASK REOPEN POLICY = NOT_ESTABLISHED
```

The highest-information residual is therefore not whether the system can reread, but whether a genuinely later task can recognize that an older compact representation is no longer sufficient and recover/reopen the correct source/version/span.

```text
T1 SUFFICIENT ≠ T2 SUFFICIENT
REOPEN CAPABILITY ≠ REOPEN POLICY
SAME-RUN REOPEN POLICY ≠ LATER-TASK REOPEN POLICY
```

Current next gate: exactly one **bounded read-only Titan localization pass** for any already-existing later-task / cross-session reuse + reopen path.

`F2 Hidden Exception` remains a candidate fixture only if that localization does not already resolve the boundary. F2 is **not authorized for creation or execution** by this ledger update.

If an existing path already preserves the distinction:

`DOCUMENT EVIDENCE → NO CHANGE → NO NEW CONSTRUCT → STOP`.

If not established, classify `TEST GAP` or `CONTRACT GAP` first. Do not infer an implementation gap automatically.

---

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

Disposition after live owner verification: `GENUINE RESIDUAL QUESTION · SOURCE→REPRESENTATION COVERAGE NOT_ESTABLISHED · LATER-TASK REOPEN POLICY NOT_ESTABLISHED · NO NEW CONSTRUCT`.

### Falsifier / downgrade condition

First inspect the existing Titan later-task / cross-session reuse + reopen path. If existing owner mechanisms preserve the distinction without material semantic loss, disposition becomes `MERGE / NO CHANGE / NO NEW CONSTRUCT`. Only if the boundary remains unestablished after localization may F2 be considered as a separately authorized discriminating fixture.

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

**Current alias:** `History-dependent cognitive availability / CASE E / CA-01`.

These names refer to one research family. CASE E is the bounded evidence-and-fixture packet for this existing line; it does not supersede the ledger family or create a second residual question.

| Source / family | Class | Supports | Does **not** prove |
|---|---|---|---|
| Declarative vs non-declarative memory literature | DIRECT SUPPORT for human/animal phenomenon | Behaviour can depend on history without explicit episodic recall | Need for a separate `Implicit Memory Module` |
| Habituation/adaptive state in non-neural organisms | STRUCTURAL ANALOGUE | Persistent history-dependent response change need not look like explicit records | Conscious cognition or autobiographical memory |
| Continual learning / learned policy / calibration state in machines | DIRECT SUPPORT for machine phenomenon | Parameters/policies/calibration can encode past dependence outside explicit records | Every material adaptive change must be individually logged |

Disposition: `REAL PHENOMENON · MECHANISM UNDERDETERMINED · GAP NOT ESTABLISHED · BOUNDED FIXTURE / CROSSWALK REQUIRED`.

Evidence map, limitations, falsifier and CA-01 protocol: [`COGNITIVE_AVAILABILITY_CASE_E_2026_09_04.md`](COGNITIVE_AVAILABILITY_CASE_E_2026_09_04.md).

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
| Universal evidence-attribution service | Current Titan evidence localizes U/A as a measurement gap, not a new authority or architecture requirement |

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
