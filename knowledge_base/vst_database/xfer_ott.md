---
plugin_name: "OTT"
developer: "Xfer Records"
category: "compressor"
type: "free multiband upward/downward compressor"
cpu_usage: "low"
best_genres:
  - dubstep
  - brostep
  - riddim
  - drum_and_bass
  - trap
  - future_bass
strengths:
  - "Free plugin (originally a port of a well-known Ableton Live device preset chain), making it universally accessible regardless of budget."
  - "Combines upward and downward compression across three bands simultaneously, producing a very dense, consistently loud, 'glued' texture with one plugin instance."
  - "Depth control lets its aggressive default character be dialed back for subtler use, rather than being an all-or-nothing effect."
  - "Extremely fast to apply — minimal parameters (Depth, Time, and per-band Up/Down amount) compared to a full manual multiband compressor setup."
weaknesses:
  - "Easy to overuse — OTT's signature dense, pumping, upward-and-downward-compressed sound is instantly recognizable and can make a mix sound processed/generic if applied at full strength on everything."
  - "Less transparent and precise than a dedicated multiband compressor like FabFilter Pro-MB; it's an aesthetic tool as much as a corrective one."
alternatives:
  - "FabFilter Pro-MB (more transparent, more controllable multiband compression)"
  - "Waves Kramer Master Tape (for a different flavor of density/character)"
recommended_settings:
  - "Dubstep/riddim bass density: Depth 50-70%, default Time setting, applied on the bass/growl bus before final gain staging — a very common bass-processing chain step in the genre."
  - "Master bus glue (subtle use): Depth 10-20% only, to add cohesion without the full 'OTT sound' becoming audible."
common_uses:
  - "Bass and growl density/glue processing in dubstep and riddim"
  - "Drum bus glue and energy in drum and bass and trap"
  - "Subtle master-bus cohesion when used at low Depth settings"
tags: ["ott", "xfer", "multiband-compression", "dubstep", "glue", "free-plugin"]
---

# OTT

OTT (Xfer Records) is a free multiband compressor that applies both upward and downward compression across three frequency bands simultaneously, producing a distinctively dense, "glued," consistently energetic sound with very few parameters to manage. It originated as a port of a preset chain built from Ableton Live's stock multiband dynamics devices, and its combination of accessibility (free) and an instantly recognizable, aggressive default character made it one of the most widely used bass-processing tools in modern bass music.

## Sound Character and Strengths

OTT's core trick — compressing both upward (raising quiet parts) and downward (lowering loud parts) across three independent bands — produces a texture that's louder and more consistently dense than single-band compression can achieve without sounding obviously squashed, which is exactly the character dubstep and riddim bass/growl processing chains want. Its Depth control is what keeps it usable beyond its signature extreme setting: at low Depth it functions as a genuinely useful glue compressor, while at high Depth it becomes the recognizable "OTT sound."

## Weaknesses

That recognizable sound is a double-edged sword — OTT at or near full strength is audible enough that overusing it (especially on a master bus) can make a mix sound generically over-processed rather than genre-appropriately dense. It's also less surgically controllable than a dedicated multiband compressor with fully adjustable crossover points, attack/release per band, and ratio per band — OTT trades that control for speed and a strong default character.

## Common Mistakes

Applying OTT at or near full Depth on a master bus by default, rather than reserving high-Depth settings for the specific bass/growl elements the technique was built for, and using low Depth (or a more transparent multiband compressor) for overall mix-bus glue.

## Cross-References

- `knowledge_base/mixing/compression/parallel_compression.md` — related dense-compression philosophy, though OTT achieves its density through multiband upward/downward compression rather than a parallel blend
- `knowledge_base/genres/edm/dubstep.md`, `knowledge_base/genres/edm/riddim.md` — genre files where OTT-style bass density processing is a standard chain step
- `knowledge_base/vst_database/fabfilter_pro_c_2.md` — a more surgical single-band alternative for cases needing precise control rather than OTT's fast, characterful default
