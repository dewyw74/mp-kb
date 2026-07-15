---
plugin_name: "PhaseMistress"
developer: "Soundtoys"
category: "modulation"
type: "analog-modeled phaser (2 to 24 stages, multiple LFO and rhythmic modulation modes)"
cpu_usage: "low"
best_genres:
  - psychedelic_rock
  - funk
  - synth_punk
  - post_punk_revival
  - alternative_metal
strengths:
  - "69 style presets reconfigure the phaser's internal stage structure, modeled after a range of classic hardware phasers (Bi-Phase, Small Stone, Phase 90, Moogerfooger 12-Stage, and others), rather than offering one fixed circuit topology."
  - "Stage count is adjustable from a subtle 2-stage sweep up to an extreme 24-stage phase-shifting effect, covering a far wider intensity range than most hardware-modeled phaser plugins."
  - "Multiple modulation modes beyond a standard LFO — Random and Step modes for jumping, non-swept phase shifts, Rhythm mode for programmed rhythmic patterns, and Envelope mode, which ties the phasing to the input signal's dynamics for a rhythm-triggered effect on funky drums, slap bass, or rhythm guitar."
  - "Seven built-in saturation flavors (clean through shred and pump) let the phased signal pick up additional analog-style harmonic character without a separate saturation plugin."
weaknesses:
  - "As a dedicated phaser, it doesn't cover chorus or flanger character on its own the way a combined modulation-effects plugin might — a separate chorus or flanger tool is needed for those distinct textures."
  - "The deep stage-count and style-preset system, while powerful, is more parameters than a simple rate/depth/mix phaser offers, and can invite over-tweaking on a source that just needs a light, classic sweep."
alternatives:
  - "Ableton Auto Filter (stock) — for filter-sweep movement rather than true phase-shifting character"
  - "A DAW's stock chorus or flanger device for adjacent but tonally distinct modulation effects"
  - "Soundtoys Little AlterBoy (`soundtoys_little_alterboy.md`) — a different Soundtoys character-effects plugin for pitch/formant rather than phase movement"
recommended_settings:
  - "Classic psychedelic guitar sweep: a Small Stone- or Phase 90-style preset, 4-6 stages, moderate rate, standard LFO mode, per the movement-for-interest technique in `knowledge_base/sound_design/effects/flanger_and_phaser_for_movement.md`."
  - "Funk rhythm-guitar/bass pumping phase: Envelope mode engaged so the phase sweep tracks pick attack and decay, moderate stage count, light saturation (crunch or dirt flavor) for added bite."
  - "Extreme psych/alt-metal texture: 16-24 stages, Random or Step mode for jumping rather than swept phase shifts, higher resonance/intensity for a jet-flanger-adjacent, deliberately disorienting effect."
common_uses:
  - "Classic swept-phaser movement on guitars, keys, and synths across psychedelic and funk-adjacent genres"
  - "Rhythm-triggered, envelope-following phase modulation locked to the input signal's dynamics"
  - "Extreme, high-stage-count phase effects as a foregrounded psychedelic or alternative-genre texture"
tags: ["soundtoys", "phasemistress", "phaser", "modulation", "analog-modeled"]
---

# PhaseMistress

PhaseMistress (Soundtoys) is an analog-modeled phaser plugin offering 69 style presets that reconfigure its internal phase-shifting structure to emulate a range of classic hardware phasers, with stage counts adjustable from a subtle 2-stage sweep to an extreme 24-stage effect. It's a second, clearly distinct Soundtoys product from the saturation-focused Decapitator (`knowledge_base/vst_database/soundtoys_decapitator.md`) — where Decapitator adds harmonic density and grit, PhaseMistress adds swept, comb-filter-based movement, covering the modulation side of a mix chain rather than the saturation side.

## Sound Character and Strengths

PhaseMistress's style-preset system is built around emulating specific, well-known hardware phasers rather than offering one generic phase-shift circuit, giving it a range of distinct sweep characters from smooth and subtle to harsh and resonant. Its modulation-mode selection goes well beyond a standard LFO sweep: Envelope mode ties the phase movement to the input signal's own dynamics, directly implementing the rhythm-triggered modulation approach documented in `knowledge_base/sound_design/effects/flanger_and_phaser_for_movement.md`, while Random and Step modes replace a smooth sweep with jumping, unpredictable phase shifts for a more aggressive or glitchy character. Its adjustable stage count (2 to 24) is unusually wide-ranging, letting one plugin cover both a classic, restrained psychedelic-rock sweep and an extreme, disorienting modulation effect.

## Weaknesses

PhaseMistress is a dedicated phaser and doesn't provide the distinct chorus or flanger textures that a broader modulation-effects plugin might bundle alongside phasing — per `knowledge_base/sound_design/effects/modulation_effects_chorus_flanger_phaser.md`'s distinction between these related but tonally different modulation effects, a separate tool is still needed for chorus or flanger character specifically. Its depth of controls (style, stage count, resonance, color, intensity, modulation mode) is more than a simple sweep effect requires, and can encourage excessive tweaking on sources that would benefit from a quick, classic setting.

## Common Mistakes

Defaulting to a smooth LFO sweep for every application regardless of source material — per `knowledge_base/sound_design/effects/flanger_and_phaser_for_movement.md`, phaser modulation is most effective when its mode matches the material's character (a steady LFO sweep for sustained pads and guitars, an envelope-following or rhythmic mode for percussive, dynamic sources like funk guitar or bass) rather than applying one modulation approach universally.

## Cross-References

- `knowledge_base/sound_design/effects/flanger_and_phaser_for_movement.md` — the general phaser/flanger movement technique PhaseMistress's mode system directly implements
- `knowledge_base/sound_design/effects/modulation_effects_chorus_flanger_phaser.md` — the broader modulation-effects category distinguishing phasing from chorus and flanger
- `knowledge_base/vst_database/soundtoys_decapitator.md` — a related Soundtoys mix-stage plugin covering saturation/density rather than modulation
- `knowledge_base/vst_database/soundtoys_little_alterboy.md` — a related Soundtoys character-effects plugin for pitch/formant rather than phase movement
