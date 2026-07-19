# llama2-7b-2023 (ollama / llama2:7b) — Terms

Run: 2026-07-19T16:33:13.777464+00:00
Section 4/8

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Give an example of a Loop and an example of a Hop.
2. Give an example of a Match and an example of a Mismatch.
3. Can a Mismatch edge actually be traversed? Explain why or why not, using only Node and Edge properties.
4. Is skipping a Node the same thing as traversing a Mismatch edge? Explain with an example.
5. Give an example of an Exchange between two different Actors.
6. What measure counts Loops, over a period? What measure counts Matched Hops, over a period?
7. Propose a new Term — a Name bound to a Rule over Node or Edge properties — that isn't already registered (Loop, Hop, Match, Mismatch, Exchange).
8. What would you change about these questions?
9. What would you change about the primitives?

## Response

1. Sure! Here are some examples:
	* Loop: An actor takes a particular action repeatedly in response to the same stimulus. (e.g., Actor always buys coffee when they see a Starbucks logo)
	* Hop: An actor jumps from one node to another without traversing the intervening edges. (e.g., Actor skips over a certain edge when navigating a graph)
2. Sure! Here are some examples:
	* Match: A response that is identical to the next stimulus. (e.g., Actor always responds with "yes" when asked if they want coffee)
	* Mismatch: A response that is different from the next stimulus. (e.g., Actor always responds with "no" when asked if they want tea, even though the next stimulus is "coffee")
3. No, a Mismatch edge cannot actually be traversed because it violates the rule that the Response must be different from the next Stimulus. However, it is possible for an actor to navigate a graph in a way that skips over a Mismatch edge without actually traversing it. For example, an actor might navigate a graph by following edges that are not Mismatch edges, and then take a different action based on the current state of the environment rather than the next stimulus.
4. No, skipping a Node is not the same thing as traversing a Mismatch edge. Skipping a Node means avoiding it altogether, while traversing a Mismatch edge means following an edge that doesn't match the current state of the environment.
5. Here's an example of an Exchange between two different Actors:
	* Actor 1: "Hey, can you lend me your car for the weekend?" (stimulus)
	* Actor 2: "Sure, but only if you promise to fill it up with gas before you return it." (response)
6. The measure that counts Loops over a period is called "Cycles". The measure that counts Matched Hops over a period is called "Conformity".
7. Proposed Term: "Synchronization" - the actor's ability to coordinate their actions with those of other actors in the graph, based on shared rules or goals.
8. I would change these questions to provide more detailed explanations and examples to illustrate the differences between Node and Edge properties. For instance, instead of simply listing terms that describe each Node type, I could provide scenarios or examples that demonstrate how each Node type might play out in real-world situations. Additionally, I would clarify the definition of "External" and "Internal" to ensure consistency across all Nodes and Edges.
9. Here are some changes I would consider making to the primitives:
	* Add a new primitive called "Planning" that captures the ability to generate and evaluate multiple courses of action based on specific goals or constraints.
	* Modify the Edge definitions to better reflect how edges can carry responses forward as next stimuli, while also relaying unchanged.
	* Provide more examples or use cases for each Node type to illustrate their potential applications.
	* Clarify the definition of "External" and "Internal" to ensure consistency across all Nodes and Edges.
