---
title: "Supersaw, Pluck, and Lead Design — Archetypes and Patch Recipes"
synthesis_method:
  - "Subtractive"
  - "Wavetable"
  - "FM"
tags:
  - "lead"
  - "pluck"
  - "supersaw"
  - "arp"
  - "chord-stab"
  - "unison"
  - "detune"
  - "preset-recipe"
  - "trance"
  - "big-room-house"
  - "electro-house"
  - "melodic-techno"
  - "future-bass"
  - "psytrance"
---

# Supersaw, Pluck, and Lead Design — Archetypes and Patch Recipes

Leads and plucks are the melodic identity of most EDM subgenres, but — like bass (see `knowledge_base/sound_design/presets/edm_bass_design.md`) — "lead design" splits into distinct disciplines depending on genre. This entry covers five lead/pluck archetypes grounded in the genre knowledge base: the classic wide supersaw lead of trance, the anthemic riff-lead hybrid of electro house and big room house, melodic techno's subdued arpeggio/motif, future bass's pitch-bent chord-stab lead, and psytrance's acid-flavored lead sequence. Genre files consulted: `knowledge_base/genres/edm/trance.md`, `uplifting_trance.md`, `progressive_trance.md`, `electro_house.md`, `big_room_house.md`, `melodic_techno.md`, `future_bass.md`, `psytrance.md`.

For the underlying mechanics of unison/detune stacking and oscillator/filter fundamentals referenced throughout, see `knowledge_base/sound_design/synthesis/subtractive_synthesis.md` (Unison and Detune, Oscillator Waveforms) and `knowledge_base/sound_design/synthesis/wavetable_synthesis.md` (Unison and Spread for Wide EDM Sounds) — this entry applies those techniques rather than re-deriving them.

## 1. Classic Supersaw Lead (Trance, Uplifting Trance)

Grounded in `trance.md`, `uplifting_trance.md`, and `progressive_trance.md` as the contrasting understated variant. This is the JP-8000/8080-style stacked-sawtooth lead that defines trance's melodic identity — wide, bright, and built to carry an 8-16 bar melodic phrase at maximum emotional size.

**Synthesis method:** Subtractive/virtual-analog (the classic supersaw circuit) or wavetable emulation (Serum, Spire, Sylenth1) — see `subtractive_synthesis.md`'s Unison and Detune section for the general mechanism this patch scales up.

**Oscillators/unison/detune:**
- 7 detuned sawtooth voices per oscillator (the canonical "supersaw" count), unison detune pushed wide — moderate-to-maximum spread for the drop, per `trance.md`'s "detuned sawtooth stacks... for width."
- Uplifting trance refines this further: rather than one patch's built-in unison, `uplifting_trance.md` recommends stacking 2-3 separately-detuned supersaw *patches* (each with its own tuning/spread character) for finer control over width and tone than a single preset provides.
- Progressive trance's contrast: `progressive_trance.md` explicitly favors "narrower unison stacks than mainstream trance (subtler width)" — the same technique dialed back for its more restrained, textural lead role. Use this as the low-intensity setting of the same patch design.

**Filter/envelope:**
- Resonant lowpass, generally open or lightly filtered at the drop for brightness; swept closed-to-open as a build device.
- Amplitude envelope: fast attack, sustained through held notes, moderate release so overlapping legato phrases blend into the wide unison texture rather than clicking on/off.

**Modulation for movement:**
- Unison/detune width is itself an automation lane in uplifting trance — narrower in verse/build sections, opened to maximum width at the breakdown climax, per `uplifting_trance.md`'s "automating unison/detune width per-section... for a more dynamic sense of scale."
- Slow filter LFO on pad-layer counterparts for breakdown movement; the lead itself stays comparatively static in timbre once the unison is set, letting melodic content and width automation carry the movement.

