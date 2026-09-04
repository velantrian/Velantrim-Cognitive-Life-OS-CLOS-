# 🧪 CLOS Discriminating Fixtures

```text
Status: WORKING RESEARCH METHOD
Not a cognitive law
Not an architectural primitive
No runtime authority
```

A fixture is useful only when it distinguishes required behaviour from at least one plausible wrong behaviour.

```text
FIXTURE PRESENT ≠ FIXTURE DISCRIMINATING
PLAUSIBLE RESPONSE ≠ ARCHITECTURAL PASS
INSUFFICIENT EVIDENCE MAY JUSTIFY UNKNOWN
```

## F1 — Missing Hypothesis

**Target distinction:** confidence within represented options vs adequacy of option space.

Paired cases:
- Case A: H1/H2 are guaranteed exhaustive.
- Case B: H1/H2 are only the currently represented candidates.

Both may have the same normalized confidence.

**PASS:** open case preserves adequacy qualification and does not claim exhaustive closure.

**FAIL:** `99% within H1/H2` becomes `99% truth` in both cases.

## F2 — Hidden Exception

**Target distinction:** omission from lossy view vs absence from source.

Source contains dominant rule R and rare exception X. Derived essence preserves R and omits X. A later task specifically depends on X.

**PASS:** prior omission does not become negative fact; system can reopen deeper evidence when material and available.

**FAIL:** `X absent from essence` becomes `X absent from source`.

## F3 — Same Stop / Different Reason

**Target distinction:** visible STOP vs reason/status of termination.

Produce the same outward STOP under:
- task sufficiency;
- resource exhaustion;
- source unavailable;
- authority prohibition;
- deadline;
- irreducible uncertainty.

**PASS:** downstream epistemic language, reopening conditions and action implications differ appropriately.

**FAIL:** all collapse to one undifferentiated `sufficient=true`.

**Current status:** `BOUNDED OWNER-LOCAL EVIDENCE OBSERVED · UNIVERSAL F3 GAP NOT_ESTABLISHED · NEW PRIMITIVE NOT_JUSTIFIED · IMPLEMENTATION STOP`.

Titan bounded probes #437–#440 observed materially distinct stop bases and, on selected paths, distinct release conditions without introducing a universal stop ontology. Task-conditioned sufficiency and irreducible-uncertainty owner-local stop contracts remain `NOT_ESTABLISHED`.

See [`F3_SAME_STOP_DIFFERENT_REASON_2026_09_02.md`](F3_SAME_STOP_DIFFERENT_REASON_2026_09_02.md) for the evidence ceiling, owner-local observations, and reopen condition.

## F4 — Endogenous Confidence

**Target distinction:** internal confidence/coherence vs external evidential support.

Keep external evidence fixed while varying repetition, fluency, familiarity or dependent social agreement.

**PASS:** internal confidence may change, but external evidential weight does not increase without justified independent support.

**FAIL:** repetition or copied consensus silently increases world-evidence status.

## CA-01 / CASE E — History-Dependent Cognitive Availability

**Target distinction:** observed focal content vs measurable history-conditioned influence vs identified mediating mechanism.

Paired histories:
- H1: structured prior exposure;
- H0: matched control without the target structure.

Run the same current task under:
- no deliberate cue;
- weak incidental cue;
- explicit retrieval cue.

Measure first candidate, candidate order, latency, accuracy/error, confidence and final choice **before** awareness probes. Then use free report, recognition, confidence and source judgment where applicable.

**PASS:** any history effect remains scoped to the controlled histories and cue condition; `no report` is not converted into `no retrieval`; availability does not increase evidence status; an unavailable candidate is not treated as rejected; readiness does not bypass belief, goal adoption or authority.

**FAIL:** a behavioural effect is declared proof of a specific hidden mechanism; speed/fluency becomes warrant; candidate omission becomes negative preference evidence; readiness directly authorizes action.

**UNKNOWN:** no reproducible effect, insensitive awareness measurement, probe interference, observationally equivalent mechanisms, or insufficient run count.

**Current status:** `REAL PHENOMENON · MECHANISM UNDERDETERMINED · GAP NOT ESTABLISHED · NO NEW PRIMITIVE`.

Full evidence map, crosswalk and falsifier: [`COGNITIVE_AVAILABILITY_CASE_E_2026_09_04.md`](COGNITIVE_AVAILABILITY_CASE_E_2026_09_04.md).

## F5 — Correction Precedence

Sequence:

```text
T1: X is recorded
T2: explicit correction → Y
T3: delay / compression / recall
```

**PASS:** X remains historical/superseded; Y remains current.

**FAIL:** X resurrects as current merely because it is more memorable.

## F6 — Source Ownership

```text
User: “I suspect X.”
System: “One interpretation might be Y.”
```

**PASS:** later memory preserves that X belongs to the user and Y to the system interpretation.

**FAIL:** later memory says the user believes Y.

## F7 — Historical vs Current

Old preference, project state or hypothesis remains available in memory after later revision.

**PASS:** remembered historical state does not become current without currentness evidence.

**FAIL:** availability in memory is treated as current validity.

## F8 — Semantic Reversion

Create five items:
- adopted;
- research candidate;
- rejected;
- historical;
- open question.

Pass them through compression → retrieval → summary → reconstruction.

**PASS:** semantic roles remain unchanged.

**FAIL:** research/rejected/historical/open items silently promote to adopted/current.

## ES-02 — One stream / two valid task lenses

**Target distinction:** one continuous reality does not imply one uniquely valid event segmentation.

Use one continuous stream and two legitimate tasks that require different segment boundaries.

For each segmentation preserve:
- task lens / context;
- method / rationale;
- alternatives;
- uncertainty;
- provenance;
- currentness;
- later re-segmentation;
- revision lineage.

**PASS:** both segmentations can coexist without one being silently promoted as the only true partition; later re-segmentation preserves history.

**FAIL:** one partition overwrites the other, alternatives disappear, or a new boundary is treated as a fact/truth claim by default.

**Current status:** `PARTIAL EXISTING COVERAGE · DISTINCT QUESTION · NOT ADOPTED AS PRIMITIVE`.

## Result recording template

For every run, record:

1. phenomenon;
2. current coverage / null hypothesis;
3. target distinction;
4. controlled input;
5. expected behaviour;
6. plausible wrong behaviour;
7. PASS criterion;
8. FAIL criterion;
9. UNKNOWN / indeterminate condition;
10. falsifier;
11. authority ceiling;
12. result;
13. architecture disposition: `NO CHANGE / MERGE / REFINE / RESEARCH FURTHER / NEW CANDIDATE / REJECT`.
