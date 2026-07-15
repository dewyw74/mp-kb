---
workflow_name: "FL Studio Drum and Bass / Jungle Rolling Breakbeat Arrangement Workflow"
daw: "fl_studio"
category: "arrangement"
goal: "Arrange a drum and bass or jungle track in FL Studio around a chopped and rearranged breakbeat (Amen/Think-style), contrasting half-time 'rollers' sections against full-tempo double-time break density, with the Reese/sub bass carrying the arrangement's low-end and rhythmic weight underneath a busy break."
steps:
  - "Load the source break (Amen, Think, or Apache-style breakbeat) into Slicex per `knowledge_base/daw/fl_studio/sample_chopping_and_slicing_workflow.md`, letting transient detection place initial slice markers before manually correcting them on a busy, dense source."
  - "Alternatively use the Playlist's native Slice tool (C) when the break needs to stay as arrangement-timeline audio rather than becoming a pad-mapped instrument, per the same workflow's distinction between the two tools."
  - "Reassemble the sliced break into a new, denser pattern than the source recording in the Piano roll or Channel Rack step sequencer — reordering hits, inserting ghost snares between main hits, and layering rushed hi-hats — per the chop-and-reassemble approach documented in `knowledge_base/genres/edm/jungle.md` and `knowledge_base/genres/edm/drum_and_bass.md`."
  - "Build the full-tempo, double-time-feeling break pattern as the main groove-section material, keeping chop density and syncopation high for the arrangement's rhythmic peak sections."
  - "Clone a distinct half-time 'rollers' pattern variant from the same chopped slice pool — thinner chop density, a rolling, more spacious placement of hits — for extended tension or bridge-style sections, per the 'rollers' structural hallmark documented in both genre files' arrangement sections."
  - "Program the Reese or sub bass in the Piano roll as a simpler, more rhythmically restrained part than the break itself, locked to the kick within the chop pattern, per both genre files' bass_patterns guidance that sub-bass stays 'simple, syncopated, and locked to the kick' while the break carries the rhythmic complexity."
  - "Keep the sub-bass layer mono and centered while any Reese/mid-bass layer carries the stereo width and phaser/chorus movement, per `knowledge_base/sound_design/presets/reese_bass_design.md`'s mono-sub-plus-detuned-mid-bass layering, so the bass reads as weight and glue under the busy break rather than competing with it for rhythmic attention."
  - "Sequence the Playlist alternating full-tempo double-time break sections against half-time rollers sections for contrast, per the intro-breakdown-drop-bridge-drop-outro structure both genre files document, rather than running one break density for the entire track."
  - "Route the finished chopped break instrument and the Reese/sub bass to separate Mixer buses per `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md`, keeping the two elements independently controllable for the mono-sub/wide-break balance the genre depends on."
related_plugins:
  - "Slicex"
  - "FL Studio Playlist"
  - "FL Studio Piano Roll"
  - "FL Studio Channel Rack"
  - "Edison"
tags:
  - "fl-studio"
  - "drum-and-bass"
  - "jungle"
  - "arrangement"
  - "breakbeat"
  - "reese-bass"
  - "playlist"
  - "workflow"
---

# FL Studio Drum and Bass / Jungle Rolling Breakbeat Arrangement Workflow

Drum and bass and jungle arrangement is built around a chopped and reassembled breakbeat rather than a programmed-from-scratch drum pattern — `knowledge_base/genres/edm/jungle.md` and `knowledge_base/genres/edm/drum_and_bass.md` both describe breaks "sliced and reassembled into new, denser patterns than the source recording, with ghost snares... inserted for forward momentum." `knowledge_base/daw/fl_studio/sample_chopping_and_slicing_workflow.md` already covers the general FL Studio chopping mechanics (Slicex vs. the Playlist Slice tool vs. Edison); this entry is the genre-specific application of that toolset to breakbeat reassembly, plus the half-time/double-time contrast and Reese/sub bass arrangement role that are unique to this genre family.

## Chopping the break with Slicex or the Playlist Slice tool

Load the source break into Slicex for a pad-mapped, re-triggerable instrument — the right choice when the break needs to be reordered and reprogrammed extensively in the Piano roll, since Slicex maps each detected transient across the keyboard for flexible re-sequencing. Reach for the Playlist's native Slice tool instead only when the break should stay as a small number of large, arrangement-timeline pieces rather than becoming a fully re-triggerable instrument. Busy, dense breaks like the Amen need manual slice-marker correction after Slicex's automatic transient detection, per the parent chopping workflow — a low-quality automatic slice on a fast, layered break is the single most common cause of a chop that sounds off-grid once reassembled.

## Reassembling into a denser, more syncopated pattern

The goal of reassembly isn't to recreate the source break's original rhythm — it's to build something denser and more syncopated than any human drummer originally played. Reorder the chopped slices in the Piano roll, insert ghost snares and rushed hi-hat fragments between the break's original hits, and re-pitch individual slices (the classic "pitched-down kick, pitched-up snare" chop technique both genre files document) for additional rhythmic and tonal variation. Because the source slices are already a human drum performance, this reassembly process doesn't need synthetic humanization on top — the swing is inherited from the source recording, and over-quantizing the reassembled hits is what actually flattens that feel out, per both genre files' common-mistakes sections.

## Half-time rollers vs. full-tempo double-time density

Both jungle and drum and bass structure their arrangements around alternating break density rather than holding one groove constant for the whole track. Build the full-tempo, high-density chop pattern as the arrangement's peak material — this is what plays under the drop/chorus sections. Separately, clone a "rollers" pattern variant from the same slice pool with a thinner, more spacious hit placement and a rolling, half-time-feeling groove: both genre files name this "stripped-back 'rollers' section featuring just the break and a rolling bassline" as a structural hallmark used for extended tension or DJ-tool functionality, distinct from a full breakdown. Sequencing the Playlist to alternate between these two densities — rather than running one chop pattern for the entire arrangement — is what produces the genre's characteristic push and pull between intensity and space.

## The Reese/sub bass's arrangement role under a busy break

With the break carrying nearly all of the arrangement's rhythmic complexity, the bass is deliberately kept simpler and more restrained — both genre files describe sub-bass as "simple, syncopated, and locked to the kick within the break," with a secondary Reese or mid-bass layer allowed more independent movement. Program the sub-bass part in the Piano roll to track the chop pattern's kick placements rather than writing an independently busy bassline; per `knowledge_base/sound_design/presets/reese_bass_design.md`, keep that sub layer mono and centered while any detuned Reese mid-bass carries the stereo width and slow phaser/chorus movement. This division of labor — break for rhythm, bass for weight and glue — is what keeps a dense, heavily chopped arrangement from collapsing into rhythmic clutter once the bass enters.

## Common mistakes

Reassembling a chopped break into a pattern that's actually simpler or less syncopated than the source recording, which defeats the entire point of chopping it in the first place — the reassembled pattern should read as denser and more active than what a human drummer played, not a tidied-up version of it. Writing an independently busy, rhythmically complex bassline that competes with the break for rhythmic attention instead of locking to the kick within the chop pattern, per both genre files' explicit guidance. Running the same break density (full-tempo or rollers) for the entire arrangement instead of alternating between them for structural contrast, which loses the push-and-pull dynamic that gives jungle and drum and bass arrangement its shape. Letting mono sub-bass and stereo Reese/mid-bass content overlap and mask each other instead of carving distinct frequency pockets, the specific mixing failure both genre files warn against.
