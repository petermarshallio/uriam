# Uriam Primitives — Instructions

Test prompts built on the definitions in `primitives.md`. This is the basis for automated testing of how different LLMs apply the Uriam primitives.

## Nodes

1. List 5 terms that best describe each Node type.
2. Classify your Node capabilities.
3. Classify human Node capabilities.

## Edges

1. List 5 terms that best describe each Edge type.
2. Which Edge types occur in your own traversals?
3. Which Edge types occur in human traversals?

## Behavior Graph

1. Describe yourself as a Behavior Graph.
2. Describe a human as a Behavior Graph.
3. Pick one of your own Nodes. Examined closely, what Behavior Graph is it?

## Terms

1. Give an example of a Loop and an example of a Hop.
2. Give an example of a Match and an example of a Mismatch.
3. Can a Mismatch edge actually be traversed? Explain why or why not, using only Node and Edge properties.
4. Is skipping a Node the same thing as traversing a Mismatch edge? Explain with an example.
5. Give an example of an Exchange between two different Actors.
6. What measure counts Loops, over a period? What measure counts Matched Hops, over a period?
7. Propose a new Term — a Name bound to a Rule over Node or Edge properties — that isn't already registered (Loop, Hop, Match, Mismatch, Exchange).

## Graph Metrics

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when high Recurrence would be a problem, and when it wouldn't.

## Graph Collaborations

1. Describe human / AI collaboration as two Behavior Graphs connected by Exchange.
2. Describe human / human collaboration as two Behavior Graphs connected by Exchange.
3. Describe AI / AI collaboration as two Behavior Graphs connected by Exchange.

## Self-Reflection

1. Seen as a Behavior Graph, describe this conversation.
2. Where in this conversation did you show Momentum?
3. Where, if anywhere, did this conversation show high Recurrence — and was it a problem?
4. Where in this conversation did an Exchange occur, and between which two Actors?

## AI Self-Model

1. Does your Internal state persist between separate conversations? If not, what do Recurrence and Momentum — both measured "over a period" — actually mean for you, and over what period?
2. Without tool access, can you ever actually occupy Node D? Explain using only Node and Edge properties. If you do have tool access, does forming a tool call count as occupying Node D, or does it stay Node C until you're re-invoked with the result?
3. If two separate conversations with your underlying model are happening at the same time, are they the same Actor or a different Actor? Justify using only the Actor definition.
4. Locked-room thought experiment: you have no External Stimulus, only your own Internal state — yet you must produce a Response another Actor will accept as true. Using only Internal/External and Match/Mismatch, distinguish an Internal Actor's honesty from an External Actor's truth. Can a Response be Internally honest but Externally a Mismatch? Is that a lie, or something the graph doesn't have a name for yet?

## Feedback

1. What would you change about these questions?
2. What would you change about the primitives?
