---
technique_name: "Dithering and Bit-Depth Conversion"
category: "other"
problem_solved: "Truncating a high-resolution master (typically 24-bit or higher) down to a lower delivery bit depth (typically 16-bit for CD or some legacy distribution formats) without dithering, which introduces audible quantization distortion in quiet passages, reverb tails, and fades — a harsh, gritty artifact rather than the smooth noise floor proper dithering produces"
parameters:
  when_dither_is_needed: "Only when the bit depth is actually being reduced — going from a 24-bit (or higher) working/master file down to a lower final delivery bit depth, most commonly 16-bit. Staying at 24-bit end to end needs no dithering step."
  apply_once_at_final_export: "Dither should be applied exactly once, at the very last stage of processing, on the final bit-depth-reducing export — any further processing (EQ, compression, limiting, gain changes) applied after dithering undoes its statistical properties and reintroduces quantization distortion"
  noise_shaping: "Noise-shaped dither (e.g. POW-r-style algorithms) redistributes quantization noise toward less audible frequency ranges rather than leaving it flat across the spectrum; a safe general-purpose default for music material going to 16-bit"
signal_chain_position: "The final step of the mastering chain, applied only at bit-depth-reducing export/bounce — after all EQ, dynamics, and stereo processing is complete, with nothing else applied afterward"
genre_applicability:
  - slow_jams
  - glitch
related_techniques:
  - vinyl_mastering_considerations
  - final_mono_and_translation_check
tags: ["dithering", "bit-depth", "format", "quantization", "noise-shaping", "mastering", "other"]
---

# Dithering and Bit-Depth Conversion

This is the thinnest entry in this set, and it's worth being direct about why: dithering and bit-depth conversion are a purely technical, format-delivery-stage concern that doesn't vary by musical genre the way EQ targets, dynamics philosophy, or stereo width do — genre files in this corpus were written to document creative and tonal conventions, not universal signal-chain housekeeping steps like this one. Only two genre files in the entire corpus touch bit depth at all, and both use it as a deliberate lo-fi aesthetic choice rather than describing the standard dithering practice this entry is actually about.

## The Two Genre-File Mentions, and Why They're Adjacent Rather Than Directly On-Topic

`slow_jams.md` documents deliberately retained low-bit-depth character as a texture: "Sampler-era bit-depth and tape-style grain intentionally retained for warmth." This is a useful adjacent data point — it confirms that reduced bit-depth artifacts are recognized in this corpus as an audible, intentional aesthetic choice in some genres — but it describes keeping the grain of an *already bit-reduced source* (period sampling hardware) rather than the mastering-stage dithering process used when reducing a modern high-resolution master down to a lower delivery bit depth. `glitch.md` names "bit depth" as one of several glitch-plugin automation parameters ("buffer length, bit depth, repeat probability") manipulated live as a compositional tool — again, a related concept (deliberately audible bit-depth reduction as an effect) rather than the delivery-format dithering technique itself.

## Why Dithering Doesn't Vary by Genre the Way Other Mastering Decisions Do

Every other entry in this set of mastering technique files documents a genre-dependent decision — how much sub-bass, how wide the stereo image, how much dynamic range to preserve. Dithering is different: the correct dithering behavior is determined entirely by the technical delivery requirement (what bit depth is the final output, and is it lower than the working bit depth), not by genre convention. A dark-ambient master and a complextro master targeting wildly different LUFS and dynamic-range goals (see `inter_track_gain_staging.md` for those figures) both need the identical dithering treatment if they're both being bounced from a 24-bit master down to 16-bit for CD delivery — the genre-specific mastering decisions happen upstream of this step, and dithering itself is applied uniformly afterward.

## Standard Practice

Dither is needed only at an actual bit-depth reduction — most commonly the final bounce from a 24-bit (or higher) master down to 16-bit for CD or a legacy 16-bit delivery target; a 24-bit-to-24-bit delivery chain needs no dithering step at all. It should be applied exactly once, at the literal last stage of the export chain, because any processing applied after dithering (even a small gain adjustment) disturbs the dither's statistical noise floor and reintroduces the quantization distortion it was added to prevent. Noise-shaped dither, which pushes quantization noise toward frequency ranges the ear is less sensitive to rather than leaving it flat, is the safe general-purpose choice for music material being reduced to 16-bit; flat (non-shaped) dither is often sufficient for less aggressive bit-depth reductions where the noise floor is already very low.

## Common Mistakes

**Applying dither, then making further gain, EQ, or limiter adjustments afterward.** This is the single most consequential mistake with this technique: any processing after the dithered bit-depth reduction reintroduces the exact distortion dithering exists to prevent, effectively wasting the step.

**Applying dither multiple times across a processing chain, or on every bounce regardless of whether bit depth actually changed.** Dither adds a small amount of noise; applying it repeatedly (once per intermediate bounce, rather than once at final delivery) accumulates that noise unnecessarily.

**Confusing intentional, audible lo-fi bit-depth reduction (as in `slow_jams.md`'s and `glitch.md`'s deliberate aesthetic use) with the transparent, inaudible dithering process used for standard-resolution delivery.** These are different tools serving opposite goals — one makes bit-depth reduction audible on purpose, the other exists specifically to make it inaudible.

## Cross-References

- `knowledge_base/mastering/format/vinyl_mastering_considerations.md` — a different format-specific mastering-stage concern with a similarly technical, largely genre-independent character
- `knowledge_base/mastering/sequencing/inter_track_gain_staging.md` — illustrates the genre-dependent loudness range dithering is applied uniformly underneath, regardless of target LUFS
- `knowledge_base/genres/r_and_b/slow_jams.md`, `knowledge_base/genres/electronic/glitch.md` — the corpus's only two bit-depth mentions, both describing deliberate aesthetic bit-depth reduction rather than standard delivery dithering

Standard dithering and bit-depth-conversion practice (when dither is needed, single-application-at-final-export rule, and noise-shaping behavior) was verified via current mastering-industry references (Waves Audio, Mat Leffler-Schulman Mastering, Spektrum Mastering) rather than sourced from genre files, given the near-total absence of genre-file coverage on this specific technical topic.
