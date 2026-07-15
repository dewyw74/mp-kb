---
title: "Unison and Detune Stacking"
synthesis_method: "unison-detune"
tags:
  - "unison"
  - "detune"
  - "supersaw"
  - "voice-stacking"
  - "trance-lead"
  - "chorus-effect"
  - "stereo-width"
---

## What Unison and Detune Stacking Is

Unison stacking runs multiple copies of the same oscillator per voice — typically anywhere from 2 to 16+ — with each copy's pitch detuned slightly away from the others (a few cents up or down) and, usually, panned across the stereo field. The detuning means each copy's waveform drifts in and out of phase with the others continuously rather than reinforcing identically, producing a natural, ever-shifting chorus-like beating and a much denser, wider harmonic spectrum than a single oscillator can produce alone. Panning the detuned copies across the stereo image turns that phase drift into audible stereo movement, giving the classic "wide" synth-lead and pad sound associated with trance, EDM, and dance-pop lead/pad patches.

The technique's best-known implementation is the **supersaw**, popularized by Roland's JP-8000 (1996) and its JP-8080 successor, which generated seven detuned sawtooth oscillators from a single "Super Saw" waveform slot specifically to deliver a massive, immediately usable trance-lead sound without manual multi-oscillator patching. "Supersaw" has since become the generic term for any dense unison-detuned sawtooth stack, whether produced by a dedicated single-oscillator supersaw algorithm or by manually stacking multiple detuned oscillators in a subtractive or wavetable synth.

## Voice Count and Detune Amount Tradeoffs

