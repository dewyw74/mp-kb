---
workflow_name: "Starting an EDM Track From a Blank Project"
daw: "generic"
category: "pre-production"
goal: "Take a new EDM track from a blank DAW project to a solid 8-bar loop with rough arrangement markers in place, in an order that avoids the two most common false starts: arranging before the core loop is good, and picking tempo/key after material already exists."
steps:
  - "Set tempo and key before writing anything, based on target subgenre."
  - "Load or bounce down a reference track for tempo, energy, and frequency-balance calibration."
  - "Choose a starting point — drum loop, bassline, or chord/melody first — based on subgenre conventions."
  - "Build a rough drum loop (kick, hats, one percussion layer) even if it isn't the eventual starting point."
  - "Add the second core element (bass or chords/motif, whichever wasn't step 4) and lock the groove."
  - "Sketch the full 8-bar loop — every element that will carry the main groove/peak section, at rough levels."
  - "A/B the loop against the reference track for tempo feel, density, and tonal balance."
  - "Block out rough arrangement markers for the whole track before detailing anything further."
  - "Duplicate the 8-bar loop across the marked sections as a placeholder skeleton."
  - "Hand off to composer_agent for chord/melody development once the loop's harmonic direction is set."
  - "Hand off to sound_design_agent for patch design once the loop's core sounds are chosen but not yet polished."
  - "Return to arrangement detail only after the loop and hand-offs are solid."
related_plugins:
  - "spectrum analyzer (e.g. Ableton EQ Eight analyzer mode, iZotope Insight, Voxengo SPAN)"
  - "loudness meter (e.g. Youlean Loudness Meter)"
  - "reference-track utility (e.g. Ableton's own track A/B via a muted reference channel, or a dedicated plugin like Mastering The Mix REFERENCE)"
tags:
  - "workflow"
  - "edm"
  - "pre-production"
  - "arrangement"
  - "reference-track"
  - "loop-based-writing"
---

# Starting an EDM Track From a Blank Project

A practical, ordered process for the first session on a new EDM track — from an empty project to a solid 8-bar loop with rough arrangement markers blocked out. This is workflow-level guidance: it tells you what order to do things in and why, not how to compose or sound-design any specific part. For those, this workflow explicitly hands off to `composer_agent` and `sound_design_agent` at the point where it makes sense to bring them in.

## 1. Set tempo and key before anything else

Don't start playing with sounds before tempo and key are locked — both shape every decision that follows (loop lengths, which samples/patches fit, how a bassline sits under a chord).

- Pick tempo from the target subgenre's documented range, not a default project tempo: house sits roughly 118-128 BPM, techno 120-150 BPM, melodic techno more narrowly 120-125 BPM (see `knowledge_base/genres/edm/house.md`, `techno.md`, `melodic_techno.md`).
- Pick a key/mode consistent with the subgenre. Minor keys (A minor, C minor, F minor, G minor) dominate across house, techno, and melodic techno per those genre files — melodic techno additionally favors natural minor or harmonic minor for cinematic tension, while house leans on minor for moodier tracks and major/gospel-influenced progressions (vi-IV-I-V) for uplifting, vocal-driven material.
- If the genre is undecided, this is the moment to decide it — everything downstream depends on it. Consult `knowledge_base/genres/edm/` for a closer match before proceeding.

## 2. Build a reference track workflow

Load a commercially released track in the target subgenre into a muted reference channel (or a dedicated reference-track plugin) before writing further.

- Use it to calibrate **tempo feel** — does your chosen BPM actually groove the way the reference does, or does it feel rushed/dragging at the same numeric tempo?
- Use it to calibrate **energy/density** — how many elements are actually playing during the reference's main groove/peak section versus its intro? This sets a realistic density target for your own 8-bar loop later.
- Use it to calibrate **frequency balance** — pull up a spectrum analyzer on the reference and compare it against your rough loop once you have one, so low-end and top-end decisions aren't made blind.
- Keep the reference track available (muted, ready to A/B) through the whole loop-sketching phase, not just at the start.

## 3. Choose a starting point based on subgenre

There is no single correct starting point for an EDM track — the right one depends on where the genre's musical identity actually lives, per the genre files:

