---
workflow_name: "Vocal Tuning Naturalness and Comping Order Philosophy"
daw: "generic"
category: "recording"
goal: "Sequence comping and pitch correction correctly, and set correction intensity appropriately for the genre, so the tuned vocal reads as either invisibly natural or deliberately stylized on purpose, rather than accidentally over-processed or built on a flawed take selection."
steps:
  - "Comp the best take or phrase selection first, evaluating candidate takes on their real, unprocessed pitch and timing, before applying any pitch correction to the comped result."
  - "Avoid spending correction effort on takes that may be discarded during comping, since tuning a take before it's chosen wastes work and can bias take selection toward whichever take happens to already sound more in tune."
  - "Decide explicitly whether the goal is transparent (inaudible) correction or stylized (audible, deliberate) correction before touching any correction parameters, since the two goals call for opposite settings."
  - "Set retune speed as a genre and stylistic decision, not a default — slow, natural-sounding retune for transparent correction, fast, audible snap for a deliberate stylized effect."
  - "Use note-accurate, graphical correction that preserves the take's natural vibrato, scoop, and inflection for transparent correction rather than rigidly quantizing every note to a flat target pitch."
  - "Treat small, consistent pitch deviations as a normal and often expressive part of a human vocal performance, not as errors that need to be corrected to a hard, mathematically centered pitch."
  - "Apply correction more conservatively on exposed, sustained notes where processing artifacts are easiest to hear, and more liberally on fast runs or busy phrases where they're harder to detect."
  - "Listen back to the corrected vocal against the original, unprocessed take specifically for naturalness, not only for pitch accuracy on a graphical display."
  - "Re-open the comp decision if correction reveals a problem in the chosen take (a phrase that needed heavier correction than expected, or that still sounds wrong even once in tune) rather than forcing a fix onto a take that was never the strongest option."
  - "Judge what counts as 'invisible' correction against the conventions of the genre being produced, not against a single universal technical standard, since genres differ sharply in how much correction reads as transparent versus already stylized."
related_plugins: []
tags:
  - "pitch-correction"
  - "auto-tune"
  - "comping"
  - "vocal-tuning"
  - "retune-speed"
  - "recording"
  - "workflow"
  - "generic"
---

# Vocal Tuning Naturalness and Comping Order Philosophy

Pitch correction and comping are often treated as two steps in an arbitrary order, applied in whatever sequence a session happens to fall into. They aren't interchangeable in order, and getting the sequence wrong routinely produces worse results than either step done carelessly on its own: tuning a take before deciding whether it's even the take worth keeping wastes effort and quietly distorts the comping decision itself. This entry covers the DAW-agnostic reasoning behind comping-before-tuning, how to calibrate correction intensity to a genre's expectations, and the specific risk of over-correcting natural pitch variation that was actually part of what made the performance work.

## Why Comping Should Happen Before Pitch Correction

Comping is a judgment about performance — which take, or which phrase from which take, carries the most conviction, the best phrasing, the most in-tune-and-in-time delivery relative to the others available. Pitch correction changes the very thing comping is supposed to judge: a take's raw pitch accuracy. Tuning takes before comping them risks making every candidate take sound similarly "correct" on a pitch level, which erases one of the more useful signals comping is meant to use, and can quietly bias the comparison toward whichever take needed the least correction to begin with rather than whichever take actually had the best feel, phrasing, and energy. It also means correction work gets done on material that may be discarded entirely once the comp is assembled — effort spent tuning a verse take that ultimately loses out to a different take in the comp is effort that produced nothing usable. Comping first, on the raw takes, and applying pitch correction only to the final comped result keeps the take-selection judgment honest and avoids wasted correction work. `knowledge_base/daw/workflow/comping_best_take_selection_philosophy.md` covers the comping judgment itself in detail; this entry picks up from the point where a final comp has already been assembled and is ready for tuning.

## Transparent vs. Stylized: Deciding Intent Before Touching Parameters

