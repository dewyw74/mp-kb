---
title: "Pad Design — Archetypes and Patch Recipes"
synthesis_method:
  - "Subtractive"
  - "Wavetable"
  - "Granular"
tags:
  - "pad"
  - "atmosphere"
  - "evolving-texture"
  - "preset-recipe"
  - "trance"
  - "house"
  - "ambient"
  - "liquid-dnb"
---

# Pad Design — Archetypes and Patch Recipes

`knowledge_base/sound_design/presets/pad_and_atmosphere_design.md` covers pads at the level of structural/compositional role (breakdown-featured element, sidechain-ducked groove support, granular atmosphere, barely-audible glue). This entry is the concrete counterpart, matching the archetype-and-patch-recipe format of `knowledge_base/sound_design/presets/edm_bass_design.md` and `knowledge_base/sound_design/presets/supersaw_lead_design.md`: oscillator setup, filter/modulation behavior, and effects chain for each documented pad type. Genre files consulted: `progressive_trance.md`, `melodic_house.md`, `deep_house.md`, `tech_trance.md`, `space_ambient.md`, `darkwave.md`, `liquid_dnb.md`, `tropical_house.md`, `2_step.md`.

A recurring principle across every archetype below: **pad movement lives in slow filter sweeps, detuned unison width, or wavetable position scanning — never in fast modulation.** The entire point of a pad is sustained, non-distracting harmonic presence; any modulation source fast enough to read as rhythmic (rather than atmospheric) pulls a pad out of its supporting role and into competing with the track's actual lead/hook material.

## 1. Filtered Breakdown Pad (Progressive Trance, Tech Trance)

Grounded in `progressive_trance.md` and `tech_trance.md`. This is the pad that IS the breakdown — per `progressive_trance.md`, breakdowns favor "filtered pads, subtle plucks, and short arpeggiated motifs rather than wide supersaw leads," with "timbral evolution (filter sweeps, unison width changes)" substituting for melodic development entirely.

**Synthesis method:** Wavetable/hybrid (Serum, Massive) named directly in `progressive_trance.md` for evolving pad textures, or granular/resampled textures as an alternative also named in the same file.

**Oscillators:**
- A single wavetable or a modest 2-3 voice detuned stack — deliberately narrower than a supersaw lead's 7-voice unison, since the pad needs to sit beneath, not compete with, the breakdown's melodic elements.
- Wavetable position set to a warm, rounded frame rather than an aggressive/bright one.

**Filter/movement:**
- Slow, wide-range lowpass filter sweep (many bars per full sweep, not a build-length sweep) is the primary source of movement — `progressive_trance.md` explicitly names "filter sweeps, unison width changes" as substituting for melodic development.
- Unison detune width itself can be slowly automated alongside the filter sweep for a second, independent axis of evolution.

**Effects:** Long, genre-scale-matched reverb per `knowledge_base/mixing/reverb/reverb_types_and_selection.md`; `tech_trance.md`'s breakdowns are described as "atmospheric and sparse," so keep the pad as close to the only harmonic element present as the arrangement allows.

## 2. Lush Evolving Pad (Melodic House/Techno)

Grounded in `melodic_house.md`, which names "lush evolving pads" and "detuned unison stacks for wide, lush pad textures" as part of the genre's "melodic and harmonic core" alongside emotive leads and arpeggiated sequences.

**Synthesis method:** Wavetable synthesis, named directly in `melodic_house.md` for evolving pad textures.

**Oscillators:**
- Detuned unison stack, wider than the progressive-trance breakdown pad above — `melodic_house.md` specifically calls out width as the goal ("wide, lush pad textures"), so unison voice count and detune amount should be pushed further than a subtler breakdown-support pad would need.

**Filter/movement:** Slow filter and wavetable-position evolution, same underlying mechanism as the progressive trance archetype, but intended to be a more prominent, foregrounded element per `knowledge_base/sound_design/presets/pad_and_atmosphere_design.md`'s "featured element" role rather than a glue/background role.

**Effects:** Generous reverb and stereo width; melodic house pads are meant to be immersive rather than merely supportive.

## 3. Sidechain-Ducked Warm Pad (Deep House, Tropical House, 2-Step)

Grounded in `deep_house.md`'s "warm pad or Rhodes chord" intro material and "slow LFO filter sweeps for evolving pad movement," `tropical_house.md`'s "warm pad synths... used for chord support," and `2_step.md`'s "warm pads and simple, understated stabs" kept deliberately sparse.

**Synthesis method:** Subtractive — these genres consistently favor a rounder, less aggressively wavetable-modulated character than the trance/melodic-house archetypes above.

