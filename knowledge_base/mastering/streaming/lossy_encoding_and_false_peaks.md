---
technique_name: False Peaks Introduced by Lossy Encoding
category: loudness
problem_solved: "A master that measures true-peak-safe (e.g. -1dBTP) on the exported WAV/FLAC file can still clip after a streaming platform's lossy codec re-encodes it, because the codec's own encode/decode process — not the D/A converter reconstructing the analog waveform — can independently raise peak levels above the source"
parameters:
  mechanism: "Lossy codecs (AAC, MP3, Opus) operate in the frequency domain, breaking audio into blocks and re-synthesizing a time-domain waveform from quantized frequency data on decode; that quantization and resynthesis process is a separate source of peak-level change from the inter-sample reconstruction a D/A converter performs, even though both can push a signal above its originally-measured true peak"
  demonstrated_overshoot: "Documented real-world example: a source file with true peaks at -0.5dBTP encoded through an Ogg Vorbis encoder came out with peaks at +0.2dBTP — clipping in the encoded file despite the source having nearly a half-dB of true-peak headroom to begin with"
  safe_margin: "Industry guidance (EBU R128, Apple Digital Masters, AES recommendations) commonly specifies -1dBTP as a true-peak ceiling for streaming delivery specifically because it needs to survive both DAC-side inter-sample reconstruction and codec-side encode/decode peak growth, not just one or the other"
  relationship_to_dac_intersample_peaks: "This is a related but mechanically distinct phenomenon from the D/A inter-sample peak issue documented in true_peak_and_intersample_peaks.md — that file concerns what happens when converting a digital file to an analog signal for playback; this entry concerns what happens to peak levels purely within the digital lossy-encode/decode process itself, before any D/A conversion occurs"
signal_chain_position: "Final limiter/true-peak stage at export, with headroom set to survive codec re-encoding specifically, not only DAC playback"
genre_applicability:
  - trap
  - dubstep
  - hard_techno
  - pop
  - speedcore
related_techniques:
  - true_peak_and_intersample_peaks
  - platform_normalization_behavior
  - codec_considerations_for_streaming
tags: ["lossy-encoding", "codec", "true-peak", "aac", "opus", "false-peaks", "streaming"]
---

# False Peaks Introduced by Lossy Encoding

`knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` documents why a sample-peak meter can't see the inter-sample overshoots a D/A converter reconstructs during playback. This entry covers a different, related mechanism: lossy codecs themselves — AAC, MP3, Opus — can independently raise a signal's peak level during their own encode/decode process, entirely apart from anything a DAC does. A master that is true-peak-safe on the exported file can still overshoot after a platform transcodes it, and the reason isn't D/A reconstruction — it's the codec's internal quantization and resynthesis.

## How This Differs From the DAC Inter-Sample Peak Mechanism

`true_peak_and_intersample_peaks.md`'s core claim is about analog reconstruction: "the actual analog waveform a D/A converter... reconstructs between samples can overshoot those measured points... A master that reads 0dBFS or just under on a sample peak meter can therefore still produce a reconstructed waveform that exceeds 0dBTP... once actually played back." That mechanism happens at the very end of the chain, at the moment digital audio becomes an analog signal, and it's a property of the D/A converter's filtering, not of any codec.

This entry's mechanism happens earlier and entirely in the digital domain. Lossy codecs work by transforming audio into the frequency domain, quantizing that frequency-domain representation to discard information the codec's psychoacoustic model predicts is inaudible, then resynthesizing a new time-domain waveform from the quantized data on decode. That resynthesis is a lossy, approximate reconstruction of the original waveform — and because it's an approximation rather than an exact copy, the resynthesized waveform's peak level can come out higher than the source's peak level, independent of what a DAC would later do with the decoded file. A documented real-world case makes the scale concrete: a source file with true peaks at -0.5dBTP, run through an Ogg Vorbis encoder, came out the other side with peaks at +0.2dBTP — clipping in the encoded file despite the source starting with nearly half a dB of true-peak headroom already in place. This is the codec's own encode/decode process doing that, not a downstream D/A converter.

