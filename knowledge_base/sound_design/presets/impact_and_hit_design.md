---
title: "Impact and Hit Design"
synthesis_method:
  - "Layered synthesis/sampling"
  - "Subtractive"
  - "Sample-based"
tags:
  - "impact"
  - "hit"
  - "braam"
  - "cinematic"
  - "transition-fx"
  - "sound-design"
  - "trailer-music"
---

# Impact and Hit Design

An impact (or "hit") is a large, one-shot transient event — typically landing on a drop, a downbeat, or a dramatic structural pivot — built to feel bigger and more physically forceful than any single acoustic or synthesized source could produce alone. Unlike a kick drum (a rhythmic, repeating element; see `knowledge_base/sound_design/presets/kick_drum_design.md`), an impact is a one-time or rarely-repeated event whose entire job is maximum perceived scale at one specific moment.

## Building the Sound

An impact is almost always a layered composite, following the same "combine specialized layers" logic as `knowledge_base/sound_design/presets/layered_kick_and_bass_construction.md`'s kick recipe, but scaled up and pitched for cinematic/trailer rather than rhythmic use:

1. **Sub layer**: a pitched-down sine sweep or a heavily lowpassed boom (often built the same way as a kick's sub layer — a fast pitch-envelope sweep from higher down to 30-50 Hz) for the felt low-end thud. Tuning this to the track's root note keeps the impact harmonically consistent with the surrounding score/track rather than clashing.
2. **Body/tonal layer — the "braam"**: a sustained, detuned brass and/or synth cluster hit — several brass (sampled or synth-brass) notes or synth oscillators stacked a semitone or more apart and held — gives the impact a dense, dissonant, unmistakably "cinematic trailer" harmonic core. `knowledge_base/genres/cinematic/epic_music.md` names this exact technique directly.
3. **Transient/noise layer**: a short burst of white noise, a cymbal crash, glass-smash, metal-scrape, or distorted orchestral hit sample for the initial "crack" that gives the impact its perceived sharpness and attack definition, layered at the very front of the hit.
4. **Reverb/tail layer**: a long, often huge convolution or algorithmic reverb send on the composite hit (or on the transient layer specifically) extends the sense of scale well past the initial transient — many impacts are perceived as much through their tail as their attack.
5. **Distortion/saturation**: driving the combined layers (or the body layer specifically) through saturation or clipping thickens the harmonic content and helps the impact read as powerful rather than merely loud.

## Genre Grounding

- `knowledge_base/genres/cinematic/epic_music.md` documents "the 'braaam' — a sustained, detuned brass/synth hit, the genre's signature sound-design element," explicitly layered with "massive hits, stingers, whooshes, and impacts... for scale beyond acoustic capability," alongside "heavy reverb and convolution for a huge, cinematic sense of space."
- `knowledge_base/genres/cinematic/superhero_score.md` documents "hybrid orchestral-electronic sound design blend[ing] processed synths and sub-bass layers with acoustic orchestra, often blurring the line between score and sound effects on impact-driven action cues," with "aggressive filtering and layering on processed percussion and synth-bass hits" to maximize impact.
- `knowledge_base/genres/cinematic/film_score.md` documents "hybrid orchestral-electronic synthesis (risers, braams, sub-bass drops)" as now-standard modern scoring tools, often synced precisely to picture timing.
- `knowledge_base/genres/cinematic/trailer_music.md` documents "heavy, distorted synthesizer subs (808s, Reeses) layered beneath orchestral cellos and contrabasses" — the sub-layer-under-acoustic-body technique applied specifically to trailer-music impact design.
- `knowledge_base/genres/edm/edm_trap.md` documents "layering sampled orchestral hits with synthesized risers/impacts for a hybrid cinematic-electronic drop sound," confirming the same technique crossing into festival EDM trap drops, alongside sampled orchestral hits and choir stabs for cinematic drama.
- `knowledge_base/genres/electronic/aggrotech.md` documents "noise risers and impact effects borrowed directly from hardcore/trance production" as a standard build-to-drop sound-design layer.

## Common Mistakes

**Skipping the sub layer and relying only on a bright transient.** Without a genuine low-frequency component, an impact reads as sharp but small — the felt physical weight comes specifically from the sub layer, the same principle documented for kicks in `kick_drum_design.md`.

**Building the "braam"/body layer as a single clean chord rather than a detuned, dissonant cluster.** A consonant chord reads as musical content, not an impact; the deliberate near-semitone detuning between voices is what gives the braam its characteristic unsettling scale.

## Cross-References

- `knowledge_base/sound_design/presets/kick_drum_design.md`, `knowledge_base/sound_design/presets/layered_kick_and_bass_construction.md` — the layered-construction principle (sub, body, transient, distortion) this entry scales up to a one-shot cinematic hit.
- `knowledge_base/sound_design/presets/riser_and_uplifter_design.md` — the buildup sound source an impact typically resolves.
- `knowledge_base/genres/cinematic/epic_music.md`, `knowledge_base/genres/cinematic/superhero_score.md`, `knowledge_base/genres/cinematic/film_score.md`, `knowledge_base/genres/cinematic/trailer_music.md`, `knowledge_base/genres/edm/edm_trap.md`, `knowledge_base/genres/electronic/aggrotech.md` — genre sources grounding this entry.
