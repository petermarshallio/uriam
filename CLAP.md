# CLAP — A Framework for Human and Machine Intelligence

**Version:** 1.0  
**Origin:** Peter Marshall, ~1996 (E-Government, London)  
**Rediscovered and formalised:** 2026-06-29  
**Audience:** Peter Marshall, Claude, and anyone building systems that think

---

## The Core Idea

CLAP is a framework for understanding how intelligence — human or artificial — moves from raw input to meaningful output. It describes four fundamental cognitive stages, the valves between them, and the property of momentum that determines how well the whole system works.

It is not a linear process. It is a spiral. Each revolution lands you somewhere higher than the last.

---

## The Matrix — This Is the Foundation

Before the acronym, there is a 2×2 matrix. Everything else derives from it.

The two axes are **source** (where does the input come from?) and **target** (where does the output go?):

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Learn** | **Create** |
| **Internal source** | **Analyse** | **Plan** |

This matrix is the lens. If you understand it, you can interpret the acronym in your own words — and you can map almost any cognitive framework, AI architecture, or decision-making model onto it.

- **Learn** — the world comes *in*. You absorb, accumulate, receive.
- **Analyse** — you work on what's *inside*. You reason, connect, critique.
- **Plan** — your internal reasoning goes *out* as structured intention. You make it concrete.
- **Create** — you act on the world, and the world responds. Something new exists.

---

## The Four Stages

### Learn

*External → Internal*

Taking in knowledge from the outside world. Reading. Listening. Watching. Accumulating. This is what a child does when they go to the library and come back with 90 books about cheese. It is also what an AI does when it ingests a corpus.

Learning is not passive — it requires selection. You cannot learn everything. The quality of what you choose to learn determines the quality of everything downstream.

**In AI terms:** corpus ingestion, retrieval, contextual grounding. The vitals files in a conference talk corpus are the product of Learn.

**In human terms:** research, reading, listening, observation, experience.

---

### Analyse

*Internal → Internal*

Working on what you already have inside. Connecting dots. Reasoning. Critiquing. Weighing options. This is the stage where raw learning becomes understanding.

Analyse is the home box for many people — including the author of this framework. It is seductive because it feels like progress. It can become a trap. The valve out of Analyse (Commit) exists precisely to prevent infinite rumination.

**In AI terms:** reasoning, chain-of-thought, the "Reason" in ReAct. The LLM Council's Perspectives are the product of Analyse applied to Learn.

**In human terms:** critical thinking, de Bono's Six Thinking Hats, the hermeneutic circle, dot-connecting.

---

### Plan

*Internal → External*

Structured intention made concrete. This is the stage that most AI agents skip — and why they fail at anything requiring sustained, coordinated effort. Plan is where internal reasoning becomes external artefact: a SMART objective, a work package, a Gantt chart, a prioritised backlog.

Plan is not thinking about what to do. It is writing it down in a form that others — or your future self — can act on.

**In AI terms:** task decomposition, agent planning, structured output. The step between Reason and Act that ReAct agents lack.

**In human terms:** project management, SMART goals, sprint planning, architectural design documents.

---

### Create

*External → External*

Acting on the world. The world responds. Something new exists that did not exist before. This is not merely "doing" — it is the act of creation, which implies intentionality and result. A wolf can blow on your house. Create is the stage where you find out if it holds.

Create generates the raw material for the next Learn. The cycle continues.

**In AI terms:** generation, tool use, execution, deployment. The "Act" in ReAct.

**In human terms:** building, writing, shipping, speaking, deciding.

---

## The Valves

Between each stage is a valve. Valves are **one-directional** — you cannot push fluid backwards through them. The cycle always moves forward. You do not retreat to a previous stage; you complete the cycle and begin a new one, richer for the revolution you just completed.

Each valve asks a single question: **is there enough here to move forward?**

Not "are you done?" — you are never done. Just: *enough to proceed.*

| Valve | Between | The question it asks |
| --- | --- | --- |
| **Select** | Learn → Analyse | Have I gathered enough to reason with? |
| **Commit** | Analyse → Plan | Have I thought enough to stop thinking and decide? |
| **Resource** | Plan → Create | Is this plan actually deliverable? Agreements, people, time? |
| **Reflect** | Create → Learn | What did doing this teach me that I didn't know before? |

**Commit** is the most important valve for people who live in Analyse. It does not demand certainty. It demands a hypothesis — something specific enough to be wrong. A scientist's commitment, not a bureaucrat's sign-off.

**Resource** is the most skipped valve. It is why houses fall down when wolves blow on them. The plan was good. The resourcing was assumed.

---

## Momentum

Momentum is not a stage. It is a property of the whole system — the rate at which you move through the spiral.

**High momentum:** each revolution of CLAP lands you somewhere genuinely new. The valves open readily because sufficient work was done in each stage.

**Low momentum:** spinning on the same level. Stuck in Analyse. Skipping valves. Returning to Learn because Commit was never crossed.

**False momentum:** moving fast but skipping stages. Lots of Create without enough Learn or Analyse. The house gets built quickly. Then the wolf arrives.

Momentum is killed by:

- Perfectionism in Analyse (the thinking trap)
- Skipping Resource (the execution trap)
- Insufficient Learn before Analyse (the opinion trap)

Momentum is built by:

- Crossing Commit with a testable hypothesis, not a proven answer
- Treating Reflect as genuinely generative, not just evaluation
- Allowing the next Learn to be informed by what Create revealed

---

## The Fractal Property — CLAP All the Way Down