## Why the Two Mechanisms Are Related but Not Interchangeable

Both mechanisms can push a signal above its measured true peak, and both are reasons to leave true-peak headroom rather than mastering right up to 0dBTP — which is why the practical guidance (commonly -1dBTP as a ceiling) is similar for both. But treating them as the same problem is a mistake: a master engineered to be safe purely against DAC inter-sample reconstruction (the concern `true_peak_and_intersample_peaks.md` addresses) is not automatically safe against codec-introduced peak growth from AAC or Opus transcoding, because the codec-side mechanism operates on the compressed, quantized representation of the audio rather than on continuous-waveform reconstruction. A master with, say, -1dBTP headroom measured against DAC reconstruction should generally survive codec transcoding too given typical codec-side overshoot magnitudes, but the two checks are conceptually separate risk sources being covered by the same numeric margin, not one check standing in for the other.

## Why This Matters More for Genres Already Running Hot

The practical stakes are highest for masters with the least true-peak margin to begin with. `codec_considerations_for_streaming.md` documents in detail why the knowledge base's loudest, most heavily limited genres (speedcore, hardstyle, riddim, trap, big room house) carry the most codec-interaction risk generally; this entry's false-peak mechanism is a specific instance of that broader risk. A master pushed close to 0dBTP on export has essentially no margin left to absorb any codec-side peak growth on top of whatever margin it already lacks against DAC reconstruction — meaning genres whose mastering philosophy treats heavy limiting as an aesthetic feature rather than something to avoid (as `lufs_targets_by_genre.md`'s loudest tier documents for speedcore, hardstyle, riddim, and big_room_house) are structurally the genres with the least room to survive this specific failure mode without a deliberately conservative true-peak ceiling.

## Practical Guidance

Set the final limiter's true-peak ceiling with both mechanisms in mind rather than either alone — -1dBTP or lower is the common baseline specifically because it's intended to survive both DAC-side reconstruction and codec-side encode/decode peak growth, not because either mechanism alone requires exactly that number. There is no way to directly "meter" codec-introduced peak growth in advance without actually running the file through a target codec's encoder and re-measuring true peak on the decoded result — spot-checking a hot master this way after mastering, rather than assuming a WAV-file true-peak reading is the final word, is the only way to verify this specific risk rather than the DAC-side one already covered by `true_peak_and_intersample_peaks.md`.

## Common Mistakes

**Assuming a true-peak-safe WAV/FLAC export is automatically safe after streaming transcoding.** As the documented -0.5dBTP-to-+0.2dBTP Ogg Vorbis example shows, codec-introduced peak growth is a real, measurable phenomenon distinct from DAC reconstruction, and headroom sufficient for one is not guaranteed sufficient for the other in every case.

**Treating this entry and `true_peak_and_intersample_peaks.md` as documenting the same problem twice.** They describe two different stages of the signal chain — codec encode/decode versus D/A analog reconstruction — that happen to call for a similar numeric safety margin, not one underlying mechanism with two names.

**Never actually verifying true peak on a codec-decoded file.** A sample-peak or even true-peak meter reading on the original WAV/FLAC export doesn't confirm what the file measures after being run through AAC or Opus encoding — that's a separate check.

## Cross-References

- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the D/A converter/playback-side inter-sample peak mechanism this entry is explicitly distinct from, while addressing a similarly-sized true-peak safety margin
- `knowledge_base/mastering/streaming/codec_considerations_for_streaming.md` — the broader set of codec-interaction risks (pre-echo, transient smearing, high-frequency harshness) that this entry's false-peak mechanism sits alongside
- `knowledge_base/mastering/streaming/platform_normalization_behavior.md` — the loudness-normalization behavior that operates independently of, but on the same platforms as, the codec transcoding discussed here
- `knowledge_base/genres/edm/speedcore.md`, `knowledge_base/genres/edm/hardstyle.md`, `knowledge_base/genres/edm/riddim.md`, `knowledge_base/genres/edm/big_room_house.md` — the loudest, least-true-peak-margin genres in the knowledge base, and therefore the most exposed to this specific failure mode
