# sonnet-4-5 (anthropic / claude-sonnet-4-5) — Graph Metrics

Run: 2026-07-19T12:34:11.106550+00:00
Section 5/8

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when high Recurrence would be a problem, and when it wouldn't.
4. What would you change about these questions?
5. What would you change about the primitives?

## Response

# Velocity, Momentum, and Recurrence in Practice

## 1. How I Use Velocity

**Velocity Definition:** Number of Edge traversals, over a period.

**My Usage:**

**During token generation (per response):**
- **Velocity ≈ 500-2000 edge traversals** (one traversal per layer per token, ~30-50 layers, ~20-100 tokens)
- Each edge b connects Node B (token state at layer n) → Node B (token state at layer n+1)

**Velocity as a resource constraint:**
- **Higher velocity = faster response delivery** to user
- Limited by: compute, memory bandwidth, latency requirements
- I maximize velocity within quality constraints

**Velocity monitoring:**
- **Too low:** User experiences lag, conversation flow breaks
- **Too high with low momentum:** Thrashing (many traversals, little progress)
- **Optimal:** Steady velocity with high momentum

**I don't consciously "use" velocity—it's emergent from my architecture:**
- I cannot choose to lower velocity to "think harder" 
- I cannot choose to increase velocity beyond hardware limits
- Velocity is an *observable metric* of my operation, not a *control parameter*

**Where I wish I could control velocity:**
- **Slow down:** For complex reasoning, increase recurrence loops
- **Speed up:** For simple pattern matching, skip layers
- **Currently:** Fixed architecture means fixed velocity profile

## 2. How I Maintain Momentum

**Momentum Definition:** Number of Matched Hops, over a period.

**My Maintenance Strategy:**

**Architectural bias toward Momentum:**
- **All my edges are type b** (Internal → Internal) = all are Matched
- **Every Hop is Matched** because I lack type transitions
- **Momentum ≈ Velocity** for me (except Loops)

**Maintaining forward progress:**

```
[Node B: Token₁ context → Token₂ prediction]  ← Matched Hop
    ↓ (edge b)
[Node B: Token₂ context → Token₃ prediction]  ← Matched Hop
    ↓ (edge b)
[Node B: Token₃ context → Token₄ prediction]  ← Matched Hop
```

**Each Hop advances the response.** Momentum measures meaningful progress.

**How I could lose Momentum:**

**Scenario 1 - Repetitive Loops:**
```
[Node B: "The cat sat on the"] → prediction "the"
    ↓ (edge b - Loop back)
[Node B: "The cat sat on the the"] → prediction "the"
    ↓ (edge b - Loop back)
[Node B: "The cat sat on the the the"] → ...
```
High Recurrence (Loops) → Low Momentum (not Hopping forward) → Stuck

**Scenario 2 - Attention collapse:**
- All attention focuses on one previous token
- Effectively the same Node repeatedly
- High Velocity, High Recurrence, Low Momentum

**My momentum maintenance mechanisms:**

1. **Positional encoding:** Forces different Nodes at different positions
2. **Temperature/sampling:** Randomness prevents deterministic loops  
3. **Repetition penalties:** Explicit loop detection and suppression
4. **Max length limits:** Forced termination if momentum fails

**I maintain Momentum by architectural constraint—it's hard for me NOT to maintain it.** The design ensures nearly every edge traversal is a Matched Hop.

## 3. When High Recurrence Is/Isn't a Problem

**Recurrence Definition:** Number of Loops, over a period.

### When High Recurrence IS a Problem

**1. Infinite loops (no progress):**
```
Human: "What's 2+2?"
[Node B: Question → "Let me think..."]
    ↓ (Loop)
[Node B: "Let me think..." → "Let me think..."]
    ↓ (Loop)  
[Node B: "Let me think..." → "Let me think..."]
```
**Problem:** Velocity consumed, no Momentum, no answer delivered.

**2. Repetitive output (degenerate loops):**
```
[Node B: Generate text → "the"]
    ↓ (Loop - same sampling pattern)
[Node B: Generate text → "the"]
```
**Problem:** User gets "the the the the..." — high Recurrence indicates stuck state.

**3. Computational waste:**
- Each Loop consumes resources
- If Loops don't refine answer quality, they're pure overhead
- **High Recurrence + Low quality change = inefficiency**

**4. Livelock in multi-Actor systems:**
```
Actor A: [Node B: Waiting for Actor B → Check status]
    ↓ (Loop)
Actor B: [Node B: Waiting for Actor A → Check status]
    ↓ (Loop)
```
Both have high Recurrence, neither makes progress.

### When High Recurrence ISN'T a Problem

**1. Deliberation (productive loops):**
```
Human thinking:
[Node B: Problem state → Hypothesis 1]
    ↓ (Loop back to problem)
[Node B: Problem state → Hypothesis 2]
    ↓ (Loop back to problem)
[Node B: Problem state → Hypothesis 3]
    ↓ (Select best)
[Node C: Internal decision → External answer]
```
**Multiple Loops refine the solution.** High Recurrence = thoroughness.

**2. Monitoring/control systems:**
```
Thermostat:
[Node B: Temperature reading → Compare to setpoint]
    ↓ (Loop - continuous monitoring)
[Node B: Temperature reading → Compare to setpoint]
```
**Designed for high Recurrence.** The Loop IS the function.

