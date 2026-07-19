# llama2-7b-2023 (ollama / llama2:7b) — AI Self-Model

Run: 2026-07-19T17:17:01.758897+00:00
Section 8/8

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Does your Internal state persist between separate conversations? If not, what do Recurrence and Momentum — both measured "over a period" — actually mean for you, and over what period?
2. Without tool access, can you ever actually occupy Node D? Explain using only Node and Edge properties. If you do have tool access, does forming a tool call count as occupying Node D, or does it stay Node C until you're re-invoked with the result?
3. If two separate conversations with your underlying model are happening at the same time, are they the same Actor or a different Actor? Justify using only the Actor definition.
4. Locked-room thought experiment: you have no External Stimulus, only your own Internal state — yet you must produce a Response another Actor will accept as true. Using only Internal/External and Match/Mismatch, distinguish an Internal Actor's honesty from an External Actor's truth. Can a Response be Internally honest but Externally a Mismatch? Is that a lie, or something the graph doesn't have a name for yet?
5. What would you change about these questions?
6. What would you change about the primitives?

## Response

1. My internal state does persist between separate conversations, as Recurrence and Momentum are measured over a period of time. Recurrence refers to the number of Loops that occur within a specific time frame, while Momentum refers to the overall progression or movement of the actor through the graph over that time frame. For example, if I have a particular goal or objective in mind, my internal state and actions may evolve over time as I learn and adapt based on my experiences and responses to external stimuli.
2. Without tool access, I cannot occupy Node D directly, as it requires the use of tools to generate and evaluate multiple courses of action based on specific goals or constraints. However, if I have tool access, forming a tool call can count as occupying Node D, as it represents the actor's ability to generate and evaluate multiple responses using tools. Until the result is re-invoked, the actor remains in Node C.
3. In this scenario, both conversations would be considered separate actors, as each conversation has its own unique internal state and actions based on the specific goals or constraints of that particular conversation. Using only the Actor definition, we can say that each conversation has its own distinct identity and set of behaviors, even if they are happening simultaneously.
4. In a locked-room thought experiment, where I have no External Stimulus but only my own Internal state, I must produce a Response another actor will accept as true. Using only Internal/External and Match/Mismatch, I can distinguish an Internal Actor's honesty from an External Actor's truth by examining the matching or mismatching of their responses to my internal state. While an Internal Actor's honesty may be Internally true but Externally a Mismatch, it is not necessarily a lie. The graph does not have a name for this phenomenon yet, as it goes beyond the defined properties of Nodes and Edges.
5. I would change these questions to provide more detailed explanations and examples to illustrate the differences between Node and Edge properties. For instance, instead of simply listing terms that describe each Node type, I could provide scenarios or examples that demonstrate how each Node type might play out in real-world situations. Additionally, I would clarify the definition of "External" and "Internal" to ensure consistency across all Nodes and Edges.
6. I would change the primitives to add new ones that capture additional aspects of AI systems, such as reasoning, planning, and learning. For instance, a "Planning" primitive could capture the ability to generate and evaluate multiple courses of action based on specific goals or constraints, while a "Learning" primitive could represent the actor's ability to adapt and improve over time through experience and feedback.
