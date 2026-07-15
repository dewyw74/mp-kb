---
plugin_name: "Little AlterBoy"
developer: "Soundtoys"
category: "vocal processing"
type: "real-time pitch and formant shifter with hard-tune and vocoder-style modes"
cpu_usage: "low"
best_genres:
  - trap
  - hyperpop
  - future_bass
  - cloud_rap
  - dubstep
strengths:
  - "Independent Pitch and Formant controls let a voice be re-pitched without changing its perceived gender/register, or formant-shifted to change apparent gender/character without altering the sung pitch, which a combined pitch-shift tool can't separate."
  - "Hard Tune mode snaps the input to the nearest semitone in real time for the audibly artificial, robotic-tuned vocal character that's a genre signature in trap and hyperpop production, distinct from transparent corrective pitch correction."
  - "Robot/vocoder mode with MIDI note control turns the plugin into a melodic vocoder, letting an external MIDI track drive the vocal's pitch for classic vocoder-style hooks and ad-libs."
  - "Includes a built-in tube saturation stage adapted from Decapitator (`soundtoys_decapitator.md`), adding harmonic warmth/edge to the processed vocal without a separate saturation plugin."
weaknesses:
  - "As a real-time, semitone-snapping pitch tool it doesn't offer the note-by-note graphical editing of a dedicated pitch-correction/melodyne-style tool — it's built for live, playable character effects rather than surgical, after-the-fact tuning correction."
  - "Its formant-shift range is tuned for the classic Soundtoys 'robot/character voice' use case rather than the transparent, natural-sounding gender-adjacent formant correction some vocal production tasks call for."
alternatives:
  - "Soundtoys PhaseMistress (`soundtoys_phasemistress.md`) — for movement/modulation character rather than pitch/formant character"
  - "A dedicated pitch-correction plugin (Melodyne-style, per `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md`'s transparent-correction category) for subtle, note-accurate tuning fixes"
  - "A DAW's stock vocoder device for straightforward robotic/vocoder textures without Little AlterBoy's formant-shift flexibility"
recommended_settings:
  - "Trap/hyperpop hard-tuned hook: Hard Tune mode engaged, fast retune speed, pitch set to the target key/scale, per the stylized-pitch-correction philosophy in `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md`."
  - "Gender-bent character vocal: Formant shifted several steps down (for a lower, more masculine timbre) or up (for a higher, more feminine timbre) with Pitch left near zero, so the sung notes stay the same but the vocal's apparent register changes."
  - "Robotic ad-lib/vocoder hook: Robot mode engaged with MIDI note input driving pitch, moderate saturation for grit, used as a foregrounded textural element rather than a lead vocal treatment."
common_uses:
  - "Audibly artificial, hard-tuned vocal hooks and ad-libs as a deliberate genre-signature effect"
  - "Gender/character-bending formant shifting independent of the vocal's actual sung pitch"
  - "MIDI-controlled robotic/vocoder vocal textures"
tags: ["soundtoys", "little-alterboy", "pitch-shift", "formant", "vocal-processing", "hard-tune"]
---

# Little AlterBoy

Little AlterBoy (Soundtoys) is a real-time vocal pitch and formant-shifting plugin offering independent control over a voice's sung pitch and its formant (perceived gender/character) content, plus a Hard Tune mode for the audibly artificial, semitone-snapped vocal effect widely used in trap, hyperpop, and adjacent genres, and a Robot/vocoder mode with MIDI note control for melodic vocoder textures. Unlike a corrective pitch-correction tool built to sound invisible, Little AlterBoy is explicitly a character/effects processor — its value is in producing audible, intentional vocal transformation rather than transparent tuning fixes.

## Sound Character and Strengths

Little AlterBoy's core strength is separating Pitch and Formant into independent controls, letting a producer re-pitch a vocal without shifting its apparent gender/register, or shift formants to change the voice's apparent character while leaving the sung melody untouched — a distinction directly relevant to `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md`'s framing of pitch correction as either a transparent, invisible tool or a deliberately audible, stylized one. Hard Tune mode sits firmly in the stylized category: fast semitone-snapping produces the deliberately robotic, artificial pitch-snap sound documented as a genre-identifying signature in trap, hyperpop, and cloud rap. Robot mode extends this further into full vocoder territory, with MIDI note input letting an external track drive the vocal's melodic content in real time.

## Weaknesses

Because it's a real-time, playable effect rather than a graphical, note-by-note editor, Little AlterBoy isn't a substitute for a dedicated pitch-correction tool when the goal is subtle, transparent, after-the-fact tuning correction — its Hard Tune mode is built to sound audible and artificial by design, not invisible. Its formant range is tuned for the classic robotic/character-voice use case rather than the more conservative formant nudges used for natural-sounding gender-adjacent correction in other production contexts.

## Common Mistakes

Using Little AlterBoy's Hard Tune mode when the actual goal is transparent pitch correction — per `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md`, transparent and stylized pitch correction are different production decisions with different tools; Little AlterBoy is built for the stylized, audibly-processed end of that spectrum, and reaching for it to quietly fix a slightly flat note will produce an audibly artificial result where a subtler tool wouldn't.

## Cross-References

- `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` — the transparent-vs-stylized pitch correction framework Little AlterBoy's Hard Tune and Robot modes sit on the stylized end of
- `knowledge_base/vst_database/soundtoys_decapitator.md` — the saturation unit Little AlterBoy's built-in tube saturation stage is adapted from
- `knowledge_base/vst_database/soundtoys_phasemistress.md` — a related Soundtoys character-effects plugin, covering modulation/movement rather than pitch/formant
