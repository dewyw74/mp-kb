---
technique_name: Tempo-Synced vs Free-Running Delay
category: delay
problem_solved: "A delay locked to a musical subdivision reinforces groove and rhythmic interplay, while a delay left free-running (unsynced) creates organic, evolving drift better suited to textural or ambient material — using the wrong one flattens the effect the genre is going for"
parameters:
  synced_division: "Common musical subdivisions (1/8, dotted 1/8, 1/16, triplet) locked to session tempo, chosen for rhythmic reinforcement or counterpoint against the existing groove"
  free_running_time: "A fixed millisecond time (often long, 500ms-2s+) left unsynced to tempo, chosen so the echo drifts against the beat rather than reinforcing it"
  feedback_and_evolution: "Free-running delays are frequently paired with high feedback for slowly evolving, semi-generative echo trails rather than discrete rhythmic repeats"
signal_chain_position: "Delay send/insert on melodic, percussive, or vocal elements, with sync mode chosen deliberately per genre rather than left at a plugin's default"
genre_applicability:
  - space_ambient
  - nu_skool_breaks
  - trap
  - cybergrind
  - math_rock
  - jazz_fusion
  - ambient
  - progressive_trance
  - psybient
  - berlin_school
related_techniques:
  - delay_throws_and_automation
  - filtered_dub_delay
tags: ["tempo-sync", "free-running-delay", "rhythmic-delay", "ambient-delay"]
---

# Tempo-Synced vs Free-Running Delay

Whether a delay's repeat time locks to the song's tempo or runs independently of it is treated across the genre corpus as a genre-defining choice, not a technical default. Rhythm-forward genres consistently specify tempo-synced delay as a compositional/groove-reinforcing device; ambient and texture-forward genres just as consistently specify free-running or loosely-synced delay so the echo drifts against the beat rather than locking to it.

## Tempo-Synced Delay as a Rhythmic Compositional Device

`math_rock.md` treats synced delay as functionally part of the arrangement rather than a spatial effect: "Delay used rhythmically (often tempo-synced) to reinforce or counterpoint the interlocking guitar parts rather than for ambient wash... functioning as a compositional device (creating additional interlocking rhythmic layers) rather than ambient space." `jazz_fusion.md` documents a nearly identical use on a different instrument: "Rhythmic and ambient delay is a genre staple on guitar and synth leads, sometimes tempo-synced for repeating echo patterns that interact with the groove," recommending "tempo-synced analog-modeled delay on guitar/synth leads for rhythmically locked echo that reinforces odd-meter grooves." `cybergrind.md` frames the same synced approach as a genre-distinguishing feature against its parent genre: "Rhythmic, tempo-synced glitch/stutter delay is a genre-signature texture device, distinguishing cybergrind's mix approach from grindcore's largely delay-free production." `nu_skool_breaks.md` and `trap.md` apply synced delay to hooks and ad-libs for width and rhythmic reinforcement rather than compositional counterpoint — `nu_skool_breaks.md`: "Precisely tempo-synced delay on stabs/hooks for rhythmic reinforcement and width," and `trap.md`: "Synced delay on melodic loops and vocal ad-libs, often a defining textural element."

## Free-Running Delay for Organic Drift and Texture

The opposite approach — leaving delay time unsynced to tempo — shows up specifically in genres where the goal is a sense of space evolving independently of the beat, or where no fixed beat exists to sync to. `ambient.md` states the choice explicitly as optional-but-deliberate: "Long, filtered delays (500ms-2s) with high feedback create evolving echo trails; sync loosely or leave free-running for organic drift." `psybient.md` and `progressive_trance.md` both favor loose or non-rhythmic sync specifically to keep delay in a textural rather than groove-reinforcing role — `psybient.md`: "Long, often non-rhythmic delay for texture rather than groove," and `progressive_trance.md`: "Ambient, often non-rhythmic or loosely synced delays layered for atmosphere rather than sharp rhythmic emphasis." `berlin_school.md` documents a related but distinct technique: pairing a slower base sequence against a precisely tempo-synced delay division specifically to generate rhythmic complexity the sequencer alone doesn't produce — "Recreate the slow-sequence-plus-delay technique using a DAW delay plugin set to a precise tempo-synced division against a deliberately slower base sequence" — a case where the delay *is* synced, but deliberately mismatched in subdivision against the underlying pattern to create the illusion of a more complex rhythm.

## Sequenced and Arpeggiated Material: Sync as Perceived Rhythmic Complexity

`space_ambient.md` documents tempo-synced delay used specifically to manufacture rhythmic interest in otherwise sparse, beatless material: "Tempo-synced delay on sequenced/arpeggiated lines creates rhythmic complexity and perceived space without adding literal instrument layers" — the delay isn't reinforcing an existing groove so much as generating the impression of one from a single sequenced part, letting a producer avoid stacking additional real instrument layers to achieve density.

## Common Mistakes

**Syncing a delay by default without considering whether the genre wants rhythmic reinforcement or organic drift.** `math_rock.md` and `ambient.md` sit at opposite ends of this choice for a reason — a synced delay on ambient pad material can feel mechanically rigid, while a free-running delay on interlocking math-rock guitar parts loses the counterpoint effect the genre depends on.

**Assuming free-running delay means "no relationship to tempo at all."** `berlin_school.md`'s slow-sequence-plus-synced-delay technique shows that even precisely tempo-synced delay can be used to generate a sense of drift or complexity when set to an unexpected subdivision relative to the underlying pattern — sync mode and perceived rhythmic looseness aren't strictly the same axis.

**Overlooking synced delay as a texture-generation tool, not just a rhythm-reinforcement one.** `space_ambient.md`'s use of synced delay on sparse sequenced lines to create "perceived space without adding literal instrument layers" is a CPU- and arrangement-efficient technique easy to miss if delay is only thought of as an echo effect.

## Cross-References

- `knowledge_base/genres/rock/math_rock.md` and `knowledge_base/genres/jazz/jazz_fusion.md` — tempo-synced delay as a compositional, groove-reinforcing device
- `knowledge_base/genres/metal/cybergrind.md`, `knowledge_base/genres/edm/nu_skool_breaks.md`, and `knowledge_base/genres/hiphop/trap.md` — synced delay on stabs, hooks, and vocal ad-libs
- `knowledge_base/genres/electronic/ambient.md`, `knowledge_base/genres/edm/psybient.md`, and `knowledge_base/genres/edm/progressive_trance.md` — free-running or loosely-synced delay for organic, non-rhythmic texture
- `knowledge_base/genres/electronic/berlin_school.md` — a synced delay deliberately mismatched against a slower sequence to generate rhythmic complexity
- `knowledge_base/genres/electronic/space_ambient.md` — synced delay generating perceived rhythmic density from sparse sequenced material
- `knowledge_base/mixing/delay/delay_throws_and_automation.md` — how delay send levels get automated on top of whichever sync mode is chosen
