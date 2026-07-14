---
plugin_name: "Electric"
developer: "Ableton"
category: "synth"
type: "electric piano modeling instrument (stock Ableton Live, physical-modeled Rhodes/Wurlitzer-style tone)"
cpu_usage: "medium"
best_genres:
  - lo_fi_hip_hop
  - liquid_dnb
  - jazz_fusion
  - smooth_jazz
  - boom_bap
strengths:
  - "Physically-modeled (rather than sampled) electric piano tone, giving continuous, expressive control over tine/hammer character, dynamics response, and tremolo/vibrato that a static sample library can't match as smoothly."
  - "Directly supports the Rhodes-style warm keys documented across `knowledge_base/genres/edm/liquid_dnb.md`'s extended-chord pad guidance and jazz-derived hip-hop/lo-fi genre files, without needing a sampled electric piano library."
  - "Included with Ableton Live Suite, with native Rack/macro and automation integration."
  - "Lower CPU and disk footprint than a large sampled electric-piano library (e.g. a dedicated Kontakt Rhodes instrument), since it's synthesizing the tone rather than streaming samples."
weaknesses:
  - "A modeled electric piano, however well-designed, doesn't capture every nuance of a deeply multi-sampled, round-robin-rich commercial electric piano library the way `knowledge_base/vst_database/native_instruments_kontakt.md`'s sample-based approach can."
  - "Limited to electric-piano-family tones specifically — not a general-purpose keys instrument the way a broader synth or sampler would be."
alternatives:
  - "Native Instruments Kontakt (see `native_instruments_kontakt.md`) with a dedicated sampled Rhodes/Wurlitzer library, for maximum sampled realism"
  - "Ableton Analog (see `ableton_analog.md`) for a more synthetic, less specifically electric-piano-modeled warm keys tone"
recommended_settings:
  - "Lo-fi hip-hop chord loop: moderate tine/hammer hardness for a mellow attack, light tremolo, and a lowpass filter/bit-reduction pass afterward per `knowledge_base/sound_design/effects/vintage_media_emulation_vinyl_tape_and_lofi_texture.md` for the genre's characteristic muffled warmth."
  - "Liquid DnB extended-chord pad: fuller, brighter tine setting for clarity on extended (7th/9th/11th) chord voicings per `knowledge_base/music_theory/chords/extended_jazz_chords.md`, with a moderate reverb send for the genre's warm, musical character."
common_uses:
  - "Rhodes/Wurlitzer-style electric piano chord and comping parts across lo-fi hip-hop, jazz-influenced, and liquid drum and bass production"
  - "Warm keys pad/chord content as an alternative to a sampled piano library, with lower CPU/disk cost"
tags: ["electric", "ableton", "stock-device", "electric-piano", "rhodes", "physical-modeling"]
---

# Electric (Ableton Live)

Electric is Ableton Live's first-party electric piano modeling instrument, using physical modeling (rather than sample playback) to generate Rhodes/Wurlitzer-style electric piano tone. Because it's synthesizing the tine/hammer interaction and amplifier character in real time rather than streaming pre-recorded samples, it offers continuous, expressive control over that character — dynamics response, tine hardness, tremolo depth — that a static sample library can only approximate through discrete velocity layers.

## Sound Character and Strengths

Electric directly serves the warm, jazz-derived electric piano role documented across several genre files in this knowledge base — the Rhodes-style keys in `knowledge_base/genres/edm/liquid_dnb.md`'s extended-chord pad guidance, and the jazz-harmony-informed keys sound common across lo-fi hip-hop and boom-bap-adjacent production. Its physical-modeling approach keeps both CPU and disk footprint lower than a large multi-sampled commercial electric piano library, since there's no sample streaming involved, while still providing continuously variable tonal control rather than a fixed set of sampled velocity layers.

## Weaknesses

However well-modeled, Electric doesn't capture every nuance a deeply multi-sampled, round-robin-rich commercial library can (per the sampling-realism techniques in `knowledge_base/sound_design/sampling/one_shot_layering_and_round_robin_variation.md`) — a producer chasing the exact sampled character of a specific famous electric piano recording may still prefer a dedicated sampled library via Kontakt. It's also a narrowly scoped instrument, limited to electric-piano-family tones rather than serving as a general-purpose keys/pad instrument.

## Common Mistakes

**Reaching for a heavy sampled Kontakt electric piano library when Electric's modeled tone would serve the part just as well at lower CPU/disk cost.** For most warm-keys chord and comping parts documented across this knowledge base's genre files, Electric's modeled tone is fully sufficient.

## Cross-References

- `knowledge_base/genres/edm/liquid_dnb.md` — the extended-chord warm-pad role Electric directly serves
- `knowledge_base/music_theory/chords/extended_jazz_chords.md` — the extended chord-voicing knowledge relevant to programming Electric parts
- `knowledge_base/sound_design/effects/vintage_media_emulation_vinyl_tape_and_lofi_texture.md` — the lo-fi processing commonly applied on top of an Electric part for lo-fi hip-hop character
- `knowledge_base/vst_database/native_instruments_kontakt.md` — the sampled-library alternative for maximum realism at higher CPU/disk cost
