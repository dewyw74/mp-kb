---
workflow_name: "Studio One Mixing Automation and Native Channel Strip"
daw: "studio_one"
category: "automation"
goal: "Automate a mix using Studio One's Read/Touch/Latch/Write automation modes and shape tone and dynamics on any Console channel using the native Channel Strip (low-cut filter, three-band EQ, dynamics) available before any plugin is inserted."
steps:
  - "Enable automation for a parameter beyond the default volume fader and pan by right-clicking it and choosing Show Automation, or by adding an Automation Track for it."
  - "Set the automation mode per track (Off, Read, Touch, Latch, Write) based on how that parameter should be captured during the current pass."
  - "Use Read mode for normal playback of existing automation without recording new changes — this is Studio One's default 'play the automation back' state."
  - "Use Touch mode when riding a fader or control live with a touch-sensitive controller, since Touch only writes while the control is actively held and reverts to Read on release."
  - "Use Latch mode when a move should keep writing at its last value after release, useful for filter sweeps or level rides that should hold rather than snap back."
  - "Use Write mode only for a deliberate full overwrite pass, since Write continuously records the current control position regardless of whether it's being touched."
  - "Draw or edit automation curves directly in the Arrange view's automation lanes for moves that don't need to be performed live."
  - "Open the native Channel Strip on any Console channel to shape low end (low-cut filter), tone (three-band parametric EQ), and dynamics (compressor/expander) before reaching for a third-party plugin."
  - "Use the Channel Strip's dynamics section — compression (threshold/ratio linked to one knob) and expansion — for fast gain-control decisions, reserving a dedicated compressor plugin for more specific character or multiband needs."
  - "Automate Channel Strip parameters (EQ gain, compression amount) the same way as any other mixer parameter, using Touch or Latch for musical, performed moves."
related_plugins:
  - "Studio One Channel Strip"
  - "PreSonus Fat Channel XT"
  - "Studio One Automation Track"
  - "Studio One Console Shaper / CTC-1 Pro Console Shaper (Mix Engine FX)"
tags:
  - "studio_one"
  - "automation"
  - "channel-strip"
  - "mixing"
  - "dynamics"
  - "eq"
  - "console"
---

# Studio One Mixing Automation and Native Channel Strip

Two Studio One mixing characteristics are worth understanding together: its four-mode automation system (Read, Touch, Latch, Write, plus Off), which controls how any automatable parameter gets captured and played back, and its native Channel Strip — a built-in low-cut filter, three-band parametric EQ, and dynamics processor available directly on every Console channel before a single plugin is inserted. Both are core, current Studio One features rather than bundled third-party add-ons.

## Automation modes

Automation in Studio One applies to any parameter on a track, instrument, or insert, but by default only the volume fader and pan of each channel strip are automation-enabled — other parameters need to be explicitly shown as automation lanes before they can be written to. Once enabled, each track's automation mode governs how moves are captured:

- **Off** — automation is disabled for that parameter.
- **Read** — existing automation plays back; this is the mode a track returns to automatically once a pass finishes.
- **Touch** — writes only while a control is actively touched (best with a touch-sensitive hardware controller), reverting to Read the instant it's released.
- **Latch** — writes from the moment a control is touched and keeps writing its last value even after release, until manually stopped.
- **Write** — continuously overwrites automation from the current control position for the whole pass, regardless of touch state.

Touch and Latch are the two modes suited to performing a mix live — riding a vocal fader, sweeping a filter — while Write is reserved for a deliberate full repass, since it will silently overwrite anything in its path. Automation can also be drawn by hand directly onto a track's automation lane in the Arrange view, which is the more common approach for precise, non-performed moves like a hard-timed filter open on a drop.

## The native Channel Strip

Every Console channel in Studio One has access to a native Channel Strip combining three processors in one: a low-cut (high-pass) filter, a three-band parametric EQ (low, mid, high — each with adjustable gain and frequency), and a dynamics section offering both compression (a single knob linking threshold from 0 dB to -20 dB and ratio from 2:1 to 10:1) and expansion (linking threshold and ratio similarly on the downward side). This is distinct from PreSonus's separately available Fat Channel XT, which is a fuller virtual recreation of the StudioLive hardware channel strip with switchable compressor and EQ models (clean/hi-fi, vintage tube opto, vintage FET) and a limiter stage — Fat Channel XT is a more elaborate, purchasable plugin, while the native Channel Strip's simpler EQ/dynamics combination is built into the channel itself.

Having usable EQ and dynamics available on every channel without opening the plugin browser changes early-mix workflow: quick tonal or dynamic decisions (tightening low end, taming a harsh band, controlling peaks) can happen immediately during tracking or a rough mix pass, with a dedicated third-party EQ or compressor reserved for parts that need more specific character, saturation, or multiband control.

## Automating Channel Strip and Mix Engine FX parameters

Channel Strip parameters automate exactly like any other mixer control — enable the parameter's automation lane, choose Touch or Latch for a performed move, or draw the curve by hand. This makes it straightforward to automate, for example, a Channel Strip low-cut sweep on a build, or a compression-amount increase into a chorus, without needing a separate automatable plugin. The same applies to Mix Engine FX like Console Shaper when loaded on a bus or Main — their parameters sit in the automation system the same way.

## Common mistakes

Assuming every mixer parameter is automation-ready by default is a common mistake — only volume and pan are enabled out of the box, and other parameters need their automation lane shown first. Leaving a track in Write mode after a pass is another frequent error, since a subsequent adjustment (even an accidental mouse bump) will silently overwrite existing automation instead of just reading it back. On the Channel Strip side, the mistake is skipping straight to a third-party EQ/compressor out of habit without checking whether the native Channel Strip's low-cut, three-band EQ, and simple compressor/expander pair already solve the problem — for many quick corrective moves it does, at no extra CPU or insert-slot cost.

## Cross-references

- `knowledge_base/daw/workflow/automation_curve_shape_and_musicality.md` — cross-DAW guidance on automation curve shape that applies directly to drawn Studio One automation lanes
- `knowledge_base/mixing/` — general dynamics and EQ decision-making that the Channel Strip's compressor/expander and three-band EQ execute inside Studio One
