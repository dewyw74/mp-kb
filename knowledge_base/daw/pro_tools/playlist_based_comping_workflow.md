---
workflow_name: "Pro Tools Playlist-Based Comping Workflow"
daw: "pro_tools"
category: "editing"
goal: "Use Pro Tools' Playlists system — a stack of alternate takes per track, distinct from Ableton/FL take-lane comping — to loop-record multiple takes, audition them, and build a single comped performance on the track's main playlist."
steps:
  - "Set up loop record over the target section so Pro Tools automatically creates a new Playlist on each pass, building up a full stack of takes without any manual setup between passes."
  - "After recording, open the Playlists list for the track (the track name menu) to confirm every take was captured as its own named, chronologically ordered Playlist (.01, .02, .03...)."
  - "Use New Playlist (Ctrl+\\ on Mac / Start+\\ on Windows) to create a fresh comp destination playlist if comping onto a clean lane rather than directly onto the best take."
  - "Switch the Playlists view to comping/lanes mode to see every take's playlist as its own lane beneath the track, and use Shift+S to solo an individual lane while auditioning."
  - "Rate takes and, if useful, filter lanes to show only regions above a chosen rating threshold before committing to a comp."
  - "Select the strongest segment in each region of the timeline across the visible lanes, then copy it to the master comp playlist (Ctrl+Opt+V) to build the final comp phrase by phrase."
  - "Use Opt+Cmd+Shift+Up/Down to cycle a selected clip through the other available playlists in place, auditioning alternates directly in the context of the surrounding comp without leaving the main lane."
  - "Apply crossfades at each comp seam using Pro Tools' standard edit tools, placing seams at rests or transient onsets per the seam-placement guidance in `knowledge_base/daw/workflow/comping_best_take_selection_philosophy.md`."
  - "Fine-tune the finished comp with clip gain, per `knowledge_base/daw/pro_tools/clip_gain_and_elastic_audio_workflow.md`, since Playlists fully support clip gain, clip effects, and normal editing tools once the comp is assembled."
  - "Consolidate or duplicate the finished comp playlist as a safety copy before deleting any unused alternate playlists, so earlier takes remain recoverable if a later revision needs them."
related_plugins:
  - "Pro Tools Playlists"
  - "Pro Tools Loop Record"
  - "Pro Tools Track Comping (Playlist Lanes)"
tags:
  - "pro-tools"
  - "comping"
  - "playlists"
  - "loop-record"
  - "take-selection"
  - "editing"
  - "vocal-comping"
---

# Pro Tools Playlist-Based Comping Workflow

Pro Tools has recorded and comped takes through Playlists since long before "take lane" comping existed in other DAWs, and the mechanics are genuinely different from Ableton's Take Lanes or FL Studio's audio-clip stacking. In Pro Tools, every track can hold multiple complete alternate Playlists — full parallel versions of that track's timeline — and comping means selecting and copying regions across those playlists into one final playlist, rather than dragging segments out of lanes attached to a single take stack. This entry covers the actual Playlist mechanics; for the take-selection judgment calls themselves (accuracy vs. feel, seam placement, how many takes is enough), see `knowledge_base/daw/workflow/comping_best_take_selection_philosophy.md`, which is DAW-agnostic and applies directly here.

## What a Playlist Actually Is

A Playlist in Pro Tools is a complete alternate arrangement of clips on a track's timeline — not a short take-lane fragment, but a full parallel version of everything on that track. A single track can hold any number of playlists, and only one is visible/active in the main track lane at a time; the others sit available in the background until called up. This is why Pro Tools documentation describes a "stack of playlists cut to the same click" — each playlist in the stack is a complete pass of the same material, ready to be auditioned or comped from.

## Loop Recording Into Playlists

Loop-recording over a section is the standard way to build up a take stack: Pro Tools automatically creates a new Playlist each time the loop cycles, so a single extended loop-record pass yields a full set of numbered alternate playlists (.01, .02, .03, and so on) with no manual setup required between passes. This is functionally similar in outcome to Ableton's Take Lanes under loop record, but structurally different — each Pro Tools pass is a full independent playlist rather than a lane layered under one shared track.

## Comping Mode and Lanes

Switching a track into its comping/lanes display shows every playlist in the stack as its own lane beneath the main track, in recording order, which is what makes multi-take auditioning practical. Shift+S solos whichever lane is currently selected so each take can be heard in isolation, and takes can be rated and lane displays filtered to only the highest-rated regions once a first listening pass has narrowed the field. Selecting a region in any lane and copying it to the master comp playlist (Ctrl+Opt+V) is the core comping action — this can be done at any granularity, from a single word to an entire verse. Opt+Cmd+Shift+Up/Down cycles a selected clip through the other playlists in place without breaking the comp's timeline context, which is the fastest way to A/B alternates for one specific phrase.

## Comping Is Full Editing, Not a Separate Mode

Once material is copied into the comp playlist, it behaves like any other track content: crossfades, clip gain, clip-based effects, and every standard edit tool apply normally. This means the comp doesn't need a separate "finishing" pass in a different tool — seam smoothing and level matching happen with the same clip gain and editing tools covered in `knowledge_base/daw/pro_tools/clip_gain_and_elastic_audio_workflow.md`.

## Common mistakes

Comping directly onto whichever playlist happens to be visible instead of creating a dedicated comp playlist, which risks overwriting a full usable take that might still be needed later. Never opening the lanes/comping view and instead scrubbing through playlists one at a time from the track menu, which makes in-context A/B auditioning far slower than it needs to be. Deleting unused alternate playlists immediately after finishing a comp, before a mix or client revision confirms the comp is truly final — Playlists are cheap to keep and expensive to have lost. Placing comp seams without a crossfade or without respecting natural rests and transients, the same seam-placement mistake covered generally in `knowledge_base/daw/workflow/comping_best_take_selection_philosophy.md`, which applies just as directly inside Pro Tools' Playlist workflow as anywhere else.
