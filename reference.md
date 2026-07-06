# Spiral — Reference

Strict definitions and lookup tables. No narrative, no metaphor beyond what's needed to define a term. For the full explanation of why any of this works, see [`about.md`](./about.md). For the framework's history, see [`origin.md`](./origin.md).

Two tiers below. **Core Concepts** are facts — what a term *is*, no rationale attached. **Usage** is how each concept gets *applied* — techniques, decision criteria, comparisons. Core Concepts are foundational enough that `about.md` echoes them (in prose, or as a table where prose can't substitute); Usage material is never duplicated there — `about.md` only links to it.

---

## Core Concepts

- **Learn** — External source → internal target. Something outside becomes part of what you know.
- **Think** — Internal source → internal target. Working on what you already have; nothing new enters, nothing yet leaves.
- **Articulate** — Internal source → external target. Internal reasoning made legible to someone or something outside yourself.
- **Build** — External source → external target. Acting on the world; the world responds; something new exists that didn't before.
- **The Matrix** — The 2×2 grid of source (where input comes from) × target (where output goes) that the four stages derive from.
- **The Cast** — The four characters, one per stage: the Muse (Think), the Director (Articulate), the Producer (Build), the Critic (Learn).
- **The Muse** — Owns Think. Turns what Learn gathered into an actual idea.
- **The Director** — Owns Articulate. Turns an idea into a take specific enough to be wrong.
- **The Producer** — Owns Build. Turns a take into something that can actually be mounted.
- **The Critic** — Owns Learn. Turns the verdict on what was Built into material for next time.
- **The Stage Manager** — The fifth presence. Owns no content, only the cues — decides when it's time to move from one cast member to the next, and can act mid-stage, not only at a cue, when momentum is under threat.
- **Cue** — The fixed crossing point between one stage and the next. Four per cycle, named Separate, Elect, Enable, and Sense.
- **Notes** — What happens at a cue: a check of what's understood against what's needed, before the Hero moves on. Quiet by default; a full multi-voice version exists ("Convening the cast for review" in the skill file — see "Usage," below, for when it earns its cost).
- **Hero** — Whoever is actually doing the work and crossing the cues — a person, or an AI.
- **Momentum** — The rate at which the cycle moves. High: each revolution lands somewhere new. Low: spinning in place, avoiding the cast. False: skipping stages to move fast.
- **Home box** — The stage someone gravitates toward, where they spend disproportionate time.
- **Neglected character** — The cast member someone most often avoids meeting.
- **The Fractal Property** — Every stage is itself a full Spiral cycle; the framework applies recursively at any granularity, cues included.
- **Reach levels** — The scope of knowledge in play at any stage: World, Enterprise, Division, Team, Self.
- **Code-switching** — Deliberately changing register (Muse/Director/Producer/Critic) to fit context, while one continuous self persists underneath doing the switching.

### The Matrix

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Learn** | **Build** |
| **Internal source** | **Think** | **Articulate** |

### The Cast

| Stage | Who's there | What they help you do |
| --- | --- | --- |
| **Think** | **The Muse** | Turn what Learn gathered into an actual idea |
| **Articulate** | **The Director** | Turn the idea into a take specific enough to be wrong |
| **Build** | **The Producer** | Turn the take into something that can actually be mounted |
| **Learn** | **The Critic** | Turn the verdict on what you Built into material you can use next time |

### The Cues

| Cue | Verb | What Notes decide |
| --- | --- | --- |
| Learn → Think | **Separate** | Separate what happened from what it felt like — decide what's actually worth thinking about |
| Think → Articulate | **Elect** | Choose a direction; commit to a take specific enough to be wrong |
| Articulate → Build | **Enable** | Clear whatever stands between the plan and actually doing it |
| Build → Learn | **Sense** | Notice what the outcome taught you, before deciding what to learn from it |

### Reach Levels

| Reach | What it is | Example in Spiral |
| --- | --- | --- |
| **World** | External peer knowledge | Conference corpus, published research |
| **Enterprise** | Organisational knowledge | Company positioning, strategy documents |
| **Division** | Team/department knowledge | GTM decisions, product roadmap |
| **Team** | Immediate colleagues | Slack conversations, shared decisions |
| **Self** | Personal knowledge and experience | Your own expertise, intuition, history |

---

## Usage

How the concepts above get applied — techniques, decision criteria, comparisons. Nothing in this section is duplicated in `about.md`; it's linked to instead.

### Techniques Each Character Draws On

Each character's job description is deliberately abstract — "turn the idea into a take specific enough to be wrong" has to mean something different for a personal decision than for a software spec. Rather than pick one universal technique per character (tried, and broke immediately on Spiral's own README example: "As a traveler, I want to visit Geneva" is not a real articulation technique), each character has a menu of established, named, well-documented methods to draw from — pick whichever one's actual domain matches the situation. The specific reference matters: it's what lets both the skill and the model agree on exactly what a name denotes, rather than a vague gesture at "be more rigorous." See `.claude/skills/spiral/SKILL.md` for when it's appropriate to name one of these out loud versus translate it into plain language.

