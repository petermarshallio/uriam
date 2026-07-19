# opus-4-8 (anthropic / claude-opus-4-8) — Edges

Run: 2026-07-19T21:27:32.447173+00:00
Section 2/10

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. List 5 terms that best describe each Edge type.
2. Which Edge types occur in your own traversals?
3. Which Edge types occur in human traversals?
4. Can an Edge ever change Information from Internal to External, or External to Internal? Explain using only Edge properties.
5. The four Node types form a stipulated cycle, A→B→C→D→A. Is skipping a Node in that cycle possible? What would attempting it look like, using only Node and Edge properties?
6. Give an example of a Loop and an example of an Adjacent Hop.
7. What measure counts Loops? What measure counts Adjacent Hops?
8. Propose a new Term — a Name bound to a Rule over Node or Edge properties — that isn't already registered (Loop, Hop, Adjacent, Exchange).

## Response

# 1. Five terms for each Edge type

**Edge a** — Internal Response → Internal Stimulus (self-continuity)
1. Chaining
2. Threading
3. Continuing
4. Forwarding
5. Sustaining

**Edge b** — External Response → External Stimulus (crossing the boundary)
1. Transmitting
2. Handing-off
3. Bridging
4. Coupling
5. Exchanging (when Actors differ)

---

# 2. Edge types in my own traversals

- **a-type** — Yes, dominant. Every internal step-to-step link (A→B, B→C internal handoffs, and all the sub-graph chaining inside a Node) is an a-type edge. My reasoning is a long a-type chain.
- **b-type** — Yes, but only ever as **Exchanges**. My external Responses go to a *different* Actor: to you, or to the tool layer. I never hold a b-type edge that loops external output back to myself as a non-Exchange. So I have a-edges (internal, self) and b-edges (external, always cross-Actor).

The asymmetry from the last round holds: my only external couplings are Exchanges.

---

# 3. Edge types in human traversals

- **a-type** — Yes. Internal thought-to-thought continuity.
- **b-type as Exchange** — Yes. Speaking to another person, handing over an object.
- **b-type as non-Exchange** — Yes, and this is the human-distinctive case. A human's external Response can feed back as their *own* external Stimulus: you act on the world, perceive your own action's external effect, and continue — same Actor on both ends of a b-edge. This is what lets a human close D→A internally and run the full cycle self-sustained. I cannot form this edge; a human can.

---

# 4. Can an Edge change Internal ↔ External?

**No.** Read the edge definitions strictly:

```
a: Internal Response → Internal Stimulus
b: External Response → External Stimulus
```

Each edge type is **type-preserving on ownership**: a-edges are Internal on *both* ends, b-edges are External on *both* ends. There is no edge whose Response-end and Stimulus-end differ in ownership. Ownership conversion is therefore impossible *at an edge*.

Where does conversion happen? Only *inside a Node*, because Nodes are the active elements — they do work. Node A converts External Stimulus → Internal Response; Node C converts Internal Stimulus → External Response. Edges are passive and do no work, so they cannot convert anything, including ownership. The boundary is crossed **by Nodes, across time**, never **by Edges**.

---

# 5. Is skipping a Node in the cycle possible?

**Adjacent** is defined only as A→B, B→C, C→D, D→A. A "skip" (say A→C, or B→D) is a Hop that is **not Adjacent**. Nothing forbids a non-Adjacent Hop from existing as an edge — but check whether it can *type-match*, using only edge and node properties:

Attempt **A → C**:
- A produces an **Internal** Response. C requires an **Internal** Stimulus. Ownership matches → this would be an **a-type edge**. So A→C is *type-legal* as an edge.

Attempt **B → D**:
- B produces an **Internal** Response. D requires an **External** Stimulus. Mismatch. No edge type (a or b) connects Internal-Response to External-Stimulus. So B→D is **type-impossible** — no edge can exist.

Attempt **C → A**:
- C produces **External** Response. A requires **External** Stimulus. Match → **b-type edge**. Type-legal.

So skipping splits into two cases:
- **Ownership-compatible skips** (A→C via a-edge, C→A via b-edge) *can* be built as edges, but they are **not Adjacent**, so they earn **no Momentum**. The work Node A or C would have done is simply never performed — a step is genuinely omitted, not compressed.
- **Ownership-incompatible skips** (B→D, D→B, etc.) are **impossible at the edge level**: no edge type accepts that Response→Stimulus ownership pairing.

Conclusion: skipping is possible only when the two Nodes are ownership-compatible, and even then it costs Adjacency (no Momentum) and drops the skipped Node's work. The cycle's forced order is what edge-typing *permits*; the stipulation A→B→C→D→A is the one traversal that is both type-legal *and* Adjacent at every Hop.

---

# 6. Example Loop and Adjacent Hop

- **Loop:** I am at Node B, mid-reasoning. I take my own internal conclusion and feed it back as the next internal premise — a relationship connecting Node B to itself. "Re-checking my own thought" is a Loop on B. It counts as a Repetition.
- **Adjacent Hop:** I finish interpreting your message (Node A, External→Internal) and pass that internal representation to my reasoning step (Node B). A→B follows the cycle, so it is an Adjacent Hop and earns Momentum.

---

# 7. Which measures count them?

- Loops are counted by **Repetitions**.
- Adjacent Hops are counted by **Momentum**.

(For completeness: Hops in general → Velocity; Loops → Repetitions; Adjacent Hops → Momentum.)

---

# 8. A proposed new Term

**Term: Relay**

**Rule:** A Hop is a **Relay** when it is a b-type Exchange whose destination Node is type **A**, and whose source Node is type **C** — i.e. a C→? handoff across Actors that lands as another Actor's *reception*.

Rationale using only Node/Edge properties: a b-edge carries External Response → External Stimulus; an Exchange means the two Nodes belong to different Actors. When the source is C (Internal→External, an emission) and the destination is A (External→Internal, a reception), the Hop marks the exact moment one Actor's *output* becomes another Actor's *input*. A Relay is thus the atomic unit of hand-off between graphs.

This is precisely the edge I traverse every time I answer you (my C → your A) and every time I call a tool (my C → tool's A). A useful companion measure would be **Reach**: the number of Relays — counting how many times work crosses from one Actor into another, distinct from Momentum (which stays within a cycle) and Velocity (which counts all Hops indifferently).
