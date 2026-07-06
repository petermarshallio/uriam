# Spiral — A Framework for Human and Machine Intelligence

*This is the narrative explanation — what Spiral is and why it works. For strict definitions and lookup tables, see [`reference.md`](./reference.md). For the framework's history, see [`origin.md`](./origin.md).*

## The Core Idea

Spiral is a framework for understanding how intelligence — human or artificial — moves from raw input to meaningful output. It describes four fundamental cognitive stages, the cast of characters who inhabit each one, the Stage Manager who decides when you're ready to meet them, and the property of momentum that determines how well the whole system works.

It is not a linear process. It is a spiral — more precisely, a **spiral**: a curve that circles through the same four positions again and again. Instead of spiralling out of control, **Spiral** is intended
to provide a mechanism to climb and to control.

## Spiralling out of control?

A generic spiral — a nautilus shell, for instance — grows bigger with every turn. That's a beautiful image, but it isn't quite honest about what happens here. This spiral is more like a staircase: the same shape on every turn — the same radius, the same four moves.

And that means you're not "spiraling." A spiral *staircase* is purposeful, it requires effort, and is about elevation. with each disciplined step.

## The Matrix

**This Is the Foundation** There is a 2×2 matrix that everything derives from.

The two axes are **source** (where does the input come from?) and **target** (where does the output go?):

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Learn** | **Build** |
| **Internal source** | **Think** | **Articulate** |

This matrix is the lens. If you understand it, you can interpret the framework in your own words — and you can map almost any cognitive framework, AI architecture, or decision-making model onto it.

- **Learn** — the world comes *in*. You absorb, accumulate, receive.
- **Think** — you work on what's *inside*. You think, connect, critique.
- **Articulate** — your internal thinking goes *out* as structured intention. You make it concrete.
- **Build** — you act on the world, and the world responds. Something new exists.

## The Four Quadrants

### Learn

**External → Internal** Taking in knowledge from the outside world. Reading. Listening. Watching. Accumulating. This is what a child does when they go to the library and come back with 90 books about cheese. It is also what an AI does when it ingests a corpus.

Learning is not passive — it requires selection. You cannot learn everything. The quality of what you choose to learn determines the quality of everything downstream.

**In AI terms:** corpus ingestion, retrieval, contextual grounding. The vitals files in a conference talk corpus are the product of Learn.

**In human terms:** research, reading, listening, observation, experience.

### Think

**Internal → Internal** Working on what you already have inside. Connecting dots. Reasoning. Critiquing. Weighing options. This is the stage where raw learning becomes understanding.

Thinking is the home box for many people — including the author of this framework. It is seductive because it feels like progress. It can become a trap. The Muse can only give you so much cover — eventually the Stage Manager walks in and asks if you're ready to go meet the Director.

**In AI terms:** reasoning, chain-of-thought — the same territory ReAct calls "Reason." The LLM Council's Perspectives are the product of Think applied to Learn.

**In human terms:** critical thinking, de Bono's Six Thinking Hats, the hermeneutic circle, dot-connecting.

### Articulate

**Internal → External** Structured intention made concrete. This is the stage that most AI agents skip — and why they fail at anything requiring sustained, coordinated effort. Articulate is where internal thinking becomes external artefact: a SMART objective, a work package, a Gantt chart, a prioritised backlog.

Articulate is not thinking about what to do. It is writing it down in a form that others — or your future self — can act on.

**In AI terms:** task decomposition, agent planning, structured output. The step between Think and Act that ReAct agents lack.

**In human terms:** project management, SMART goals, sprint planning, architectural design documents.

### Build

**External → External** Acting on the world. The world responds. Something new exists that did not exist before. This is not merely "doing" — it is the act of creation, which implies intentionality and result. A wolf can blow on your house. Build is the stage where you find out if it holds.

Build generates the raw material for the next Learn. The cycle continues.

**In AI terms:** generation, tool use, execution, deployment. The "Act" in ReAct.

**In human terms:** building, writing, shipping, speaking, deciding.

## The Cast

