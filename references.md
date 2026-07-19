# Uriam — References

Every named external source this framework draws on, in one place. Previously scattered as inline parentheticals across `about.md` (now `fundamentals.md`), `reference.md`, `origin.md`, and now `bin/profile/primitives.md` — this consolidates them. Grouped by category; within each, listed in the order they matter to the framework, not alphabetically.

For how each concept is actually defined, see `reference.md`. This file only answers "where did this come from and what did we take from it."

---

## Modeling Languages (Actor / Role / Interaction)

| Source | What it is | What Uriam draws from it | Used in |
| --- | --- | --- | --- |
| **ArchiMate** (The Open Group) | Enterprise architecture modeling standard | **Business Actor** ("an organizational entity capable of performing behavior") and **Business Role** ("the responsibility for performing specific behavior, to which an actor can be assigned") — the exact grounding for Actor/Role, non-circular by design. Also **Business Collaboration** (two or more roles working together) and **Business Interaction** (the collective behaviour a Collaboration performs). | `bin/profile/primitives.md` (Actor, Role), `reference.md` (Actor, Role, Collaboration, Interaction), `origin.md` (2026-07-06 entry) |
| **UML** (OMG Unified Modeling Language) | Software/systems modeling standard | Use Case Actor definition ("a role played by an entity that interacts with the subject, but which is external to the subject") — checked against ArchiMate during the Actor/Role grounding work; UML defines Actor *as* a role, so it doesn't independently ground the term the way ArchiMate does. Cited as a rejected alternative, not a source of the final definition. | Design discussion behind `bin/profile/primitives.md`'s Actor/Role (2026-07-19) |
| **BPMN** (Business Process Model and Notation) | Business process modeling standard | Participant/Role distinction — a Pool represents a concrete Participant, which may reference a Role as "a class of resources" (e.g. "Manager," "Customer"). Confirmed the direction of grounding Actor concretely and deriving Role from it, ahead of checking ArchiMate directly. | Design discussion behind `bin/profile/primitives.md`'s Actor/Role (2026-07-19) |
| **The Actor Model** (Carl Hewitt) | Concurrent computation formalism in computer science | Treats "Actor" as a computational primitive, undefined except by behavior (receiving a message, acting) — no dependency on "Role" at all. Independent confirmation, from outside business/enterprise modeling entirely, that Actor should ground first. | Design discussion behind `bin/profile/primitives.md`'s Actor/Role (2026-07-19) |

---

## Cognitive & Learning Frameworks

