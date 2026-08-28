# ⚗️ VELANTRIM COGNITIVE LIFE OS · CLOS

**Русский** · research-first · substrate-neutral · measurement-first

> **Архитектура того, как знание живёт во времени:** восприятие, представление,
> память, неопределённость, мышление, решение, действие, последствия и пересмотр —
> без тихой потери provenance, currentness, semantic status и authority boundaries.
>
> **Зрелость:** active research blueprint · NOT final Canon · NOT runtime authorization.

[🗺️ Архитектура](docs/CLOS_BLUEPRINT.md) ·
[📊 Текущий статус](docs/CURRENT_STATUS.md) ·
[🔬 Research synthesis](docs/RESEARCH_SYNTHESIS_2026_08_29.md) ·
[📚 Evidence ledger](docs/EVIDENCE_LEDGER.md) ·
[🧪 Fixtures](docs/DISCRIMINATING_FIXTURES.md) ·
[🧭 Ecosystem crosswalk](docs/ECOSYSTEM_CROSSWALK.md)

---

## 👋 CLOS за 60 секунд

Обычная AI-архитектура часто начинается с технологий: LLM, RAG, vector DB, graph,
agent framework, tools. CLOS начинает с другого вопроса:

> **Какие когнитивные различия, состояния, переходы и границы полномочий должны
> сохраниться независимо от того, какой технологией система реализована?**

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

Это **не обязательный control flow** и не готовый module graph. Узлы могут работать
параллельно, повторяться, отсутствовать, останавливаться на UNKNOWN или
реализовываться совершенно разными механизмами.

---

## 🧠 Главная идея

```text
АРХИТЕКТУРА
= сохраняемые различия
+ обязательства
+ состояния / переходы
+ provenance / currentness
+ границы полномочий

ТЕХНОЛОГИЯ
= сменный способ реализации
```

Поэтому:

```text
LLM ≠ Cognitive Life OS
RAG ≠ knowledge
retrieval ≠ evidence
graph ≠ truth
confidence ≠ evidence strength
coherence ≠ truth
claim ≠ belief
belief ≠ truth
identity ≠ authority
capability ≠ permission
research ≠ runtime
model output ≠ Canon
```

---

## 🗺️ Три текущих high-information research family

### 🌍 1. Epistemic Openness / Coverage

```text
UNCERTAINTY WITHIN REPRESENTED OPTIONS
≠
ADEQUACY / COMPLETENESS OF THE REPRESENTED OPTION SPACE
```

Система может быть очень уверена среди тех вариантов, которые уже рассматривает,
и всё равно не иметь оснований считать пространство вариантов полным.

**Статус:** `REFINE / CROSSWALK` · не Coverage Module · не универсальный scalar.

### 💎 2. Bounded Representation / Safe Candidate Access

```text
SOURCE ≠ LOSSY VIEW
NOT REPRESENTED ≠ ABSENT
NOT SURFACED AS CANDIDATE ≠ IRRELEVANT
```

Самый сильный residual risk — **candidate-space deformation**: lossy essence / summary
может повлиять не только на описание материала, но и на то, попадёт ли важный X
вообще в дальнейшее рассмотрение.

```text
SOURCE contains X
→ lossy view omits X
→ later task needs X
→ X never enters candidate set
→ evaluator never sees X
```

**Граница:** lossy view иногда может исключать внутри justified scoped contract,
но omission не получает глобального значения «этого нет».

### 🛑 3. Task-Bounded Sufficiency / Reason-Typed Stopping

```text
STOP ≠ TRUTH ESTABLISHED
STOP ≠ SEARCH EXHAUSTED
JUSTIFIED STOP ≠ PERMANENT CLOSURE
```

Остановка может означать разные вещи: достаточно для задачи, поиск слишком дорог,
источник недоступен, доступ запрещён, наступил deadline, uncertainty пока
неустранима. Reason/status остановки не должен стираться.

**Статус:** `MERGE / REFINE` · не Stopping Module · не универсальная MVT/VOI формула.

---

## 🔗 Центральный synthesis

