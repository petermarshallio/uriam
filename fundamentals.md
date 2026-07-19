# Uriam — Fundamentals

*This is the plain-English expansion of [`primitives.md`](./bin/profile/primitives.md) — same structure, same vocabulary, explained rather than formally defined. For strict definitions and lookup tables, see [`reference.md`](./reference.md). For the framework's history, see [`origin.md`](./origin.md). For optional ways to visualize it, see [`analogy-spiral.md`](./analogy-spiral.md) and [`analogy-production.md`](./analogy-production.md) — neither is required reading.*

## The Primitives, in Plain English

**Actor** — a person or an AI system: whatever is capable of doing things and taking on Roles.

**Role** — a responsibility an Actor takes on, not a fixed identity. You play a lot of roles, depending on which quadrant you're in: something like a student while Internalising, a detective while Examining, a maker while Externalising, and so on — more on the specific ones people (and this document) reach for most often in [`analogy-production.md`](./analogy-production.md). Nothing here requires those particular names; they're one illustration, not the only one.

**Internal / External** — a question of ownership, not of medium or body part: Information an Actor owns is Internal to it; Information it doesn't own is External. A machine's own memory is genuinely internal to that machine, even though nothing resembling human comprehension occurs there. A sensor reading sitting in a file nobody consults is external on both ends; the same reading entering a system's own long-term memory is external-to-internal, for that system, because the memory is genuinely its interior.

Recalling something you already knew doesn't count as new Information arriving — a memory, a fact you'd filed away, was always yours, just not active a moment ago. What's actively engaged right now versus what's owned but dormant is a real distinction, borrowed from computer science's own notion of a working set (see `references.md`) — but it's a separate question from Internal/External, not a redefinition of it. Ownership doesn't move when something merely comes back into view.

**A Node** transforms one occurrence into another — an incoming Stimulus becomes an outgoing Response.

## The Graph

Nodes and Edges combine to form a Behavior Graph — the shape an Actor's behavior actually takes, moment to moment.

### The Four Nodes

Every Node has a source (where its Stimulus comes from) and a target (where its Response goes) — each Internal or External. That gives four possible Nodes:

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Internalising** (A) | **Interacting** (D) |
| **Internal source** | **Examining** (B) | **Externalising** (C) |

- **Internalising** — the world comes in. Reading, listening, watching, accumulating.
- **Examining** — you work on what's already inside. Reasoning, connecting, critiquing — nothing new enters, nothing yet leaves.
- **Externalising** — internal thinking goes out as something concrete. A memo, a plan, a line of code, a spoken confession.
- **Interacting** — something already out there meets something else already out there, and the world responds. Not the moment a plan becomes real (that already happened, at Externalising) — what happens *after*: whether it holds.

A traversal that lands back on the same Node is a **Loop**. One that lands on a different Node is a **Hop**.

### Edges

An Edge connects one Node's Response to the next Node's Stimulus, carrying it forward unchanged. Only a Node transforms Internal into External or back again; an Edge just relays.

That gives Edges a type too, depending on whether the Response's Internal/External-ness survives the handoff:

- **Match** — the Response and the next Stimulus share a type. This is what a normal traversal looks like.
- **Mismatch** — they differ. Internal becomes External, or vice versa, with no Node in between to actually do that work.

### The Edge Contract

Mismatch edges are not valid — they can't actually be traversed. An Edge that claimed to turn an Internal Response into an External Stimulus, with nothing in between, would be doing a Node's job without being one: quietly performing the exact transformation this whole model exists to make visible. Every name this framework has ever given its fourth stage before "Interacting" — Do, Creating, Create, Build — turned out to fail for a version of this same reason (the full history is in `origin.md`). If it looks like a Mismatch happened, look again: something upstream did the actual converting, and got mislabeled as a relay instead of a Node.

### The Behavior Graph, and the Fractal Property

Examined closely, a single Node is itself a full Behavior Graph — a smaller Internalising→Examining→Externalising→Interacting cycle, one level down. The Internalising stage of a project *is* its own complete cycle: you interact with small experiments, internalise what they teach you, examine what you found, and externalise the next experiment. This is structurally true at any granularity, not a metaphor — the same four questions apply whether you're looking at five minutes or five years.

### Graph Metrics

Each of these counts something, over a period — the measure isn't the thing itself.

- **Velocity** — the number of Edge traversals. Says nothing about which ones; churn and genuine progress both register.
- **Recurrence** — the number of Loops. High Recurrence usually means **Stagnation** — spending Velocity without ever leaving a Node — though not always: a deliberately slow, contemplative pace looks the same from the outside and isn't a malfunction.
- **Momentum** — the number of Matched Hops. The closest thing to "real progress": movement to a genuinely different Node, carried by a Response the next Node can actually use.

### Graph Collaborations

A Behavior Graph is owned by an Actor. Each Actor sees every other Actor as external to itself — including another instance of the same underlying system.

**Exchange** — a d-type edge (External→External) whose Response and next Stimulus belong to two *different* Actors. This is what collaboration actually is, structurally: one Actor's Interacting-stage output becoming another Actor's Internalising-stage input. A human reading an AI's answer is an Exchange. An AI reading a human's question is the same Exchange, run the other way. Two AI systems handing work back and forth are doing the same thing a human team does — Exchange doesn't care which side of it is a person.

Knowledge in play at any Node also has a **reach** — how far it extends beyond the Actor doing the work: from what's true industry-wide (World), down to what's specific to this one exchange (Self), with Enterprise, Division, and Team in between. The richest thinking pulls on more than one reach level at once — Self knowledge without World knowledge is parochial; World knowledge without Self knowledge is generic.

## Elsewhere

Two things worth knowing about but that don't belong in a section-for-section mirror of `primitives.md`: how Uriam compares to Bloom's, Kolb's, ReAct, OODA, Six Thinking Hats, the Hermeneutic Circle, Belbin, and multi-agent orchestration frameworks; and how each Node maps onto AI system design specifically (corpus ingestion, reasoning, structured output, tool execution). Both live as full tables in `reference.md`'s "Usage" section, not duplicated here.

---

*This document mirrors [`primitives.md`](./bin/profile/primitives.md) section for section — if the two ever disagree, `primitives.md` is correct. Pictures for the vocabulary above live in [`analogy-spiral.md`](./analogy-spiral.md) and [`analogy-production.md`](./analogy-production.md); neither is required reading.*
