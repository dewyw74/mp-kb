---
workflow_name: "FL Studio Orchestral and Strings MIDI Programming Workflow"
daw: "fl_studio"
category: "midi"
goal: "Program realistic orchestral and string MIDI parts in FL Studio's Piano roll — velocity layering and keyswitch articulation control with a sample library, legato programming with correct overlap timing, and CC1/CC11 expression and dynamics automation — rather than a flat, single-articulation MIDI part that reads as programmed rather than performed."
steps:
  - "Load a multisampled orchestral/string library (typically hosted in Native Instruments Kontakt, per `knowledge_base/vst_database/native_instruments_kontakt.md`) with velocity-layer and articulation coverage rather than a single-velocity, single-articulation patch."
  - "Identify the library's keyswitch note range (usually below the playable range) and place keyswitch notes in the Piano roll immediately before the phrase that needs the corresponding articulation, per `knowledge_base/sound_design/sampling/multisampling_and_velocity_layers.md`'s documentation of articulation switching in orchestral sample libraries."
  - "Program dynamics primarily through velocity, since a properly multisampled library uses distinct recordings (not just volume scaling) for soft, medium, and hard-played notes — set velocity to genuinely match the intended dynamic level rather than leaving every note at a default value."
  - "For legato phrases, overlap consecutive notes' start/end points slightly in the Piano roll (rather than leaving a gap or exact edge-to-edge placement) so the library's true-legato transition sampling actually triggers between the two notes, per the true-legato distinction documented in `knowledge_base/sound_design/sampling/multisampling_and_velocity_layers.md`."
  - "Switch to a dedicated legato/sustain keyswitch or articulation lane before phrases that need connected, bowed/sung continuity, and switch back to a detached articulation (staccato, spiccato) for phrases that need separation, rather than leaving one articulation active for the entire part."
  - "Draw CC1 (mod wheel, typically mapped to dynamic swell/intensity in orchestral libraries) automation across sustained notes and phrases to add crescendo/diminuendo movement within a single held note, which velocity alone — set once at note-on — cannot produce."
  - "Draw CC11 (expression) automation for overall phrase-level dynamic shaping and to control the balance between the library's dynamic layers in real time, layering it with CC1 rather than using only one of the two controllers."
  - "Apply light timing humanization to entrances and releases per `knowledge_base/midi/programming/humanization_and_groove_timing.md`, since orchestral ensembles naturally have small inter-player timing spread that a perfectly quantized MIDI part doesn't reproduce."
  - "Reference `knowledge_base/midi/programming/pitch_bend_and_expressive_controller_automation.md` for any string part that needs a portamento glide or an expressive pitch-bend gesture between notes, distinct from the discrete keyswitch/articulation changes covered above."
related_plugins:
  - "FL Studio Piano Roll"
  - "native_instruments_kontakt"
tags:
  - "fl-studio"
  - "orchestral"
  - "strings"
  - "midi-programming"
  - "keyswitch"
  - "legato"
  - "cc-automation"
  - "velocity-layers"
---

# FL Studio Orchestral and Strings MIDI Programming Workflow

A flat MIDI string or orchestral part — uniform velocity, one articulation, no continuous controller movement — plays back as recognizably programmed no matter how good the underlying sample library is, because the library's realism depends on the MIDI data actually exercising its velocity layers, articulation switches, and legato transitions rather than triggering the same default patch state on every note. This workflow covers the FL Studio Piano roll mechanics for driving those library features correctly: keyswitch placement, legato overlap timing, and CC1/CC11 dynamics automation.

## Loading a library that supports the technique

The whole workflow depends on starting from a genuinely multisampled library rather than a single-velocity, single-articulation patch. Native Instruments Kontakt is the format the professional orchestral sample library industry standardized on, per `knowledge_base/vst_database/native_instruments_kontakt.md`, precisely because its scripting engine supports the deep round-robin, velocity-layer, and keyswitch behavior this workflow relies on — a lighter native sampler generally won't expose the same articulation-switching surface.

## Keyswitch placement

Most orchestral libraries map their available articulations (legato, staccato, spiccato, tremolo, pizzicato) to keyswitch notes sitting below the instrument's normal playable range. Place a keyswitch note in the Piano roll immediately before the phrase that needs the corresponding articulation — keyswitches take effect for notes played after them, so placing one even slightly late means the first note or two of the intended phrase plays back in the wrong articulation. `knowledge_base/sound_design/sampling/multisampling_and_velocity_layers.md` documents why this matters more than it might seem: a fully multisampled instrument's articulations are genuinely different recordings, not a processed variant of one core sample, so triggering the wrong one produces an audibly different (not just subtly different) result.

## Velocity as the primary dynamics driver

Set note velocity to match the intended dynamic level deliberately, rather than leaving every note at whatever value the Piano roll defaults to. A properly velocity-layered library — per `knowledge_base/sound_design/sampling/multisampling_and_velocity_layers.md` — uses distinct recordings for soft, medium, and hard-played notes because a real instrument's timbre changes with dynamics, not just its loudness; a flat-velocity MIDI part only ever triggers one velocity layer regardless of the musical dynamic intended, which reads as static even if the notes themselves are well-placed.

## Legato programming and overlap timing

For connected, bowed or sung phrases, overlap consecutive notes slightly in the Piano roll — the end of one note extending a small amount past the start of the next — rather than placing notes edge-to-edge or leaving a gap between them. This overlap is what triggers a true-legato library's dedicated note-to-note transition sample rather than simply re-triggering a fresh sustain on the new note; per `knowledge_base/sound_design/sampling/multisampling_and_velocity_layers.md`, "a crossfaded sustain can approximate a legato phrase's loudness contour but can't reproduce the actual transitional sound" that a genuine legato-sampled transition captures. Getting the overlap amount right is library-specific — too little overlap can fail to trigger the transition at all, too much can produce an audible double-attack — so check the specific library's documented legato-trigger behavior rather than assuming a fixed overlap value works universally.

## CC1 and CC11 for expression and dynamics

Velocity sets a note's dynamic level at the moment it's triggered, but it can't produce movement within a single held note — a swell, a crescendo into a sustained chord, a diminuendo at the end of a phrase. Draw CC1 (mod wheel) automation across sustained notes for exactly this kind of intra-note dynamic movement, since most orchestral libraries map CC1 to a dynamic layer crossfade or intensity parameter specifically for this purpose. Layer CC11 (expression) on top for phrase-level dynamic shaping and overall balance control — the two controllers are complementary rather than redundant, and using only one leaves either the within-note swell or the overall phrase shape unaddressed.

## Timing humanization

Even a well-articulated, well-automated part can still read as mechanical if its timing is perfectly quantized, since a real ensemble has small, natural inter-player timing spread on entrances and releases. Apply light humanization to note entrances and releases per `knowledge_base/midi/programming/humanization_and_groove_timing.md` — enough to soften the mechanical edge without introducing enough spread to sound genuinely uncoordinated.

## Common mistakes

Placing a keyswitch note at the same position as (or after) the first note of the phrase it's meant to affect, causing the phrase to start in the wrong articulation before the switch takes effect. Leaving every note at a flat, default velocity, which only ever triggers one of the library's velocity layers regardless of the intended musical dynamic. Programming legato phrases with notes placed edge-to-edge instead of overlapped, which fails to trigger the library's true-legato transition sampling and falls back to a re-triggered sustain that sounds disconnected. Relying on velocity alone for all dynamic expression and skipping CC1/CC11 automation entirely, which leaves sustained notes and long phrases static regardless of how well the note-level dynamics were programmed.
