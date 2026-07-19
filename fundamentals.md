# Uriam — Fundamentals

*This is the plain-English expansion of [`primitives.md`](./bin/profile/primitives.md) — same structure, same vocabulary, explained rather than formally defined. For strict definitions and lookup tables, see [`reference.md`](./reference.md). For the framework's history, see [`origin.md`](./origin.md). For optional ways to visualize it, see [`analogy-spiral.md`](./analogy-spiral.md) and [`analogy-production.md`](./analogy-production.md) — neither is required reading.*

## The Primitives, in Plain English

**Actor** — a person or an AI system: whatever is capable of doing things and taking on Roles.

**Role** — a responsibility an Actor takes on, not a fixed identity. You play a lot of roles, depending on which quadrant you're in: something like a student while Internalising, a detective while Examining, a maker while Externalising, and so on — more on the specific ones people (and this document) reach for most often in [`analogy-production.md`](./analogy-production.md). Nothing here requires those particular names; they're one illustration, not the only one.

**Internal / External** — a question of ownership, not of medium or body part: Information an Actor owns is Internal to it; Information it doesn't own is External. A machine's own memory is genuinely internal to that machine, even though nothing resembling human comprehension occurs there. A sensor reading sitting in a file nobody consults is external on both ends; the same reading entering a system's own long-term memory is external-to-internal, for that system, because the memory is genuinely its interior.

Recalling something you already knew doesn't count as new Information arriving — a memory, a fact you'd filed away, was always yours, just not active a moment ago. What's actively engaged right now versus what's owned but dormant is a real distinction, borrowed from computer science's own notion of a working set (see `references.md`) — but it's a separate question from Internal/External, not a redefinition of it. Ownership doesn't move when something merely comes back into view.

**Information** — a representation of something in the observable universe. What flows into a Node as a Stimulus, and back out as a Response.

**A Node** transforms one piece of Information into another — an incoming Stimulus becomes an outgoing Response.

## The Graph

Nodes and Edges combine to form a Uriam Graph — the shape an Actor's behavior actually takes, moment to moment.

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

An Edge connects one Node's Response to the next Node's Stimulus, carrying it forward unchanged, and only in one direction — a Response only ever becomes the next Stimulus, never the reverse. Only a Node transforms Internal into External or back again; an Edge just relays.

That gives Edges exactly two types, depending on which side of Internal/External the Response and next Stimulus sit on: Internal handed to Internal, or External handed to External. There's no third kind. A single Edge can never carry an Internal Response into an External Stimulus, or back again — that crossing needs a Node in between to actually do the work.

One structural consequence worth knowing: Internalising and Externalising can never Loop directly onto themselves — doing so would require exactly the Internal↔External crossing an Edge can't make. Only Examining and Interacting can.

### The Edge Contract

An Edge that claimed to turn an Internal Response into an External Stimulus, with nothing in between, would be doing a Node's job without being one: quietly performing the exact transformation this whole model exists to make visible. Every name this framework has ever given its fourth stage before "Interacting" — Do, Creating, Create, Build — turned out to fail for a version of this same reason (the full history is in `origin.md`). If it looks like an Edge just did that crossing, look again: something upstream did the actual converting, and got mislabeled as a relay instead of a Node.

### The Cycle, and Adjacent

The four Nodes fall into one order — Internalising → Examining → Externalising → Interacting → Internalising — and this has to be stated as its own fact, not derived from the Node types alone: Examining and Externalising both start from an Internal Stimulus, and Internalising and Interacting both start from an External one, so a Node's Stimulus type alone never tells you which Node comes next.

A Hop that follows this stated order is **Adjacent**. Not every valid Hop is Adjacent — a Response can validly reach a Node other than the next one in the cycle (Internalising can hand straight to Externalising, skipping Examining entirely, and the Edge carrying it is still perfectly valid) — but only the Hops that follow the stated order count toward Momentum, below.

### The Uriam Graph, and the Fractal Property

Examined closely, a single Node is itself a full Uriam Graph — a smaller Internalising→Examining→Externalising→Interacting cycle, one level down. The Internalising stage of a project *is* its own complete cycle: you interact with small experiments, internalise what they teach you, examine what you found, and externalise the next experiment. This is structurally true at any granularity, not a metaphor — the same four questions apply whether you're looking at five minutes or five years.

### Graph Metrics

Each of these is a plain count — no time window built in, and no judgment about quality. Whether a given Loop was worthwhile, or a Response was actually true, isn't something these measures decide.

- **Velocity** — the number of Hops. Says nothing about which ones; churn and genuine progress both register.
- **Repetitions** — the number of Loops.
- **Momentum** — the number of Adjacent Hops: movement that follows the stated cycle, not just movement to somewhere different.

### Graph Collaborations

A Uriam Graph is owned by an Actor. Each Actor sees every other Actor as external to itself — including another instance of the same underlying system.

**Exchange** — an External-to-External Edge whose Response and next Stimulus belong to two *different* Actors. Only External-to-External Edges can ever cross an Actor boundary this way — Internal Information belongs to whoever owns it, by definition, so it can never be handed directly to another Actor's Internal. This is what collaboration actually is, structurally: one Actor's Interacting-stage output becoming another Actor's Internalising-stage input. A human reading an AI's answer is an Exchange. An AI reading a human's question is the same Exchange, run the other way. Two AI systems handing work back and forth are doing the same thing a human team does — Exchange doesn't care which side of it is a person.

Knowledge in play at any Node also has a **reach** — how far it extends beyond the Actor doing the work: from what's true industry-wide (World), down to what's specific to this one exchange (Self), with Enterprise, Division, and Team in between. The richest thinking pulls on more than one reach level at once — Self knowledge without World knowledge is parochial; World knowledge without Self knowledge is generic.

## Elsewhere

Two things worth knowing about but that don't belong in a section-for-section mirror of `primitives.md`: how Uriam compares to Bloom's, Kolb's, ReAct, OODA, Six Thinking Hats, the Hermeneutic Circle, Belbin, and multi-agent orchestration frameworks; and how each Node maps onto AI system design specifically (corpus ingestion, reasoning, structured output, tool execution). Both live as full tables in `reference.md`'s "Usage" section, not duplicated here.

---

*This document mirrors [`primitives.md`](./bin/profile/primitives.md) section for section — if the two ever disagree, `primitives.md` is correct. Pictures for the vocabulary above live in [`analogy-spiral.md`](./analogy-spiral.md) and [`analogy-production.md`](./analogy-production.md); neither is required reading.*
