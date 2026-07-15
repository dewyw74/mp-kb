---
plugin_name: "Repro"
developer: "u-he"
category: "synth"
type: "component-modeled analog synth (Sequential Pro-One and Prophet-5 emulation)"
cpu_usage: "medium"
best_genres:
  - chillwave
  - synthwave
  - detroit_techno
  - deep_house
  - space_ambient
strengths:
  - "Component-level modeling of two distinct vintage Sequential Circuits synths in one product — Repro-1 (monophonic Pro-One) and Repro-5 (polyphonic Prophet-5) — rather than a single generic 'vintage analog' approximation."
  - "Three selectable oscillator models per voice (P1, P5, and u-he's own 'Ideal' oscillator), letting a patch choose exactly how much vintage circuit imperfection versus modern cleanliness it wants."
  - "Repro-5's per-voice polyphonic distortion (each voice processed independently, avoiding the intermodulation a single shared distortion stage would create across a chord) is a genuinely distinctive feature not commonly found in other Prophet-5 emulations."
  - "Built-in effects (Jaws wavefolder, Lyrebird delay, RESQ resonant EQ, Drench reverb, Sonic Conditioner saturator/transient designer) cover most of a vintage-pad or lead patch's processing chain without leaving the plugin."
weaknesses:
  - "Two distinct synth models bundled in one product (Repro-1 monophonic, Repro-5 polyphonic) means a producer reaching for 'Repro' needs to know upfront which specific vintage instrument's behavior — monophonic Pro-One or polyphonic Prophet-5 — the patch actually calls for."
  - "Component-level modeling carries a real CPU cost relative to a simpler virtual-analog synth; running many simultaneous Repro instances is heavier than an equivalent count of Sylenth1 or Spire instances."
alternatives:
  - "u-he Diva (see `u-he_diva.md` — broader multi-model analog emulation rather than two specific vintage instruments)"
  - "Arturia V Collection (see `arturia_v_collection.md` — includes its own Prophet-5-lineage and Pro-One-adjacent emulations alongside dozens of other vintage instruments)"
recommended_settings:
  - "Chillwave/synthwave warm pad: Repro-5 polyphonic mode, P5 oscillator model, slow attack, resonant lowpass filter cutoff swept gently by a slow LFO, light chorus and Drench reverb for width and vintage-tape-adjacent warmth."
  - "Detroit techno/deep house ensemble stab: Repro-5 with two detuned oscillators, moderate polyphonic distortion drive for texture, paired with tape saturation per the genre's documented layering of vintage-emulation plugins with tape/cassette warmth."
common_uses:
  - "Vintage analog pad and warm chord layers for chillwave, synthwave, and downtempo electronic production"
  - "Authentic Prophet-5/Pro-One lead and bass tones where component-level modeling accuracy matters more than a generic 'analog-style' patch"
  - "String-machine/ensemble-adjacent warmth layered with tape saturation for detroit techno and deep house texture work"
tags: ["u-he", "repro", "repro-1", "repro-5", "synth", "analog-modeled", "prophet-5"]
---

# Repro

Repro (u-he) is a component-level analog emulation of two distinct vintage Sequential Circuits synthesizers sold as one product: Repro-1, a faithful model of the monophonic Pro-One, and Repro-5, a polyphonic model of the Prophet-5. Rather than approximating "vintage analog character" generically, u-he modeled each instrument's actual circuit behavior — including, in Repro-5, a distortion stage applied per-voice rather than to the summed polyphonic signal, avoiding the note-to-note intermodulation a single shared distortion stage would introduce across a chord.

## Sound Character and Strengths

`knowledge_base/genres/electronic/chillwave.md` cites u-he Repro directly (alongside Arturia's V Collection) for combining vintage synth emulation with tape/cassette emulation to build the genre's authentically warm pad and chord sound — this is the space Repro-5's polyphonic, component-modeled character was built for. Its three oscillator model options (P1, P5, and the "Ideal" u-he oscillator) give a patch designer direct control over how much of the original hardware's imperfection to retain versus a cleaner modern rendering, which matters for genres like detroit techno and deep house where vintage-adjacent warmth is layered deliberately with modern tape saturation rather than left raw.

## Weaknesses

Because Repro-1 and Repro-5 model two functionally different instruments (monophonic vs. polyphonic, with different circuit lineages), the plugin requires knowing which specific vintage character a patch calls for rather than reaching for one generic "analog synth" preset category. The depth of component-level modeling also makes Repro meaningfully heavier on CPU than a lighter virtual-analog synth aimed at a similar sonic territory.

## Common Mistakes

Loading Repro-1 (monophonic Pro-One model) for a task that needs polyphonic chords, or vice versa — the two models aren't interchangeable presets within the same engine but distinct synthesis targets, and picking the wrong one means fighting the plugin's fundamental voice architecture rather than its sound.

## Cross-References

- `knowledge_base/genres/electronic/chillwave.md` — cites u-he Repro combined with Arturia V Collection and tape/cassette emulation for authentic vintage warmth
- `knowledge_base/vst_database/u-he_diva.md` — lists "u-he Repro" as an alternative within its own alternatives field, the two products' most natural in-house comparison
- `knowledge_base/vst_database/arturia_v_collection.md` — the broader vintage-instrument-collection alternative covering similar Prophet-lineage and analog-warmth territory
- `knowledge_base/mixing/saturation/tape_saturation.md` — the tape-warmth processing genre files pair with Repro's vintage-modeled oscillators
