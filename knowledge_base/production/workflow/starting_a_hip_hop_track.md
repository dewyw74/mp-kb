---
workflow_name: "Starting a Hip-Hop Track From a Blank Project"
daw: "generic"
category: "pre-production"
goal: "Take a new hip-hop/trap track from a blank DAW project to a solid 8-16 bar beat loop ready for a vocalist, in an order that matches the genre's beat-first (rather than song-first) writing convention."
steps:
  - "Set tempo based on target subgenre (trap/drill run faster-feeling via double-time hi-hats at a moderate base BPM; boom bap sits slower and more laid-back)."
  - "Choose the sample or 808/bass-and-drum starting point based on subgenre convention: boom bap and East Coast styles typically start from a sampled loop; trap and drill typically start from the 808/kick relationship first."
  - "Build the drum foundation (kick, snare/clap, hi-hat pattern) before adding melodic material, per the hi-hat-as-signature-element and 808-as-lead-element guidance in `knowledge_base/midi/patterns/drum_pattern_programming.md` and `knowledge_base/midi/patterns/bass_and_808_pattern_programming.md`."
  - "Add a short (2-4 note or sampled-loop) melodic bed, kept deliberately minimal so it leaves room for a future vocal."
  - "Loop the full 8-16 bar beat and check it against a genre reference track for tempo feel, hi-hat density, and low-end weight."
  - "Apply sidechain ducking between 808/kick and other low-mid elements to avoid masking, per `knowledge_base/mixing/compression/sidechain_pumping.md`."
  - "Block out a rough beat-switch or energy-change point if the track is planned to run longer than a single loop, per trap's common structural device of a mid-track beat switch."
  - "Hand off to a vocalist or topline writer once the beat loop is solid, per `knowledge_base/production/songwriting/topline_and_vocal_hook_arrangement.md`."
  - "Finish arrangement detail (intro, outro, ad-lib space, structural variation) only after the vocal is recorded or the reference vocal take is locked."
related_plugins:
  - "spectrum analyzer (e.g. FabFilter Pro-Q 3, Voxengo SPAN)"
  - "loudness meter (e.g. Youlean Loudness Meter)"
  - "reference-track utility"
tags:
  - "workflow"
  - "hip-hop"
  - "trap"
  - "boom-bap"
  - "pre-production"
---

# Starting a Hip-Hop Track From a Blank Project

Hip-hop and its subgenres are documented across this knowledge base as beat-first writing traditions — the drum/808 or sampled-loop foundation typically exists before a vocalist is involved, in contrast to the topline-and-instrumental-in-parallel or fully song-first approaches more common in other genres. This workflow sequences that beat-first process in an order that avoids two common false starts: building melodic material before the drum/bass relationship is locked, and detailing full arrangement before a vocal exists to arrange around.

## Goal

Get a solid, reference-checked 8-16 bar beat loop ready to hand off to a vocalist, without prematurely locking arrangement decisions that should really be made in response to a finished vocal take.

## 1. Set tempo by subgenre feel, not just BPM

Trap and drill often feel faster than their base BPM suggests because of double-time hi-hat subdivisions layered over a moderate tempo; boom bap and East Coast styles sit at a more directly-felt, laid-back tempo. Choose the number with the genre's actual felt density in mind, not just a target BPM in isolation.

## 2. Pick the genre-appropriate starting element

Per `knowledge_base/genres/hiphop/boom_bap.md` and `knowledge_base/genres/hiphop/east_coast_hip_hop.md`, sample-based subgenres typically start from the sampled loop, since the loop's chop points and swing define the whole beat's feel. Per `knowledge_base/genres/hiphop/trap.md` and `knowledge_base/genres/hiphop/drill.md`, 808-driven subgenres start from the kick/808 relationship, since the bass line's slides and syncopation are the beat's structural core.

## 3. Build drums before melody

Program the kick/snare/hi-hat foundation first. For hi-hat-driven subgenres, this means establishing the roll/triplet/velocity-accent pattern that `knowledge_base/midi/patterns/drum_pattern_programming.md` documents as the genre's actual rhythmic-interest carrier before any melodic part is added — adding melody first risks writing something that competes with a hi-hat pattern that hasn't been decided yet.

## 4. Keep the melodic bed minimal by design

Per `knowledge_base/midi/patterns/melody_and_arpeggio_pattern_programming.md`, hip-hop's instrumental melodic loops are typically 2-4 notes, deliberately restrained so they don't crowd a vocal that doesn't exist yet. Resist the urge to fully develop this part at the beat-building stage — its job is atmosphere, and over-developing it now creates rework later once a vocal needs the space.

## 5. Reference-check and sidechain before handoff

A/B the loop against a genre reference for hi-hat density and low-end weight, and apply sidechain ducking between the 808/kick and other low-mid content so the beat doesn't mask on club or earbud playback alike.

## Common mistakes

Detailing full song arrangement (verses, hooks, bridges) before a vocalist has recorded anything — hip-hop arrangement decisions (where the hook lands, where ad-lib space is needed, whether a beat switch happens) are usually downstream of the vocal performance, not upstream of it. Also common: over-writing the instrumental melodic loop at the beat stage, leaving no room for the vocal once it's added.

## Alternatives

For hip-hop-adjacent genres where the vocal is written first (some pop-rap crossover work), start from a topline sketch over a rough drum-only loop instead, and build out the full beat once the vocal melody and phrasing are set.
