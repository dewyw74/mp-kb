---
title: "FM Bass Patch Design"
synthesis_method:
  - "FM"
tags:
  - "fm-bass"
  - "dx7"
  - "operators"
  - "funk"
  - "synth-pop"
  - "sound-design"
---

# FM Bass Patch Design

`knowledge_base/sound_design/synthesis/fm_synthesis.md` surveys FM's role across the EDM growl-bass genres (dubstep, riddim, bass house, neurofunk, bassline, complextro) at the level of "why FM reaches this timbre." This entry is the dedicated, buildable FM bass patch walkthrough — operator setup, ratio choice, and envelope design — extended specifically to the non-EDM lineage (funk, synth-pop, R&B) where FM bass originated commercially on the DX7/DX100 and predates the modern growl-bass application by a decade.

## Building the Patch

1. **Operator count and algorithm**: a 2-operator (one carrier, one modulator) patch is sufficient for most bass roles — bass needs to read clearly and consistently more than it needs dense timbral complexity, so simpler algorithms are the practical default; reserve 4-6 operator stacks for more aggressive growl-bass work (see `knowledge_base/sound_design/presets/growl_and_wobble_bass_design.md`).
2. **Carrier:modulator ratio**: near-integer ratios (1:1, 1:2, 2:1) keep the bass tonally clean and musically pitched — appropriate for funk/pop bass roles that need to lock in with a bassline's harmonic function. Higher or non-integer ratios push toward the metallic, snarling growl-bass territory `fm_synthesis.md` documents for dubstep/riddim; ratio choice is the primary fork between "clean FM bass" and "growl FM bass."
3. **Modulation index and its envelope**: a moderate, envelope-controlled index gives punch and harmonic richness on the attack without turning harsh — per `fm_synthesis.md`'s harshness-taming guidance, keep index under envelope control rather than static, spiking briefly on the attack and settling for the sustain.
4. **Carrier envelope**: fast attack, sustain shaped to the part's rhythmic role — funk-style FM bass often uses a fairly short, punchy decay for a "plucked" articulation that locks tightly with drums, distinct from a sustained pad-like envelope.
5. **Feedback**: light feedback on the modulator adds grit and edge appropriate to a more aggressive funk/electro-funk bass tone; keep it minimal for a cleaner pop-bass application.

## Genre Grounding

- `knowledge_base/genres/r_and_b/electro_funk.md` documents the Minimoog and, "later in the 1980s," the Yamaha DX100 (a compact single-operator-per-voice DX7 relative) as core bass sound sources, with "aggressive, even compression" applied to keep the deep, heavy FM/analog-hybrid bass tone consistent beneath the talk box lead.
- `knowledge_base/genres/electronic/synth_pop.md` documents FM synthesis introducing "metallic bell tones, punchy FM basses, and glassy leads that became a genre signature in the DX7 era" — a direct, explicit naming of FM bass as a defining synth-pop sound-design element distinct from the genre's PWM/subtractive lead and pad work.
- `knowledge_base/genres/r_and_b/minneapolis_sound.md` documents "FM synthesis (Yamaha DX7) for bell-like and bass tones," paired with analog polysynths (Prophet-5, Oberheim) and Minimoog analog bass — FM bass used as one voice within a broader synth-bass palette rather than the sole bass source.
- `knowledge_base/genres/r_and_b/contemporary_r_and_b.md` documents "Synth bass (frequently 808 subs or Moog-style analog plucks)" alongside "FM synth bells (DX7)" — showing FM's bass role persisting into modern R&B production alongside 808-style sub-bass.
- `knowledge_base/genres/edm/riddim.md`, `knowledge_base/genres/edm/dubstep.md`, `knowledge_base/genres/edm/bassline.md` (per `fm_synthesis.md`'s fuller survey) document the higher-ratio, higher-index growl-bass application of the same underlying 2-operator technique — confirming ratio and index as the specific parameters that separate this entry's clean funk/pop bass patches from the EDM growl-bass family.

## Common Mistakes

**Using a high modulation index by default regardless of genre context.** A static high index is the source of unwanted harshness in any FM bass patch; funk/pop applications specifically need a tamer, envelope-shaped index to stay clean and musical rather than snarling.

**Assuming FM bass is an EDM-only technique.** The commercial DX7/DX100 FM bass sound predates dubstep/riddim by roughly three decades and has an entirely separate funk/pop/R&B lineage with different ratio and envelope conventions.

## Cross-References

- `knowledge_base/sound_design/synthesis/fm_synthesis.md` — carrier/modulator/ratio/index fundamentals and the EDM growl-bass survey this entry extends into funk/pop territory.
- `knowledge_base/sound_design/presets/growl_and_wobble_bass_design.md` — the higher-ratio, higher-index FM bass application for aggressive EDM growl bass.
- `knowledge_base/sound_design/presets/edm_bass_design.md` — the broader bass-archetype survey this entry's FM-specific technique complements.
- `knowledge_base/genres/r_and_b/electro_funk.md`, `knowledge_base/genres/electronic/synth_pop.md`, `knowledge_base/genres/r_and_b/minneapolis_sound.md`, `knowledge_base/genres/r_and_b/contemporary_r_and_b.md` — genre sources grounding this entry.
