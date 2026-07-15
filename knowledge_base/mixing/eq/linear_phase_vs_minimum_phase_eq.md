---
technique_name: "Linear-Phase vs. Minimum-Phase EQ"
category: eq
problem_solved: "Phase distortion or smearing introduced by EQ becoming audible (transient softening, comb-filtering when summed with a duplicate/related signal) in contexts sensitive enough that it matters — versus the added latency and pre-ringing artifacts that come with avoiding it"
parameters:
  minimum_phase_behavior: "Standard analog-modeled EQ behavior — every boost or cut introduces a small, frequency-dependent phase shift around the affected frequencies, with effectively zero added latency"
  linear_phase_behavior: "Uses FFT-based processing to apply gain changes with no phase shift at all, at the cost of algorithmic latency (typically several milliseconds to tens of milliseconds) and potential pre-ringing on transients near a steep cut"
  when_linear_matters: "Mastering-bus and parallel-signal-path contexts where phase coherence between processed and unprocessed (or two differently-processed) copies of a signal must be preserved"
  when_minimum_phase_is_preferable: "Real-time tracking/monitoring (latency-sensitive), and single-channel processing on transient-heavy material where pre-ringing would be more audible than the minimum-phase EQ's own phase shift"
signal_chain_position: "Mix-bus or mastering-stage EQ where phase coherence across the full signal or between parallel paths matters; minimum-phase EQ remains the default for per-channel mixing work"
genre_applicability: []
related_techniques:
  - eq_matching
  - tilt_eq
  - subtractive_eq
tags: ["linear-phase", "minimum-phase", "phase-distortion", "mastering-eq", "pre-ringing"]
---

# Linear-Phase vs. Minimum-Phase EQ

This is a technical-implementation distinction rather than a genre-driven aesthetic choice, and it's worth saying plainly: no entry in this knowledge base's genre corpus discusses linear-phase or minimum-phase EQ by name. Genre entries describe *what* tonal balance a mix or master should have (see `additive_eq.md`, `subtractive_eq.md`, and `tilt_eq.md` for genre-grounded coverage of that), but not which phase-behavior category of EQ algorithm should be used to get there — that choice sits one level below genre aesthetics, in the mixing engineer's general technical toolkit. What follows is general audio-engineering theory, included because it directly explains *how* the EQ moves documented elsewhere in this knowledge base actually behave once applied.

## Why EQ Introduces Phase Shift At All

Any EQ built on a conventional analog-modeled filter design (the type used in the overwhelming majority of channel-strip and mixing EQs) works by combining delayed and non-delayed versions of a signal to reinforce or cancel specific frequencies — and that delay is, by definition, a phase shift. This is called minimum-phase behavior: the phase shift is concentrated around the frequencies being boosted or cut, it happens with effectively no added latency, and it's the same behavior a physical analog EQ circuit (or an equalized loudspeaker, or a room) exhibits. For the vast majority of individual-channel EQ moves — the presence boosts, high-pass filters, and subtractive cuts documented throughout this knowledge base's genre entries — minimum-phase EQ is the default and the phase shift it introduces is either inaudible or is itself part of the EQ's characteristic sound (many "vintage-style" analog EQ emulations lean into this phase behavior as part of their tonal identity).

## What Linear-Phase EQ Trades For

Linear-phase EQ uses a fundamentally different implementation — typically FFT-based (Fast Fourier Transform) convolution — to apply a gain curve to a signal with zero phase shift at any frequency. The tradeoff is twofold: linear-phase processing introduces algorithmic latency (the plugin has to look ahead at a block of upcoming audio before it can output a phase-accurate result, typically a few milliseconds up to tens of milliseconds depending on the plugin's FFT window size), and it can produce audible pre-ringing — a soft, smeared artifact that appears *before* a sharp transient when a steep linear-phase cut or boost is applied near that transient's frequency content. This pre-ringing is a direct consequence of enforcing zero phase shift: a filter that doesn't shift phase at all has to "spread" its effect symmetrically in time around the frequency event, including backward into the moments just before it.

## When the Distinction Actually Matters

The practical case for linear-phase EQ is phase coherence between related signal paths — most commonly at the mastering-bus stage, or anywhere a signal is being processed in parallel with an unprocessed or differently-processed copy of itself. If a minimum-phase EQ shifts the phase of one path but not the other, summing them back together can produce audible comb-filtering (frequency-dependent cancellation) that a phase-coherent linear-phase EQ would avoid entirely. This connects directly to techniques documented elsewhere in this knowledge base that rely on summing parallel signal paths: `parallel_compression.md`'s blended dry/wet drum bus and `saturation_as_mix_glue.md`'s parallel saturation sends are both scenarios where phase mismatch between the two paths — introduced by any minimum-phase processing inserted on only one of them — could degrade the blend, making linear-phase EQ (if EQ is needed on just one path) the safer choice in that specific configuration.

## Why Minimum-Phase Remains the Default for Most Mixing Work

Despite linear-phase's phase-coherence advantage, it isn't the default choice for general per-channel mixing EQ, for two practical reasons documented in general engineering practice: the added latency makes minimum-phase EQ the only sensible choice for tracking or live monitoring, and the pre-ringing artifact — while usually subtle — can be genuinely audible on sharply transient material (drums, plucked strings, percussive vocal consonants) when a steep linear-phase cut sits near the transient's frequency content. Since most of the EQ moves documented across this knowledge base's genre corpus are per-channel, non-parallel-path decisions on exactly this kind of transient-rich material (drum bus carving, guitar cuts, vocal presence boosts), minimum-phase EQ is the implicit default throughout — the distinction becomes a deliberate choice specifically in the narrower mastering-bus and parallel-path contexts described above.

## Common Mistakes

**Reaching for linear-phase EQ as a general-purpose "higher quality" default.** The zero-phase-shift property only matters when phase coherence between related signal paths is actually at stake — using linear-phase EQ on a single, non-parallel channel trades away latency and risks pre-ringing for a phase-accuracy benefit that has no signal path to actually apply to.

**Not accounting for linear-phase latency when it's inserted on only one of several summed paths.** If a linear-phase EQ is added to one parallel path but not another, the latency mismatch (not just phase) between the two paths can itself cause timing-related smearing when they're summed back together — matching latency (via delay compensation) across all paths is necessary once any one of them uses linear-phase processing.

**Applying a steep linear-phase cut close to a transient-heavy element's fundamental.** This is the classic pre-ringing trigger — a steep cut near a kick or snare's fundamental frequency can produce an audible soft "whoosh" just before the hit, which is more objectionable on that material than the minimum-phase alternative's own phase shift would have been.

## Cross-References

- `knowledge_base/mixing/compression/parallel_compression.md` — a parallel-path blending scenario where phase coherence between paths is directly relevant to this choice
- `knowledge_base/mixing/saturation/saturation_as_mix_glue.md` — another parallel-send context where minimum-phase EQ on only one path could introduce a phase mismatch
- `knowledge_base/mixing/eq/eq_matching.md` — spectral-matching EQ implementations are commonly linear-phase, since matching curves are often broad, mastering-stage moves
- `knowledge_base/mixing/eq/tilt_eq.md` — another broad, mastering-stage EQ tool where the phase-behavior choice is most likely to be a deliberate decision
