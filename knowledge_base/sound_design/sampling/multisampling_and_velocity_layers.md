---
title: "Multisampling and Velocity Layers"
technique: "Building a playable instrument from multiple recorded samples across pitch, velocity, and articulation"
tags:
  - "multisampling"
  - "velocity-layers"
  - "articulation"
  - "sampling"
  - "orchestral-mockup"
  - "true-legato"
---

# Multisampling and Velocity Layers

`knowledge_base/sound_design/sampling/one_shot_layering_and_round_robin_variation.md` covers round-robin sampling — cycling through several recorded takes of the *same* note/hit to avoid mechanical repetition. This entry covers a different sample-library-construction dimension: multisampling, where an instrument is built from many recordings spanning *different* pitches, *different* velocities (playing dynamics), and *different* articulations (playing techniques), so a single instrument responds convincingly across its full expressive range rather than just avoiding repetition on one note. Genre files consulted for grounding: `knowledge_base/genres/classical/romantic_drama_score.md` (cross-referenced as `knowledge_base/genres/cinematic/romantic_drama_score.md`), `knowledge_base/genres/classical/neoromanticism.md`, `modernism.md`, `renaissance.md`, `chamber_music.md`, `knowledge_base/genres/jazz/bossa_nova.md`, `swing.md`, `knowledge_base/genres/edm/tropical_house.md`, `knowledge_base/genres/cinematic/trailer_music.md`.

## Velocity Layers for Dynamic Realism

A velocity-layered instrument uses different recordings for soft, medium, and hard-played notes (rather than just scaling the volume of one recording up or down), because a real instrument's timbre — not just its loudness — changes with playing dynamics:

- `tropical_house.md` documents this directly for melodic sample content: "lead instrument samples use velocity layers for realistic articulation," distinguishing a properly multisampled lead from a single-velocity sample that only gets louder or softer without changing character.
- `trailer_music.md` documents a deliberately narrow, purpose-driven use of velocity layers: "Trailer music uses the top velocity layers of orchestral sample libraries almost exclusively" — for maximum-impact material, only the loudest, most aggressive-sounding recorded layer is used, skipping the softer layers entirely rather than triggering them dynamically. This is a curation decision built on top of a library that already has full velocity coverage — see `sample_library_curation_workflow.md` for the selection side of this.

## True Legato vs. Simple Crossfaded Sustains

Several classical/orchestral genre files distinguish "true legato" sampling — where the library contains dedicated recordings of actual note-to-note transitions — from simpler libraries that just crossfade between separately-triggered sustained notes:

- `neoromanticism.md` states this distinction explicitly: "program them with genuine legato transitions (true legato sample patches, not simple crossfaded sustains) to capture the genre's sweeping melodic character" — a crossfaded sustain can approximate a legato phrase's loudness contour but can't reproduce the actual transitional sound (a bow changing string, a slide between notes) that true legato sampling captures as its own recorded event.
- `chamber_music.md` and `romantic_drama_score.md` (per `knowledge_base/genres/cinematic/romantic_drama_score.md`) both recommend "detailed solo-string and wind sample libraries with true legato and varied articulation" and "high-quality solo piano and chamber-string sample libraries with true legato and expressive dynamic control," respectively, for convincing virtual mockups of intimate, performance-detail-dependent genres.
- `renaissance.md` extends the same principle to vocal material: "high-quality choral sample libraries with true legato/polyphonic voice-leading engines to render convincing imitative counterpoint mockups" — polyphonic voice-leading here means the library can correctly crossfade multiple simultaneous vocal lines' transitions, not just one melodic line's.

## Articulation Switching

Beyond legato transitions, a fully multisampled instrument typically includes separate recorded articulations — distinct playing techniques that produce genuinely different waveforms, not just a processed variant of one core recording:

- `modernism.md` documents this at its most demanding: "sample libraries with genuine extended-technique articulation switches (snap pizzicato, col legno, flutter-tongue, extreme-register patches) rather than pitch-shifting standard articulations, which cannot replicate the era's characteristic strained timbre" — the file is explicit that pitch-shifting a normal articulation is not an acceptable substitute for an actual recorded extended technique, because the two produce audibly different results.
- `bossa_nova.md` documents articulation switching for a specific idiomatic technique: "high-quality nylon-string guitar sample libraries with fingerstyle articulation switching for realistic bossa comping in DAW mockups" — switching between recorded fingerstyle articulations (rather than one generic guitar patch) is what makes a programmed bossa comp pattern read as idiomatically played rather than generic.
- `swing.md` documents articulation switching applied at the ensemble-section level rather than a solo instrument: "use full big-band sample libraries with true legato/section articulations rather than single-hit samples," recommending producers "layer sampled big-band section patches with true legato and swing-quantized MIDI to approximate live section phrasing convincingly" — here, the multisampled unit is an entire horn or reed section's recorded articulations, not one instrument's.

## How Multisampling Differs From Round-Robin

Round-robin sampling (per `one_shot_layering_and_round_robin_variation.md`) solves *repetition* — several takes of the *same* note/velocity/articulation, cycled through so identical triggers don't sound mechanically identical. Multisampling solves *range* — enough distinct recordings across pitch, velocity, and articulation that the instrument responds accurately no matter what's played. A fully realized sample library typically needs both simultaneously: round-robin variation within each individual pitch/velocity/articulation cell, multiplied across the full multisampled range — which is why comprehensive orchestral libraries can require many thousands of individual recorded samples.

## Common Mistakes

**Pitch-shifting a single articulation instead of using a genuinely recorded extended technique.** Per `modernism.md`, this specifically fails to replicate the era's "characteristic strained timbre" — pitch-shifting changes frequency but not the fundamentally different excitation mechanism (bow position, embouchure, mallet type) that defines an extended technique's actual sound.

**Relying on crossfaded sustains where the genre's melodic style depends on audible transitions.** Per `neoromanticism.md`, sweeping legato lines expose the difference between a true legato patch and a crossfaded approximation more than short, detached phrases would — genre choice should inform which library feature actually matters for a given mockup.

**Using a library's full velocity/articulation range indiscriminately when the genre calls for a narrower, purpose-specific slice.** Per `trailer_music.md`, deliberately restricting to only the top velocity layers is itself the correct choice for maximum-impact material — using the full dynamic range there would undercut the intended effect, the reverse of the usual "use everything the library offers" instinct.

## Cross-References

- `knowledge_base/sound_design/sampling/one_shot_layering_and_round_robin_variation.md` — round-robin variation within a single pitch/velocity/articulation cell, the repetition-avoidance technique this entry's range-building multisampling complements.
- `knowledge_base/sound_design/sampling/sample_library_curation_workflow.md` — how the velocity-layer coverage documented here is selected from and evaluated within a library.
- `knowledge_base/sound_design/sampling/pitch_shifting_samples_for_harmonic_content.md` — chromatic sampler mapping across pitch, the pitch-axis counterpart to this entry's velocity/articulation-axis coverage.
- `knowledge_base/genres/classical/neoromanticism.md`, `modernism.md`, `renaissance.md`, `chamber_music.md` — true legato and extended-technique articulation switching for orchestral/chamber mockups.
- `knowledge_base/genres/jazz/bossa_nova.md`, `swing.md` — idiomatic fingerstyle and big-band section articulation switching.
- `knowledge_base/genres/edm/tropical_house.md`, `knowledge_base/genres/cinematic/trailer_music.md`, `romantic_drama_score.md` — velocity-layered instruments in electronic and cinematic production contexts.
