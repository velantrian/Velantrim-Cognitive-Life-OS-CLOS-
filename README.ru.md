# ⚗️ VELANTRIM COGNITIVE LIFE OS · CLOS

**Русская версия** · [English README](README.md)

> **CLOS** — research-first, substrate-neutral архитектурная программа о том, какие когнитивные различия, состояния, переходы и границы полномочий должны сохраняться во времени независимо от конкретной реализации.
>
> **Статус:** `ACTIVE RESEARCH BLUEPRINT · NOT FINAL CANON · NOT IMPLEMENTATION AUTHORIZATION · NOT RUNTIME AUTHORIZATION`

[🗺️ Blueprint](docs/CLOS_BLUEPRINT.md) · [📊 Current status](docs/CURRENT_STATUS.md) · [🔬 Research synthesis](docs/RESEARCH_SYNTHESIS_2026_08_29.md) · [📚 Evidence](docs/EVIDENCE_LEDGER.md) · [🧪 Fixtures](docs/DISCRIMINATING_FIXTURES.md) · [🧭 Crosswalk](docs/ECOSYSTEM_CROSSWALK.md)

---

## 🧠 Что исследует CLOS

CLOS начинает не с LLM, RAG, graph DB или agent framework, а с вопроса:

> **Что когнитивная система должна уметь различать, сохранять и пересматривать, даже если технология реализации полностью заменится?**

```text
🌍 reality / experience
        ↓
👁 perception
        ↓
🧩 representation
        ↓
🧠 memory / current model
        ↓
🧭 orientation + attention
        ↓
💭 reasoning / reconstruction
        ↓
🛑 deepen / stop / UNKNOWN
        ↓
🧪 options / hypotheses
        ↓
⚖️ decision / inhibition
        ↓
🔐 authority
        ↓
🛠 action / no action
        ↓
🌊 consequence
        ↓
🪞 revision / learning ↺
```

Это **не обязательный control flow**, не module graph и не ownership map.

---

## 🔒 Ключевые границы

```text
retrieval ≠ evidence
claim ≠ belief
belief ≠ truth
confidence ≠ evidence strength
coherence ≠ truth
identity ≠ authority
capability ≠ permission
research ≠ Canon
Canon ≠ implementation authorization
implementation ≠ runtime authorization
model output ≠ Canon
```

Через compression, retrieval, reconstruction и handoff важные различия должны сохраняться либо явно маркироваться как утраченные: semantic role, provenance, scope, time/currentness, uncertainty, revision history и authority/constraint. Рабочее имя этой discipline — **Meaning Envelope**; это не обязательный класс, таблица или отдельный модуль.

---

## 🔬 Текущий research frontier

Подробная аргументация хранится в [`docs/CLOS_BLUEPRINT.md`](docs/CLOS_BLUEPRINT.md) и [`docs/RESEARCH_SYNTHESIS_2026_08_29.md`](docs/RESEARCH_SYNTHESIS_2026_08_29.md). README хранит только навигационный summary, чтобы не создавать несколько конкурирующих копий research wording.

| Направление | Текущий статус |
|---|---|
| 🌍 Coverage / possibility-space adequacy | `REFINE / CROSSWALK` |
| 💎 Lossy representation / Safe Candidate Access | `REFINE / FIXTURE` |
| 🛑 Reason-Typed Stopping / reopening | `MERGE / REFINE` |
| 📍 Event Segmentation / ES-02 | `DISTINCT QUESTION · NOT ADOPTED AS PRIMITIVE` |

Общий structural synthesis остаётся research-level:

> **Система должна уметь действовать на основании неполных внутренних представлений, не превращая ограничения собственного представления, поиска, памяти или внутреннего состояния в свойства внешнего мира.**

`STATUS: STRONG STRUCTURAL SYNTHESIS · NOT NEW LAW`

---

## 🧪 Метод исследования

```text
DON'T INVENT
→ CROSSWALK
→ FIND RESIDUAL GAP
→ FORMULATE OBSERVABLE FAILURE
→ TRY TO DESTROY THE GAP
→ BOUNDED FIXTURE
→ RESULT
→ MERGE / REFINE / REJECT
→ ONLY THEN CONSIDER ARCHITECTURAL CHANGE
```

```text
REAL PHENOMENON ≠ ARCHITECTURAL GAP
REAL GAP ≠ NEW PRIMITIVE / MODULE / OWNER
BIOLOGICAL ANALOGUE ≠ ARCHITECTURAL PROOF
REPEATED ACROSS DOMAINS ≠ UNIVERSAL LAW
```

---

## 🧩 Место в экосистеме Velantrim

CLOS — **отдельная research surface**, а не седьмой sovereign owner.

| Проект | Project-local responsibility |
|---|---|
| 💠 Crystal | memory / evidence / provenance / Canon admission |
| 🗿 Titan | orchestration / tools / runtime realization |
| 🧬 Native Kernel | substrate-neutral semantic / epistemic-history invariants |
| 🌀 Mentaury Soul | cognition / beliefs / self / identity-domain semantics |
| 🌎 Continuum | process continuity / handoff / currentness |
| 🪁 Mentaury-Kernel | cross-domain composition invariants |

```text
CLOS RESULT
≠ OWNER ADOPTION
≠ IMPLEMENTATION
≠ RUNTIME ENABLEMENT
≠ PRODUCTION AUTHORITY
```

Подробнее: [`docs/ECOSYSTEM_CROSSWALK.md`](docs/ECOSYSTEM_CROSSWALK.md).

---

## 📚 Где что хранится

- **GitHub** — versioned portable research docs + reviewable diffs;
- **Notion · ⚗️ Velantrim Cognitive Life OS 📖** — live current research wording/checkpoint;
- **Google Docs · ⚗️ Velantrim Cognitive Life OS 📖** — подробный rationale, комментарии и research history.

```text
CURRENT ARCHITECTURE ≠ RESEARCH ARCHIVE
REVISION ≠ SILENT OVERWRITE
HISTORY ≠ CURRENT STATE
```

## 🎯 Следующий gate

Не расширять архитектуру по умолчанию. Следующий high-information шаг — live crosswalk + bounded fixtures. Если existing vocabulary уже выражает требуемое поведение без material semantic loss, правильный результат:

`MERGE / REFINE EXISTING / NO NEW CONSTRUCT`.