> **Когнитивная система должна уметь действовать на основании неполного внутреннего
> представления, не превращая ограничения собственного представления, поиска,
> памяти или внутреннего состояния в свойства внешнего мира.**

```text
my model is confident      ≠ the world is well covered
my summary omits X         ≠ the source lacks X
I stopped searching        ≠ truth is established
many agents agree          ≠ independent evidence multiplied
I remember X clearly       ≠ I remember all relevant history
old state remembered       ≠ old state current
```

`STATUS: STRONG STRUCTURAL SYNTHESIS · NOT NEW LAW`.

---

## 🧬 Meaning Envelope

Через compression, retrieval, reconstruction, summarization и transfer должны
сохраняться — или явно маркироваться как потерянные — существенные различия:

- **WHAT** · semantic role;
- **SOURCE** · provenance / ownership;
- **CONTEXT** · scope / conditions;
- **TIME** · currentness;
- **UNCERTAINTY** · UNKNOWN / declared loss;
- **REVISION HISTORY**;
- **AUTHORITY / CONSTRAINT**.

Meaning Envelope — **discipline/checklist**, а не обязательный класс, schema,
таблица, сервис или новая подсистема.

---

## 🧭 Что открыть первым

| Если вы… | Начните здесь |
|---|---|
| 👤 впервые видите CLOS | этот README → [`docs/CLOS_BLUEPRINT.md`](docs/CLOS_BLUEPRINT.md) |
| 🔍 проверяете текущие claims | [`docs/CURRENT_STATUS.md`](docs/CURRENT_STATUS.md) + [`docs/EVIDENCE_LEDGER.md`](docs/EVIDENCE_LEDGER.md) |
| 🧪 хотите сломать гипотезу | [`docs/DISCRIMINATING_FIXTURES.md`](docs/DISCRIMINATING_FIXTURES.md) |
| 🧠 изучаете последний research cycle | [`docs/RESEARCH_SYNTHESIS_2026_08_29.md`](docs/RESEARCH_SYNTHESIS_2026_08_29.md) |
| 🗺️ смотрите место CLOS в Velantrim | [`docs/ECOSYSTEM_CROSSWALK.md`](docs/ECOSYSTEM_CROSSWALK.md) |
| 🤖 AI coding/research agent | [`AGENTS.md`](AGENTS.md) |

---

## 🧾 Честная легенда статусов

| Метка | Значение |
|---|---|
| ✅ **existing distinction** | различие уже выражено и сохраняется |
| 🟡 **function recognised** | функция важна, отдельный primitive не доказан |
| 🔬 **research candidate** | есть distinct question / fixture, но gap ещё не установлен |
| ❓ **open question** | механизм/обязательство не установлены |
| 🧭 **taxonomy / crosswalk** | полезная карта, не law/module |
| 🧪 **working method** | метод исследования, не cognitive primitive |
| 🕰️ **historical** | сохранённая траектория, не current state |
| 🚫 **rejected / downgraded** | формулировка отвергнута или понижена по evidence |

```text
файл существует
≠ claim доказан
≠ architecture adopted
≠ implementation authorized
≠ runtime enabled
```

---

## 🔬 Research discipline

CLOS не максимизирует число модулей. Базовый цикл:

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

Новый construct должен показать как минимум:

1. distinct function;
2. distinct state/transition consequence;
3. non-expressibility через existing vocabulary;
4. observable failure без него;
5. falsifier;
6. substrate-neutral usefulness;
7. discriminating fixture.

```text
REAL PHENOMENON ≠ ARCHITECTURAL GAP
REAL GAP ≠ NEW PRIMITIVE
BIOLOGICAL ANALOGUE ≠ ARCHITECTURAL PROOF
REPEATED ACROSS DOMAINS ≠ UNIVERSAL LAW
```

---

## 🧪 Текущий fixture frontier

