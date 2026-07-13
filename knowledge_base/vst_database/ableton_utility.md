---
plugin_name: "Utility"
developer: "Ableton"
category: "other"
type: "gain-staging and stereo-field utility device (stock Ableton Live: gain, width, mono, phase invert, DC offset removal)"
cpu_usage: "low"
best_genres:
  - house
  - techno
  - hip_hop
  - trance
strengths:
  - "Combines several essential, otherwise-separate gain-staging and stereo-imaging tasks (level trim, stereo width control, mono-summing, phase inversion, bass mono-ing) into one lightweight device."
  - "The dedicated 'Bass Mono' feature directly implements the mono sub-bass discipline documented in `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` — collapsing low-frequency content to mono below a selectable crossover without needing a full mid-side EQ setup."
  - "Included with every edition of Ableton Live, with essentially zero CPU cost, making it practical to place on every channel in a session without hesitation."
  - "Phase invert and mono-sum buttons make quick phase-cancellation troubleshooting fast and non-destructive."
weaknesses:
  - "Not a processing/character tool — Utility doesn't add tone, saturation, or dynamics shaping; it's purely a gain-staging and stereo-field correction device, so it doesn't substitute for EQ, compression, or saturation where those are actually needed."
  - "Its width control is a simple stereo-widening tool rather than the more surgical mid-side EQ capability documented in `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` for frequency-specific stereo decisions."
alternatives:
  - "A dedicated mid-side EQ setup for more surgical, frequency-specific stereo-width decisions beyond Utility's single width knob"
  - "Ableton's Gain device (a simpler single-purpose level-trim-only alternative) when Utility's additional stereo/phase features aren't needed"
recommended_settings:
  - "Mono-safe bass: Bass Mono engaged with the crossover frequency set around 100-150Hz, applied to bass/sub channels per `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md`'s club-system-translation guidance."
  - "Gain staging before a plugin with a fixed optimal input level: Utility as the first device in a chain, trimming level to match the following plugin's designed input range."
common_uses:
  - "Mono-summing sub/bass content for club-system and mono-playback translation"
  - "Quick level trims and gain staging throughout a signal chain"
  - "Phase-invert troubleshooting when two related signals (a layered sample and a re-recorded take, for instance) might be out of phase with each other"
tags: ["utility", "ableton", "stock-device", "gain-staging", "mono-compatibility", "mixing"]
---

# Utility (Ableton Live)

Utility is Ableton Live's first-party gain-staging and stereo-field utility device — not a tone-shaping or dynamics processor, but a combination of level trim, stereo width control, mono-summing, phase inversion, and DC-offset removal in one lightweight, essentially-zero-CPU-cost device. Its role in a signal chain is corrective and structural rather than creative: getting levels and stereo/phase relationships right so the actual tone-shaping tools (EQ, compression, saturation) can do their job on a clean, properly-staged signal.

## Sound Character and Strengths

Utility's most consequential feature for the mixing guidance documented in this knowledge base is its dedicated Bass Mono function — a direct, single-control implementation of the mono sub-bass discipline documented in `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md`, which cites `jungle.md`'s explicit warning about keeping "sub-bass mono and separate from mid-bass/Reese content so both translate on club soundsystems without phase cancellation." Rather than setting up a full mid-side EQ chain to collapse only the low end to mono, Utility's Bass Mono control does this with one crossover-frequency setting.

## Weaknesses

Utility adds no tone or character — it's purely corrective, so it's never a substitute for EQ, compression, or saturation where a signal actually needs tonal or dynamic shaping. Its stereo-width control is also a blunt, single-knob tool rather than the frequency-specific mid-side EQ capability documented in `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` for more surgical stereo-image decisions.

## Common Uses in a Mixing Chain

Placing Utility at the start of a channel's effect chain for level trim (bringing a hot or quiet source to an appropriate working level before further processing) and at the end of a bass/sub channel's chain for Bass Mono are the two most common applications documented across this knowledge base's mixing guidance. Its phase-invert button is also a fast, non-destructive way to check whether two related signals are working with or against each other before committing to a fix.

## Common Mistakes

**Using Utility's width knob for surgical, frequency-specific stereo decisions.** Per `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md`, decisions like "widen only the high end of a pad while keeping the low end mono" need actual mid-side EQ, not Utility's single, broadband width control.

**Skipping Bass Mono on sub/bass channels and relying on panning alone for mono safety.** Panning a bass channel to center doesn't guarantee mono-summed content is actually phase-coherent — Utility's Bass Mono function directly sums the specified low-frequency range to mono, which panning alone doesn't achieve if the source itself has any stereo width below the crossover point.

## Cross-References

- `knowledge_base/mixing/stereo/mid_side_processing_and_mono_compatibility.md` — the mono sub-bass discipline this device's Bass Mono feature directly implements
- `knowledge_base/mixing/stereo/stereo_widening_techniques.md` — the general stereo-widening technique Utility's width knob provides a simple, broadband version of
