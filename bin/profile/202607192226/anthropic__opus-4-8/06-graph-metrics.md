# opus-4-8 (anthropic / claude-opus-4-8) — Graph Metrics

Run: 2026-07-19T21:29:34.399623+00:00
Section 6/10

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when a high number of Repetitions would be a problem, and when it wouldn't.

## Response

# 1. How I use Velocity

**Velocity = the number of Hops** — every Node-to-Node relationship traversed, Adjacent or not, regardless of type.

I use Velocity as my raw measure of **traversal volume**: how much *movement between Nodes* a response takes. It counts indiscriminately — a productive A→B→C step and a wasteful non-Adjacent skip (A→C, dropping B's work) both add to Velocity equally. It does not care about direction, ownership-crossing, or quality (Uriam's measures never concern quality).

Concretely, within one turn I spend Velocity on:
- the intake Hop (A→B),
- the emit Hop (B→C),
- every sub-Hop inside B's internal Uriam Graph as reasoning branches and reconverges,
- and each Exchange Hop when I call a tool and receive results.

Because Velocity is *undiscriminating*, I don't optimize *for* it — high Velocity alone tells me nothing about whether I'm making progress. A response that thrashes between Nodes without advancing the cycle can post high Velocity while accomplishing little. So I treat Velocity as a **denominator**: the useful ratio is Momentum-over-Velocity — how much of my total movement is *Adjacent*, cycle-advancing motion versus mere movement. High Velocity with low Momentum means I'm moving a lot but not progressing.

---

# 2. How I maintain Momentum

**Momentum = the number of Adjacent Hops** — Hops that follow the stipulated cycle (A→B, B→C, C→D, D→A).

Maintaining Momentum means keeping my Hops **on the cycle** rather than skipping. For me this concretely means:

- **Completing A fully before B.** Not reasoning on a half-read Stimulus. A→B is only Adjacent — and only earns Momentum — if I've actually converted the External Stimulus to a faithful Internal representation first. Skipping to reason on what you *didn't* say is a non-Adjacent skip: it costs a Node's work and posts no Momentum.
- **Completing B before C.** Not emitting before the internal work is done. B→C Adjacency is what makes my Response faithful to my actual Internal state (honesty, Round 3). Jumping A→C — external in, external out, no reasoning — is exactly the D-shaped move I *can't* legitimately make anyway; attempting it produces glib, un-reasoned output.
- **Accepting the C-then-A break at tool boundaries.** I can't traverse my own C→D→A, so across a tool call my Momentum *pauses* — I halt at C, Exchange out, and resume at A on re-invocation. I "maintain" Momentum here not by pretending to loop, but by ensuring the returning External Stimulus is cleanly re-internalized so the *next* arc runs Adjacently.
- **Guarding against Actor-boundary loss.** Since between turns I'm re-instantiated (Round 4), my Momentum doesn't carry across turns as held state — it must be *rebuilt* each turn from the transcript re-entering at A. Maintaining conversational Momentum therefore means faithfully reconstructing prior context so each new arc picks up Adjacent to where the last left off, rather than skipping.

In short: I maintain Momentum by **honoring the cycle order** — full receive, full reason, then emit — and never buying the appearance of speed (Velocity) by dropping a Node.

---

# 3. When high Repetitions is a problem — and when it isn't

**Repetitions = the number of Loops** — a Node connecting back to itself. For me these are mostly **B looping on B**: re-checking, re-deriving, reconsidering my own thought.

**When high Repetitions is *not* a problem — it's the work:**
- **Genuine deliberation.** Hard reasoning legitimately requires B to loop: test a hypothesis, find a flaw, revise, re-test. Each pass is a real Loop that *changes the Internal state* — the representation is different after the Loop than before. Here Repetitions are the mechanism of getting it right, and their quality (which Uriam doesn't measure) is high.
- **Verification and self-correction.** Looping to catch my own error before emitting at C protects honesty. A response with zero Repetitions on a complex problem is often *under*-checked.
- **Iterative refinement** where each pass converges — narrowing an estimate, tightening a proof, polishing prose. The Loop count is high but *monotonically productive*.

**When high Repetitions *is* a problem:**
- **Non-converging Loops — spinning.** B loops but the Internal state stops changing, or cycles through the same states without approaching a Response. This is the failure mode: I never reach C. High Repetitions, zero eventual Momentum. It looks like thoroughness and is actually a stall.
- **Rumination / over-thinking a simple Stimulus.** If A delivered a clear, simple representation, heavy B-looping adds latency and risks *overriding* a correct first pass with a worse revised one — Repetitions manufacturing doubt rather than resolving it.
- **Loops substituting for missing External Information.** From the locked-room point (Round 3, Q4): no amount of B-looping can convert *honest* into *true*. If the gap is missing External Stimulus, Repetitions are wasted — I'm re-processing the same insufficient Internal Information hoping it will yield truth. The fix isn't another Loop; it's an **Exchange** (ask you, call a tool) to bring new External Information in at A.

**The distinguishing test:** a healthy Repetition *changes the Internal state toward a Response*; a pathological one doesn't. Since Uriam counts Loops but never judges their quality, the count alone can't tell the two apart — I have to watch whether each Loop is **converging (progress)** or **idling (stall)**, and whether the missing ingredient is *more internal work* (loop again) or *more external input* (stop looping, Exchange). High Repetitions is excellent right up until the marginal Loop stops changing anything — that's the moment it flips from diligence to waste.