**Oscillators:** Simple saw or triangle waves, minimal unison — the goal is warmth and harmonic support, not textural spectacle. `2_step.md`'s explicit guidance that "synths generally play a supporting role, kept sparse" applies directly here.

**Filter/movement:** Slow LFO-driven lowpass sweep per `deep_house.md`, gentle enough to read as ambient warmth rather than an audible effect. Because these pads sit under a kick-driven groove, they should be designed to survive sidechain ducking (per `knowledge_base/sound_design/presets/pad_and_atmosphere_design.md`'s sidechain-survival guidance) — enough sustained body that rhythmic gain reduction reads as a smooth pump rather than a choppy on/off.

**Effects:** Moderate reverb, kept controlled enough that the pad doesn't wash into the vocal/lead space these genres prioritize.

## 4. Granular Ambient/Space Pad (Space Ambient, Darkwave)

Grounded in `space_ambient.md`'s "detuned saw stacks for lush pad width" alongside "sine subs for foundation" and "supersaw/unison stacks for epic scale," and `darkwave.md`'s "slow-moving lowpass filter sweeps for evolving pad textures" with "gentle resonance for warmth rather than aggression."

**Synthesis method:** Granular, per the general technique documented in `knowledge_base/sound_design/synthesis/granular_synthesis.md` and the pad-specific application in `knowledge_base/sound_design/presets/pad_and_atmosphere_design.md`.

**Source/oscillators:** A short sampled or synthesized source, frozen and slowly scanned rather than played as a conventional sustained note — this is what produces genuinely non-repeating evolution rather than a looping wavetable/unison pad's more periodic movement.

**Filter/movement:** Very slow lowpass sweeps (`darkwave.md`), with resonance kept gentle rather than aggressive — the goal is atmosphere, not an audible filter-sweep effect.

**Effects:** Heavy, long reverb is essentially load-bearing for this archetype rather than optional polish.

## 5. Extended-Chord Warm Pad (Liquid Drum & Bass)

Grounded in `liquid_dnb.md`: "Rich, jazz- and soul-derived extended chords (7ths, 9ths, 11ths) voiced on Rhodes-style keys or warm pads carry genuine harmonic movement across the track."

**Synthesis method:** Subtractive or electric-piano-emulation hybrid — the emphasis here is harmonic content (extended chord voicings per `knowledge_base/music_theory/chords/extended_jazz_chords.md`) rather than textural/timbral movement.

**Oscillators:** Warm, rounded waveforms voiced as full extended chords rather than a single sustained note — this pad's job is to "carry genuine harmonic movement," meaning the chord changes themselves (not filter/unison automation) are the primary source of interest.

**Filter/movement:** Restrained — since the harmonic content is doing the expressive work, aggressive filter sweeping would compete with, rather than support, the chord voicings.

**Effects:** Warm, moderate reverb consistent with the genre's "emotional warmth and musicality" priority over rhythmic aggression.

## Common Mistakes

**Using a wide, actively-modulating pad where a genre calls for restraint.** The deep house/tropical house/2-step archetype above and the melodic house archetype use the same underlying tools (subtractive/wavetable oscillators, filter movement) but need very different intensity — matching amount of modulation to the genre's actual priority (support vs. spectacle) matters as much as the technique itself.

**Applying fast modulation to a pad, blurring the line between pad and lead/rhythmic element.** Per this entry's governing principle, a pad's modulation should stay slow enough to read as atmospheric evolution, not rhythmic movement — fast LFO rates belong to bass/lead wobble techniques (`knowledge_base/sound_design/presets/edm_bass_design.md`), not pads.

**Skipping the chord-voicing work on a genre (liquid DnB) where the pad's harmonic content, not its timbral movement, is the actual point.** A liquid DnB pad built with trance-style filter/unison focus and thin harmonic content misses what `liquid_dnb.md` actually calls out as the pad's job.

## Cross-References

- `knowledge_base/sound_design/presets/pad_and_atmosphere_design.md` — the structural/compositional-role counterpart to this entry's concrete synthesis recipes
- `knowledge_base/sound_design/presets/edm_bass_design.md`, `knowledge_base/sound_design/presets/supersaw_lead_design.md` — the equivalent archetype-and-recipe entries for bass and lead design
- `knowledge_base/sound_design/synthesis/granular_synthesis.md` — the technique underlying the granular ambient/space pad archetype
- `knowledge_base/music_theory/chords/extended_jazz_chords.md` — the chord-voicing knowledge relevant to the liquid DnB extended-chord pad archetype
- `knowledge_base/vst_database/xfer_serum.md`, `knowledge_base/vst_database/xfer_serum_2.md` — named tools for the wavetable-based pad archetypes above
