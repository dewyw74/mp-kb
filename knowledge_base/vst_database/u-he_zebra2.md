---
plugin_name: "Zebra2"
developer: "u-he"
category: "synth"
type: "modular subtractive/additive synth"
cpu_usage: "low"
best_genres:
  - glitch
  - space_rock
  - idm
  - ambient
  - experimental
strengths:
  - "Wireless modular architecture — modules only appear on the patching grid when actually added, keeping a genuinely deep modular synth's workspace uncluttered compared to a traditional patch-cable modular interface."
  - "Combines subtractive and additive/spectral synthesis in one engine: freehand or spline-drawn waveforms, spectral effects, and morphing between waves go well beyond a conventional wavetable oscillator's fixed table set."
  - "Built-in granular oscillator mode (cited alongside dedicated granular tools like Output Portal for live-performance glitch and texture work) lets Zebra2 function as a granular instrument without a separate plugin."
  - "Exceptionally low CPU usage for its depth, making multiple simultaneous instances practical even in a modulation-heavy, many-layer sound-design session — a genuine rarity among synths this flexible."
weaknesses:
  - "The modular, patch-it-yourself architecture has a real learning curve compared to a fixed-signal-flow synth like Diva or Sylenth1 — building a patch from scratch requires understanding routing and module choice, not just adjusting a handful of labeled knobs."
  - "Its four XY macro pads (each controllable up to 64 parameters) are powerful but require deliberate setup to be useful in performance; an unconfigured patch doesn't expose that expressive control by default."
alternatives:
  - "Spectrasonics Omnisphere (see `spectrasonics_omnisphere.md` — deeper sample library, less patching-focused workflow)"
  - "Arturia Pigments (see `arturia_pigments.md` — comparable multi-engine breadth with a more guided, less fully modular interface)"
  - "Native Instruments Reaktor (community-built modular ensembles for even deeper custom patching)"
recommended_settings:
  - "Glitch/granular live-performance texture: granular oscillator module feeding the modulation matrix from an XY pad, live-input or sample-based grain source, filter and spectral-effect modules chained after for real-time manipulation."
  - "Space rock/sci-fi drone: additive/spectral oscillator with slow spline-morphed waveform shape, long attack/release envelope, resonant filter sweep automated across the section for an evolving, otherworldly texture."
common_uses:
  - "Granular and glitch-oriented live-performance instruments for glitch and IDM production"
  - "Evolving sci-fi/drone textures for space rock and ambient scoring"
  - "Deep custom modular patch design where a fixed-architecture synth's signal flow is too limiting"
tags: ["u-he", "zebra2", "synth", "modular", "granular", "glitch"]
---

# Zebra2

Zebra2 (u-he) is a "wireless" modular synthesizer combining subtractive and additive/spectral synthesis in a single engine, where modules only appear on the patching interface once they've actually been added to a patch — avoiding the visual clutter of a traditional patch-cable modular rig while retaining genuine modular flexibility. It includes a granular oscillator mode alongside its four conventional wavetable oscillators (16 waves each with integrated spectral effects) and a dedicated FM oscillator module closely related to the Yamaha DX7's architecture.

## Sound Character and Strengths

`knowledge_base/genres/electronic/glitch.md` cites Zebra's granular mode directly, alongside the dedicated granular plugin Output Portal, as a live-performance glitch instrument — its ability to function as both a granular synthesizer and a full modular subtractive/additive engine in one low-CPU plugin is what earns it that citation over a narrower single-purpose granular tool. `knowledge_base/genres/rock/space_rock.md` cites Zebra alongside VCV Rack for evolving, sci-fi-adjacent drone textures beyond what vintage hardware modular synths could achieve, and it appears in `knowledge_base/vst_database/spectrasonics_omnisphere.md`'s own alternatives list as the comparable modular-depth option for hybrid sample/synthesis work. Its wireless modular UI is arguably its single biggest practical advantage: genuine patch-cable-level flexibility without a patch-cable interface's visual overhead, and CPU usage stays low even as patch complexity grows.

## Weaknesses

Zebra2's modular architecture is a double-edged strength — building a patch means choosing and routing modules rather than adjusting a fixed panel of labeled controls, which is a meaningfully steeper learning curve than most subtractive or wavetable synths aimed at similar territory. Its four XY performance pads, each capable of controlling many parameters at once, need deliberate configuration to become useful; they don't do anything meaningful in an unpatched, default state.

## Common Mistakes

Approaching Zebra2 like a conventional fixed-architecture synth and only ever loading factory presets, rather than using its actual modular strength — per its citation in `glitch.md` and `space_rock.md`, its value in this knowledge base is specifically for granular/glitch performance instruments and evolving spectral textures that a fixed-signal-flow synth can't produce as directly.

## Cross-References

- `knowledge_base/genres/electronic/glitch.md` — cites u-he Zebra's granular mode as a live-performance glitch instrument alongside Output Portal
- `knowledge_base/genres/rock/space_rock.md` — cites Zebra for evolving, sci-fi-adjacent drone textures via granular synthesis and modular routing
- `knowledge_base/sound_design/synthesis/granular_synthesis.md` — documents Zebra2's Zebralette granular oscillator mode as a hybrid patch-design tool
- `knowledge_base/vst_database/spectrasonics_omnisphere.md` — lists u-he Zebra as its own modular-depth alternative