Each stage of CLAP is itself a full CLAP cycle.

The Learn stage of a project *is* a CLAP cycle: you Create experiments to learn from, Learn from them, Analyse what you found, Plan the next experiment.

The Analyse stage of a decision *is* a CLAP cycle: you Create hypotheses, Learn what they imply, Analyse the implications, Plan which to test.

This is not a metaphor. It is structurally true. CLAP scales from a five-minute decision to a thirty-year career. The same four questions, the same four valves, applied recursively at every level of granularity.

*"It's CLAP all the way down."*

This fractal property means the framework is never the wrong size. If a stage feels too large to act on, run CLAP inside it. The cycle will break it into manageable revolutions.

---

## Non-Linearity and Entry Points

CLAP is not always CLAP. You do not have to start with Learn.

People have a **home box** — the stage they gravitate toward, where they spend disproportionate time. They also have a **neglected box** — the valve they most often skip.

| Entry point | Who does this | Risk |
| --- | --- | --- |
| **Learn first** | Researchers, readers, the cautious | Never crossing Commit |
| **Analyse first** | Strategists, overthinkers | Analysing without sufficient raw material |
| **Plan first** | Managers, executors | Planning based on assumptions, not evidence |
| **Create first** | Builders, hackers, the impatient | Learning only from failure, expensively |

None of these is wrong. All of them are incomplete without the others.

The framework does not judge your entry point. It asks: which valve have you not crossed recently?

---

## Relation to Other Frameworks

The matrix is the key to these comparisons. CLAP is not derived from any of these — it predates most of them in the author's practice — but the overlaps are illuminating.

| Framework | Learn | Analyse | Plan | Create | What CLAP adds |
| --- | --- | --- | --- | --- | --- |
| **Bloom's Taxonomy** | Remember / Understand | Analyse / Evaluate | — | Create | The matrix; the valves; non-linearity |
| **Kolb's Cycle** | Concrete Experience | Reflective Observation | Abstract Conceptualisation | Active Experimentation | One-way valves; momentum; fractal property |
| **ReAct (AI agents)** | Observe | Reason | — | Act | **Plan** — the missing stage in most AI agents |
| **OODA Loop** | Observe | Orient | Decide | Act | Fractal property; momentum; home boxes |
| **Six Thinking Hats** | White Hat | Red/Black/Yellow | Blue Hat | Green Hat | The matrix; the spiral structure |
| **Hermeneutic Circle** | — | The whole circle | — | — | CLAP externalises what the circle keeps internal |

The most important comparison is **ReAct**. ReAct goes Observe → Reason → Act. It has no Plan stage. This is not an oversight — it reflects a genuine architectural assumption that agents should be fast and flexible. CLAP says: fast and flexible is fine for simple cycles, but without Resource (the Plan→Create valve), complex work collapses.

---

## CLAP and the Dimensions of Knowledge

Each stage operates across multiple **reach levels** — the scope of knowledge being drawn on:

| Reach | What it is | Example in CLAP |
| --- | --- | --- |
| **World** | External peer knowledge | Conference corpus, published research |
| **Enterprise** | Organisational knowledge | Company positioning, strategy documents |
| **Division** | Team/department knowledge | GTM decisions, product roadmap |
| **Team** | Immediate colleagues | Slack conversations, shared decisions |
| **Self** | Personal knowledge and experience | Your own expertise, intuition, history |

The richest Analyse happens when multiple reach levels are in play simultaneously. A decision informed only by World knowledge (what the industry thinks) without Self knowledge (what you specifically know) is incomplete. A decision informed only by Self knowledge without World knowledge is parochial.

**For AI systems:** this reach hierarchy maps directly to the system prompt (Enterprise/Division/Team knowledge) + corpus (World knowledge) + user input (Self knowledge). The most valuable outputs emerge from the collision of all three.

---

## Applying CLAP to AI System Design

CLAP was developed for human cognition. It maps cleanly onto AI system design because good AI systems are trying to replicate good thinking.

| CLAP stage | What an AI system does |
| --- | --- |
| **Learn** | Corpus ingestion, retrieval, contextual grounding |
| **Analyse** | Reasoning, chain-of-thought, multi-perspective critique |
| **Plan** | Structured output, task decomposition, response framing |
| **Create** | Generation, tool use, final response |

**The retrieval question** maps to the Select valve: given everything in the corpus, which parts are worth reasoning with for this query? This is what RAG architectures are trying to solve — and what pre-digested intelligence layers (like LLM Council-generated vitals files) solve more elegantly by doing the Select work at ingestion time rather than query time.

**The system prompt** is the Enterprise/Division/Team knowledge that sits above the World corpus. It is the difference between a system that knows what the industry thinks and a system that knows what *you* think about what the industry thinks.

---

## A Note on Origin

This framework was first developed in approximately 1996 while building the first local government website in London as part of an early E-Government implementation. The original formulation was Learn, Think, Plan, Do — with a matrix identifying the source/target directionality of each stage.

Over thirty years it has been renamed (CLAP, LTPD, Perpetual Idea Machine), extended (bridges, gateways, valves), and applied to personal decisions, organisational change, and now AI system design.

It was rediscovered and formalised in a single conversation on 2026-06-29 — which is itself a demonstration of the fractal property. The conversation was a CLAP cycle about CLAP.

The framework has survived thirty years not because it was written down carefully, but because it was *true enough to keep being useful.* This document is the first attempt to write it down carefully.

---

*"It's CLAP all the way down."*
