---
workflow_name: "Ableton Session View Clip Launching and Follow Actions"
daw: "ableton"
category: "session"
goal: "Use Session View's launch quantization, Follow Actions, and scene-triggering logic to build clips and scenes that behave predictably in a live or semi-improvised performance context, distinct from using Session View purely as a song-sketching tool."
steps:
  - "Set Global Quantization in the Control Bar to the grid value that should govern clip and scene launches by default (1 Bar is the common starting point for song-section material)."
  - "Override quantization per clip in the Clip View Launch box when a specific clip needs to trigger faster or slower than the global setting, such as a 1/4-note fill or an unquantized FX one-shot."
  - "Enable Legato Mode on clips that should hand off play position rather than restart from bar one, so switching between variation clips stays in sync with the bar the track is already on."
  - "Select clips that should play in sequence, right-click, and choose Create Follow Action Chain to build an ordered playback sequence without setting each clip's Follow Action individually."
  - "Set Follow Action A/B choices and the Chance A/Chance B percentage slider on clips that should trigger the next clip probabilistically rather than deterministically."
  - "Choose Linked timing when a Follow Action should fire relative to the clip's own loop length, or Unlinked with an explicit Follow Action Time when it should fire on a fixed clock independent of clip length."
  - "Apply Follow Actions to scenes (double-click a scene to edit) when an entire section, not just one clip, should automatically advance to the next scene."
  - "Use the master channel strip's global Follow Actions on/off button to disable all Follow Actions instantly during a performance if the automatic chaining needs to be overridden live."
related_plugins:
  - "Ableton Session View"
  - "Ableton Follow Actions"
  - "Ableton Legato Mode"
  - "Ableton Global Quantization"
tags:
  - "ableton"
  - "session-view"
  - "follow-actions"
  - "clip-launching"
  - "quantization"
  - "legato"
  - "performance"
---

# Ableton Session View Clip Launching and Follow Actions

Session View's clip-launching mechanics are the layer beneath the song-building workflow documented in `knowledge_base/daw/ableton/session_to_arrangement_workflow.md`. That entry covers using Session View to compose a song and capture it into Arrangement; this entry covers the launch-quantization, Follow Action, and scene-triggering mechanics that make clips behave correctly whether the set is being sketched, performed live, or used as a generative sequencing tool in its own right.

## Global and per-clip quantization

Global Quantization, set in the Control Bar, determines the grid a clip or scene launch snaps to by default — a click on a clip slot does not fire immediately, it waits for the next quantization boundary (bar, beat, or a smaller subdivision). This keeps clips launched by hand or by controller locked to the beat instead of starting off-grid. Individual clips can override the global setting in the Clip View Launch box, which is useful for a fill or transition clip that needs to fire on a 1/4-note boundary rather than waiting a full bar, or for an FX one-shot that should trigger with no quantization at all.

## Legato Mode

Legato Mode changes what happens at the moment a new clip takes over a track: instead of restarting playback from the beginning of the new clip, Live continues from the same position the previous clip was already at. This matters most when switching between alternate takes of essentially the same loop (an A/B drum variation, a filtered vs. unfiltered version of the same chord clip) — Legato keeps the switch feeling like one continuous part rather than a rhythmic stutter. Legato Mode works independent of quantization and is commonly combined with Follow Actions so that automatic clip changes stay glued to the beat the track was already playing.

## Follow Actions: legacy behavior and the Live 11 chain workflow

Follow Actions tell a clip what to do after it finishes playing (or after a set time), without requiring a human to trigger the next clip. The underlying A/B follow-target and chance mechanism has existed for many Live versions; Live 11 made building and reading Follow Action setups substantially faster and clearer:

- **Follow Action Chains**: select a run of clips, right-click, and choose Create Follow Action Chain to automatically wire them to play in order — a fast way to build a sequence that previously required setting each clip's Follow Action by hand.
- **Chance as a percentage slider**: Follow Action Chance A and Chance B are shown as percentages that sum to 100% and can be set with a slider, replacing the older numeric-weight entry.
- **Linked vs. Unlinked timing**: a Linked Follow Action fires at the end of the clip (or after the number of loops set in the Follow Action Multiplier); an Unlinked Follow Action fires after a fixed Follow Action Time regardless of the clip's own length — useful for a generative or evolving arrangement where clip length and section length should be decoupled.
- **Scene-level Follow Actions**: Follow Actions can now be set on entire scenes, not just individual clips, so a whole section can automatically hand off to the next.
- **Global on/off**: a dedicated button in the master channel strip disables all Follow Actions at once, which is the fastest way to regain manual control mid-performance without hunting down individual clip settings.

## Scene triggering logic

Launching a scene fires every clip in that scene's row simultaneously (skipping empty slots, which leave the currently playing clip in that track untouched). Because of this, scenes work best when built as complete section snapshots — every track that should change state for that section has a clip in the row, and tracks that should keep playing through the section transition are simply left blank in that scene. Select Next/Previous Scene commands (and their key-mappable shortcuts) let a performer step through a scene list without needing to look at the grid, which matters when scenes are also carrying their own Follow Actions and the performer needs to know which scene is about to fire.

## Common mistakes

Leaving Global Quantization at a long value (1 Bar or longer) for every clip in a set, including short fills and one-shots that need to fire immediately — override quantization per clip rather than fighting the global setting. Building a long Follow Action chain without testing the Chance percentages in context; a 50/50 split feels very different once tempo, section length, and the surrounding clips are actually playing than it does read as two numbers in a list. Forgetting that Legato Mode only helps when the clips being switched between share a compatible tempo and phrase length — switching Legato between clips of different bar lengths can still produce an audible jump.
