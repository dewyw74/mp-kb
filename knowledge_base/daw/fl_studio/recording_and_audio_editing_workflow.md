---
workflow_name: "FL Studio Recording and Audio Editing Workflow"
daw: "fl_studio"
category: "recording"
goal: "Record audio into Playlist audio tracks, edit and clean it up with Edison, and comp the best material from multiple takes into a final usable performance."
steps:
  - "Set the audio input device and levels in Audio Settings before recording, checking for headroom rather than recording hot to the input meter."
  - "Arm a Playlist audio track for recording and choose whether to record straight to the Playlist or through an Edison instance inserted on the input's Mixer track."
  - "Use loop/overdub recording for parts that benefit from multiple takes (vocals, solo instruments), letting FL Studio place each pass into its own lane so takes can be compared afterward."
  - "Trim, fade, and clean each take directly in the Playlist for basic edits, or open the recorded region in Edison for detailed editing, noise removal, or time manipulation."
  - "Use Edison's slicing tools to chop a recorded performance or loop into individually editable or re-triggerable segments when the material needs to be rearranged rather than just cleaned up."
  - "Audition takes lane by lane, muting or soloing each one, and manually cut the best sections from each take onto a single comp track."
  - "Crossfade or trim comp edit points so splices between takes are inaudible, checking transients and breath/attack points closely."
  - "Render or consolidate the final comped take to a single clean audio clip once editing is finished, keeping the original take lanes intact in case revisions are needed later."
related_plugins:
  - "FL Studio Playlist"
  - "Edison"
  - "FL Studio Mixer"
  - "izotope_rx"
  - "celemony_melodyne"
tags:
  - "fl-studio"
  - "recording"
  - "audio-editing"
  - "edison"
  - "comping"
  - "workflow"
---

# FL Studio Recording and Audio Editing Workflow

Recording audio in FL Studio runs through the Playlist's audio tracks, with Edison — Image-Line's integrated recording and editing plugin — handling the detailed editing, cleanup, and slicing work that the Playlist's own trim/fade tools don't cover. This workflow applies to vocal takes, DI or mic'd instrument recordings, and any external hardware captured per `knowledge_base/daw/fl_studio/external_hardware_sync_and_recording.md`.

## Preparing to record

Set the correct input device and confirm signal is reaching FL Studio in Audio Settings before arming anything. Recording with headroom rather than a hot input level matters more in FL Studio's audio path than it might in a mix-bus context, since a clipped recording can't be fixed by any downstream editing in Edison or elsewhere. Arm the target Playlist audio track, and decide up front whether the take should be recorded directly to the Playlist as a standard audio clip, or captured through an Edison instance inserted on the input Mixer track for immediate access to Edison's editing tools without a separate import step.

## Loop recording and multiple takes

For parts likely to need more than one attempt — lead vocals, a solo instrumental pass — loop/overdub recording captures each pass into its own lane rather than overwriting the previous attempt. FL Studio plays back the prior take while recording the next one, so a performer can react to what's already been captured. This produces a stack of take lanes on the same section, which is the raw material the comping step works from.

## Editing in Edison

Edison is FL Studio's dedicated audio-editing plugin: it opens a recorded region for trimming, noise removal, reversing, time-stretching/pitch-shifting, and convolution reverb processing, with click-free editing and full undo history. For most cleanup — trimming silence, removing a click or a stray noise, tightening a take's start point — Edison is the right tool rather than trying to do the same edit with the Playlist's zoomed-in waveform view. Edison also supports drumloop-style slicing, which is useful not just for drum breaks but for chopping any recorded performance into segments that need to be individually moved, replaced, or re-triggered.

## Slicing for rearrangement

When a recorded take needs to be rearranged rather than simply trimmed — reordering phrases, pulling the best syllable-level takes from different passes, chopping a performance into playable one-shots — Edison's slicing tools break the audio into discrete, individually addressable regions. This is functionally the audio equivalent of breaking a MIDI pattern into edit-friendly pieces, and it's what makes fine-grained comping below possible rather than being limited to whole-take swaps.

## Comping the best take

With several take lanes recorded, audition each one by muting/soloing individual lanes and identify the strongest sections across all of them — rarely will a single take be the best choice start to finish. Cut the winning sections from each lane and assemble them onto one comp track in the Playlist, matching FL Studio's flexible lane/track structure rather than a dedicated one-click comping tool (FL Studio does not have a single-button vocal comping feature; the comp is built manually from take lanes, per Image-Line's own forum guidance on the workflow). Crossfade or carefully trim each splice point so the transition between takes isn't audible — checking consonant onsets and breath sounds closely on vocal comps, since mismatched transients are where a comp edit is most likely to be heard.

## Finishing the comp

Once the comp track is complete, render or consolidate it into a single clean audio clip so downstream mixing treats it as one continuous performance rather than a stack of edited fragments. Keep the original take lanes in the project (muted or archived on unused tracks) rather than deleting them, in case a later revision needs to pull from a different take than the one originally chosen.

## Common mistakes

Recording without checking input headroom and clipping a take that then can't be fully repaired at the editing stage. Comping takes without crossfading or trimming splice points carefully, leaving audible clicks or timing jumps at every edit. Deleting original take lanes immediately after comping instead of archiving them, which removes the ability to revise the comp later without re-recording.
