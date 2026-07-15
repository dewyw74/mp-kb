---
plugin_name: "Pigments"
developer: "Arturia"
category: "synth"
type: "hybrid wavetable/granular/virtual-analog synth"
cpu_usage: "medium"
best_genres:
  - colour_bass
  - space_ambient
  - dubstep
  - ambient
  - melodic_techno
strengths:
  - "Six synthesis engines (virtual analog, wavetable, granular, sample, harmonic, and physically-inspired modal) available two at a time in a single patch, letting one oscillator supply a clean detuned saw while the other granulates a sample or morphs a wavetable underneath it."
  - "Granular engine turns any imported sample into a pad or texture source, directly serving the vowel/formant 'talking' bass-lead hybrid patches documented for colour bass and the evolving arpeggio/drone work documented for Berlin-School-style ambient."
  - "Color-coded, drag-and-drop modulation interface keeps a genuinely deep modulation matrix approachable, avoiding the steep learning curve of an equivalently deep modular synth."
  - "Low-to-medium CPU cost relative to its synthesis depth, making two-engine patches practical in sessions with several other synth instances running."
weaknesses:
  - "Running two full synthesis engines simultaneously (e.g., granular plus wavetable) costs meaningfully more CPU than a single-engine patch, and the granular engine in particular can spike usage with large imported samples or high grain density."
  - "The sheer number of engine combinations makes it easy to end up with an unfocused patch that uses complexity for its own sake rather than serving a specific sonic goal — the same discipline problem any six-engine hybrid synth invites."
alternatives:
  - "Spectrasonics Omnisphere (see `spectrasonics_omnisphere.md` — deeper sample library, heavier CPU load)"
  - "u-he Zebra2 (see `u-he_zebra2.md` — modular routing depth over Pigments' curated multi-engine approach)"
  - "Xfer Serum 2 (see `xfer_serum_2.md` — wavetable-first alternative without granular/modal engines)"
recommended_settings:
  - "Colour bass vowel/talking lead: wavetable engine on oscillator 1 with a formant-shaped table, granular engine on oscillator 2 processing a short vocal or vowel sample, blended and run through a resonant filter with envelope modulation on cutoff for the 'talking' movement."
  - "Berlin-School evolving arpeggio: virtual analog engine for the core oscillator tone, slow LFO-modulated wavetable position on a second engine layer, sequenced through Pigments' built-in arpeggiator or an external step sequencer per `space_ambient.md`'s modular-sequencer technique."
common_uses:
  - "Hybrid vowel/formant bass-lead patches in colour bass and dubstep"
  - "Evolving granular pad and drone textures for ambient and space ambient production"
  - "General-purpose wavetable and virtual-analog sound design where a single synth needs to cover multiple synthesis approaches without switching plugins"
tags: ["arturia", "pigments", "synth", "wavetable", "granular", "hybrid-synth"]
---

# Pigments

Pigments (Arturia) is a hybrid software synthesizer offering six distinct synthesis engines — virtual analog, wavetable, granular, sample-based, harmonic, and a physically-inspired modal engine — with any two runnable simultaneously in a single patch. Where most synths commit to one synthesis paradigm (Serum to wavetable, Diva to virtual analog), Pigments' core idea is letting a producer freely combine two of those paradigms in the same patch, then blend and modulate between them with a color-coded, drag-and-drop modulation system.

## Sound Character and Strengths

Pigments' two-engine-at-once architecture is what `knowledge_base/genres/edm/colour_bass.md` cites it for specifically: the genre's signature vowel/formant "talking" bass-lead hybrid patches benefit from pairing a wavetable engine's formant-shaped tables with the granular engine's ability to process a short vocal or vowel sample, producing a hybrid timbre neither engine alone would reach as directly. `knowledge_base/genres/electronic/space_ambient.md` cites Pigments (alongside Arturia's CS-80 V) for authentic Berlin-School-style evolving arpeggios, where its granular and wavetable engines generate the slowly shifting, generative-feeling textures the genre's modular-sequencer aesthetic calls for. The interface itself is a real strength: a six-engine synth could easily become unmanageable, but Pigments' adaptive, color-coded modulation matrix and reactive Play View keep patch-building fast even at real depth.

## Weaknesses

Running two full engines in parallel — especially granular alongside anything else — costs noticeably more CPU than a single-engine wavetable or virtual-analog patch, and large imported samples in the granular engine can spike usage further. The breadth of engine combinations also invites a specific failure mode: stacking engines because the option exists rather than because the patch needs it, producing a busier, less focused sound than a simpler single-engine approach would.

## Common Mistakes

Defaulting to a two-engine patch for a sound that a single engine would handle just as well — per the general synthesis-selection discipline documented across `knowledge_base/sound_design/synthesis/`, added synthesis complexity should be driven by a specific timbral need (like colour bass's vowel-formant hybrid) rather than used reflexively just because the plugin makes it easy.

## Cross-References

- `knowledge_base/genres/edm/colour_bass.md` — cites Pigments for wavetable/granular vowel-formant bass-lead hybrid design
- `knowledge_base/genres/electronic/space_ambient.md` — cites Arturia's Pigments/CS-80 V for Berlin-School-style evolving arpeggios
- `knowledge_base/sound_design/synthesis/granular_synthesis.md` — the granular-engine technique Pigments implements alongside its other five synthesis modes
- `knowledge_base/vst_database/spectrasonics_omnisphere.md` — a heavier, sample-library-driven alternative for the same hybrid sample/synthesis role