| Source | What it is | What Uriam draws from it | Used in |
| --- | --- | --- | --- |
| **Bloom's Taxonomy** | Educational objectives classification (Remember/Understand → Analyse/Evaluate → Create) | Comparison point: splits cleanly into Internalising/Examining/Build, with no real Externalising stage of its own — same gap as ReAct. | `fundamentals.md`, `reference.md` ("Relation to Other Frameworks") |
| **Kolb's Experiential Learning Cycle** | Concrete Experience → Reflective Observation → Abstract Conceptualisation → Active Experimentation | Near-exact structural match to Internalising→Examining→Externalising→Interacting, without the Repertoire or fractal property. Reflective Observation specifically maps to the Student's technique menu. | `fundamentals.md`, `reference.md` (comparison table, Student's techniques) |
| **The Hermeneutic Circle** | Whole-informs-parts-informs-whole interpretive method (philosophy/theology) | The whole cycle collapses onto Examining alone in this framework's comparison — Uriam externalises what the circle keeps internal. | `fundamentals.md`, `reference.md` |
| **De Bono's Six Thinking Hats** | Six-lens structured thinking method | Colour-codes the same territory as the matrix (White=Internalising, middle hats=Examining, Blue=Externalising, Green=Interacting). The Blue Hat specifically — process-control, not a fifth hat — is cited as independent validation for the Conductor/code-switching distinction. | `fundamentals.md`, `reference.md` |
| **Zimmerman's self-regulated learning** | Educational psychology model of self-directed learning cycles | Grounds the Conductor role for a solo human — the internal executive/task-initiation function, distinct from content-generation. | `reference.md` (Conductor table) |
| **Gollwitzer's implementation intentions** | "If-then" planning research in motivation psychology | Same grounding role as Zimmerman, above — the documented gap between forming an intention and acting on it. | `reference.md` (Conductor table) |

---

## AI Agent Architecture

| Source | What it is | What Uriam draws from it | Used in |
| --- | --- | --- | --- |
| **ReAct** (Yao et al.) | Observe → Reason → Act agent architecture | The framework's most-cited comparison: ReAct's missing Externalising step is repeatedly used to explain why AI agents reason well and then act prematurely. | `fundamentals.md`, `reference.md`, `SKILL.md`, `origin.md` |
| **Horvitz's mixed-initiative interaction research** | HCI research on shared control between human and system | Grounds who plays Conductor in an AI↔human flow — the call emerges from Notes, not either side unilaterally; automation bias is cited as the failure mode of skipping that joint check. | `reference.md` (Conductor table) |
| **AutoGen's `GroupChatManager`** (Microsoft) | Multi-agent orchestration framework | One of three independently-converged engineering examples of a Conductor-shaped role: something whose only output is whose turn it is. | `fundamentals.md`, `reference.md` |
| **CrewAI's hierarchical-process manager** | Multi-agent orchestration framework | Same role as AutoGen, above — independent convergent evidence. | `fundamentals.md`, `reference.md` |
| **MetaGPT's SOP-driven role router** | Multi-agent orchestration framework | Same role as AutoGen/CrewAI, above — third independent convergence. | `fundamentals.md`, `reference.md` |
| **LangGraph's supervisor pattern** | Multi-agent orchestration framework | Cited alongside AutoGen/CrewAI/MetaGPT as a shipped supervisor-agent example. | `reference.md` (Conductor table) |

---

## Decision & Team Frameworks

| Source | What it is | What Uriam draws from it | Used in |
| --- | --- | --- | --- |
| **OODA Loop** (Boyd) | Observe-Orient-Decide-Act military decision cycle | Comparison point — this framework's military cousin, missing the same stage ReAct is missing. | `fundamentals.md`, `reference.md` |
| **Belbin Team Roles** | Team-role psychometric model | The Coordinator role was originally named "Chairman" before Belbin renamed it — cited as independent precedent for the same authority-word-to-process-word correction this framework made with the Conductor. | `fundamentals.md`, `reference.md`, `origin.md` |
| **Transactional Analysis** (Eric Berne) | Parent/Adult/Child ego-state model in psychology | Grounds code-switching for humans — distinct behavioural registers moved between deliberately, without losing continuity of self. | `analogy-production.md` |
| **Cooper's Stage-Gate process** | Product development gating methodology | Contrast case for "Cue" — a gate is a pass/fail checkpoint requiring approval to open; a cue is a signal to enter. Used to sharpen what a Cue is *not*. | `analogy-production.md` |
| **RACI** | Responsible/Accountable/Consulted/Informed decision-rights framework | Rejected as the wrong lens for cue decision rights — "Accountable" doesn't fit a Conductor that owns no content. | `reference.md` (DACI section) |
| **DACI** | Driver/Approver/Contributor/Informed decision-rights framework | Adopted in place of RACI — separates authority to proceed from ownership of the work, which fits the Hero/Conductor split. | `reference.md` (DACI section) |

---

## Information Science

| Source | What it is | What Uriam draws from it | Used in |
| --- | --- | --- | --- |
| **Ranganathan's Fourth Law of Library Science** (1931) | "Save the time of the reader" | Names the same discipline Internalising requires: not over-fetching. | `fundamentals.md` |
| **Taylor's four levels of information need** (1968) | Information-seeking behavior model | Names the gap between what someone actually needs and what they end up asking for. | `fundamentals.md` |
| **Marchionini's lookup/learn/investigate split** (2006) | Information-seeking taxonomy | Distinguishes a known-item fetch from an open-ended topic browse — different Internalising strategies. | `fundamentals.md` |
| **Bates' berrypicking model** (1989) | Information-seeking behavior model | Echoes the Fractal Property — real Internalising happens bit-at-a-time across an evolving query. | `fundamentals.md` |

---

## Named Techniques (Repertoire Technique Tables)

Every row in `reference.md`'s four "Techniques Each Character Draws On" tables cites a specific, named real-world source. Listed here by character; full fit-rationale is in `reference.md`, not repeated here.

**The Student (Internalising):** After-Action Review (US Army 4-question format) · Blameless Postmortem (Google SRE Book) · Kolb's Reflective Observation (see Cognitive & Learning Frameworks, above) · Start/Stop/Continue (standard Agile retrospective format)

**The Philosopher (Examining):** Socratic Method (Platonic elenchus) · Dialectical Reasoning (Hegelian thesis-antithesis-synthesis) · First Principles Thinking (Cartesian/Aristotelian decomposition) · Six Thinking Hats (see above) · Second-Order Thinking (Munger's latticework of mental models) · Hermeneutic Circle (see above) · Double-Loop Learning (Argyris & Schön's governing-variables model) · 5 Whys (Toyota Production System)

**The Maker (Externalising):** SMART Goals (Doran, 1981) · User Stories + Acceptance Criteria (Mike Cohn's Agile format) · PRD (standard product-requirements-document format) · RFC / ADR (Nygard's Context-Decision-Consequences template) · The Pyramid Principle (Barbara Minto) · PR-FAQ (Amazon's "Working Backwards") · Pre-mortem (Gary Klein, 2007 HBR "Project Premortem") · Definition of Done (Scrum Guide)

**The Witness (Interacting):** PDCA's "Do" phase (Deming/Toyota Plan-Do-Check-Act) · Chaos Engineering (Netflix's Principles of Chaos Engineering) · Canary Deployment / A-B Testing (progressive-delivery practice) · Observability (SRE practice)

**The Conductor:** Kanban WIP Limits (Anderson's Kanban Method) · Timeboxing (standard agile/personal-productivity practice) · Daily Standup (Scrum Guide's Daily Scrum) · Incident Commander (SRE incident-response practice)

**Also cited once, outside the tables:** Lean Startup's Build-Measure-Learn loop (Eric Ries) — cited in `fundamentals.md` as an existing name for the Fractal Property in miniature.

---

## Gaps

A few sources above are cited by name only, without edition, year, or a direct link — worth tightening if this document is ever published alongside the framework rather than kept as an internal working reference:

- Ranganathan, Taylor, Marchionini, Bates — no specific paper/edition recorded beyond the year already in `fundamentals.md`.
- Argyris & Schön (Double-Loop Learning), Munger (Second-Order Thinking), Minto (Pyramid Principle) — no specific work cited.
- Zimmerman, Gollwitzer, Horvitz — no specific paper cited, just the named concept.