#### The Critic (Learn)

| Method | Specific reference | Fits because |
| --- | --- | --- |
| After-Action Review | US Army's 4-question format (expected/actual/why/next) | Converts an outcome's verdict into reusable knowledge |
| Blameless Postmortem | Google SRE Book's postmortem culture | Extracts lessons from failure without assigning blame |
| Kolb's Reflective Observation | Kolb's Experiential Learning Cycle, stage 2 specifically | Digests raw experience before forming any concept |
| Double-Loop Learning | Argyris & Schön's governing-variables model | Questions whether the goal itself was right |
| 5 Whys | Toyota Production System root-cause technique | Chases a symptom back to its actual cause |
| Start/Stop/Continue | Standard Agile retrospective format | Recurring ritual turning outcomes into forward action |

#### The Muse (Think)

| Method | Specific reference | Fits because |
| --- | --- | --- |
| Socratic Method | Platonic elenchus (self-questioning to test a claim) | Interrogates a claim already held, unexamined |
| Dialectical Reasoning | Hegelian thesis-antithesis-synthesis triad | Reconciles opposing ideas already in mind |
| First Principles Thinking | Cartesian/Aristotelian decomposition to fundamentals | Strips a concept down, rebuilds from scratch |
| Six Thinking Hats | De Bono's six sequential lenses | Forces six angles onto the same material |
| Second-Order Thinking | Munger's latticework of mental models | Traces downstream consequences of an existing idea |
| Hermeneutic Circle | Whole-informs-parts-informs-whole interpretive method | Whole reframes parts; parts refine the whole |

#### The Director (Articulate)

| Method | Specific reference | Fits because |
| --- | --- | --- |
| SMART Goals | Doran's 1981 Specific/Measurable/Achievable/Relevant/Time-bound | Makes intent checkable, not just aspirational |
| User Stories + Acceptance Criteria | Mike Cohn's Agile format | Frames a need as testable, falsifiable intent |
| PRD | Standard product-requirements-document format | Commits problem and requirements before building starts |
| RFC / ADR | Nygard's Context-Decision-Consequences template | Records a decision's reasoning so it's challengeable |
| The Pyramid Principle | Barbara Minto's MECE, conclusion-first structure | Leads with the answer, then structures support |
| PR-FAQ | Amazon's "Working Backwards" pre-build press release | Writes the finished result before anything's built |

#### The Producer (Build)

| Method | Specific reference | Fits because |
| --- | --- | --- |
| Pre-mortem | Gary Klein's 2007 HBR "Project Premortem" | Imagines failure first, to catch it early |
| Definition of Done | Scrum Guide's completion-criteria artifact | Sets the checkable bar for "actually finished" |
| MVP / Build-Measure-Learn | Eric Ries's Lean Startup loop | Ships the smallest real thing to learn from |
| Kanban WIP Limits | Kanban Method's work-in-progress caps | Caps in-progress work so things get finished |
| PDCA's "Do" phase | Deming/Toyota Plan-Do-Check-Act cycle | Executes the plan at real scale, for real |

None of these are mandatory and none is "the" technique for a character — they're a vocabulary of well-trodden, nameable patterns to reach for instead of reasoning from a vague personality trait.

### The Stage Manager — Who Plays the Role

| Flow | Who plays the Stage Manager | Grounding |
| --- | --- | --- |
| **Human, solo** | Internal executive function — the transition/initiation faculty, distinct from the content-generating faculty | Zimmerman's self-regulated learning cycle; Gollwitzer's implementation intentions; executive-function research on task-initiation (the well-documented gap between having an idea and acting on it) |
| **AI, solo** | Orchestrator logic — iteration budgets, reflection nodes, the state machine governing phase transitions | ReAct's missing Articulate step is this failure mode by another name: no governance of when Think ends, so the loop thrashes or never converges |
| **AI → Human** | Whichever side holds the authority to call the cue: the assistant nudging a stalled human, or the human cutting off an over-reasoning agent | Horvitz's mixed-initiative interaction research; automation bias (deferring the cue-call to the AI even when it's wrong) |
| **Human → Human** | A distinct, named role in the group — not the person doing the Learning, Thinking, Articulating, or Building | Scrum Master; chief of staff; the literal theatrical stage manager, who calls cues but never appears onstage |
| **AI → AI** | A supervisor/manager agent whose only output is whose turn it is and whether the phase is complete | Already shipped: LangGraph's supervisor pattern, AutoGen's `GroupChatManager`, CrewAI's hierarchical-process manager, MetaGPT's SOP-driven role router |

