---
title: "Velocity Editing And Dynamics"
technique_name: Velocity Editing and Dynamics
category: programming
problem_solved: "Deciding how much velocity variation a part should carry — from near-uniform hits to wide expressive swings — and which elements in a track are the intended carriers of dynamic contrast"
genre_applicability:
  - trap
  - speedcore
  - swing
  - jazz_fusion
  - hard_bop
  - east_coast_hip_hop
  - jungle
  - progressive_trance
related_techniques:
  - drum_pattern_programming
  - bass_and_808_pattern_programming
  - humanization_and_groove_timing
tags: ["velocity", "dynamics", "midi-programming", "expression"]
---

# Velocity Editing and Dynamics

Velocity data is one of the most genre-differentiating MIDI parameters in this knowledge base, precisely because "add some velocity variation" is not a universal rule — genre files document everything from deliberately near-zero velocity variation to wide, structurally important dynamic swings, and each choice is tied to a specific functional reason.

## Deliberately Uniform Velocity

`speedcore.md` treats consistent maximal velocity as central to the genre's identity, not an oversight: "Kick velocity is generally maximal and consistent — the aggression comes from distortion processing, not velocity dynamics." The distinction matters: the genre still wants aggression, but it's engineered through distortion and processing rather than through velocity contrast, so the MIDI data itself stays flat. `lo_fi_hip_hop.md` and `g_funk.md` document a gentler version of the same idea for opposite reasons — `lo_fi_hip_hop.md`: "Soft, consistent, low-key dynamic range throughout — the genre avoids dramatic dynamic contrast by design," and `g_funk.md`: "Consistent, groove-supporting dynamics rather than dramatic contrast; the genre's power comes from sustained pocket and feel."

## Velocity as the Primary Groove Carrier

Trap inverts the above — velocity variation is exactly where the genre's groove lives, particularly on the hi-hat. `trap.md`: "Hi-hats carry extensive, deliberate velocity variation for the genre's characteristic rolling, human-adjacent groove even at high subdivision speed." This is a specific and important combination: the hi-hat's *timing* stays tightly quantized (per the genre's humanization notes) while its *velocity* carries all the groove information — a case where feel is encoded entirely in one MIDI dimension rather than spread across timing and velocity together.

## Structural Velocity Jumps

`swing.md` documents velocity change used as an arrangement device rather than a continuous texture: "Keep section-writing velocity relatively uniform within a chorus to mimic disciplined ensemble dynamics, with a clear velocity jump at the shout chorus; solo lines should have wider, more expressive velocity variation." The uniform-velocity sections aren't a limitation — they're what makes the shout chorus's velocity jump register as a structural, arranged event rather than incidental variation. `jazz_fusion.md` documents a related but continuous approach: "High dynamic range with hard-hitting accented hits on unison figures; solo synth/guitar lines benefit from expressive velocity and mod-wheel automation to mimic bends and swells" — here velocity and CC automation work together to simulate the physical gesture of a bent note.

## Velocity Inherited From Source Material

`east_coast_hip_hop.md` and `boom_bap.md` both source their velocity data from sampled drum breaks rather than programming it by hand: "Drum hits carry natural, sample-derived dynamic variation rather than uniform, quantized velocity." `jungle.md` extends this to re-triggered chops specifically: "Break-chop velocity is kept close to the source sample's natural dynamics to preserve the 'played' feel of the original breaks, with deliberate accents added on re-triggered ghost notes for extra swing." The technique here is restraint — resisting the urge to flatten or re-quantize velocity data that already carries a real drummer's dynamics.

## Accent-Driven Velocity

`hard_bop.md` ties velocity specifically to backbeat emphasis: "Strong, consistent velocity on backbeat-emphasizing drum hits; horn solo velocity should reflect bluesy, vocal-like dynamic swells rather than bebop's rapid whisper-to-shout extremes" — a useful contrast against bebop's more extreme dynamic range, showing that "wide dynamic range" itself has genre-specific sub-flavors (extreme whisper-to-shout vs. warmer, vocal-like swells). `drill.md` and `phonk.md` both call for deliberate velocity accents on specific hits (808 slides/rimshots, cowbell/808 respectively) rather than broad variation across the whole pattern.

## Common Mistakes

**Applying uniform "humanize velocity" randomization regardless of genre.** Speedcore and lo-fi hip-hop specifically want flat, consistent velocity; randomizing it by default undoes a deliberate genre choice rather than fixing a mechanical-sounding part.

**Flattening sample-derived velocity from breakbeats or drum breaks.** `east_coast_hip_hop.md`, `boom_bap.md`, and `jungle.md` all depend on preserving the original performance's dynamics — re-quantizing velocity to a uniform value removes the "played" feel the sample was chosen for.

**Spreading velocity variation evenly instead of concentrating it structurally.** `swing.md`'s shout-chorus jump only works as a structural event because the surrounding sections stay comparatively uniform — even, continuous variation throughout would blur the arrangement's dynamic arc.

## Cross-References

- `knowledge_base/genres/edm/speedcore.md`, `knowledge_base/genres/hiphop/lo_fi_hip_hop.md`, `knowledge_base/genres/hiphop/g_funk.md` — deliberately uniform, low-variation velocity
- `knowledge_base/genres/hiphop/trap.md` — velocity as the primary carrier of hi-hat groove
- `knowledge_base/genres/jazz/swing.md`, `knowledge_base/genres/jazz/jazz_fusion.md` — structural velocity jumps and expressive automation
- `knowledge_base/genres/hiphop/east_coast_hip_hop.md`, `knowledge_base/genres/hiphop/boom_bap.md`, `knowledge_base/genres/edm/jungle.md` — velocity inherited from sampled source material
- `knowledge_base/genres/jazz/hard_bop.md` — accent-driven backbeat velocity vs. bebop's wider dynamic extremes
- `knowledge_base/midi/patterns/drum_pattern_programming.md` — how velocity interacts with ghost notes and ensemble writing
