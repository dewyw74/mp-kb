---
technique_name: "Dynamic EQ — Frequency-Dependent Compression"
category: eq
problem_solved: "A frequency range that's only a problem sometimes — harsh only at high playing intensity, sibilant only on certain syllables, or masked only when a competing element is present — where a static EQ cut would remove wanted content during the quiet or clean moments"
parameters:
  threshold_behavior: "A frequency band's gain reduction (or boost) engages only once the signal in that band crosses a threshold, unlike static EQ which applies its curve constantly"
  de_essing_relationship: "De-essing is dynamic EQ scoped specifically to sibilant frequencies (typically 4-9kHz) on vocals — a special case of the broader technique"
  sidechain_variant: "Some 'dynamic EQ' behavior is achieved via one element's level triggering gain reduction in a specific band of another element, functionally identical to multiband sidechain compression"
  band_width: "Narrower and more targeted than the broad shelves used in static tonal-balance EQ, since the goal is surgical correction of a specific recurring problem, not an overall tonal shift"
signal_chain_position: "Per-element, typically after static/corrective EQ has handled constant problems, reserved for content that changes character with playing intensity, arrangement density, or specific moments in a performance"
genre_applicability:
  - djent
  - classical_period
  - electric_blues
  - bass_house
  - vocal_trance
  - soft_rock
  - country_pop
  - choral_music
  - christian_rock
related_techniques:
  - subtractive_eq
  - frequency_masking
  - sidechain_pumping
tags: ["dynamic-eq", "de-essing", "frequency-dependent-compression", "multiband", "sibilance"]
---

# Dynamic EQ — Frequency-Dependent Compression

Dynamic EQ applies gain reduction (or boost) to a specific frequency band only when that band crosses a threshold, rather than applying a fixed curve all the time the way static EQ does. This knowledge base's genre entries describe the technique across a wider range of applications than the one most people associate with it (de-essing) — from taming resonances that only appear at high playing intensity, to managing extended-range bass content, to functioning as an automated substitute for constant manual EQ or level automation.

## De-Essing: The Most Common Special Case

De-essing — dynamic EQ scoped to sibilant frequencies, engaging only when harsh "S" and "T" consonant energy crosses a threshold — is the most frequently documented instance of the broader technique. `country_pop.md` pairs it directly with compression in its processing list: "Heavy vocal compression and de-essing to keep the vocal incredibly bright but smooth." `choral_music.md` applies the identical logic at ensemble scale rather than to a single vocalist: "De-essing to manage the harsh 'S' consonants of a large group singing simultaneously" — a problem a static EQ cut couldn't solve without dulling every non-sibilant moment too. `christian_rock.md` and `soft_rock.md` both list de-essing alongside dynamic EQ as complementary vocal-clarity tools rather than the same tool twice — `soft_rock.md`: "Vocal-focused mixing techniques (dynamic EQ, careful de-essing, parallel compression) to achieve maximum clarity and warmth on the lead vocal," implying de-essing handles the sibilance case specifically while broader dynamic EQ handles other frequency-dependent vocal issues.

## Taming Resonance That Only Appears at High Intensity

A second, distinct use case documented in the corpus is suppressing a resonance or harshness that only becomes a problem when a performer plays or sings loudly — exactly the scenario a static cut can't handle without also dulling quieter passages. `classical_period.md` describes this precisely: "Using dynamic EQ on the string section to automatically duck harsh resonances only when the violins play at maximum velocity (fortissimo)." `electric_blues.md` documents the inverse framing of the same idea — using dynamic EQ to let a guitar's tone expand rather than to suppress it: "Dynamic EQ on guitar to let tone open up naturally as playing intensity increases." Both quotes describe the same underlying mechanism (a frequency band's behavior changing with signal intensity) applied to opposite goals — one holding a problem frequency in check at loud moments, the other allowing a tonal quality to bloom as intensity rises — which is the core flexibility dynamic EQ offers over a fixed static curve.

## Managing Bass Content That Moves

`djent.md` and `bass_house.md` both apply dynamic EQ to a low-end management problem that a fixed EQ notch can't solve because the offending content isn't fixed in level or frequency. `djent.md` lists it as a defining modern production technique: "Applying dedicated low-end management plugins (multiband compression, dynamic EQ) to keep extended-range guitar/bass tight and defined." `bass_house.md` extends the same logic to a sub/mid-bass separation problem: "Multiband sidechain and dynamic EQ to keep sub and mid-range bass content separately controlled and impactful." In both cases, the low end isn't consistently problematic — it becomes muddy or masks other elements only at certain moments or intensities, which is exactly the condition dynamic EQ is built to handle without permanently thinning the bass.

## Dynamic EQ as an Automation Substitute

`vocal_trance.md` documents a use case that reframes dynamic EQ as a labor-saving alternative to manual automation rather than a corrective tool: "Using dynamic EQ or automated sidechain from the vocal into competing synth/pad frequencies to keep the vocal consistently intelligible without manual automation for every phrase." This is a meaningfully different framing from the de-essing and resonance-taming cases above — here dynamic EQ isn't fixing a defect in one element, it's automatically managing an ongoing masking relationship between two elements (vocal vs. pads) that would otherwise require hand-drawn EQ automation across the whole song.

## Common Mistakes

**Using dynamic EQ where a static cut would do.** If a frequency is a problem constantly rather than only at certain intensities or moments, a simple static EQ cut is more transparent and predictable than a dynamic band reacting to a threshold — reserve dynamic EQ for content that genuinely changes character, as in `classical_period.md`'s fortissimo-only resonance or `electric_blues.md`'s intensity-dependent tone.

**Treating de-essing and general dynamic EQ as identical rather than nested.** `soft_rock.md` and `christian_rock.md` both list them as separate tools used together — de-essing is dynamic EQ narrowly scoped to sibilance; broader dynamic EQ on a vocal or instrument handles other frequency-dependent problems a dedicated de-esser isn't built for.

**Setting the threshold to catch every instance of a problem frequency, including musically intentional ones.** `electric_blues.md`'s "let tone open up naturally as playing intensity increases" only works if the dynamic EQ is tuned to enhance that natural behavior rather than clamp it down every time it occurs — an overly aggressive threshold defeats the expressive effect the genre is using the technique to achieve.

## Cross-References

- `knowledge_base/genres/country/country_pop.md` and `knowledge_base/genres/classical/choral_music.md` — de-essing as the vocal/choir-specific case of dynamic EQ
- `knowledge_base/genres/classical/classical_period.md` — dynamic EQ ducking string resonance only at fortissimo intensity
- `knowledge_base/genres/rock/electric_blues.md` — dynamic EQ allowing guitar tone to open up with playing intensity rather than suppressing it
- `knowledge_base/genres/metal/djent.md` and `knowledge_base/genres/edm/bass_house.md` — dynamic EQ for extended-range and sub/mid-bass low-end management
- `knowledge_base/genres/edm/vocal_trance.md` — dynamic EQ as an automated substitute for manual vocal-vs-pad EQ automation
- `knowledge_base/genres/rock/soft_rock.md` and `knowledge_base/genres/rock/christian_rock.md` — dynamic EQ and de-essing used together as complementary vocal-clarity tools
- `knowledge_base/mixing/eq/frequency_masking.md` — the static-EQ diagnostic this technique extends into the time/intensity dimension