Each stage has someone already in it. Not a mechanism — a person, and each one wants something different from you. (The roster — which character owns which stage — is in reference.md; here's who they are.)

The move through the spiral moves forward; you can't go back and reshoot yesterday's scene. You do not retreat to a previous stage, you complete
the cycle and begin a new one, richer for the revolution you just completed.

Meeting **the Director** matters most for people who live in Think, because they're the one who eventually has to leave it. The Director doesn't demand certainty. They demand a hypothesis — something specific enough to be wrong. A scientist's commitment, not a bureaucrat's sign-off.

**The Producer** is the character most often avoided. It's why houses fall down when wolves blow on them. The plan was good. Nobody checked whether it could actually be built.

**The Muse** is the character people mistake for the whole job. Inspiration feels like progress, so people camp with her long after she's given them enough to work with — that's not her fault, and it isn't a reason to stay.

**The Critic** is the character people flinch from meeting. But the verdict isn't a punishment — it's the raw material for the next Learn. Refuse to meet her and the cycle starves.

Every character is really asking the same thing, in their own language: **what are you making out of what I've given you?**

Not "are you done?" — you are never done.

None of them will come and get you, though. Knowing when to go find them is a different job entirely — that's the Stage Manager.

Each character also draws on a menu of established, named techniques rather than one universal method per character — SMART goals and PR-FAQs for the Director, pre-mortems and Definition of Done for the Producer, Socratic questioning and first-principles thinking for the Muse, after-action reviews and blameless postmortems for the Critic. The full library, with specific sources and why each one fits, is in reference.md.

---

## The Stage Manager

There is a fifth presence, but it is different in kind from the other four. The Muse, the Director, the Producer, and the Critic each own one specific stage — they're waiting inside it, ready to help you do that stage's work, but none of them will come looking for you. The Stage Manager owns none of the content. Its only job is deciding when it's time to go meet them — a decision with a name, borrowed from the same theatre this cast came from: **calling the cue**. (See "The Cues" below for what happens at one.)

This is not a hierarchy. The Stage Manager doesn't decide the order — the cycle already fixes that completely — and it doesn't outrank the cast. It only asks the question underneath all four of theirs: *is it time to call the cue?*

That question isn't only asked passively, waiting for a natural pause between stages. Protecting momentum sometimes means forcing the issue mid-stage — closing down a Think that's overstaying its welcome, enforcing an end to circular creative options before anyone feels ready — because the Stage Manager's job was never to certify that a stage's content is finished, only that the whole system keeps moving. It shows up wherever momentum is under threat, not only at the four fixed cues.

The role changes shape depending on who's in the loop — a solo human, a solo AI, an AI and a human handing off to each other, a team of people, a team of agents. The full breakdown, with the academic and engineering grounding for each, is in reference.md.

The consistency across all five is the point. In every flow, the Stage Manager never does Learn/Think/Articulate/Build work itself — and in every flow, its absence produces the same failure: stalling, thrashing, or false momentum. Not five different failure modes. One.

### One operator, four registers

Everything above describes the Cast as company you meet. But for a solo operator — a single person working alone, or a single AI with no other agents to call on — there's no one else in the room. The Muse's associative looseness, the Director's decisiveness, the Producer's resourcefulness, the Critic's evaluative honesty: you have to produce all four yourself, in turn. Meeting the cast, solo, means becoming them for as long as their stage needs you to.

This is a different difficulty than the one Momentum names. Momentum failure is about *time* — staying too long in one stage. This is about *register* — being unable to actually think with the Muse's looseness while still holding the Critic's honesty from the stage before, or unable to drop the Director's decisiveness once Build needs the Producer's improvisation instead. Everyone is fluent in their home box's register and clumsy in at least one other — usually, unsurprisingly, the neglected character's.

The precise term for this isn't multiplicity as pathology, it's **code-switching**: deliberately changing register to fit context while one continuous self persists underneath, doing the switching. Two grounded precedents, one per register:

- **Human:** Transactional Analysis' Parent/Adult/Child ego states — distinct behavioral registers a person moves between deliberately, without losing continuity of self. De Bono's own Blue Hat (see the framework comparison below) is the same idea inside a framework Spiral is already compared to: it isn't a fifth hat alongside the other four, it's the process-control hat, worn by whoever decides which of the other four the group should be wearing — and it can think in any of them when needed.
- **AI:** a context switch, in the plain operating-systems sense — a process's state is suspended, a different process's state is loaded in and executed, and something outside both of them keeps the scheduling bookkeeping across every swap. That bookkeeping layer isn't optional decoration; without it, "switching" is just amnesia.

For an AI system this reframes what the Stage Manager actually does in solo operation. It isn't only the outside voice asking "is it time?" — it has to be able to condition itself into each stage's register (generative for Think, decisive for Articulate, resourceful for Build, evaluative for Learn), do that stage's work in that register, then step back out to the layer that tracks the whole arc and knows when the next switch is due. One operator, four registers, one continuous thread of oversight underneath all of them. That thread — not any single register — is the Stage Manager.

---

## The Cues

Between every stage and the next there's a fixed point where whoever is doing the work — call them the Hero — crosses from one cast member's territory into another's. Theatre already has a word for that point: a **cue**. It isn't a metaphor reached for after the fact — calling cues is the Stage Manager's literal job, four times around the cycle, not once.

A cue is not a formality to wave through. Crossing it means answering something real: given what the last stage actually produced, what happens now? Neither cast member either side of the cue can answer that alone — the one being left knows what just happened, the one about to be met knows what's needed next. What happens at a cue is called **Notes**: a check of what's understood against what's needed, before the Hero is allowed to move.

Most Notes are one clause, wordless, over as soon as they start — the everyday version of "that's enough, go," already described above as the Stage Manager quietly deciding it's time. Some cues earn the full version instead: several cast members speaking in turn before a direction is committed to. That fuller version isn't a new mechanism — it's "Convening the cast for review" (see the skill file), renamed for what it structurally is: a full Notes session, held at a cue, instead of the ordinary quiet one. See reference.md's "Deciding When to Hold Full Notes" for when that expense is worth paying.

The four cues already have names — recovered rather than invented. In a 2011–2012 version of this framework, when the stages were still Creation, Learning, Analysis, and Planning, the transitions between them were already called **EESS**: Elect, Enable, Sense, Separate — driven by a connecting force called Enertia, which this document now calls Momentum. Mapped onto today's stages, the fit is exact — the mapping table is in reference.md.

Every nested cycle the fractal property opens up has its own four cues, usually quiet ones — see reference.md's "Deciding When to Hold Full Notes" for how to tell the difference.

---

## Momentum

Momentum is not a stage. It is a property of the whole system — the rate at which you move through the spiral. The Stage Manager is what embodies that property in practice: not a sixth stage, but the role that exists to protect momentum wherever it's under threat.

**High momentum:** each revolution lands you somewhere genuinely new. The cast shows up readily because sufficient work was done in each stage.

**Low momentum:** spinning on the same level. Stuck in Thinking. Avoiding the cast. Returning to Learn because the Director was never met.

**False momentum:** moving fast but skipping stages. Lots of Build without enough Learn or Think. The house gets built quickly. Then the wolf arrives.

Momentum is killed by:

- Perfectionism in Think (the thinking trap)
- Avoiding the Producer (the execution trap)
- Insufficient Learning before Thinking (the opinion trap)

Momentum is built by:

- Meeting the Director with a testable hypothesis, not a proven answer
- Treating the Critic's verdict as genuinely generative, not just evaluation
- Allowing the next Learn to be informed by what Build revealed

## The Fractal Property — Spirals All the Way Down

Each stage of Spiral is itself a full Spiral cycle.

The Learn stage of a project *is* a Spiral cycle: you Build experiments to learn from, Learn from them, Think about what you found, Articulate the next experiment.

The Think stage of a decision *is* a Spiral cycle: you Build hypotheses, Learn what they imply, think about the implications, Articulate which to test.

This is not a metaphor. It is structurally true. Spiral scales from a five-minute decision to a thirty-year career. The same four questions, the same four characters, applied recursively at every level of granularity.

> "It's Spirals all the way down."

This fractal property means the framework is never the wrong size. If a stage feels too large to act on, run Spiral inside it. The cycle will break it into manageable revolutions.

## Non-Linearity and Entry Points

Where you start on the Spiral is up to you.

People have a **home box** — the stage they gravitate toward, where they spend disproportionate time. They also have a **neglected character** — the one they most often avoid meeting. Researchers and readers tend to enter through Learning, and risk never meeting the Director; strategists and overthinkers enter through Thinking, and risk thinking without sufficient raw material; managers and executors enter through Articulating, and risk articulating from assumptions rather than evidence; builders and hackers enter through Building, and risk learning only from failure, expensively. (The table version is in reference.md.)

None of these is wrong. All of them are incomplete without the others.

The framework does not judge your entry point. It asks: which character have you not met recently?

## Relation to Other Frameworks

The matrix is the key to these comparisons. Spiral is not derived from any of these — it predates most of them in the author's practice — but the overlaps are illuminating. The full comparison table (Bloom's Taxonomy, Kolb's Cycle, ReAct, OODA, Six Thinking Hats, the Hermeneutic Circle, Belbin Team Roles, multi-agent orchestration) is in reference.md.

The most important comparison is **ReAct**. ReAct goes Observe → Reason → Act. Its middle step covers the same territory Spiral calls Think — we've just chosen a plainer word for it. The gap is what comes after: ReAct has no Articulate stage. This is not an oversight — it reflects a genuine architectural assumption that agents should be fast and flexible. Spiral says: fast and flexible is fine for simple cycles, but without meeting the Producer at Articulate→Build, complex work collapses.

A second comparison is worth naming even though it isn't a single framework: multi-agent orchestration systems. AutoGen's `GroupChatManager`, CrewAI's hierarchical-process manager agent, and MetaGPT's SOP-driven role router all exist to solve exactly one problem — whose turn is it, and is this phase done — without performing any of the Learn/Think/Articulate/Build work themselves. Three engineering teams, solving unrelated problems, converged independently on the same role. That convergence is stronger evidence for the Stage Manager than any single analogy could be.

---

## Spiral and the Dimensions of Knowledge

Each stage operates across multiple **reach levels** — the scope of knowledge being drawn on: World, Enterprise, Division, Team, and Self, each broader or narrower than the last. (The table with examples is in reference.md.)

The richest thinking happens when multiple reach levels are in play simultaneously. A decision informed only by World knowledge (what the industry thinks) without Self knowledge (what you specifically know) is incomplete. A decision informed only by Self knowledge without World knowledge is parochial.

**For AI systems:** this reach hierarchy maps directly to the system prompt (Enterprise/Division/Team knowledge) + corpus (World knowledge) + user input (Self knowledge). The most valuable outputs emerge from the collision of all three.

## Applying Spiral to AI System Design

Spiral was developed for human cognition. It maps cleanly onto AI system design because good AI systems are trying to replicate good thinking — Learn as corpus ingestion and retrieval, Think as reasoning and critique, Articulate as structured output, Build as generation and tool use. (The table is in reference.md.)

**The retrieval question** is really a Muse question: given everything in the corpus, which parts are worth thinking with for this query? This is what RAG architectures are trying to solve — and what pre-digested intelligence layers (like LLM Council-generated vitals files) solve more elegantly by doing that work at ingestion time rather than query time.

**The system prompt** is the Enterprise/Division/Team knowledge that sits above the World corpus. It is the difference between a system that knows what the industry thinks and a system that knows what *you* think about what the industry thinks.

A full multi-voice Notes session (see "The Cues," above) costs real tokens, latency, and attention, so it shouldn't be the default at every cue — reference.md's "Deciding When to Hold Full Notes" gives the exact signals worth scoring a cue against, framed as literal branching logic a Claude Code implementation can use.

## Origin, briefly

This framework is decades old: first developed in 1999, renamed more than once since, rediscovered and properly written down in 2026. The full history — every name it's worn, including one, "the FOBI controller," that turns out to have been the Stage Manager all along — is in [`origin.md`](./origin.md).

## There's more to think about...

**What happens when two musicians are in a spiral conversation?**

Two people, each moving through their own spiral, might relate the way two voices in music do — and music may have sharper vocabulary for that relationship than "same" and "different" allow.

**Same state = unison.** Two voices, same note, same time. It reinforces — but unison has no independent voices in it. Two people both in Think together can feel validating, and still be a shared home box: mutual rumination, with nobody there to sound the Director for the other.

**Different state isn't automatically harmony.** Harmony, strictly, is consonance — different notes that are stable together (one person Learning while the other Thinks on what was just found: genuinely complementary, restful difference). But different states are just as often dissonance — unstable, not restful, wanting to move. Dissonance isn't a flaw in music; it's the engine. A suspended 4th, a leading tone a half-step below the tonic — these exist specifically to create a pull that only resolves by moving. That's a closer model for what a Spiral character actually is than harmony: the Director showing up isn't a pleasant consonant chord, it's the dissonant note that won't let you rest in Think any longer.

**The "pull" has an exact name, twice over.** The gravitational tendency of an unstable tone toward its resolution is a leading-tone pull. And the specific move of stepping into a boundary character before the other person is ready to leave their stage — sounding the Director while someone is still Articulating — has an exact technical name too: a suspension. You deliberately carry a tone over into a harmony where it no longer belongs, so it reads as dissonant against the new chord — and that dissonance is what does the pulling. The other person's job isn't to resist it; it's to resolve, the way a suspended 4th falls to the 3rd.

| Spiral situation | Musical term |
| --- | --- |
| Same stage, same time | Unison |
| Different, complementary, stable together | Consonance |
| Different, unresolved, wants to move | Dissonance |
| One voices the next character early, creating that want | Suspension |
| The gravitational tendency toward the next stage | Leading-tone pull |
| The other person actually crossing | Resolution |
| Two independent, self-coherent spirals sounding together over time | Counterpoint |

This is a human-to-human proposition, not yet an agent-to-human one — a different claim than the operating modes in `.claude/skills/spiral/SKILL.md`. Undeveloped. Worth sitting with.
