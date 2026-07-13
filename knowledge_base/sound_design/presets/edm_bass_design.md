---
title: "EDM Bass Design — Archetypes and Patch Recipes"
synthesis_method:
  - "Subtractive"
  - "FM"
  - "Wavetable"
  - "Sample-based"
tags:
  - "bass"
  - "wobble"
  - "growl"
  - "reese"
  - "sub-bass"
  - "acid"
  - "303"
  - "preset-recipe"
  - "dubstep"
  - "drum-and-bass"
  - "techno"
  - "future-bass"
---

# EDM Bass Design — Archetypes and Patch Recipes

Bass is the load-bearing element across almost every EDM subgenre, but "bass design" is not one skill — it is at least six distinct disciplines that happen to share the low end of the spectrum. This entry surveys the major bass archetypes found across the EDM knowledge base and gives a concrete, buildable patch recipe for each: oscillator setup, filter/envelope behavior, the LFO or modulation technique that creates movement, and the effects chain that finishes the sound. Genre files consulted for grounding: `knowledge_base/genres/edm/dubstep.md`, `brostep.md`, `riddim.md`, `neurofunk.md`, `drum_and_bass.md`, `melodic_techno.md`, `dub_techno.md`, `future_bass.md`, `acid_house.md`, `acid_techno.md`.

A recurring principle across nearly every archetype below: **layer a clean sine sub beneath the modulated/distorted mid-bass character.** Every genre file surveyed here independently converges on this same technique — the mid-bass carries the genre's identity (wobble, growl, screech, squelch) while a separate, undistorted sub layer carries the physical low-end weight that translates on a soundsystem. Losing the clean sub under layers of distortion is the single most common mistake cited across these files.

## 1. Wobble / Growl Bass (Dubstep, Brostep)

Grounded in `dubstep.md` and `brostep.md`. This is the LFO-automated resonant filter technique that defines both genres — the difference between them is speed, extremity, and layering density, not the underlying mechanism.

**Synthesis method:** Subtractive (Massive, Sylenth1, Serum) as the base engine, with FM cross-modulation layered in for metallic edge in the brostep variant.

**Oscillators:**
- 2-3 detuned sawtooth oscillators, unison-stacked with moderate detune (~15-25 cents) for width and beating.
- A Reese-style pair (two sawtooths tuned a few cents apart, one panned hard left/right) beneath the main stack for extra thickness.
- A separate, undistorted sine sub-oscillator an octave (or two) below the root, kept mono and centered — this is the "felt more than heard" layer dubstep.md calls out explicitly.

**Filter/envelope:**
- Resonant lowpass filter (24dB/oct for weight) with moderate-to-high resonance.
- Short amp envelope (near-instant attack, sustained through the note) — the *filter*, not the amplitude, carries the rhythmic interest.
- Filter envelope amount kept low; the LFO does the real work (below).

**LFO/modulation for movement:**
- One LFO routed to filter cutoff, synced to 1/4, 1/8, or triplet subdivisions — this is the "wobble" itself. UK dubstep favors smoother, slower-to-mid-rate sine or triangle LFO shapes; brostep pushes the same mechanism to fast, erratic rates with square/stepped LFO shapes for the "screech" and stutter character described in brostep.md.
- Brostep variant: layer 3-6 separate bass patches, each with independently automated filter cutoff, pitch, and distortion amount, so the composite sound is constantly shifting rather than a single static wobble.
- Envelope-driven pitch bends/glides on individual notes for aggressive "stab" articulation, more prominent in growl-bass riffs than pure wobble lines.

**Effects chain:**
- Distortion/waveshaping stage on the mid-bass layer only (not the sub) for harmonic growl.
- Dubstep: light, controlled distortion, generous reverb/delay reserved for pads rather than the bass itself, to preserve punch.
- Brostep: distortion, bitcrushing, and waveshaping stacked in series across multiple patches; multiband saturation to control aggression per frequency band; gating/stutter effects on some layers for rhythmic chaos.
- Sidechain compression from the kick into the bass bus on both variants for rhythmic pumping.
- Keep the sub layer's send to distortion/reverb at zero — it stays clean and mono.

## 2. Riddim Gate Bass

Grounded in `riddim.md`. Riddim strips the wobble concept down to its rhythmic core: one note, tightly gated, with variation coming entirely from timbre and rhythm rather than pitch.

**Synthesis method:** FM synthesis for metallic/growling tone, or wavetable synthesis for a robotic, scanning timbre.

