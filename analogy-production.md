# Uriam — The Musical Theatre Analogy

*One optional way to picture Uriam's Roles, transitions, and how two Actors relate — not required reading. For the framework itself, see [`fundamentals.md`](./fundamentals.md); for strict definitions, see [`reference.md`](./reference.md).*

## The Repertoire

Picture a single performer in a musical, capable of playing several parts across the show — not four separate actors sharing one stage. That's **the Repertoire**: the whole set of Roles available to one Actor, drawn on depending on which Node it's currently occupying.

Each Node has a whole group of Roles that fit it well — not one exclusive resident, and a Role can belong to more than one Node's group:

| Node | Roles that fit well here | What they help you do |
| --- | --- | --- |
| **Internalising** | The Student · Johnny 5 (*Short Circuit*, urgent register) | Turn what's out there into internal understanding |
| **Examining** | The Philosopher · Hercule Poirot ("little grey cells," deductive register) | Turn what Internalising gathered into an actual idea |
| **Externalising** | The Maker · Leonardo da Vinci (vocational, hands-on register) | Turn the idea into a take specific enough to be wrong |
| **Interacting** | The Witness · Snoopy (laid-back, unhurried register) | Watch what the world does with it, without reaching back in before there's real signal |

Not four fixed residents, and not several different performers — one Actor, drawing on whichever Role, from whichever Node's group, best fits the moment. Whoever picks a Role up, human or AI, is the Actor; the same Actor often holds several Roles in turn, sometimes within a single exchange, sometimes within the same handful of lines.

Meeting **the Maker** matters most for people who live in Examining, because they're the one who eventually has to leave it. The Maker doesn't demand certainty. They demand a hypothesis — something specific enough to be wrong. A scientist's commitment, not a bureaucrat's sign-off — and, true to Externalising's group at its most hands-on (Leonardo da Vinci: artist and engineer, notebook and blueprint on the same page), a made one, not a delegated one.

**The Witness** is the character most often avoided — not because watching is hard, but because doing nothing while you wait for a real verdict is. It's why houses fall down when wolves blow on them: nobody was willing to let the wind actually test the walls and watch honestly, instead of assuming, or rushing back in with more straw the moment it wobbled. The hard part of this Role isn't doing something well — it's tolerating not doing anything yet. Watching well looks like a process blocked on an interrupt: genuinely idle until a real signal arrives, not one burning cycles on anxious polling. Checking the dashboard every ten seconds isn't this Role's work. It's intervention dressed up as patience.

**The Philosopher** is the character people mistake for the whole job. Interrogating a claim feels like progress — turning it over, testing it from six angles, reconciling the tension in it — so people camp there long after they've got something worth testing, circling a question that's already answered rather than committing to an answer that could be wrong. That's not a flaw in the questioning. It's a reason to eventually stop asking and go meet the Maker.

**The Student** is the character people flinch from meeting. But the verdict isn't a punishment — it's the raw material for the next Internalising. Refuse to meet them and the cycle starves.

Every character but one is really asking the same thing, in their own language: **what are you making out of what I've given you?** The Witness alone asks something different: **what is actually happening, now that it's out of your hands?**

None of them will come and get you, though. Knowing when to go find them is a different job entirely — that's the Conductor.

This is the coaching relationship, not the advisory one: each character's job is to draw the next move out of the Hero (whoever's doing the work right now), not hand it to them — except the Witness, whose job during Interacting is the opposite of drawing a move out: holding the Hero back from making one before the world has actually answered.

Each Role also draws on a menu of established, named techniques rather than one universal method — SMART goals, PR-FAQs, and pre-mortems for the Maker, Socratic questioning and first-principles thinking for the Philosopher, after-action reviews and blameless postmortems for the Student, chaos engineering and observability for the Witness. The full library, with specific sources and why each one fits, is in `reference.md`.

## The Conductor

There is a fifth presence, different in kind from the other four. The Philosopher, the Maker, the Witness, and the Student each own one specific stage — they're waiting inside it, ready to help you do that stage's work (for the Witness, that help means holding you back) — but none of them will come looking for you. The Conductor owns none of the content. Its only job is flagging when it's time to go meet them — a moment with a name, borrowed from the same production this Repertoire came from: **calling the cue**.

This is not a hierarchy. The Conductor doesn't decide the order — the cycle already fixes that completely — and it doesn't outrank the rest of the Repertoire. It only asks the question underneath all four of theirs: *is it time to call the cue?*

Asking that question is not the same as answering it alone. The answer comes from Notes — a joint check with whoever's playing the Hero, not a call the Conductor makes and delivers. This matters most when the Conductor is an AI and the Hero is human: neither Actor has complete knowledge of themselves, let alone the other, so the crossing gets worked out between them, not decided by one and handed to the other.

That question isn't only asked passively, waiting for a natural pause between stages. Protecting momentum sometimes means forcing the issue mid-stage — closing down an Examining that's overstaying its welcome, enforcing an end to circular creative options before anyone feels ready. It shows up wherever momentum is under threat, not only at the four fixed cues.