- **Voice count**: more unison voices produce a denser, smoother chorus effect and a louder perceived stack (before gain compensation), but each additional voice costs CPU linearly and, past a certain point, adds diminishing width returns while increasing masking risk against other elements in a mix — 7-voice unison (the JP-8000's original count) remains a widely used reference point precisely because it's dense enough to sound massive without becoming an unmanageable, muddy blob.
- **Detune amount**: a small detune spread (a few cents) produces a subtle chorus-like thickening that stays close to in-tune; a wide detune spread produces audible beating, dissonant shimmer, and — pushed far enough — a genuinely out-of-tune, unstable character. Detune amount and voice count interact: a wide detune spread across many voices gets muddy and indistinct fast, while a narrow spread across many voices can sound thin despite the high voice count, because the copies stay too close together to build real spectral density. Most supersaw-style patches use a moderate detune spread with 5-7+ voices as the balance point between density and clarity.
- **Stereo spread**: panning the detuned voices across the stereo field (rather than summing them to mono) is what turns the beating into perceived width; a mono-summed unison stack still thickens the tone but loses the immersive stereo-field effect that defines the trance/EDM "wall of synth" sound.

## Where Unison and Detune Stacking Appears in the Genre Corpus

This is one of the most heavily documented sound-design techniques in the entire genre corpus, especially across EDM's trance and hard-dance lineage and dance-oriented pop:

- **Trance and hard dance** — `knowledge_base/genres/edm/trance.md` documents "Virtual analog subtractive (Roland JP-8000/8080-style supersaw)" as a core synth type; `knowledge_base/genres/edm/uplifting_trance.md` and `knowledge_base/genres/edm/vocal_trance.md` both specify "Virtual analog supersaw (Roland JP-8000/8080-style...)" for instrumental hooks and choruses; `knowledge_base/genres/edm/uk_hardcore.md` and `knowledge_base/genres/edm/happy_hardcore.md` both document "Virtual-analog supersaw/square leads (hard-trance lineage)"; `knowledge_base/genres/edm/hard_trance.md` documents "Virtual analog subtractive (Roland JP-8000/8080, Access Virus)" and, in its production notes, "Recreating classic hoover synths in modern wavetable/virtual-analog synths ... using detuned PWM oscillators."
- **Pop and dance-pop** — `knowledge_base/genres/pop/dance_pop.md` documents "Supersaw/unison stacks for pads and leads" directly among its synth types, noting "supersaw/unison stacks deliver wide, bright pads and leads." `knowledge_base/genres/pop/scandipop.md` documents "Supersaw or detuned saw stacks for wide, euphoric chorus synths," contrasted against "Simple sine/triangle for restrained verse bass and pads" — using unison density itself as a structural, section-to-section arrangement device (sparse verse, dense unison chorus).
- **Breaks and IDM-adjacent electronic** — `knowledge_base/genres/electronic/nu_skool_breaks.md` documents "heavy use of supersaw-style unison stacks in the more trance/progressive-influenced strand," and `knowledge_base/genres/electronic/idm.md` documents "detuned/microtonal oscillator stacks" among its oscillator types, applying the same unison-detune mechanism toward unease and microtonal texture rather than trance-style euphoria.
- **Contrast case — psytrance** — `knowledge_base/genres/edm/psytrance.md` explicitly documents choosing *against* the supersaw palette: leads "favor exotic, psychedelic timbres (metallic FM tones, heavily modulated wavetables) over clean supersaw sounds," a useful genre-level signal that unison/detune stacking is a deliberate stylistic choice (associated with trance's warmer, euphoric character) rather than a universal EDM default — psytrance reaches for FM (see `fm_synthesis.md`) specifically to avoid the supersaw sound.
- **Aggressive/metallic variants** — `knowledge_base/electronic/aggrotech.md` documents "Detuned supersaw stacks" alongside sawtooth bass and FM operator stacks for metallic stabs, and `knowledge_base/genres/electronic/deconstructed_club.md` documents "Detuned/microtonal stacks for unease" — showing the same voice-stacking mechanism repurposed for tension and aggression rather than euphoric width when the detune spread is pushed wider and the harmonic content left less "polished."

## Practical Unison/Detune Sound Design

- **Start with the JP-8000 reference point**: 7 voices, moderate detune, full stereo spread, as a known-good starting configuration before adjusting for density vs. clarity tradeoffs specific to the mix.
- **Gain-compensate as voice count changes**: adding unison voices raises the stack's summed level; most synths auto-compensate, but verify gain staging manually when comparing patches with different voice counts.
- **Automate detune amount for arrangement contrast**: `scandipop.md`'s verse/chorus contrast (narrow detune verse pads vs. wide supersaw chorus) is a directly reusable arrangement technique — automate the detune spread parameter itself as a section-to-section build device, not just filter cutoff.
- **Watch low end**: heavy unison detuning on bass-register parts can smear the fundamental and cause phase cancellation issues in mono playback (club systems, phone speakers); many productions keep the sub/bass fundamental as a single clean oscillator and reserve unison stacking for mid/high register leads and pads.

## Cross-References

- `knowledge_base/genres/edm/trance.md`, `knowledge_base/genres/edm/uplifting_trance.md`, `knowledge_base/genres/edm/vocal_trance.md`, `knowledge_base/genres/edm/hard_trance.md` — JP-8000/8080-style supersaw as the genre-defining lead sound.
- `knowledge_base/genres/pop/dance_pop.md`, `knowledge_base/genres/pop/scandipop.md` — supersaw/unison stacking as core pad and chorus-lead sound design.
- `knowledge_base/genres/edm/psytrance.md` — deliberate avoidance of supersaw in favor of FM, illustrating unison/detune as a stylistic choice rather than a default.
- `knowledge_base/genres/electronic/idm.md`, `knowledge_base/genres/electronic/deconstructed_club.md`, `knowledge_base/genres/electronic/aggrotech.md` — the same technique repurposed for unease/aggression via wider detune spreads.
- `knowledge_base/sound_design/synthesis/subtractive_synthesis.md` — the oscillator/filter architecture unison stacking is most commonly layered onto.
- `knowledge_base/sound_design/synthesis/oscillator_sync.md` — a related but mechanically distinct analog lead-thickening/movement technique often found in the same trance/hard-dance lead patches.