**Oscillators:**
- FM: 2-3 operator stack, moderate-to-high modulation index for aggressive harmonic content; carrier tuned to the root note.
- Wavetable: a single wavetable position slowly scanned (see modulation below) rather than multiple detuned oscillators — riddim's texture comes from timbral evolution within one sustained note, not stacking.
- Sine sub layer beneath, as in the wobble archetype above, kept centered and mono for "maximum physical impact."

**Filter/envelope:**
- Resonant lowpass, often pushed to extreme/aggressive settings per riddim.md.
- Amplitude shaped by the gate pattern itself (see below) rather than a conventional ADR envelope — each gated segment gets its own fast attack/fast release.

**LFO/modulation for movement:**
- The defining technique: a tightly quantized LFO or, better, a step sequencer/MIDI-triggered modulation lane driving filter cutoff and/or amplitude, locked precisely to the half-time groove. Riddim.md is explicit that gate/LFO sync precision — not pitch content — is the genre's core sound-design skill.
- Pitch stays static or moves only within a narrow interval; do not introduce melodic pitch variation between pattern repeats — vary gate timing, distortion amount, and filter movement instead.
- Wavetable position/scan can be modulated slowly across a drop for evolving timbre without touching rhythm or pitch.
- Optional: sidechain/duck the bass pattern itself from the kick for an additional layer of rhythmic punctuation within the gated pattern.

**Effects chain:**
- Heavy distortion/waveshaping for weight and aggression — riddim runs hotter and drier than UK dubstep.
- Minimal reverb; the mix stays dry and forward by design.
- Multiband distortion/saturation to preserve low-end weight while pushing mid/high aggression.
- Bass kept centered and largely mono — riddim.md notes this is for maximum physical impact on club/festival systems, a contrast to brostep's wider stereo bass-wall approach.

## 3. Reese / Growl Bass (Neurofunk, Drum & Bass)

Grounded in `neurofunk.md` and `drum_and_bass.md`. The Reese bass — named for the classic technique of two detuned sawtooths — is drum and bass's signature mid-bass voice, reaching its most aggressive, layered form in neurofunk.

**Synthesis method:** Layered FM and wavetable synthesis combined in a single patch, per neurofunk.md's explicit recommendation, plus subtractive layering for the classic Reese pair.

