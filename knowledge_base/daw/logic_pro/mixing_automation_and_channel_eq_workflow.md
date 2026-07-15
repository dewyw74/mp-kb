---
workflow_name: "Logic Pro Mixing Automation and Channel EQ Workflow"
daw: "logic_pro"
category: "automation"
goal: "Write and refine mix automation using Logic's Read/Touch/Latch/Write/Trim/Relative automation modes, and use the stock Channel EQ as the default corrective and tonal-shaping tool on individual channel strips and buses."
steps:
  - "Set a track's automation mode before recording any moves: Read to play back existing automation with no writing, Touch to write only while a control is actively held, Latch to keep writing after release until playback stops, Write to overwrite everything for the duration of playback, or Trim to offset existing automation by a relative amount."
  - "Use Touch mode for most manual fader and send moves, since it preserves everything already automated outside the moment a control is actually touched."
  - "Reserve Write mode for a genuine first pass on a track with no automation yet, since it silently overwrites any existing data for as long as playback runs."
  - "Use Trim (combined with Touch or Latch) to nudge an entire existing automation curve up or down without redrawing it from scratch."
  - "Use Relative automation for Volume, Pan, or Send levels when a secondary offset curve should ride on top of an existing primary curve rather than replacing it."
  - "Switch back to Read mode once a pass is finished so accidental control moves during later playback can't overwrite finished automation."
  - "Insert Channel EQ as the first tonal-shaping plug-in on a channel strip, after any input trim, for both corrective and creative frequency work."
  - "Use the highpass and lowpass filter bands to remove unneeded sub-rumble or air rather than doing that with a parametric bell band."
  - "Use the four parametric bands for surgical cuts (resonances, boxiness, harshness) and the shelving bands for broad tonal tilt, referencing the FFT analyzer overlay to see the current frequency content while adjusting."
  - "Automate Channel EQ band gain or frequency directly (via Touch/Latch) for moves that should evolve across a section, such as a gradual high-shelf lift into a chorus."
related_plugins:
  - "Logic Pro Channel EQ"
  - "Logic Pro Automation"
  - "Logic Pro Gain"
  - "FabFilter Pro-Q 3"
  - "Ableton EQ Eight"
tags:
  - "logic_pro"
  - "automation"
  - "channel-eq"
  - "mixing"
  - "touch-latch-write"
  - "trim-automation"
  - "eq"
---

# Logic Pro Mixing Automation and Channel EQ Workflow

Logic's automation system is mode-based rather than curve-drawn-by-default the way Ableton's clip envelopes are, and its default corrective EQ, Channel EQ, is a single flexible eight-band tool rather than a family of separate stock EQs. Both are the natural entry point for shaping a Logic mix: automation modes control how new moves interact with what's already written, and Channel EQ is where almost every channel strip's tonal work starts.

## Automation modes and what each one actually does

Each track's automation mode can be set independently, and the mode determines how a fader or knob move is captured relative to existing automation:

- **Read**: plays back existing automation; moving a control does not write anything.
- **Touch**: plays back existing automation like Read, but writes new values only while a control is actively held — on release, the control snaps back to following whatever was already automated.
- **Latch**: behaves like Touch while a control is held, but on release the new value keeps being written until playback stops, rather than reverting to the prior curve.
- **Write**: overwrites all existing automation for the parameter for the entire duration of playback, whether or not a control is actively touched — this is destructive to anything previously written on that parameter.
- **Trim**: offsets the existing automation curve up or down by the amount a control is moved, rather than replacing it outright; Trim works in combination with Touch or Latch.
- **Relative**: adds a secondary automation curve on top of an existing primary curve for Volume, Pan, or Send level, so the original curve's shape is preserved underneath an overriding offset.

Touch is the safest default for most manual mixing moves because it can't damage automation outside the exact window a control was held. Write should be treated as a deliberate, first-pass-only choice, since running it a second time over a track that already has finished automation will erase that work during playback.

## Building an automation pass

A typical pass starts in Touch mode for level and send moves during a listen-through, using Trim afterward to correct an entire section (a verse that reads a little quiet against the chorus) without redrawing every point in it. Relative automation is useful when an existing volume curve is good but an entire section still needs to sit a few dB under or over it — a Relative pass adds that offset without disturbing the underlying curve, which keeps the original work recoverable. This pairs with the philosophy in `knowledge_base/mixing/automation/automation_vs_static_balance.md` and `knowledge_base/daw/workflow/automation_curve_shape_and_musicality.md`: automation should read as a musical decision, not a technical patch, regardless of which DAW is drawing the curve.

## Channel EQ as the default mixing tool

Channel EQ is an eight-band parametric EQ present on every channel strip type: a highpass filter, a low shelving band, four fully parametric bell bands, a high shelving band, and a lowpass filter, each with an adjustable slope where relevant. Its built-in FFT analyzer overlays the channel's real-time frequency content on the EQ curve, which makes it useful for both corrective work (finding and cutting a specific resonance) and broader tonal shaping (a gentle high shelf for air, a low shelf pulled back for space in a busy low end).

Because Channel EQ ships on every strip at no extra CPU-license cost and covers both filtering and parametric duties in one plug-in, it is the natural first EQ insert on most channels and buses, with a dedicated third-party EQ like FabFilter Pro-Q 3 reserved for cases needing linear-phase processing, mid/side-specific bands, or a more visual dynamic-EQ workflow — see `knowledge_base/mixing/eq/subtractive_eq.md` and `knowledge_base/mixing/eq/boost_vs_cut_philosophy.md` for the underlying EQ decisions Channel EQ is used to execute.

## Common mistakes

Leaving a track in Write mode after a first automation pass and running playback again, which silently erases everything just written on that parameter. Using Latch when Touch was actually wanted, producing an automation curve that holds a value long after the intended move was meant to end. Reaching for a parametric bell band to remove sub-rumble instead of using Channel EQ's own highpass filter, which does the job with a cleaner slope and no extra resonance risk. Judging an EQ move purely from the FFT analyzer's visual curve instead of listening in context, which is the same soloed-vs-in-context trap covered in `knowledge_base/mixing/eq/soloed_vs_in_context_eqing.md`.