**Effects chain:**
- Long plate/hall reverb (generous — `trance.md` calls this "the genre's expansive, big room in the sky space").
- Synced eighth/dotted-eighth delay for rhythmic motion and extra perceived width without added unison voices.
- Extreme stereo widening — hard left-right spread via detune and stereo imaging tools; kept centered/mono is the opposite instruction, reserved strictly for the bass and kick beneath it.
- Multiband saturation on the lead bus for brightness and perceived size at the drop (`uplifting_trance.md`).

## 2. Anthemic Riff Lead (Electro House, Big Room House)

Grounded in `electro_house.md` and `big_room_house.md`. Distinct from the supersaw archetype above in that this lead is deliberately *not* wide and pretty — it's a short, aggressive, distorted riff that also functions as the bass, and its identity comes from sound-design aggression rather than harmonic development.

**Synthesis method:** Subtractive/virtual-analog base with heavy distortion staged on top; FM or wavetable layering for metallic edge. `electro_house.md` is explicit this riff sound design is "the single most important creative decision in the track."

**Oscillators/unison/detune:**
- Detuned sawtooth stack, but narrower and more focused than a trance supersaw — the goal is punch and midrange cut, not airy width.
- Built as a "Frankenstein patch" per `electro_house.md`: a sub-sine layer for low-end weight, a mid-range distorted saw/square for the riff body, and a bright noise or FM top layer for aggression — three layers combined into one hybrid bass-and-lead part.
- Big room house's version simplifies this to a short, punchy, heavily saturated single riff patch (per `big_room_house.md`), written as a highly repetitive 1-2 bar, 2-4 pitch pattern — melodic minimalism is deliberate, not a limitation.

**Filter/envelope:**
- Resonant lowpass/bandpass, aggressive envelope movement for the "growl" or "squelch" riff articulation (`electro_house.md`).
- Big room variant: bandpass filtering specifically to carve a clear, punchy midrange presence that cuts on a festival PA.
- Fast attack, short-to-moderate decay — the riff is rhythmic and punchy, not sustained.

**Modulation for movement:**
- Fast, rhythmic filter envelope modulation synced to the groove, driving the riff's growl articulation on every hit.
- Pitch-bend/portamento slides between riff notes for expressive, semi-robotic character.
- Fast LFO/unison detune specifically on the riff patch for aggression and width at the drop (`big_room_house.md`).

**Effects chain:**
- Distortion/saturation/bitcrushing staged in multiple passes (soft clipping, then bitcrushing, then waveshaping) rather than one blunt distortion block — `electro_house.md`'s recommended technique for complex harmonic signature.
- Short or no reverb on the riff itself to preserve punch; reverb reserved for breakdown pads and buildup risers.
- Heavy sidechain compression from the kick, and multiband compression on the drop bus so low-end punch and high-end riff clarity are controlled independently.
- Stereo placement: unlike the trance lead, keep the core riff/bass hybrid narrower and closer to centered for low-end translation — width is spent on buildup risers and pads instead.

## 3. Plucky Arp Lead / Motif (Melodic Techno)

Grounded in `melodic_techno.md`. The sharpest contrast to both archetypes above: melodic techno's lead is subdued, evolving, and restrained in width, prioritizing genuine harmonic/melodic development over impact. `melodic_techno.md` calls arpeggiated sequences and lead motifs "the genre's most important instrumental category," but the character is atmospheric and cinematic rather than aggressive or maximal.

**Synthesis method:** Subtractive analog/virtual-analog character for warmth, or wavetable/FM for evolving modern textures — often blended in the same track, per `melodic_techno.md`'s "analog-style or digital subtractive/wavetable synths."

