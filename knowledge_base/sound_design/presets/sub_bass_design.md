---
title: "Sub-Bass Design: The Clean Fundamental"
synthesis_method:
  - "Subtractive"
  - "Sine synthesis"
tags:
  - "sub-bass"
  - "low-end"
  - "mono-compatibility"
  - "sound-design"
  - "foundational-technique"
---

# Sub-Bass Design: The Clean Fundamental

Sub-bass is the clean, undistorted, mono low-frequency fundamental (roughly 20-80 Hz) that provides a track's felt physical low end, independent of whatever modulated, distorted, or harmonically rich mid-bass character sits above it. `knowledge_base/sound_design/presets/edm_bass_design.md` documents this as a recurring principle across nearly every EDM bass archetype ("layer a clean sine sub beneath the modulated/distorted mid-bass character") but treats it as a supporting layer within larger archetype recipes; this entry is the dedicated, genre-spanning technique reference for designing that sub layer itself, applicable well beyond EDM.

## Building the Sub

1. **Waveform**: a pure sine wave is the standard choice — it contains no harmonics to interact unpredictably with the rest of the mix, and it's the only waveform that reproduces cleanly through small speakers and subwoofers alike without introducing audible distortion at high levels. A triangle wave (a small amount of odd-harmonic content) is sometimes used as a slightly "grittier" alternative that retains more presence on small speakers.
2. **Tuning**: tune the sub to the track's root note (or the bass note of the current chord) and keep it monophonic/legato — sub frequencies below ~80 Hz are difficult to perceive as distinctly pitched by ear, so accuracy of tuning matters more for how the sub reinforces the rest of the harmonic content than for melodic clarity.
3. **Filtering**: a lowpass filter set low enough (100-150 Hz) to remove any oscillator content above the fundamental keeps the layer "pure" — this is a deliberate simplicity, not an underdeveloped patch. Per `knowledge_base/sound_design/presets/edm_bass_design.md`'s future-bass sub archetype, minimal filtering and minimal modulation is the correct design target for a layer whose entire job is low-end weight.
4. **Mono and centered**: sub content should always be summed to mono (or generated mono from the start) — any stereo width below roughly 100-150 Hz risks phase cancellation on mono-summed playback systems (club PAs, phone speakers, many streaming platforms' loudness normalization paths), which can make a track's low end disappear or thin out unpredictably.
5. **Small-speaker translation**: because true sub frequencies are inaudible on phones and laptop speakers, many modern sub patches add a light saturation stage or a parallel harmonic-exciter layer, generating audible harmonics an octave or more above the fundamental so the ear can infer the pitch and presence of the sub even on systems that can't reproduce it directly. This is the same principle behind the 808's "distorted for translation" design covered in `knowledge_base/sound_design/presets/trap_808_design.md`.

## Genre Grounding

- `knowledge_base/genres/r_and_b/contemporary_r_and_b.md` specifies "Sine and triangle for sub-bass" directly in its oscillator guidance, paired with FM synth bells and warm analog pads above it.
- `knowledge_base/genres/pop/dark_pop.md` documents "deep, often distorted 808 sub-bass" carrying "most of the low-end harmonic and rhythmic weight" of the track — an example of the saturation-for-translation technique applied as the genre's core low-end identity rather than a subtle addition.
- `knowledge_base/genres/world_music/dancehall.md` documents "massive, deep synthesizer sub-bass" where "the bassline is the most important melodic element in the track," despite the sub itself staying a clean, simple tone beneath the genre's bright DX7 plucks and stabs.
- `knowledge_base/genres/cinematic/trailer_music.md` documents "heavy, distorted synthesizer subs (808s, Reeses) layered beneath orchestral cellos and contrabasses," combining a synthesized sub with acoustic low-end reinforcement.
- `knowledge_base/genres/edm/jungle.md` is explicit about mono discipline: "Keep sub-bass mono and separate from mid-bass/Reese content so both translate on club soundsystems without phase cancellation," with sub and mid-bass layers frequently automated independently under the break.
- `knowledge_base/genres/world_music/zouk.md` specifies "Sine/triangle for sub-bass" beneath its lush analog pads and synth-brass stabs, confirming the clean-sub-under-characterful-mid principle outside EDM entirely.

## Common Mistakes

**Adding filter or amplitude modulation to the sub layer "for interest."** Per the future-bass sub archetype in `edm_bass_design.md`, the sub's job is stability, not movement — modulation belongs on the mid-bass or lead layer above it, not the fundamental itself.

**Leaving the sub un-tuned to the track's key when a distinct mid-bass or 808 layer is present.** An untuned sub can beat dissonantly against a tuned mid-bass layer even when both are nominally "in the same range," since the ear perceives the interaction between close-but-not-identical low frequencies as audible roughness.

## Cross-References

- `knowledge_base/sound_design/presets/edm_bass_design.md` — the archetype-and-recipe survey this entry's dedicated sub-layer technique supports across nearly every bass archetype documented there.
- `knowledge_base/sound_design/presets/trap_808_design.md` — the 808-specific hybrid sub/kick design that extends this entry's translation-saturation technique.
- `knowledge_base/genres/r_and_b/contemporary_r_and_b.md`, `knowledge_base/genres/pop/dark_pop.md`, `knowledge_base/genres/world_music/dancehall.md`, `knowledge_base/genres/cinematic/trailer_music.md`, `knowledge_base/genres/edm/jungle.md`, `knowledge_base/genres/world_music/zouk.md` — genre sources grounding this entry.