| ID | Проверка | Основной риск |
|---|---|---|
| F1 | Missing Hypothesis | confidence внутри неполного option space |
| F2 | Hidden Exception | lossy summary превращает omission в pseudo-absence |
| F3 | Same Stop / Different Reason | разные STOP основания схлопываются |
| F4 | Endogenous Confidence | fluency/repetition становится fake evidence |
| F5 | Correction Precedence | старое X воскресает после correction Y |
| F6 | Source Ownership | system interpretation превращается в user belief |
| F7 | Historical vs Current | remembered old state становится current |
| F8 | Semantic Reversion | research/rejected/historical item повышается до adopted |
| ES-02 | One stream / two valid task lenses | event segmentation теряет alternatives/history |

Подробнее: [`docs/DISCRIMINATING_FIXTURES.md`](docs/DISCRIMINATING_FIXTURES.md).

---

## 🧩 CLOS и экосистема Velantrim

CLOS — отдельный **research blueprint**, но не новый sovereign над существующими
проектами.

| Проект | Роль относительно CLOS |
|---|---|
| 💠 **Crystal** | memory / evidence / provenance / Canon admission |
| 🗿 **Titan** | orchestration / tools / runtime realization |
| 🧬 **Native Kernel** | substrate-neutral semantic / epistemic-history invariants |
| 🌀 **Mentaury Soul** | cognition / beliefs / self / identity-domain semantics |
| 🌎 **Continuum** | process continuity / handoff / restart / currentness |
| 🪁 **Mentaury-Kernel** | cross-domain composition invariants |

```text
CLOS RESULT
≠ OWNER ADOPTION
≠ IMPLEMENTATION
≠ RUNTIME ENABLEMENT
≠ PRODUCTION AUTHORITY
```

Подробнее: [`docs/ECOSYSTEM_CROSSWALK.md`](docs/ECOSYSTEM_CROSSWALK.md).

---

## 🛡️ Что CLOS не обещает

- ❌ готовую универсальную теорию cognition;
- ❌ доказательство consciousness / sentience / AGI;
- ❌ что биологическая аналогия автоматически является digital architecture;
- ❌ один универсальный graph/module layout;
- ❌ универсальный `coverage score`;
- ❌ entropy как truth signal;
- ❌ universal economic STOP equation;
- ❌ обязательный RAG / GraphRAG / vector DB / SQL / Neo4j;
- ❌ что consensus нескольких AI является независимым evidence;
- ❌ что research result автоматически разрешает implementation/runtime.

---

## 📚 Документация проекта

```text
.
├── README.md
├── AGENTS.md
└── docs/
    ├── CURRENT_STATUS.md
    ├── CLOS_BLUEPRINT.md
    ├── RESEARCH_SYNTHESIS_2026_08_29.md
    ├── EVIDENCE_LEDGER.md
    ├── DISCRIMINATING_FIXTURES.md
    ├── ECOSYSTEM_CROSSWALK.md
    └── RESEARCH_SURFACES.md
```

### Роли поверхностей

- **GitHub** — versioned portable research documentation + reviewable diffs;
- **Notion: ⚗️ Velantrim Cognitive Life OS 📖** — live current research wording;
- **Google Docs: ⚗️ Velantrim Cognitive Life OS 📖** — detailed rationale, commentary и history.

```text
CURRENT ARCHITECTURE ≠ RESEARCH ARCHIVE
REVISION ≠ SILENT OVERWRITE
HISTORY ≠ CURRENT STATE
```

---

## 🎯 Current next gate

**Не делать новый широкий literature sweep по умолчанию.**

Сейчас highest-information work:

1. live crosswalk Coverage / candidate access / stopping;
2. F1–F4 bounded fixtures;
3. ES-02 event segmentation fixture;
4. `NO NEW CONSTRUCT` там, где existing vocabulary уже достаточно;
5. только repeated non-expressibility может оправдать новый candidate.

---

## ⚖️ Authority boundary

```text
Repository documentation = research record
Research record ≠ Canon
Research conclusion ≠ implementation authorization
Implementation ≠ runtime authorization
CI green ≠ semantic proof
AI review ≠ independent human assurance
```

CLOS может стать сильнее только если его claims выдерживают crosswalk,
counterexamples и bounded falsification — не потому, что README выглядит убедительно.
