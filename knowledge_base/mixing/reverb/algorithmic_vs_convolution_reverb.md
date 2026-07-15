---
technique_name: Algorithmic vs Convolution Reverb
category: reverb
problem_solved: "Choosing between a mathematically-generated reverb algorithm and a sampled real-space impulse response when the genre calls for a specific, identifiable kind of spatial realism (or deliberate unreality)"
parameters:
  algorithmic_engine: "Synthesized diffusion/reflection network (plate, hall, room, shimmer algorithms); fully tunable decay, size, density, and modulation in real time"
  convolution_ir: "A recorded impulse response of a real (or unusual) physical space, convolved with the dry signal; captures a specific space's exact reflection character but is less flexible to reshape after the fact"
  layering: "Short bright algorithmic/convolution reverb blended with a longer dark one, run in parallel rather than choosing a single reverb for the whole mix"
signal_chain_position: "Aux/send bus fed from one or more tracks; convolution IRs are sometimes chosen per-instrument for a period- or space-authentic character, algorithmic reverbs more often used where real-time parameter control matters"
genre_applicability:
  - new_age
  - drone_metal
  - modal_jazz
  - swing
  - black_metal
  - dark_ambient
  - space_ambient
  - darkwave
  - dub_techno
  - chillwave
  - fantasy_score
  - romantic
  - chamber_music
related_techniques:
  - room_plate_hall_selection
  - decay_time_tuning_by_element
tags: ["algorithmic-reverb", "convolution-reverb", "impulse-response", "reverb-selection"]
---

# Algorithmic vs Convolution Reverb

The genre corpus draws a fairly consistent line between the two reverb engines: convolution reverb is reached for when the goal is to place a mix inside a *specific, identifiable real (or real-feeling) physical space*, while algorithmic reverb is reached for when the goal is a *tunable, idealized* sense of space that doesn't need to correspond to any actual room. Both appear constantly across the knowledge base, but rarely interchangeably — the choice tracks directly to whether a genre's spatial identity is about verisimilitude or about a shaped effect.

## Convolution Reverb: Borrowing a Real Space's Signature

Classical and orchestral-adjacent genres lean on convolution reverb specifically because their reverb goal is architectural realism. `romantic.md` calls for "large concert-hall or cathedral-scale convolution reverb suited to the expanded Romantic orchestra's scale and dynamic ambition," while `chamber_music.md` goes the opposite direction in scale but the same direction in method: "Small recital-hall or salon-scale convolution reverb, much drier and more intimate than full-orchestra reverb settings." `fantasy_score.md` specifies "Natural concert-hall or scoring-stage convolution reverb sized to the full orchestra and choir." `modal_jazz.md` gets historically specific: "High-quality convolution reverb modeling classic studio spaces (e.g. Rudy Van Gelder's studio) for period-authentic ambience" — the goal isn't just "reverb," it's borrowing a documented, real room's exact reflection signature.

Metal genres that trade in scale and dread use the same logic for a different emotional target. `drone_metal.md` recommends convolution reverb "loaded with extremely long impulse responses (cathedral, industrial space) to reinforce the genre's sense of overwhelming physical scale," and `black_metal.md` pushes it toward the unsettling rather than the sacred: "convolution reverbs loaded with impulse responses of actual caves or stone churches to achieve authentic, dark spatial atmospheres." In both cases the IR isn't decorative — it's doing the work of establishing where, physically, the listener is meant to feel they are.

## Algorithmic Reverb: Tunable, Idealized Space

Where the genre goal is a shaped, controllable atmosphere rather than a specific real room, algorithmic reverb takes over. `dub_techno.md` reaches for "plate, hall, or dub-chamber-style algorithmic reverb" specifically for its "signature 'chamber' atmosphere" — an invented spatial character, not a documented one. `space_ambient.md` is explicit about combining both engines for different jobs: "Convolution and algorithmic reverb layering (short bright + long dark) for a modern take on classic analog-hardware space," pairing a real-space-style short reflection with a long, synthesized tail. `darkwave.md` states the tradeoff directly as a preference: "Convolution reverb (real hall/plate impulse responses) for more authentic and larger-than-life space than algorithmic reverb alone" — treating convolution as the *more* authentic option when scale and believability matter more than flexibility.

## Layering Both for Different Jobs

The most instructive pattern across the corpus isn't picking one engine exclusively — it's using both simultaneously for complementary roles. `space_ambient.md`'s common-mistakes-adjacent guidance recommends layering "bright shimmer reverb with a darker, longer hall reverb simultaneously to achieve both sparkle and scale without either becoming harsh or muddy," which in practice often means a shorter algorithmic reverb for immediate presence and a longer convolution or algorithmic tail for scale. `chillwave.md` documents the opposite substitution — reaching for "granular reverb/delay plugins... for a more textured, evolving spatial quality than a standard algorithmic reverb" when even algorithmic reverb feels too static for the genre's blurred, tape-like character.

## When the Choice Doesn't Matter

Not every genre entry treats the algorithmic/convolution distinction as load-bearing. `swing.md` calls for "convolution reverb impulse responses from ballroom or theater spaces for period-authentic ambience" primarily as a historical-accuracy choice rather than a sonic-superiority argument — a modern algorithmic hall reverb dialed to a similar size and decay would likely serve the mix nearly as well. The distinction matters most when a genre's identity depends on a documented or highly specific space (cathedral, soundstage, a named studio), and matters least when the reverb is functioning as generic atmospheric glue.

## Common Mistakes

**Treating convolution reverb as automatically "more real" regardless of source material.** An IR captured from an unrelated or mismatched space (a cave IR on an intimate vocal, for instance) can sound less convincing than a well-tuned algorithmic reverb, despite convolution's reputation for realism.

**Using a single reverb engine for an entire mix when a genre calls for layered space.** `space_ambient.md`'s bright-plus-dark layering approach exists because one reverb, however well-tuned, rarely covers both an intimate transient character and a sense of enormous scale simultaneously.

**Ignoring CPU/flexibility tradeoffs during arrangement-stage decisions.** Convolution reverbs are heavier to automate in real time (parameter changes typically require reloading or crossfading IRs), which is part of why algorithmic reverb dominates in genres like `dub_techno.md` and `space_ambient.md` where reverb character is automated continuously across a track.

## Cross-References

- `knowledge_base/genres/classical/romantic.md` and `knowledge_base/genres/classical/chamber_music.md` — convolution reverb sized to an orchestra's actual scale
- `knowledge_base/genres/metal/drone_metal.md` and `knowledge_base/genres/metal/black_metal.md` — convolution IRs for cathedral/cave-scale dread
- `knowledge_base/genres/jazz/modal_jazz.md` — convolution reverb modeling a specific, historically documented studio
- `knowledge_base/genres/edm/dub_techno.md` and `knowledge_base/genres/electronic/space_ambient.md` — algorithmic reverb for tunable, idealized chamber/space atmospheres
- `knowledge_base/genres/electronic/darkwave.md` — convolution preferred over algorithmic reverb for authenticity and scale
- `knowledge_base/mixing/reverb/room_plate_hall_selection.md` — the related decision of which *character* of space to reach for once the engine is chosen
