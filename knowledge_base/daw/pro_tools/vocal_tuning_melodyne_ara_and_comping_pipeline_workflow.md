---
workflow_name: "Pro Tools Vocal Tuning (Melodyne ARA) and Comping Pipeline Workflow"
daw: "pro_tools"
category: "editing"
goal: "Sequence Playlist comping, ARA2-integrated Melodyne pitch correction, and insert-based Auto-Tune or mix processing in the correct Pro Tools-native order, so tuning and comping decisions don't fight each other and pitch correction happens on a finished performance rather than a moving target."
steps:
  - "Finish comping the performance to a single master Playlist first, per `knowledge_base/daw/pro_tools/playlist_based_comping_workflow.md`, before opening any tuning tool — tuning a take that later gets swapped for a different comped phrase wastes the correction work already done."
  - "Choose ARA2 Melodyne when detailed, editable, non-destructive pitch and timing correction is the goal, since ARA2 integration means Melodyne reads the actual clip data directly inside the Pro Tools Edit Window rather than processing audio in a black-box real-time plugin."
  - "Initiate Melodyne on a whole track by right-clicking the track's nameplate and choosing Melodyne > Edit, or on a single clip by right-clicking that clip and choosing Edit from its Melodyne submenu (Shift+Ctrl+A opens the currently selected clip)."
  - "Use Track Mode when the whole track's contents should be visible and editable together in Melodyne, and Clip Mode when work should stay scoped to one specific clip at a time."
  - "Edit pitch, timing, and formant on the Melodyne 'blobs' directly in the integrated editor pane, which appears as its own tab at the bottom of the Pro Tools Edit Window rather than a separate floating application window."
  - "Commit Melodyne's edits back to the Pro Tools track (via right-click) once corrections are finalized, so the corrected audio becomes the track's actual clip data going forward."
  - "Reach for Auto-Tune Pro as a track insert instead of Melodyne specifically when a vocal needs real-time correction while tracking, a stylized hard-tuned effect, or its built-in Harmony Player — Auto-Tune's real-time signal-chain position makes it the right tool for effects the artist needs to hear back while performing, where Melodyne's offline, post-take editing model does not apply."
  - "Place any chosen tuning tool before EQ, compression, or saturation in the insert order on that track, since correcting pitch on an already-EQ'd or already-compressed signal makes the correction react to a shaped signal instead of the source performance."
  - "Use clip gain, per `knowledge_base/daw/pro_tools/clip_gain_and_elastic_audio_workflow.md`, to even out level before or after tuning as needed — tuning tools correct pitch, not level, so uneven takes still need a clip gain pass either way."
  - "Bounce or freeze the tuned, comped vocal to a new track/playlist once the ARA edit is finalized if the session needs to be handed off to a system without Melodyne installed, since ARA edits depend on Melodyne being present to remain re-editable."
related_plugins:
  - "Celemony Melodyne (ARA2)"
  - "Antares Auto-Tune Pro"
  - "Pro Tools Playlists"
  - "Pro Tools Clip Gain"
tags:
  - "pro-tools"
  - "vocal-tuning"
  - "melodyne"
  - "ara2"
  - "auto-tune"
  - "comping"
  - "vocal-chain"
  - "editing"
---

# Pro Tools Vocal Tuning (Melodyne ARA) and Comping Pipeline Workflow

Pro Tools' vocal pipeline runs through two tools that solve different problems and, critically, have to happen in the right order: Playlist-based comping assembles the best performance first, and Melodyne — integrated via ARA2 directly into the Edit Window — or Auto-Tune Pro as a real-time insert then corrects pitch and timing on that finished performance. Doing tuning before comping is finalized means correction work gets thrown away every time a comp decision changes which take is active. This entry covers the Pro-Tools-native mechanics; for the judgment calls behind comping order and how much correction preserves natural feel, see `knowledge_base/daw/workflow/vocal_tuning_naturalness_and_comping_order_philosophy.md`, and compare against `knowledge_base/daw/ableton/vocal_tuning_and_comping_pipeline_workflow.md` for the same sequencing question in a DAW without ARA.

## Comp First, Tune Second

Because Playlists hold complete alternate takes (see `knowledge_base/daw/pro_tools/playlist_based_comping_workflow.md`), the comping decision — which phrase from which take ends up in the final master playlist — should be locked before any tuning tool touches the audio. Tuning a take that later gets swapped out during a comp revision wastes the correction pass entirely, and worse, can leave a tuned segment sitting next to an untuned one if the swap happens after tuning was already applied to only part of the vocal.

## Melodyne via ARA2

ARA2 (Audio Random Access) is what lets Melodyne read Pro Tools clip data directly rather than processing audio through a real-time plugin instance. Initiating Melodyne — via a track's right-click Melodyne > Edit, or a clip's own Melodyne submenu — opens Melodyne's "blob" editor as an integrated pane inside the Pro Tools Edit Window itself, addressable in either Track Mode (whole track) or Clip Mode (single clip). Because this is a direct-access edit rather than a processed audio stream, corrections stay non-destructive and re-editable as long as Melodyne remains installed on whatever system opens the session; edits are committed back to the Pro Tools track via right-click once finalized.

## Auto-Tune Pro as a Real-Time Insert

Auto-Tune Pro occupies a different role: as a standard real-time insert, it's the right tool when correction needs to be audible during tracking (an artist singing to a tuned monitor mix), when a stylized hard-tune effect is the intended sound rather than a corrected one, or when its built-in Harmony Player is needed. Where Melodyne's ARA2 model is built around editing a finished take after the fact, Auto-Tune's insert-chain position makes it the tool for correction that has to happen in real time, in the signal path, while performance is still happening.

## Insert Order Around the Tuning Tool

Whichever tool is used, it belongs before EQ, compression, or saturation in the track's insert order. Tuning a signal that's already been shaped by a compressor or EQ means the correction algorithm is reacting to an altered signal rather than the actual source performance, which increases the odds of audible artifacts. Clip gain (see `knowledge_base/daw/pro_tools/clip_gain_and_elastic_audio_workflow.md`) handles the separate problem of uneven level and can be applied before or after tuning, since neither Melodyne nor Auto-Tune corrects for level on its own.

## Common mistakes

Running Melodyne or Auto-Tune on individual takes before the comp is finalized, then having to redo correction work every time a comp swap changes which take is active. Placing a tuning plugin after EQ or compression in the insert chain, causing it to react to an already-shaped signal instead of the source. Reaching for Auto-Tune's real-time insert model for detailed, editable correction work that Melodyne's ARA2 approach handles with far more precision and revisability. Handing off a session with committed-but-uncollapsed ARA edits to a system without Melodyne installed, leaving the receiving engineer unable to re-open the correction.