- **Groove/drum-loop-first**, then bassline: fits house and most techno. House arrangement "begins with drums alone... other elements are layered in gradually" (`house.md`), and house harmony is explicitly "groove-first" — often a single chord or slow vamp, with the loop rather than a developed phrase as the compositional unit. Techno is similar: arrangement is "fundamentally loop-based," melodic content is "frequently minimal or absent," and musical interest comes from "rhythm, timbre, and repetition-with-variation" rather than harmonic movement (`techno.md`). For both, start with kick + hats + one percussion layer, then add the bassline, before worrying about chords or melody at all.
- **Chord/motif-first**, then groove: fits melodic techno. Its melodic characteristics note that, unlike most techno, it "foregrounds genuine harmonic and melodic development" and that the arpeggio/lead motif is "the genre's most important instrumental category, carrying most of its identity" (`melodic_techno.md`). For this subgenre, sketching the core chord progression (e.g. i-VI-III-VII) or arpeggio motif first — even before the drums are detailed — is justified, though a minimal rhythmic loop should still exist under it early since the genre's identity sits deliberately between techno's rhythmic hypnosis and melodic development.
- **Bassline-first** is a reasonable variant within the groove-first camp (common in acid-house/303-driven or bass-forward techno workflows) — same rationale as drum-loop-first, just swapping which rhythmic/harmonic anchor comes first.

If genre is ambiguous or genuinely open, default to groove-first — it's the safer starting point across the broadest range of EDM subgenres and avoids over-composing before the track has a rhythmic identity.

## 4-5. Build the rough loop's core two elements

Whichever element didn't lead in step 3, add it now and lock the groove between the two before adding anything else:

- If you started with drums, add bass next and get the kick/bass relationship right (sidechain feel, note lengths, low-end pocket) before layering chords or leads on top.
- If you started with a chord/motif (melodic techno path), add a minimal rhythmic loop under it now — even a placeholder kick and hat pattern — so the harmonic material isn't developed in a rhythmic vacuum.
- Keep everything rough: placeholder sounds are fine here. The goal is groove and harmonic direction, not final sound design.

## 6. Sketch the full 8-bar loop

Extend to every element that will be present in the track's main groove/peak section — drums, bass, chords/motif, and any core hook — as one continuous 8-bar loop at rough relative levels (no detailed mixing yet).

- 8 bars is long enough to hear whether the loop actually holds interest on repeat (a core requirement for loop-based EDM writing per the techno and house files) without burning time on arrangement decisions that aren't ready yet.
- Resist the urge to jump into full-song arrangement at this stage — a loop that isn't good on repeat won't be saved by arrangement.

## 7. A/B against the reference track

Solo-toggle between your loop and the muted reference channel from step 2. Check tempo feel, element density relative to the reference's main section, and rough tonal balance on a spectrum analyzer. Adjust the loop, not the reference — the reference is a calibration tool, not a template to copy.

## 8. Block out rough arrangement markers

Before detailing anything further, lay down section markers for the whole track using the target subgenre's documented structure as a starting template:

- House: drums-only intro -> groove establishment -> chord/vocal intro -> main groove/hook -> breakdown -> build -> final groove -> drums-only outro (`house.md`).
- Techno: DJ-mixable loop intro -> layer build -> layer build -> peak/full groove -> optional breakdown -> second peak -> DJ-mixable outro (`techno.md`).
- Melodic techno: intro (atmosphere + rhythmic loop) -> arpeggio/motif introduction -> build -> peak (full groove + melody) -> breakdown (melodic/emotional) -> build 2 -> peak 2 -> outro (`melodic_techno.md`).

These markers are placeholders for bar-count and energy planning only — do not compose the build/breakdown/outro content yet.

## 9. Duplicate the loop as a skeleton

Copy the 8-bar loop into the marked sections as a rough placeholder (e.g. the full loop dropped into every "peak" marker, a stripped version into "intro"/"outro" markers). This gives a listenable full-length skeleton fast, and makes it obvious early whether the arrangement plan actually works before any section is composed in detail.

## 10-11. Hand off to composer_agent and sound_design_agent

Once the skeleton loop is solid — groove locks, harmonic direction is set, and the rough arrangement plays through without an obvious structural problem — bring in the specialist agents rather than continuing to improvise alone:

- **`composer_agent`**: once the loop's harmonic direction (key, mode, chord progression or motif shape) is established but not yet fully developed — e.g. extending melodic techno's arpeggio motif across the build and breakdown, or writing a house chord-stab/vocal-hook riff.
- **`sound_design_agent`**: once the loop's core sounds are chosen in role (kick, bass, lead/motif, pad) but still placeholder-quality — for actual synthesis method, patch design, and effects-chain decisions per instrument.

Bringing these in before the loop is solid risks polishing material that gets thrown out when the groove or arrangement plan changes; bringing them in too late means composing/sound-designing every section from scratch instead of once on the loop and reusing.

## 12. Return to arrangement detail

Only after the hand-offs land does full arrangement detailing belong — varying the duplicated skeleton per section, automating builds/breakdowns, and finishing transitions. That work is covered by other entries under `knowledge_base/production/arrangement/`.
