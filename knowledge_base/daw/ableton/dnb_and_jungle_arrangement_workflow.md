---
workflow_name: "Ableton Drum and Bass / Jungle Rolling-Breakbeat Arrangement Workflow"
daw: "ableton"
category: "arrangement"
goal: "Arrange a drum and bass or jungle track in Ableton around a chopped and rearranged breakbeat, using Simpler's Slice mode or Slice to New MIDI Track to build the rolling drum pattern, contrasting half-time and double-time sections for arrangement variety, and giving the Reese/sub bass its correct structural role underneath a busy break."
steps:
  - "Warp the source break (Amen, Think, Apache, or a custom break) to project tempo using Beats warp mode, then slice it via Simpler's Slice playback mode or right-click > Slice to New MIDI Track, per `knowledge_base/daw/ableton/sample_chopping_and_slicing_workflow.md`, choosing Transients division over Bar/note-length division since the goal is chopping at each detected hit, not evenly."
  - "Reassemble the sliced break's MIDI clip into a denser, more syncopated pattern than the source recording — inserting ghost snares and rushed hi-hats between the original hits by re-triggering slices from elsewhere in the same break — per the reassembly technique documented in `knowledge_base/genres/edm/jungle.md` and `knowledge_base/genres/edm/drum_and_bass.md`."
  - "Preserve the break's original velocity information from the slice rather than flattening every hit to one velocity, since `jungle.md` notes the chops retain natural human swing and dynamic variation from the source performance without needing synthetic humanization."
  - "Build the sub-bass as its own MIDI track locked rhythmically to the kick within the break pattern, kept mono and centered per both genre files' mixing guidance, so it reads as the arrangement's low-end anchor under the busy chopped break rather than competing rhythmically with it."
  - "Layer a Reese or mid-bass element (detuned, phase-modulated saw pair, per `knowledge_base/genres/edm/drum_and_bass.md`'s sound-design notes) as a separate, more melodically or rhythmically active layer above the sub, automated independently from the sub-bass's simpler, kick-locked pattern."
  - "Build a half-time section by muting or filtering out every other break-slice trigger (or duplicating the MIDI clip and deleting alternating hits) so the perceived tempo halves while the underlying project tempo and sub-bass pulse stay constant, giving the arrangement a contrasting low-density 'rollers' section per both genre files' bridge convention."
  - "Contrast the half-time rollers section against a full double-time chopped-break section by re-enabling the full slice density, so the arrangement alternates between sparse, spacious half-time passages and dense, rapid-fire full-break passages rather than sustaining one density throughout."
  - "Automate a highpass or lowpass filter on the break bus during intro/breakdown spans (per `knowledge_base/mixing/automation/filter_sweep_automation.md`) to establish tempo and atmosphere before the full chopped break and sub-bass enter at the first drop, per both genre files' DJ-mixable intro convention."
  - "Reassemble the outro by peeling break-slice density and sub-bass back down in reverse of the intro build, mirroring the intro's filtered/thinned pattern for a DJ-friendly exit rather than a hard structural ending."
  - "Bus-compress the full reassembled break (per `knowledge_base/mixing/compression/drum_bus_compression.md`'s jungle citation) once slicing and re-triggering is complete, gluing the individually re-triggered slices back into a cohesive-sounding break rather than leaving them to sound like separate, disconnected hits."
related_plugins:
  - "Ableton Simpler"
  - "Ableton Slice to New MIDI Track"
  - "Ableton Drum Rack"
  - "Ableton Warp (Beats mode)"
  - "Ableton Auto Filter"
  - "Ableton Glue Compressor"
tags:
  - "ableton"
  - "arrangement"
  - "drum-and-bass"
  - "jungle"
  - "breakbeat"
  - "slicing"
  - "half-time"
  - "reese-bass"
---

# Ableton Drum and Bass / Jungle Rolling-Breakbeat Arrangement Workflow

Drum and bass and jungle arrangement is built from a different atomic unit than most genres documented in `knowledge_base/daw/ableton/` — instead of MIDI-programmed drums or a looped groove, the core rhythmic material is a chopped and reassembled breakbeat, sliced into individual hits and re-sequenced into a pattern denser and more syncopated than any human drummer originally played. This entry covers the Ableton-specific mechanics of that process: slicing the break with Simpler or Slice to New MIDI Track (building on the general slicing mechanics in `knowledge_base/daw/ableton/sample_chopping_and_slicing_workflow.md`), contrasting half-time and double-time sections for arrangement variety, and giving the sub/Reese bass its correct structural role underneath a constantly active break. Grounded in `knowledge_base/genres/edm/drum_and_bass.md` and `knowledge_base/genres/edm/jungle.md`, both of which treat the chopped break as the genre's core "instrument" rather than an optional texture layer.