**Oscillators:**
- Two (or more) detuned sawtooth oscillators — the classic Reese pair — detuned enough to create a slow, churning phase-beating rather than a fast unison shimmer.
- FM operator layer added on top for metallic, snarling harmonic content (neurofunk's defining addition over a plain Reese).
- Sine sub layer beneath for low-end weight, kept separate from the modulated layers.
- Neurofunk technique: resample and re-layer the processed bass multiple times, building complexity in stages rather than trying to get the full growl from oscillators alone.

**Filter/envelope:**
- Aggressive, fast-moving resonant filter, often bandpass/notch-filtered in combination with lowpass for metallic, industrial texture.
- Fast envelope response on filter cutoff and pitch per note — the goal is rhythmic, almost rap-like phrasing where each note gets its own articulate filter/pitch move, per neurofunk.md.

**LFO/modulation for movement:**
- Fast LFO and envelope modulation on filter cutoff and pitch, programmed per-note rather than as a single repeating cycle — this is what separates a static Reese pad from genuine neurofunk growl bass.
- Ring modulation and FM cross-modulation for dissonant, metallic color.
- In broader drum and bass (liquid-adjacent uses of Reese), dial back the modulation rate and depth for a smoother, phaser/chorus-like movement instead of the aggressive neurofunk treatment — the same oscillator technique scales from smooth to violent depending on modulation intensity.

**Effects chain:**
- Heavy distortion/saturation/waveshaping applied in stages (not one single distortion block) for complex, evolving harmonic content.
- Very short, nearly dry reverb — neurofunk.md is explicit that space is minimized to keep the mix "forward and aggressive," a sharp contrast to dubstep's more generous ambience.
- Multiband distortion/compression to control the low end while preserving upper-harmonic aggression.
- Bass and kick centered and mono; only atmospheric/high-frequency metallic textures get stereo width.

## 4. Rolling Sub Bass (Melodic Techno, Dub Techno)

Grounded in `melodic_techno.md` and `dub_techno.md`. Neither genre file uses the term "rolling bass" directly, but both independently describe the same underlying design: a warm, sub-anchored bass that provides harmonic foundation and rhythmic propulsion without becoming a lead element — built for hypnotic repetition across long sections rather than dramatic movement.

**Synthesis method:** Subtractive, using warm analog or virtual-analog oscillator models (Juno/Prophet-style character, per dub_techno.md).

**Oscillators:**
- Sine or triangle for the fundamental — dub_techno.md specifies sine-based sub bass explicitly.
- Optional low-level sawtooth layer, heavily filtered, blended underneath for harmonic richness without brightness (used in melodic techno's "warm, often sub-focused bass with subtle movement").
- Keep the patch monophonic/legato-friendly — both genres favor slow-moving or static bass patterns rather than rhythmically busy ones.

**Filter/envelope:**
- Gentle lowpass filtering — dub_techno.md is explicit this is "rarely used as a dramatic sweep"; the filter's job is warmth, not spectacle.
- Slow attack/release on the amplitude envelope so notes bloom and decay smoothly into the groove rather than articulating percussively.
- In melodic techno, filter cutoff can be swept slowly across a build (paired with the arpeggio build) to add harmonic evolution to the bass without turning it into a wobble.

**LFO/modulation for movement:**
- Slow LFO on filter cutoff (melodic_techno.md: "slow LFO modulation on filter cutoff... for constantly evolving texture") — rate measured in bars, not beats, so the movement reads as a breathing evolution rather than a rhythmic effect.
- Dub techno's real "movement" is not on the bass oscillator itself but on the delay feedback path processing the chord stab above it (see effects below) — the bass stays comparatively static and lets the delayed chord decay carry the sense of motion. Design the bass patch to be a stable low anchor, not a modulation showcase.
- Sidechain compression from the kick, used gently in both genres — dub_techno.md warns aggressive pumping "works against the aesthetic"; melodic_techno.md calls for "moderate" sidechain that maintains groove cohesion "without ducking the melodic content too aggressively."

**Effects chain:**
- Light, gentle bus compression only — both genre files explicitly caution against heavy compression, which would flatten the dynamic breathing room the genres depend on.
- Minimal distortion/saturation — a touch of tape warmth (dub_techno.md) at most; this archetype is defined by warmth, not aggression.
- Reverb/delay sends kept low on the bass itself even though the genre as a whole is reverb/delay-heavy — those effects belong on the chord stab and pads above, while the sub stays dry, mono, and centered for club translation.
- Highpass filtering on any delay feedback path elsewhere in the mix to keep the bass's low end from building up in the echo tail (dub_techno.md's specific warning).

## 5. Future Bass Chord-Stab Bass

Grounded in `future_bass.md`. Distinct from the other archetypes here in that the "bass" in future bass is deliberately subordinate to a pitch-bent chord lead sitting above it — the sub's job is pure harmonic support, not independent character.

**Synthesis method:** Wavetable synthesis (Serum is the genre-associated tool per future_bass.md) for the chord lead; simple subtractive sine synthesis for the sub layer beneath it.

**Oscillators:**
- Sub: a single clean sine oscillator (occasionally lightly saturated), tuned to track the chord progression's root motion note-for-note.
- The chord lead itself (technically a separate patch, but essential context for the sub's design) uses detuned wavetable/supersaw stacks — the sub must sit cleanly beneath this wide, chorused layer without competing for the same frequency space.

**Filter/envelope:**
- Sub: minimal filtering — a gentle lowpass to remove any harmonic content above the fundamental, since future_bass.md specifies the sub should be "clean and simple," reinforcing root motion rather than carrying independent melodic or rhythmic pattern.
- Fast-enough attack to lock rhythmically with the chord stab hits above it, since the two elements need to read as a single, unified low-end event.

**LFO/modulation for movement:**
- Very little modulation on the sub itself by design — future_bass.md is explicit the sub "sits beneath and reinforces the chord stabs' root notes rather than carrying an independent melodic pattern," unlike dubstep/riddim/neurofunk where the bass *is* the modulation showcase.
- The genre's signature modulation — pitch-wheel/portamento automation — belongs on the chord-lead patch, not the sub; keep the sub pitch-locked and stable so the portamento swoop above it reads clearly against a fixed low end.
- Lowpass filter movement synced to the chord stab's rhythmic hits ("breathing" pulse per future_bass.md) can be applied to the chord layer; leave the sub filter static.

**Effects chain:**
- Sidechain-style ducking from kick/snare into the sub, moderate rather than extreme (future_bass.md contrasts this explicitly with trance-style hard sidechaining).
- No reverb or chorus on the sub — those belong on the chord stabs and pads to create the genre's "wall of sound," while the sub stays tight and centered below roughly 100-150 Hz, per future_bass.md's mixing guidance, so the wide chorus/reverb layers above don't turn the low end to mud.
- Light saturation only if extra perceived loudness/warmth is needed; keep it subtle.

## 6. Acid / 303 Bass (Acid House, Acid Techno)

Grounded in `acid_house.md` and `acid_techno.md`. Unlike every other archetype above, acid bass isn't primarily a patch-design problem — it's a *performance* problem. The instrument (TB-303 or an accurate emulation) is fixed; the skill is real-time or automated manipulation of a small parameter set.

**Synthesis method:** Dedicated TB-303 emulation (Xfer Cthulhu, Audiorealism ABL, TAL-U-NO-62-adjacent tools, Roland Cloud TB-03) rather than a general-purpose subtractive synth — the 303's specific filter circuit and accent/slide implementation are the entire point and are hard to replicate generically.

**Oscillators:**
- Single sawtooth (the iconic 303 tone) or square, per the instrument's own oscillator selection — no stacking, no unison, no detuning. Acid's identity depends on this single-oscillator simplicity contrasted against everything happening at the filter stage.

**Filter/envelope:**
- The 303's own resonant lowpass filter, driven hard with high resonance — both genre files agree this filter *is* the entire sound-design focus of the genre.
- Envelope modulation (env mod) amount and decay are core performance parameters, not set-and-forget controls — they shape how aggressively each note's filter "pops" open before closing.
- Acid techno pushes resonance further, toward self-oscillation, for a harsher squelch than acid house's comparatively controlled tone.

**LFO/modulation for movement:**
- No conventional LFO — movement comes from live or automated tweaking of cutoff frequency and resonance in real time, described in both genre files as the genre's primary "performance" technique. Record this as an actual knob-turning pass (physical controller or drawn automation that mimics one) rather than a static filter setting.
- Accent and slide parameters on the 303's own 16-step sequencer create the squelching, glissando-like articulation — accent adds emphasis/extra filter push on specific steps; slide glides pitch between consecutive notes. These sequencer-level parameters do as much of the "modulation" work as any filter automation.
- Acid techno layers multiple detuned or differently-filtered 303 lines running simultaneously for a denser, more chaotic composite texture than acid house's single-line approach.

**Effects chain:**
- Acid house: minimal processing by design — light compression that preserves the natural rise and fall of resonant sweeps, sparse reverb/delay so as not to dilute the raw filter character, largely mono output reflecting the genre's hardware-era origins.
- Acid techno: distortion/overdrive pushed deliberately further than acid house for a dirtier tone (historically achieved via Devil Fish-modded hardware, now via emulations with added drive stages); more prominent delay during breakdowns for disorienting texture; heavier saturation on the drum bus to match the harder-edged bass.
- Modern practice common to both, per the genre files: layer a separate sub-bass synth beneath the 303 to add low-end weight the original hardware lacked, while keeping the 303 itself untouched and dominant in the midrange — the same clean-sub-plus-characterful-mid principle that runs through every archetype in this document.

## Cross-Archetype Summary

| Archetype | Core mechanism | Modulation source | Typical stereo placement |
|---|---|---|---|
| Wobble/Growl (dubstep/brostep) | LFO-swept resonant lowpass | Tempo-synced LFO on filter cutoff | Sub mono; mid-bass narrow to wide by subgenre |
| Riddim gate | Step-sequenced gate on one note | Quantized LFO/step modulation, tightly synced | Mono/centered |
| Reese/growl (neurofunk/DnB) | Detuned oscillator pair + FM layering | Fast per-note filter/pitch envelopes | Mono/centered |
| Rolling sub (melodic/dub techno) | Warm sine anchor, minimal movement | Slow bars-long LFO or none | Mono/centered |
| Future bass sub | Clean sine locked to chord root | Near-none; modulation lives on the chord lead instead | Tight, centered below ~100-150 Hz |
| Acid/303 | Resonant filter performance | Live/automated cutoff+resonance, accent/slide | Mono (classic) to mildly widened (modern) |

The pattern that emerges across all six: genres that put the bass in the lead-instrument role (wobble, riddim, Reese, acid) build modulation directly into the bass patch as the primary compositional device, while genres that use bass as harmonic foundation (rolling sub, future bass sub) deliberately restrain bass modulation and place the expressive movement elsewhere in the arrangement. Diagnosing which role a given track needs its bass to play is the first decision — before oscillator choice, before filter type — in any EDM bass design task.
