---
workflow_name: "Ableton Guitar DI Recording and Reamping Workflow"
daw: "ableton"
category: "recording"
goal: "Record a clean, unprocessed DI guitar signal before any amp simulation is applied, preserving the flexibility to choose or change tone and amp later without re-tracking, then reamp that DI signal through an amp-sim plugin or a real amp via a hardware reamp box."
steps:
  - "Connect the guitar directly to an audio interface's high-impedance instrument input (or a passive DI box feeding a line input), bypassing any amp, pedal, or amp-sim plugin on the way in, so the recorded track is the guitar's raw signal."
  - "Record the DI signal to its own Arrangement track with no amp-sim or effect plugins active on the input path, confirming by ear that the recorded take sounds thin and unprocessed rather than already tone-shaped."
  - "Track a scratch or reference amp tone on a separate, muted or low-in-the-mix track (either monitoring through an amp-sim plugin or a real amp) so the performer has usable tone in their headphones while playing, without that tone being baked into the actual recorded track."
  - "Once tracking is complete, duplicate the DI track and insert an amp-sim plugin such as `knowledge_base/vst_database/neural_dsp_archetype.md` directly on the duplicate, auditioning several amp/cabinet combinations against the mix without needing to re-record the performance."
  - "For real-amp reamping, route the DI track's output to a spare analog output on the interface, connect that output to a hardware reamp box (e.g. a Radial-style reamp box) to convert the line-level, low-impedance signal back to an instrument-level, high-impedance signal the amp expects."
  - "Feed the reamp box's output into the real amp's instrument input, mic the amp's cabinet as normal, and record the mic'd signal to a new Arrangement track in sync with the original DI track."
  - "Match playback level between the DI signal being reamped and a normal guitar-level signal so the amp is driven the way it would be by a live instrument, adjusting the reamp box's output level or a pad/attenuator if the amp's front end is overdriven or underdriven."
  - "A/B the in-the-box amp-sim result against the real-amp reamp (when both are captured) or against genre reference tone, and keep whichever best matches the target genre's guitar sound per the relevant `knowledge_base/genres/rock/` or `knowledge_base/genres/metal/` entry."
  - "Comp and edit the reamped or amp-sim track using standard take management (per `knowledge_base/daw/ableton/multitrack_recording_and_take_comping_workflow.md`) if multiple amp/tone passes were captured for the same DI performance."
related_plugins:
  - "Ableton Audio In / Instrument Input"
  - "Ableton Track Freeze"
  - "Neural DSP Archetype"
tags:
  - "ableton"
  - "recording"
  - "guitar"
  - "di"
  - "reamping"
  - "amp-sim"
  - "tracking"
  - "flexibility"
---

# Ableton Guitar DI Recording and Reamping Workflow

Recording a guitar's clean DI (direct injection) signal before any amp simulation or real-amp tone is applied keeps every tone decision open after the performance is captured. This entry covers why DI-first tracking preserves that flexibility, and the two ways to apply amp tone afterward — reamping through an amp-sim plugin entirely in-the-box, or reamping through a real amp and cabinet using a hardware reamp box and the audio interface's spare outputs.

## Why DI-First Preserves Flexibility

A guitar performance recorded through a specific amp or amp-sim tone commits to that tone at the moment of tracking — if the mix later calls for a different amp character, more or less gain, or a different cabinet, the only options are re-tracking the part or living with a compromised tone. A DI recording sidesteps this entirely: the raw, unprocessed instrument signal is captured once, and every downstream tone decision (which amp, how much gain, which cabinet, whether to blend two amp tones) can be made or remade during mixing without asking the performer to replay the part. This matters most on parts that are difficult or impossible to exactly replicate — a specific take's phrasing, feel, or a one-off performance — where re-tracking to fix a tone decision risks losing something the original take had.

## Tracking the DI Signal

Connect the guitar directly to the audio interface's high-impedance instrument input, or through a passive DI box into a line input, with no amp, pedal, or amp-sim plugin in the recording path. The resulting track will sound noticeably thin and unprocessed on its own — this is expected and correct; a DI track is not meant to sound finished. Because playing through a completely dry, unprocessed signal is difficult for most performers to judge feel and dynamics against, track a scratch amp tone (a real amp or an amp-sim plugin used only for headphone monitoring) on a separate track, muted or excluded from the final mix, so the take is played with real amp feedback in the performer's ears while the actual recorded track stays clean.

## Reamping Through an Amp-Sim Plugin

The simpler and lower-cost path: duplicate the DI track and insert an amp-sim plugin directly on it, such as `knowledge_base/vst_database/neural_dsp_archetype.md`, whose Archetype line models a specific artist's full amp, cabinet, and effects chain. Because the underlying signal is still the original DI take, multiple amp-sim instances or presets can be auditioned side by side against the rest of the mix with no re-tracking, and the choice can be revisited at any later mixing session.

## Reamping Through a Real Amp

For a real-amp reamp, the DI track's output is routed to a spare analog output on the interface (not the main monitor output), which feeds a hardware reamp box. A reamp box exists because studio line-level, low-impedance signals are the wrong level and impedance for a guitar amp's instrument input — the box converts the DI signal back down to an instrument-level, high-impedance signal so the amp responds the way it would to a guitar plugged in directly. The reamp box's output feeds the amp's input as normal, the cabinet is mic'd as normal, and the mic'd result is recorded to a new track in sync with the original DI performance. Match the reamped signal's level to what a normally-played guitar would deliver to the amp — too hot or too quiet a signal drives the amp's front end differently than a live player would, changing the resulting tone.

## Common mistakes

Recording through an amp-sim or real amp with no clean DI safety track, which removes the ability to change tone later if the recorded tone turns out wrong for the mix. Forgetting to route a scratch monitoring tone to the performer, which makes tracking a genuinely dry signal difficult to play against. Feeding a DI signal directly into a real amp's input without a reamp box, which mismatches level and impedance and produces a thin, wrong-sounding result compared to true reamping. Driving a reamp box's output too hot or too quiet into the amp without checking against a normal guitar-level reference, which changes how hard the amp's preamp is driven and skews the resulting tone away from what the amp would normally deliver.
