---
workflow_name: "FL Studio Guitar DI Recording and Reamping Workflow"
daw: "fl_studio"
category: "recording"
goal: "Record a clean, unprocessed DI guitar signal into FL Studio before any amp simulation is applied, preserving the flexibility to change tone or amp choice later without re-tracking, then reamp that DI through an amp-sim plugin or a real amp via a hardware reamp box."
steps:
  - "Plug the guitar into the audio interface's Hi-Z/instrument input (or an external DI box), and route it to a Playlist audio track's Mixer insert with no amp-sim plugin loaded on that insert yet."
  - "Set input gain on the interface for headroom rather than a hot level, since a DI guitar signal's picking transients can clip an over-driven input before any amp-sim processing is even involved."
  - "Record the full DI performance per `knowledge_base/daw/fl_studio/recording_and_audio_editing_workflow.md`, optionally monitoring through a lightweight amp-sim placed only on the monitoring path (not printed to the recorded file) so the player hears a usable tone while tracking."
  - "Confirm after recording that the printed audio clip is the untouched DI signal — no amp-sim, cab IR, or heavy EQ baked in — since that clean signal is what preserves every downstream tone option."
  - "Insert an amp-sim plugin such as `neural_dsp_archetype` on the DI track's Mixer insert (or a send) to reamp entirely in the box, selecting amp/cab voicing to match the genre without re-tracking the performance."
  - "For hardware reamping, route the DI track's output through a passive reamp box (converting the recorded line-level signal back to instrument level) into a real amp, mic the amp, and record the mic'd result into a new audio track."
  - "Try multiple amp-sim instances or hardware reamp passes on separate Mixer inserts fed from the same DI clip, since the DI never needs to be re-recorded to audition a different tone."
  - "Once a final tone is chosen, keep the original DI clip archived (muted, not deleted) on its own track, per the take-archiving practice in `knowledge_base/daw/fl_studio/recording_and_audio_editing_workflow.md`, so the tone decision stays revisable later."
  - "Route the finished reamped signal into the guitar bus using the gain-staging conventions in `knowledge_base/daw/fl_studio/mixing_bus_routing_and_gain_staging_workflow.md`."
related_plugins:
  - "FL Studio Mixer"
  - "FL Studio Playlist"
  - "neural_dsp_archetype"
  - "Edison"
tags:
  - "fl-studio"
  - "recording"
  - "guitar"
  - "di"
  - "reamping"
  - "amp-sim"
  - "workflow"
---

# FL Studio Guitar DI Recording and Reamping Workflow

Recording a guitar's direct, unprocessed signal (DI) before any amp simulation or mic'd-amp tone is applied is what makes reamping possible at all — once a tone decision is baked into the recorded audio, changing it later means re-tracking the performance, not just swapping a plugin. This workflow covers getting a clean DI into FL Studio, monitoring through a temporary tone without printing it, and reamping the DI afterward through either an amp-sim plugin or a real amp via a hardware reamp box.

## Why DI-first preserves flexibility

A DI signal is the guitar's raw electrical output, captured before any amp, cabinet, or microphone coloring it. Recording DI-only means the performance and the tone decision are decoupled: the same take can be run through a clean, bright amp-sim voicing one day and a heavy, saturated one the next, without the guitarist replaying a single note. This matters most on parts that are hard to get right in a single take — a long solo, a tightly performed rhythm part — where a wrong amp choice discovered during mixing would otherwise force either living with it or scheduling a re-record.

## Recording the DI signal

Plug into the audio interface's Hi-Z/instrument input (or a dedicated DI box feeding a line input) and route the signal to a Playlist audio track's Mixer insert with no amp-sim loaded on that insert. Set input gain conservatively — a DI guitar signal carries strong picking-transient peaks that can clip an input gain staged too hot, and a clipped DI recording can't be un-clipped by any amp-sim or reamp step afterward. Record the take per `knowledge_base/daw/fl_studio/recording_and_audio_editing_workflow.md`'s general audio-recording mechanics; nothing about the DI-first approach changes how the take itself is captured, only what's (not) printed alongside it.

## Monitoring through a temporary tone

Playing guitar against a completely dry, unprocessed DI signal is difficult to perform well against — most players need to hear something resembling a finished amp tone to play convincingly. Load a lightweight amp-sim on the Mixer insert's monitoring path (or on a separate monitoring bus that isn't part of the recorded signal chain) so the performer hears a usable tone in real time, while the audio actually written to disk stays the clean DI. This is standard practice specifically because it removes any tension between "what sounds good to play against" and "what stays flexible for the mix."

## Reamping in the box with an amp-sim plugin

Once the DI is recorded, insert an amp-sim plugin — `knowledge_base/vst_database/neural_dsp_archetype.md` documents Neural DSP's Archetype series as exactly this kind of tool, built to eliminate the need for a loud recording room or physical amp to get a mix-ready guitar tone — directly on the DI track's Mixer insert or on a send if multiple tone variations need to run in parallel. Because the underlying DI never changes, switching between amp-sim titles, adjusting gain, or trying a completely different genre-appropriate voicing costs nothing beyond a plugin swap.

## Reamping through real hardware

For a genuine mic'd-amp tone rather than a simulation, route the DI track's output through a passive reamp box, which converts the recorded line-level signal back down to instrument level so a real amplifier can react to it the same way it would to a guitar plugged in live. Mic the amp as usual and record the mic'd signal into a new audio track via the interface — the DI clip stays untouched and available for a different amp or a different mic placement on a later pass, since the reamp box lets the same recorded performance be sent through the amp repeatedly.

## Auditioning multiple tones from one take

Because reamping (in the box or through hardware) never consumes or alters the source DI, it's practical to run the same DI clip through several amp-sim instances or several hardware reamp passes on separate Mixer inserts and compare them directly, rather than committing to one tone early and discovering partway through mixing that it doesn't sit well. Keep the original DI clip archived and muted on its own track once a final tone is chosen, exactly as with any other take-archiving decision, so the choice stays revisable without a re-record.

## Common mistakes

Printing an amp-sim tone directly onto the recorded take instead of keeping it on the monitoring path only, which quietly removes the entire point of tracking DI-first. Recording the DI too hot because the player is used to gain-staging for a full amp tone rather than a clean instrument-level signal, clipping transients that can't be recovered at the reamp stage. Deleting the DI clip after committing to a final amp-sim or hardware tone, closing off the flexibility that was the reason to record DI in the first place.

## Cross-references

- `knowledge_base/vst_database/neural_dsp_archetype.md` — the amp-sim product line most directly built around this DI-first, reamp-later workflow
- `knowledge_base/daw/fl_studio/recording_and_audio_editing_workflow.md` — general audio recording and take-archiving mechanics this workflow builds on
- `knowledge_base/daw/fl_studio/mixing_bus_routing_and_gain_staging_workflow.md` — gain-staging conventions for routing the finished reamped signal into the mix
- `knowledge_base/daw/fl_studio/bass_di_and_amp_blend_workflow.md` — the same DI-first flexibility principle applied to bass, with the added option of blending DI and amp signals rather than choosing one