Before any correction parameter gets touched, the more important decision is which of two fundamentally different goals is being pursued. Transparent correction aims to be inaudible as an effect — the listener should come away with the impression of an unaided, skillfully in-tune performance, with the correction itself never announcing its presence. Stylized correction is the opposite: it foregrounds the correction as an audible, deliberate texture, sometimes as an explicit melodic or rhythmic device in its own right. These two goals call for close to opposite settings across nearly every relevant parameter — retune speed, how much natural pitch drift and vibrato is preserved versus flattened, and how rigidly notes get pulled to a quantized target. Setting parameters before deciding which goal is in play is how correction ends up in the worst of both worlds: too aggressive to stay invisible, too conservative to read as a deliberate stylistic choice. `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` documents how sharply genres split on this choice — some build their entire vocal identity around audible, foregrounded correction, others treat any audible correction as actively damaging to the genre's authenticity, and a few genres deliberately use both approaches on different vocal elements within the same track.

## Retune Speed as a Genre and Stylistic Choice, Not a Default

Retune speed — how quickly a correction tool pulls a note to its target pitch — is one of the most consequential single parameters in this decision, and it should never be left at a default setting without a deliberate reason. A slow retune speed follows the natural pitch contour of a note closely, correcting the overall center of a note's pitch while leaving its natural vibrato, scoop into pitch, and expressive drift mostly intact — this is the setting transparent, natural-sounding correction is built on. A fast retune speed pulls pitch to its target almost immediately, flattening vibrato and expressive drift into a rigid, audibly quantized pitch — this is the mechanism behind the deliberately robotic, audible-effect sound associated with heavily stylized vocal production. Neither setting is more "correct" than the other; the right choice is whichever one matches the genre and the specific artistic intent for that vocal, decided in advance rather than arrived at by leaving a plugin on its default.

## The Risk of Over-Correcting Natural Expressive Pitch Variation

Even when transparent correction is clearly the goal, it's easy to over-correct. Human vocal performances are not perfectly pitch-centered by nature, and much of what makes a performance sound alive — a note that scoops slightly up into pitch, a held note that drifts a few cents as breath support changes, a slightly flat delivery on an emotionally loaded phrase — is not a flaw to be corrected out but part of the expressive content of the performance itself. Correcting every one of these small deviations to a mathematically flat target pitch can leave a vocal that is technically more "in tune" by a pitch-detection algorithm's standard and simultaneously less convincing and less human to a listener, because some of what read as expressive imperfection has been quietly removed along with the genuine pitch errors. The goal of transparent correction is a performance that still sounds like a person singing, just without the specific pitch mistakes that would otherwise be distracting — not a performance flattened to the pitch-perfect output of an algorithm. This is why note-accurate, phrase-by-phrase correction that preserves vibrato and natural contour generally serves transparent correction better than a blanket, uniformly aggressive setting applied across an entire vocal.

## Judging "Invisible" Correction by Genre Convention, Not a Universal Standard

What counts as inaudible, "transparent" correction is itself a moving target defined by genre convention rather than a fixed technical threshold. A correction intensity that would read as suspiciously perfect and over-processed in a genre built around raw, unaided vocal authenticity might register as entirely normal, expected polish in a genre where flawless, heavily corrected vocals are the established convention. Judging whether a correction pass is "invisible enough" means listening with the target genre's own conventions in mind, not applying one universal standard of naturalness to every vocal regardless of style.

## Common Mistakes

**Tuning every take before comping instead of comping first.** This wastes correction effort on takes that may be discarded and can quietly bias take selection toward whichever take needed the least correction rather than whichever take actually performed best.

**Leaving retune speed at a default setting without deciding on transparent versus stylized intent first.** A default setting is rarely the right setting for either goal; it should be a deliberate choice made before any other correction parameter is touched.

**Correcting every small pitch deviation to a flat, mathematically centered target.** This risks removing genuine expressive content — vibrato, scoop, natural drift — along with real pitch errors, leaving a technically accurate but less convincing performance.

**Applying the same correction intensity across an entire vocal regardless of phrase exposure.** Heavy-handed correction is far more likely to be audible on an exposed, sustained note than on a fast, busy run, and treating every phrase identically ignores that difference.

**Judging naturalness only from a graphical pitch display instead of by ear.** A correction pass that looks perfectly centered on a pitch graph can still sound processed and unnatural, and a pass that looks imperfect on the graph can still sound completely convincing; the ear is the actual test, not the display.

## Cross-References

- `knowledge_base/daw/workflow/comping_best_take_selection_philosophy.md` — the take-selection judgment that should be finished before pitch correction begins.
- `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` — the genre-by-genre split between transparent, corrective-only pitch correction and audible, stylized use, including which genres treat each approach as identity-defining.
- `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` — where pitch correction sits relative to de-essing, compression, and other vocal-chain processing depending on transparent versus stylized intent.