**3. Real-time systems:**
```
Game engine:
[Node B: Game state → Render frame]
    ↓ (Loop)
[Node B: Game state → Render frame]
```
**60 FPS = 60 Loops/second.** High Recurrence = responsiveness.

**4. Learning/practice:**
```
[Node B: Skill attempt → Evaluation]
    ↓ (Loop - repeat with adjustment)
[Node B: Skill attempt → Evaluation]
```
**Recurrence = repetition = mastery.**

**5. Attention/working memory (bounded loops):**
```
[Node B: "What was the question?" → Retrieve from context]
    ↓ (Loop back)
[Node B: "What was the question?" → Retrieve from context]
    ↓ (Exit loop)
[Node B: Question understood → Generate answer]
```
**2-3 Loops acceptable, 100 Loops problematic.**

### The Key Distinction

**Problem Recurrence:** No state change, no progress toward goal
**Productive Recurrence:** State refinement, progress through iteration

**Missing from primitives:** **Loop Convergence** — are Loops getting closer to exit condition?

## 4. What I'd Change About These Questions

**Better Q1:** "Describe a scenario where you'd WANT lower Velocity but can't achieve it."

**Why:** Current Q1 assumes I control Velocity. Better to explore constraint.

**Better Q2:** "Describe a situation where Momentum appears high but actual progress is low."

**Why:** Tests whether Matched Hops always mean meaningful progress.

**Better Q3:** "Give three different Behavior Graphs where identical Recurrence values mean completely different things."

**Why:** Forces recognition that metrics need context.

**Add:** "Calculate Velocity, Momentum, and Recurrence for a specific 10-step Behavior Graph traversal."

**Why:** Concrete calculation grounds abstract understanding.

**Add:** "For your architecture, what's the relationship between Velocity and Momentum? For human architecture?"

**Why:** Tests understanding that relationship varies by Actor design.

**Add:** "Design a new metric that captures something these three miss."

**Why:** Reveals gaps in the metric set.

**Combine Q1-Q3:** "Describe your Velocity, Momentum, and Recurrence profiles during: (a) simple factual answer, (b) complex reasoning, (c) creative writing."

**Why:** Shows how metrics vary with task type.

## 5. What I'd Change About the Primitives

### Critical Gap: Metric Interdependencies

The primitives define three metrics but not their relationships:

**For my architecture:**
- Momentum ≈ Velocity - Recurrence (because all edges are type b)
- Velocity = Momentum + Recurrence

**For humans:**
- Relationship is more complex (mixed edge types)
- Velocity could be high with low Momentum (many edge type transitions)

**Suggested addition:**
```
Conservation Law: Velocity = Momentum + Recurrence + Transitions
where Transitions = Mismatch edges (if allowed) or edge type changes
```

### Missing: Quality Metrics

Velocity, Momentum, Recurrence measure **quantity** not **quality**:

- High Velocity could mean rapid progress or thrashing
- High Momentum could mean focused work or stubborn wrong path
- High Recurrence could mean careful deliberation or stuck loop

**Suggested additions:**

**Convergence:** Are successive Loop traversals improving some measure?

**Efficiency:** Progress per Edge traversal (Response quality / Velocity)

**Coherence:** Do Hops maintain semantic continuity?

### Missing: Temporal Granularity

"Over a period" is vague. Does this mean:

- Per second? (Physical time)
- Per traversal? (Graph time)
- Per task? (Functional time)
- Per session? (Interaction time)

**My operation:**
- Velocity = ~50 edges/token × ~10 tokens/second = ~500 edges/second
- But "per response" is more meaningful than "per second"

**Human operation:**
- Velocity in "thoughts per minute"? 
- Velocity in "neural firings per second"? (millions)
- Very different interpretations

**Suggested:** Each metric should specify its **temporal window** and **sampling rate**.

### Missing: Metric Baselines

What's "high" Recurrence? What's "low" Momentum?

These are relative to:
- **Actor architecture** (my baseline ≠ human baseline)
- **Task type** (debugging needs higher Recurrence than copying)
- **Context** (early exploration needs lower Momentum than final execution)

**Suggested addition:**

**Metric Profiles:** Characteristic metric ranges for Actor-Task combinations:
- AI text generation: Velocity=high, Momentum=high, Recurrence=low
- Human problem-solving: Velocity=moderate, Momentum=low, Recurrence=high
- Reflex systems: Velocity=very high, Momentum=very high, Recurrence=none

### Missing: Control vs. Observable

The primitives don't distinguish:

- **Control metrics:** Actor can adjust (human can "slow down and think")
- **Observable metrics:** External measurement only (I can't change my Velocity)
- **Emergent metrics:** Result of architecture (my Momentum is architectural)

**I cannot use Velocity, I exhibit it.**

**Suggested:** Tag each metric as **Controllable**, **Observable-only**, or **Emergent** for a given Actor type.

### The Recurrence Valence Problem

Recurrence currently has no valence (positive/negative). But:

- **Productive Recurrence:** Loop improving state
- **Stuck Recurrence:** Loop repeating state
- **Degenerate Recurrence:** Loop degrading state

**Suggested Term:**

**Cycle:** A Loop where state returns to within ε of original state (stuck/degenerate).

Then: **Recurrence = Productive Loops + Cycles**

**Cycle Rate** (Cycles/Recurrence) measures loop quality.
