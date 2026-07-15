---
plugin_name: "EchoBoy"
developer: "Soundtoys"
category: "delay"
type: "analog-modeled echo/delay processor emulating vintage tape, tube, and solid-state echo units"
cpu_usage: "medium"
best_genres:
  - dub_techno
  - shoegaze
  - boom_bap
  - psychedelic_rock
  - dream_pop
strengths:
  - "30 built-in echo styles model specific vintage hardware (tape echoes, bucket-brigade analog delays, early digital units), giving each repeat a distinct saturation, wow/flutter, and filtering character rather than one generic clean delay."
  - "Four echo modes (Single, Dual, Ping-Pong, Rhythm) cover everything from a simple mono slapback to a 16-tap rhythmic delay pattern within one plugin."
  - "Groove, Feel, and Accent controls let repeats rush or drag against the beat and take on swing, which a purely tempo-synced digital delay can't reproduce."
  - "Adjustable saturation and a feedback-path EQ mean the repeats degrade musically as feedback builds, mimicking the way tape and analog echo units lose top end and gain grit over successive repeats."
weaknesses:
  - "Its emulated saturation and modulation stages make it heavier on CPU than a simple digital delay, which matters when instantiating many instances across a busy session."
  - "The vintage-modeled coloration on every style is a poor fit when a mix genuinely needs a clean, transparent, unaffected digital delay repeat — a simpler delay is the better tool there."
  - "The depth of the Style menu and rhythm/groove controls has a steeper learning curve than a basic time/feedback/mix delay."
alternatives:
  - "Valhalla Delay (`valhalla_delay.md`) — cleaner mode-based delay design with a stronger diffusion/reverb-blend feature set, less focused on vintage hardware emulation specifically"
  - "Ableton Reverb and Echo (stock, simpler delay engine)"
  - "A DAW's stock ping-pong or tape delay device for lighter-weight, less characterful repeats"
recommended_settings:
  - "Dub-style chord echo: Single or Dual mode, a tape-style echo style, high feedback with the feedback-path EQ rolled off in the highs and lows so repeats darken and narrow with each pass, synced to a slow subdivision."
  - "Boom-bap/psychedelic slapback: Single mode, short delay time (80-120ms), low feedback (1-2 repeats), light saturation for warmth without an audible rhythmic echo."
  - "Shoegaze/dream pop wash: Rhythm or Ping-Pong mode, moderate-to-high feedback, wide stereo spread, blended with a long reverb send per the layered delay-into-reverb technique in `knowledge_base/mixing/delay/delay_as_width_and_depth_tool.md`."
common_uses:
  - "Vintage-character rhythmic and atmospheric delay on guitars, vocals, chords, and percussion"
  - "Dub-lineage chord/echo texture as a genre-defining production element"
  - "Tempo-synced multi-tap and ping-pong delay patterns with groove/swing applied to the repeats"
tags: ["soundtoys", "echoboy", "delay", "echo", "analog-modeled", "tape-delay"]
---

# EchoBoy

EchoBoy (Soundtoys) is an analog-modeled echo and delay plugin built around 30 style presets, each emulating a specific piece of vintage echo hardware — tape units, bucket-brigade analog delays, and early digital echo boxes — rather than offering one clean, generic repeat. It ships with four operating modes (Single, Dual, Ping-Pong, and Rhythm), the last of which functions like a tape echo with up to 16 selectable read heads for complex, evolving rhythmic patterns. It is widely regarded as an industry-standard delay specifically because it treats the delay's saturation, modulation, and feedback-path tone as central creative parameters rather than side effects of a clean digital repeat.

## Sound Character and Strengths

EchoBoy's Style menu is its defining feature: selecting a vintage-modeled echo character changes not just the tone of each repeat but how the repeats degrade and saturate as feedback accumulates, closely matching the tape/analog echo behavior documented in `knowledge_base/mixing/delay/delay_feedback_and_self_oscillation.md`. Its Groove, Feel, and Accent controls push it beyond a purely tempo-synced digital delay — repeats can rush or drag against the grid and pick up swing, which is directly useful for the rhythmic delay-throw techniques covered in `knowledge_base/mixing/delay/delay_throws_and_automation.md`. The feedback-path EQ lets repeats progressively darken and narrow, a key part of the dub-lineage delay texture that genres like dub techno build entire arrangements around.

## Weaknesses

The saturation and modulation modeling that give EchoBoy its character also make it more CPU-intensive than a simple digital delay, and its vintage coloration works against a mix that specifically wants a transparent, uncolored repeat. The Style menu and rhythm/groove system are deep enough that dialing in a specific, intentional character takes longer than adjusting a basic time/feedback/mix delay.

## Common Mistakes

Reaching for a single default Style regardless of the source material — per `knowledge_base/mixing/delay/delay_types_and_sync.md`'s point that delay character should be chosen deliberately to match the genre and element, EchoBoy's whole value is in matching a specific vintage echo character to the task (a bright, clean early-digital style for a synth pluck versus a dark, saturated tape style for a dub chord) rather than leaving the Style knob untouched.

## Cross-References

- `knowledge_base/mixing/delay/delay_feedback_and_self_oscillation.md` — the feedback/saturation behavior EchoBoy's Style-modeled circuits directly implement
- `knowledge_base/mixing/delay/delay_throws_and_automation.md` — the rhythmic delay-throw technique EchoBoy's Groove/Feel/Accent controls are built for
- `knowledge_base/mixing/delay/delay_as_width_and_depth_tool.md` — general delay-for-width philosophy relevant to EchoBoy's Ping-Pong and Dual modes
- `knowledge_base/vst_database/valhalla_delay.md` — a cleaner, mode-based alternative delay from a different developer, less centered on vintage hardware emulation