**Oscillators/unison/detune:**
- Sawtooth base, but unison kept moderate rather than maximal — width comes from layering multiple detuned voices for lush pad/chord support around the arp, not from pushing a single lead patch as wide as a trance supersaw.
- The arpeggiator/sequencer itself is treated as the primary melodic device: 1-4 bar patterns that develop and layer gradually across extended sections, rather than a long single melodic phrase (contrast with trance's 8-16 bar developing phrase).

**Filter/envelope:**
- Resonant lowpass, swept slowly across builds for "evolving arpeggio texture" — the filter sweep is measured in bars, mirroring the rolling sub-bass archetype in `edm_bass_design.md`'s melodic/dub techno section.
- Moderate attack rather than instant-pluck attack in some voicings — melodic techno's arp character sits between a hard pluck and a legato pad, contributing to its "more subdued/evolving" identity versus trance's aggressive, fully-open lead.

**Modulation for movement:**
- Slow LFO modulation on filter cutoff and pad parameters for constantly evolving texture — the core movement mechanism, applied over bars rather than beats.
- Arpeggiator-driven rhythmic pitch movement is itself the "core melodic device" (`melodic_techno.md`) — treat sequencer pattern design (note order, gate length, octave range) as equal in importance to sound design.
- Moderate, expressive velocity variation (unlike techno's typically mechanical velocity) for a more musical feel.

**Effects chain:**
- Long, lush hall/plate reverb for cinematic depth — generous, similar in spirit to trance's reverb use but applied to a narrower, more restrained source signal.
- Tempo-synced stereo delay on the arp/motif is a signature texture, adding hypnotic movement and width without widening the unison itself.
- Subtle tape/analog saturation for warmth rather than aggression.
- Sidechain from kick kept moderate — `melodic_techno.md` explicitly warns against ducking the melodic content too aggressively, a contrast to trance and big room house's hard pump.

## 4. Future Bass Pluck / Chord-Stab Lead

Grounded in `future_bass.md`. Cross-reference: `edm_bass_design.md` Section 5 ("Future Bass Chord-Stab Bass") already documents the clean sine sub that sits beneath this lead — this entry covers the chord-stab lead itself, which that bass section treats only as context. Do not re-read that sub-layer material here; the two patches are designed as a matched pair.

**Synthesis method:** Wavetable synthesis (Xfer Serum is the genre-associated tool per `future_bass.md`), with detuned supersaw-style stacking for width.

**Oscillators/unison/detune:**
- Full triads or extended chords (add9, maj7) voiced across a detuned wavetable/supersaw stack — the chord itself is the "lead," not a separate melody line played over static harmony.
- Layer multiple detuned chord voices with slightly offset pitch-bend timing for a thicker, more three-dimensional stab, per `future_bass.md`'s modern-technique guidance.

**Filter/envelope:**
- Lowpass filter movement synced to the chord stab's rhythmic hits for a "breathing" pulse — filter envelope retriggers on each stab rather than staying static.
- Fast attack on each stab hit for percussive impact; the stab needs to read as a rhythmic element as much as a harmonic/melodic one.

**Modulation for movement:**
- Pitch-wheel/portamento automation is the genre's single most identifying sound-design signature (`future_bass.md`) — every stab (or groups of stabs) gets an expressive pitch-bend swoop, drawn in or performed via a pitch wheel/MPE controller. This is the defining difference from the trance supersaw lead, which stays pitch-stable and gets its motion from width/filter automation instead.
- Vibrato/LFO pitch modulation on sustained tones for additional expressive movement.
- Chord stabs are programmed as syncopated, off-beat rhythmic hits (see `knowledge_base/midi` for general programming technique) rather than long legato phrases.

**Effects chain:**
- Lush reverb and wide stereo chorus for the genre's "wall of sound" — comparable in generosity to trance's reverb use but paired with heavier chorus for glossiness.
- Multiband saturation for warmth and loudness without harshness.
- Moderate sidechain-style ducking from kick/snare, explicitly lighter than trance-style hard sidechaining per `future_bass.md`.
- Wide stereo imaging on the stab/pad content; the paired sub-bass (see `edm_bass_design.md`) stays tight and centered below ~100-150 Hz so the wide chorus/reverb layers don't muddy the low end.

## 5. Acid Lead Sequence (Psytrance)

Grounded in `psytrance.md`. Distinct from the four melodic/harmonic leads above: psytrance treats its lead layer more like the acid/303 bass archetype in `edm_bass_design.md` (Section 6) — a resonant-filter performance instrument — but pitched and sequenced as a rapid melodic layer stacked above the rolling bassline rather than as the bass itself.

**Synthesis method:** FM synthesis (Native Instruments FM8, Ableton Operator per `psytrance.md`) for metallic, "alien" lead timbres, or wavetable synthesis (Serum, Massive) for evolving psychedelic textures — explicitly favored over clean supersaw sounds for this role.

**Oscillators/unison/detune:**
- FM operator stacks rather than detuned saw unison — the metallic, exotic character comes from operator ratios and modulation index, not from stacking/detuning voices the way the trance or future-bass leads do.
- When layering for the peak section, use multiple detuned FM/acid patches across octaves panned across the stereo field, per `psytrance.md`'s modern-technique guidance, rather than widening a single patch's unison.
- Melodic content favors Phrygian dominant or harmonic minor intervals in short repeating 2-4 bar cells for the genre's psychedelic, quasi-Eastern color.

**Filter/envelope:**
- Highly resonant, fast-modulating lowpass filter — the genre's signature "squelch," structurally the same mechanism as the acid bass archetype but applied to a pitched lead sequence.
- Bandpass filtering for narrow, cutting, psychedelic lead timbres distinct from the bassline's broader lowpass sweep.

**Modulation for movement:**
- Fast filter-envelope and LFO modulation per-note or per-group, not a single macro sweep — `psytrance.md` is explicit that fine-grained, near-continuous automation (filter cutoff, resonance) is what makes the part feel "alive" rather than mechanical.
- Accent patterning via velocity/filter movement on specific subdivisions, mirroring the accented-16th-note technique used on the bassline, applied here to the lead sequence for hypnotic groove.

**Effects chain:**
- Heavy, often filtered/resonant delay with automated feedback for trailing psychedelic echo texture — this is the lead's primary sense-of-space device, used more assertively than a simple reverb tail.
- Flanger/phaser for swirling, disorienting movement.
- Reverb used sparingly on this element during rhythmic/peak sections (to avoid smearing the fast 16th-note grid) but opened up generously if the same patch carries into a breakdown.
- Aggressive frequency-lane EQ carving against the bassline and other simultaneous sequenced layers — psytrance stacks many fast-moving parts at once, so each must occupy a narrow, well-defined slot rather than compete broadband.

## Cross-Archetype Summary

| Archetype | Core mechanism | Width source | Character |
|---|---|---|---|
| Classic supersaw (trance) | 7-voice detuned saw stack | Unison/detune width, automated per section | Wide, bright, sustained, euphoric |
| Anthemic riff (electro/big room house) | Distorted saw+sub+noise hybrid | Narrower, midrange-focused | Punchy, aggressive, short-repeating |
| Plucky arp/motif (melodic techno) | Sequenced 1-4 bar arp pattern | Moderate unison, restrained | Subdued, evolving, cinematic |
| Chord-stab (future bass) | Detuned chord voicing + pitch-bend | Wide chorus/reverb, offset pitch-bend layers | Percussive, glossy, expressive swoop |
| Acid lead (psytrance) | FM/resonant-filter sequence | Multi-octave panned layering, not unison | Metallic, squelchy, hypnotic |

The pattern across all five: genres that put the lead in an emotionally sustained role (trance, future bass) invest in width and pitch/filter automation as expressive devices, while genres that use the lead percussively (electro/big room house riffs, psytrance acid sequences) invest instead in per-note filter/accent articulation and narrower, more surgical frequency placement. Melodic techno sits deliberately between these poles — genuine melodic development, but restrained width and subdued articulation, which is precisely what separates its "motif" character from trance's "hook." Diagnosing which of these five roles a track's lead needs to play — before oscillator choice, before unison width — is the same first decision `edm_bass_design.md` recommends for bass design, applied to the melodic layer instead.
