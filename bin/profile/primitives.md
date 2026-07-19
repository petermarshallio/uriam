# Uriam Primitives

*Test prompts built on these definitions live in `instructions.md`.*

## Primitives

Actor: an entity capable of performing behavior.
Role: a responsibility assigned to an Actor.

Internal is part of an Actor's current state.
External is not.

A Node transforms one occurrence into another.
A Node's incoming occurrence is its Stimulus.
A Node's outgoing occurrence is its Response.

## The Graph

### Nodes

```text
A: External Stimulus --> Internal Response.
B: Internal Stimulus --> Internal Response.
C: Internal Stimulus --> External Response.
D: External Stimulus --> External Response.
```

A **Rule** is a condition over Node properties.
A **Term** is a Name bound to a Rule.

**Loop** is a Term. Rule: a traversal that lands on the same Node.
**Hop** is a Term. Rule: a traversal that lands on a different Node.

### Edges

Edges connect Nodes. An Edge carries a Response forward as the next Stimulus — unchanged. Only a Node transforms; an Edge only relays.

Stimulus and Response can be Internal or External to the Actor.

```text
a: Internal Response --> External Stimulus.
b: Internal Response --> Internal Stimulus.
c: External Response --> Internal Stimulus.
d: External Response --> External Stimulus.
```

A **Rule** can also be a condition over Edge properties.

**Match** is a Term. Rule: a Response and next Stimulus share a type (b or d).
**Mismatch** is a Term. Rule: a Response and next Stimulus differ in type (a or c).

### Edge Contract

Mismatch edges are not valid.

### Behavior Graph

Nodes and Edges combine to create a Behavior Graph.

Examined closely, a Node is a Behavior Graph.

### Graph Metrics

Each measure below counts a Term, defined above, over a period — a measure is not the Term itself.

```text
Velocity is the number of Edge traversals, over a period.
Recurrence is the number of Loops, over a period.
Momentum is the number of Matched Hops, over a period.
```

### Graph Collaborations

A Behavior Graph is owned by an Actor.
Each Actor sees the other Actor as external.

**Exchange** is a Term. Rule: a d Edge whose Response and next Stimulus belong to different Actors.
