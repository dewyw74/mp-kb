---
workflow_name: "FL Studio Pad and Velocity Curve Expressive Calibration Workflow"
daw: "fl_studio"
category: "midi"
goal: "Calibrate velocity response for a keyboard or pad controller in FL Studio for more natural, expressive playing, using the global MIDI Settings velocity curve, FPC's per-pad velocity curves, and Piano roll post-record velocity editing — FL Studio has no single unified velocity-calibration wizard, so this spans several real, separate tools."
steps:
  - "Identify which velocity problem is actually present before touching any setting: a controller that reads uniformly too hard or too soft across every key or pad (a global calibration problem), versus individual pads or notes that need different treatment (a per-instrument or per-note problem) — these are fixed in different places."
  - "For a globally miscalibrated controller, open Options > MIDI Settings (F10) and use the velocity curve control on the Input page to remap incoming velocity values before they reach any instrument."
  - "Keep in mind this MIDI Settings velocity curve applies globally to MIDI input rather than per individual connected device, so recalibrating it for one controller's feel can also affect the feel of any other controller connected at the same time."
  - "For pad-specific calibration during finger drumming, open FPC and adjust each pad's individual velocity curve — linear, logarithmic, or exponential — rather than relying only on the global MIDI Settings curve, since different pads or drum sounds often want different dynamic response."
  - "After recording, use the Piano roll's velocity level editor (the bar graph beneath the notes) to hand-correct individual note velocities that still read too uniform or too erratic even with a well-set hardware curve."
  - "Apply the Piano roll's Humanize tool sparingly for small, musically-plausible velocity and timing variation across a recorded part, rather than trying to fix a hardware calibration problem after the fact with humanization."
  - "Use the Randomize tool only when genuinely random, non-performance-plausible velocity variation is actually the goal, keeping it distinct from Humanize's more natural-feeling variation, per `knowledge_base/daw/fl_studio/groove_and_humanization_workflow.md`."
  - "Re-test a calibrated curve by playing the same phrase at a few clearly different intended dynamic levels — soft, medium, hard — and confirming the recorded velocities land in musically distinct, usable ranges rather than clustering near one extreme."
  - "Once a good curve is found for a specific controller, note or save it as the default starting point for that hardware, since recalibrating from scratch every session wastes time that a documented known-good setting avoids."
related_plugins:
  - "FL Studio MIDI Settings"
  - "FPC"
  - "FL Studio Piano Roll"
tags:
  - "fl-studio"
  - "velocity-curve"
  - "expressive-playing"
  - "calibration"
  - "midi"
  - "workflow"
---

# FL Studio Pad and Velocity Curve Expressive Calibration Workflow

FL Studio does not have one unified "velocity calibration" panel — the ability to shape how hard or soft a controller's dynamics feel is spread across three separate, real tools: a global velocity curve in MIDI Settings, per-pad velocity curves inside FPC, and post-record velocity editing in the Piano roll. Treating these as one combined toolkit, rather than expecting a single wizard to solve every velocity problem, is what actually gets a controller feeling natural and expressive.

## Where velocity calibration actually happens in FL Studio

Before adjusting anything, identify which layer of the problem is actually being solved. A keyboard or pad controller that reports notes uniformly too soft or too hard across its whole range points to a hardware-input calibration issue, fixed in MIDI Settings. A specific pad on a drum controller that feels wrong compared to its neighbors points to a per-pad issue, fixed in FPC. A recorded part that sounds too flat or too erratic even though the hardware itself feels fine points to a data-editing issue, fixed in the Piano roll. These three problems look similar from the keyboard but live in different places in FL Studio.

## Global input curve in MIDI Settings

Options > MIDI Settings (F10), on the Input page, exposes a velocity curve control that remaps incoming MIDI velocity values before they reach any instrument — useful for a controller whose own velocity feel is fixed and can't be adjusted in its own hardware or driver software. This setting is global: it applies to MIDI input generally rather than to one specific connected device individually, so it is the right tool when only one controller is connected, but a compromise when multiple controllers with different natural feels are connected at once, since recalibrating it to suit one will change the feel of the others too.

## Per-pad curves in FPC

For finger drumming and pad-based performance, FPC exposes its own per-pad velocity curve — linear, logarithmic, or exponential — set independently for each pad. This matters because a kick or snare pad and a hi-hat or cymbal pad often want different dynamic response: a kick might feel best with a curve that reaches full velocity quickly under moderate force, while a hi-hat might want a wider, more gradual curve for controlling openness and accent by touch. Calibrating pads individually in FPC, rather than relying solely on the global MIDI Settings curve, is what makes finger-drummed material feel controlled rather than either mushy or spiky.

## Post-record correction in the Piano roll

Even a well-calibrated controller produces recorded velocity data that sometimes needs hand correction — a passage that reads slightly flatter or more erratic than intended. The Piano roll's velocity level editor, the bar graph shown beneath the notes, allows direct per-note velocity adjustment after recording, without needing to re-record the part. This is the right tool for fixing specific notes or short passages rather than for solving a systemic hardware feel problem, which belongs upstream in MIDI Settings or FPC.

## Humanize vs. Randomize

Once the underlying velocity data is basically musical, the Piano roll's Humanize tool can add small, performance-plausible variation to keep a part from sounding perfectly even, per `knowledge_base/daw/fl_studio/groove_and_humanization_workflow.md`. The Randomize tool produces variation that is not trying to sound like a real performance, and is a different tool for a different goal — it should not be reached for as a fix when the actual problem is an uncalibrated velocity curve, since randomizing on top of bad calibration just produces erratic-sounding results in a different way.

## Testing and saving a known-good curve

After adjusting a curve, verify it by ear: play a short phrase at deliberately soft, medium, and hard dynamics, and confirm the recorded velocity values land in clearly separated, musically usable ranges rather than bunching near the top or bottom of the scale. Once a curve setting is confirmed to work well for a specific controller, keep a note of it (or, for FPC, save the calibrated kit as a preset) so it doesn't need to be rediscovered by trial and error at the start of every session.

## Common mistakes

Expecting a single global "velocity calibration" feature to exist and solve every dynamics problem, when FL Studio actually spreads this across MIDI Settings, FPC, and the Piano roll. Recalibrating the global MIDI Settings curve to fit one controller while forgetting it also affects every other connected MIDI device. Using Humanize or Randomize to paper over a genuinely miscalibrated hardware curve instead of fixing the curve itself. Never re-testing a calibrated curve across a full soft-to-hard dynamic range, so a curve that looks reasonable in the editor turns out to feel wrong under actual playing.
