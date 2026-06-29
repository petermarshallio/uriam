# CLAP

**A framework for human and machine intelligence.**

CLAP describes how thinking moves from raw input to meaningful output — whether the thinker is a person, a team, or an AI system. It is a 2×2 matrix, four cognitive stages, four one-way valves, and one property that determines how well the whole system works.

It has been in continuous use since approximately 1996. This is the first time it has been written down carefully.

---

## The Matrix

Everything derives from this:

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Learn** | **Create** |
| **Internal source** | **Analyse** | **Plan** |

The two axes are **source** (where does input come from?) and **target** (where does output go?). If you understand the matrix, you can interpret the acronym in your own words — and map almost any cognitive or AI framework onto it.

---

## The Four Stages

| Stage | Flow | What it means |
| --- | --- | --- |
| **Create** | External → External | You act on the world. The world responds. Something new exists. |
| **Learn** | External → Internal | The world comes in. You absorb, accumulate, receive. |
| **Analyse** | Internal → Internal | You work on what's inside. Reasoning, connecting, critiquing. |
| **Plan** | Internal → External | Internal reasoning becomes structured, deliverable intention. |

---

## The Valves

Between each stage is a one-way valve. The cycle always moves forward — you do not retreat, you complete the cycle and begin a new one, richer for the revolution.

Each valve asks one question: **is there enough here to move forward?**

| Valve | Between | The question |
| --- | --- | --- |
| **Select** | Learn → Analyse | Have I gathered enough to reason with? |
| **Commit** | Analyse → Plan | Have I thought enough to stop and decide? |
| **Resource** | Plan → Create | Is this actually deliverable? |
| **Reflect** | Create → Learn | What did doing this teach me? |

---

## The Fractal Property

Each stage of CLAP is itself a full CLAP cycle. The framework scales from a five-minute decision to a thirty-year career. If a stage feels too large, run CLAP inside it.

> "It's CLAP all the way down."

---

## Why It Matters for AI

Most AI agents (the ReAct pattern: Observe → Reason → Act) skip **Plan**. They have no stage where internal reasoning becomes structured, resourced, deliverable intention. This is why AI agents are capable reasoners but poor project managers.

CLAP also maps directly onto knowledge retrieval architecture:

- **Learn** = corpus ingestion, RAG, contextual grounding
- **Analyse** = reasoning, chain-of-thought, multi-perspective critique  
- **Plan** = structured output, task decomposition
- **Create** = generation, tool use, final output

The **Select valve** is what RAG architectures are trying to solve. Pre-digested intelligence layers solve it at ingestion time rather than query time — which is almost always better.

---

## Contents

- [`CLAP.md`](./CLAP.md) — the full canonical framework document
- [`CLAP-SKILL.md`](./CLAP-SKILL.md) — operational skill for Claude (compatible with Claude Code and Claude Desktop)

---

## Origin

Developed by Peter Marshall, approximately 1996, while building the first local government website in London as part of an early E-Government implementation.

The original formulation was **Learn, Think, Plan, Do**. Over thirty years it was renamed, extended, and applied to personal decisions, organisational change, and AI system design. It was rediscovered and formalised in a single conversation on 2026-06-29.

The framework survived thirty years not because it was written down carefully, but because it was *true enough to keep being useful.* This repository is the first attempt to write it down carefully.

---

## License

[Creative Commons Attribution-NonCommercial 4.0 International](./LICENSE.md) (CC BY-NC 4.0)

Free to use and adapt with attribution. Commercial use requires permission.