## Slicing the Break: Transients, Not Bars

Per `knowledge_base/daw/ableton/sample_chopping_and_slicing_workflow.md`, both Simpler's Slice playback mode and the Slice to New MIDI Track dialog can chop a sample, but the division choice matters here specifically: Transients (slice at detected onsets) is the correct choice for a breakbeat, not Bar or fixed note-length divisions, since the goal is capturing each of the break's real, irregularly-timed hits as an individually re-triggerable slice. Warping the break to project tempo in Beats mode first keeps every resulting slice locked to the grid even after project tempo changes, which matters once slices start getting re-triggered out of their original order.

## Reassembly Is the Drum Programming

Once sliced, the actual composition work in this genre happens in the resulting MIDI clip, not at the synthesis or sample-selection stage: per `jungle.md` and `drum_and_bass.md`, both genres build their drum pattern by reassembling a break's individual hits into something denser and more syncopated than the source recording, inserting ghost snares and rushed hi-hats by re-triggering slices from elsewhere in the same break between its original hits. This reassembly *is* the drum programming in these genres — treat the auto-generated chromatic note order from Slice to New MIDI Track as a starting point to rearrange, never as a finished pattern. Preserve the break's original per-slice velocity rather than flattening every hit to a uniform level; `jungle.md` is explicit that this preserved human swing is what gives a reassembled break its "played" feel without needing synthetic humanization layered on top.

## Sub-Bass and Reese as Separate, Differently-Automated Layers

Both genre files treat sub-bass and mid-bass/Reese character as functionally distinct layers, not one bass part. Build the sub as its own MIDI track, locked rhythmically to the kick within the break pattern, kept mono and centered — this is the arrangement's low-end anchor and needs to stay simple and predictable even while the break above it gets rhythmically dense. The Reese or mid-bass layer, by contrast, is where melodic or rhythmic movement can happen: a detuned, phase-modulated saw pair automated with its own pitch glides and rhythmic variation, independent of the sub's steadier pattern. Keeping these on separate tracks with separate automation lanes avoids the "letting sub and mid-bass overlap and mask each other" mistake both genre files name directly.

## Half-Time vs. Double-Time as the Arrangement's Density Contrast

Where house and techno vary arrangement through layer rotation and micro filter moves (per `knowledge_base/daw/ableton/house_and_techno_arrangement_workflow.md`), drum and bass and jungle's fast tempo gives producers a different contrast tool: alternating between a sparse half-time "rollers" section (muting or deleting alternating slice triggers so the perceived beat halves while the underlying tempo and sub pulse stay constant) and a full double-time section at full slice density. This half-time/full-time alternation is the structural equivalent of both genre files' documented "stripped 'rollers' section" bridge convention — a hallmark structural device across nearly all drum and bass and jungle subgenres, used for extended tension before the next full drop reintroduces the dense chopped pattern.

## DJ-Functional Intro, Drop, and Outro

Per both genre files' arrangement notes, a filtered or half-time break with pad or vocal-sample atmosphere establishes tempo before the full chopped break and sub-bass enter at the first drop — automate a highpass or lowpass filter on the break bus across this span using the same mechanics as `knowledge_base/mixing/automation/filter_sweep_automation.md`. Mirror this in reverse at the outro, peeling break density and sub-bass back down rather than composing a new ending, for the same DJ-mixable functionality documented across both genre files.

## Common mistakes

Treating the auto-generated slice order from Slice to New MIDI Track as a finished pattern instead of rearranging it into an actual reassembled break. Over-quantizing or flattening slice velocity until the break's natural human swing is lost — both genre files name this directly as undermining the genre's essential groove. Letting the sub-bass and Reese/mid-bass layer share one track or one automation lane instead of separating them, risking the low-end masking both genre files warn against. Skipping bus compression on the reassembled break, leaving re-triggered slices sounding disconnected rather than glued into one cohesive pattern per `knowledge_base/mixing/compression/drum_bus_compression.md`.