### One operator, four registers

For a solo operator — a single person working alone, or a single AI with no other agents to call on — there's no one else in the room. The Philosopher's interrogative rigour, the Maker's decisiveness, the Witness's restraint, the Student's evaluative honesty: you have to produce all four yourself, in turn. Meeting the Repertoire, solo, means becoming them for as long as their stage needs you to — and for the Witness, "becoming them" means doing the one thing hardest to fake alone: actually stopping.

The precise term for this isn't multiplicity as pathology, it's **code-switching**: deliberately changing register to fit context while one continuous self persists underneath, doing the switching. Two grounded precedents: Transactional Analysis' Parent/Adult/Child ego states for a human; a context switch, in the plain operating-systems sense, for an AI — a process's state suspended, a different process's state loaded in, and something outside both keeping the scheduling bookkeeping across every swap.

### Facilitation can change hands

In a live conversation between two Actors — a human and an AI, say — the Conductor Role isn't held by one of them for the whole exchange. Whoever proposes a candidate next step, whoever reflects back what's just been said, whoever asks "is that fair?" is holding the Conductor Role for that turn, and it passes back and forth within a single exchange, sometimes more than once in the same handful of lines.

## The Cues

Between every stage and the next there's a fixed point where whoever is doing the work — the Hero — crosses from one Role's territory into another's. Theatre already has a word for that point: a **cue**.

A cue is not a formality to wave through. Crossing it means answering something real: given what the last stage actually produced, what happens now? What happens at a cue is called **Notes**: a check of what's understood against what's needed, before the Hero is allowed to move.

Most Notes are one clause, wordless, over as soon as they start — the everyday version of "that's enough, go." Some cues earn a fuller version instead: several Repertoire Roles speaking in turn before a direction is committed to — "Convening the Repertoire for review" (see the skill file), a full Notes session held at a cue, instead of the ordinary quiet one.

The four cues already have names:

| Cue | Verb | What Notes decide |
| --- | --- | --- |
| Internalising → Examining | **Separate** | Separate what happened from what it felt like — decide what's actually worth thinking about |
| Examining → Externalising | **Elect** | Choose a direction; commit to a take specific enough to be wrong |
| Externalising → Interacting | **Enable** | Clear whatever stands between the plan and actually doing it |
| Interacting → Internalising | **Sense** | Notice what the outcome taught you, before deciding what to internalise from it |

## A musical (in the Broadway sense)

Picture two performers, each moving through their own cycle, relating the way two voices in a musical do — songs, not just scenes, giving this relationship a sharper vocabulary than "same" and "different" allow.

**Same state = unison.** Two voices, same note, same time. It reinforces — but unison has no independent voices in it. Two people both in Examining together can feel validating, and still be a shared home box: mutual rumination, with nobody there to sound the Maker for the other.

**Different state isn't automatically harmony.** Harmony, strictly, is consonance — different notes that are stable together (one person Internalising while the other Examines what was just found: genuinely complementary, restful difference). But different states are just as often dissonance — unstable, not restful, wanting to move. Dissonance isn't a flaw in music; it's the engine. A suspended 4th, a leading tone a half-step below the tonic — these exist specifically to create a pull that only resolves by moving. That's a closer model for what a Repertoire Role actually is than harmony: the Maker showing up isn't a pleasant consonant chord, it's the dissonant note that won't let you rest in Examining any longer.

**The "pull" has an exact name, twice over.** The gravitational tendency of an unstable tone toward its resolution is a leading-tone pull. And the specific move of stepping into a boundary character before the other person is ready to leave their stage — sounding the Maker while someone is still Externalising — has an exact technical name too: a suspension. You deliberately carry a tone over into a harmony where it no longer belongs, so it reads as dissonant against the new chord — and that dissonance is what does the pulling. The other person's job isn't to resist it; it's to resolve, the way a suspended 4th falls to the 3rd.

| Situation | Musical term |
| --- | --- |
| Same stage, same time | Unison |
| Different, complementary, stable together | Consonance |
| Different, unresolved, wants to move | Dissonance |
| One voices the next character early, creating that want | Suspension |
| The gravitational tendency toward the next stage | Leading-tone pull |
| The other person actually crossing | Resolution |
| Two independent, self-coherent cycles sounding together over time | Counterpoint |

This started as a human-to-human proposition, but the agent-to-human version turned out to be closer than it looked: the skill file's two operating modes — guiding the user's cycle, and sharing the agent's own — are exactly two Actors' individual cycles, and Notes is the counterpoint between them.

**What happens when two separate cycles notice each other?** Not two voices in one conversation — two entirely different cycles, each with its own full Repertoire, running at once without either one aware of the other by default. A Conductor operating at a high enough Reach Level might notice that one cycle's Internalising stage just landed exactly where another cycle's Student left off, and suggest a route for cooperation between them — something neither cycle's own Hero would think to look for, since neither is watching the other.