### Non-Linearity and Entry Points

| Entry point | Who does this | Risk |
| --- | --- | --- |
| **Learning first** | Researchers, readers, the cautious | Never meeting the Director |
| **Thinking first** | Strategists, overthinkers | Thinking without sufficient raw material |
| **Articulating first** | Managers, executors | Articulating based on assumptions, not evidence |
| **Building first** | Builders, hackers, the impatient | Learning only from failure, expensively |

### Relation to Other Frameworks

| Framework | Learn | Think | Articulate | Build | What Spiral adds |
| --- | --- | --- | --- | --- | --- |
| **Bloom's Taxonomy** | Remember / Understand | Analyse / Evaluate | — | Create | The matrix; the cast; non-linearity |
| **Kolb's Cycle** | Concrete Experience | Reflective Observation | Abstract Conceptualisation | Active Experimentation | The cast; momentum; fractal property |
| **ReAct (AI agents)** | Observe | Think | — | Act | **Articulate** — the missing stage in most AI agents |
| **OODA Loop** | Observe | Orient | Decide | Act | Fractal property; momentum; home boxes |
| **Six Thinking Hats** | White Hat | Red/Black/Yellow | — | Green Hat | The matrix; the spiral structure; the Blue Hat is Six Thinking Hats' own Stage Manager, not an Articulate-analog — the same missing-Articulate gap ReAct has, just less visible |
| **Hermeneutic Circle** | — | The whole circle | — | — | Spiral externalises what the circle keeps internal |
| **Belbin Team Roles** | — | — | — | — | Independent validation for **the Stage Manager**: Belbin's Coordinator role was originally named "Chairman" before being renamed — the same correction, authority word to process word, that this framework just made |
| **Multi-agent orchestration** (AutoGen, CrewAI, LangGraph) | Retrieval / tool nodes | Worker-agent reasoning | Task routing | Worker-agent execution | Confirms **the Stage Manager** is buildable: supervisor/manager agents already do this exact job in production, without performing any Learn/Think/Articulate/Build work themselves |

### Applying Spiral to AI System Design

| Spiral stage | What an AI system does |
| --- | --- |
| **Learn** | Corpus ingestion, retrieval, contextual grounding |
| **Think** | Reasoning, chain-of-thought, multi-perspective critique |
| **Articulate** | Structured output, task decomposition, response framing |
| **Build** | Generation, tool use, final response |

### Deciding When to Hold Full Notes

A full Notes session — the multi-voice mode described in `about.md`'s "The Cues," implemented as "Convening the cast for review" in the skill file — costs real tokens, real latency, and real attention. Most cues shouldn't pay for it. An agent implementing this framework needs an actual rule for when the expense is worth it, not "use your judgement":

| Signal | Favors quiet Notes (default) | Favors full Notes |
| --- | --- | --- |
| **Position in the fractal hierarchy** | An interior cue, inside a nested sub-cycle | A cue that closes the top-level cycle — the one whose output actually reaches the user or takes an action |
| **Cost of being wrong** | Cheap to redo — another Learn pass, a discarded draft | Expensive or irreversible — commits to a claim that gets published, or a Build that changes external state |
| **Evidence quality** | The last stage's output is unambiguous — one clear reading | The evidence genuinely supports more than one defensible interpretation — thin corpus, conflicting sources, a close call |
| **Momentum history** | First time at this cue this cycle | The same cue has been crossed and re-crossed without real progress — a quiet call already failed once |
| **Explicit request** | Not asked for | Explicitly asked for ("convene the cast on that," "run a Spiral review") |

Default to quiet. Convening is the exception that earns its cost, not the baseline behaviour — the multi-agent orchestration frameworks above converged independently on lightweight supervisors precisely because full multi-voice deliberation on every step is too expensive to run by default. A Claude Code implementation working against real data can treat this table as literal branching logic: score the cue against these five signals, and only pay for a full Notes session when at least the fractal-position signal and one other both point that way.
