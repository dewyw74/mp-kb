---
title: "Oscillator Sync"
synthesis_method: "oscillator-sync"
tags:
  - "hard-sync"
  - "oscillator-sync"
  - "master-slave-oscillator"
  - "sync-sweep"
  - "lead-synthesis"
  - "analog-synthesis"
---

## What Oscillator Sync Is

Oscillator sync (almost always "hard sync" in practice) links two oscillators so that one — the **slave** — is forcibly restarted at the beginning of its waveform cycle every time the other — the **master** — completes a cycle of its own. The master's frequency is what the ear perceives as the note's pitch; the slave's own frequency knob no longer controls pitch at all once synced, because it never gets to complete a full cycle at its own rate — instead, sweeping the slave's frequency control reshapes *where within its cycle* it gets cut off and restarted each time the master resets it, which reshapes the resulting waveform's harmonic content without changing the perceived pitch.

Circuit-level, this was originally implemented directly in the oscillator hardware: on the CEM3340 VCO chip used in synthesizers like the Sequential Prophet-5, a positive-going pulse from the master oscillator is fed into a dedicated sync input pin that shorts the slave's internal timing capacitor to ground, forcing its waveform to restart exactly on the master's rising edge. Because the reset happens mid-cycle at an unpredictable phase relative to the slave's own natural period, the resulting waveform is a jagged, irregular composite that changes shape continuously as the slave/master frequency ratio is swept — this constantly shifting waveshape is the source of hard sync's instantly recognizable "throaty," vowel-like, sweeping tone quality.

## Why Sweeping Sync Sounds the Way It Does

At a 1:1 slave:master ratio, hard sync does nothing audible — the slave would complete its own cycle at exactly the moment it gets reset, so no early truncation occurs. As the slave's free-running frequency is tuned progressively higher than the master's, it gets cut off earlier and earlier in its own cycle before being reset, producing a waveform with a rapidly changing harmonic spectrum — additional harmonics appear and shift as the cutoff point moves. Slowly sweeping the slave oscillator's tuning while holding a note produces the technique's signature effect: a moving, vowel-like formant sweep layered on top of a fixed fundamental pitch, distinct from a filter sweep because the *harmonic content itself* is being generated differently at each moment rather than an existing spectrum being progressively removed. This is why sync sweeps read as more aggressive and more "alive" than an equivalent filter sweep on a static waveform — the technique is generating new harmonic material continuously, similar in spirit (though mechanically unrelated) to how FM's modulation index sweep continuously changes generated sideband content.

Hard sync was popularized on late-1970s/early-1980s analog polysynths, most famously the Sequential Prophet-5 and early Oberheim instruments, prized "for a more metallic and aggressive timbre" especially on lead sounds — The Cars' "Let's Go" is a widely cited example of the Prophet-5's hard-sync lead tone in a commercial recording.

## Where Oscillator Sync Appears in the Genre Corpus

Oscillator sync by name does not turn up as a documented technique anywhere in the current `knowledge_base/genres/` corpus — searches for "sync," "hard sync," and related terms return no genre-file hits. This is a real gap rather than an oversight to paper over: hard sync is a real, well-established, historically significant analog synthesis technique (heard throughout 1980s synth-pop, new wave, and trance/hard-dance lead and bass patches in the decades since), but it has not yet been documented as a named technique in any current genre file's sound-design section. Where the corpus discusses genres that plausibly use sync-swept leads — `knowledge_base/genres/edm/trance.md` and `knowledge_base/genres/edm/hard_trance.md`, for instance, document supersaw and virtual-analog lead patches extensively — the sync mechanism itself isn't called out; those files describe unison/detune stacking and resonant filter movement instead (see `unison_and_detune_stacking.md` and `filter_type_comparison.md`). Reason from general synthesis knowledge for sync-specific guidance rather than treating any genre file as documenting it, and treat this as a candidate gap for future genre-file expansion rather than an assumption to present as sourced fact.

## Practical Sync Sound Design

- **Classic sync lead**: two sawtooth oscillators, slave detuned progressively sharp of the master and swept slowly (by hand or with a slow LFO/envelope) for the moving, vowel-like formant sweep that defines the sound.
- **Sync plus filter**: layering a resonant lowpass sweep on top of a sync sweep compounds two independently moving harmonic-content sources — this combination, common on analog and virtual-analog leads, is more aggressive and harder to fully "tame" than either technique alone, so it typically needs restraint on resonance and sync-sweep depth to avoid harshness.
- **Sync for basses**: a subtler, narrower-range sync sweep (small slave/master ratio movement) adds growl and edge to a bass patch without the more extreme vowel-sweep character used on leads.
- **Soft sync vs. hard sync**: some modern virtual-analog and wavetable synths offer a "soft sync" mode that resets the slave's phase less abruptly (allowing partial cycles to complete), producing a gentler, less aliased version of the same effect — useful when hard sync's full harshness is unwanted but some of its movement character is desired.
- **Digital aliasing caution**: like FM at high index, sync-generated waveforms contain fast, discontinuous jumps that can alias badly in naively-implemented digital oscillators; modern soft-synths apply band-limiting or oversampling specifically to keep sync patches clean at high pitches.

## Cross-References

- `knowledge_base/sound_design/synthesis/subtractive_synthesis.md` — the filter-based sweep technique sync is most often compared against and layered with.
- `knowledge_base/sound_design/synthesis/fm_synthesis.md` — a mechanically different but perceptually related technique for generating continuously shifting harmonic content via modulation rather than a forced waveform restart.
- `knowledge_base/sound_design/synthesis/unison_and_detune_stacking.md` — the more heavily genre-documented analog-lead-thickening technique that frequently appears alongside (but is technically distinct from) sync in trance/hard-dance lead patches.
- `knowledge_base/genres/edm/trance.md` and `knowledge_base/genres/edm/hard_trance.md` — genres whose lead sound design plausibly draws on sync-adjacent aggressive analog lead character, though the current files document unison/detune and filter technique rather than sync specifically.
