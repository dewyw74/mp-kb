---
plugin_name: "Steven Slate Drums 5"
developer: "Steven Slate Audio"
category: "sampler"
type: "acoustic drum sampler/rompler with pre-processed, mix-ready kit tones"
cpu_usage: "medium"
best_genres:
  - heavy_metal
  - classic_rock
  - pop
  - hip_hop
  - country_pop
strengths:
  - "Library specs run deep for a fast-workflow tool: 84 kicks, 77 snares, 58 toms, 11 hi-hats, 6 rides, 14 crashes, 4 splashes, 3 chinas, and additional percussion/SFX, all recorded at 24-bit with up to 24 velocity layers per instrument and 12 alternate (round-robin) hits per velocity layer to avoid identically repeated triggers."
  - "148+ preset kits arrive pre-balanced, compressed, and tuned toward a big, already-mixed drum tone, so a kit can be dropped into a session and sit usably in a mix with comparatively little further mixing work — SSD5's defining trade-off against a build-from-scratch multi-mic tool like Superior Drummer 3."
  - "The mixer can output up to 16 stereo and 16 mono channels (48 channels total, DAW-dependent) for full discrete routing of individual mics/kit pieces out to the DAW's own mixer and plugins when more control than the pre-balanced kits provide is needed."
  - "Per-instrument, bypassable ADSR shaping — addressable independently per mic or across all mics on an instrument — allows attack/decay/sustain/release and sustain-phase volume shaping directly on a sampled hit without needing an external transient shaper."
  - "2,400+ grooves played by real drummers plus Groove AI, which analyzes a song's audio and recommends a matching MIDI groove, speed up finding an appropriate pattern for a given track."
weaknesses:
  - "SSD5 is a MIDI-triggered sampler, not a drum-audio replacer/reinforcement tool — that is a separate Steven Slate Audio product, Trigger 2. SSD5 cannot itself analyze and retrigger an existing recorded drum track the way Superior Drummer 3's audio-to-MIDI engine or a dedicated trigger plugin can."
  - "The pre-balanced, already-processed character of its kits — SSD5's biggest workflow advantage — is also a limitation for a producer who wants to build a drum tone entirely from raw, unprocessed multi-mic captures the way Superior Drummer 3's library allows."
alternatives:
  - "Toontrack Superior Drummer 3 (see `toontrack_superior_drummer_3.md` — raw multi-mic library for building a drum tone from scratch, plus an audio-to-MIDI engine for converting real performances)"
  - "XLN Audio Addictive Drums 2 (see `xln_audio_addictive_drums_2.md` — comparable workflow speed via genre-targeted ADpaks with a more customizable mixer)"
  - "Native Instruments Battery 4 (see `native_instruments_battery.md` — cell-based one-shot sampler for programmed/chopped kits rather than a full sampled acoustic kit)"
recommended_settings:
  - "Fast mix-ready drum bed: load a genre-matched preset kit, use Groove AI to get a starting MIDI groove suggestion from a reference audio track, and lean on the kit's existing pre-balance rather than rebuilding a mix chain from raw mic channels — per `knowledge_base/mixing/compression/drum_bus_compression.md`, any further bus glue should stay light (2-4dB) since the kit itself is already substantially compressed."
  - "Discrete routing for further mix work: route individual kit pieces/mics out to separate DAW channels via the up-to-16-stereo/16-mono output configuration when a track needs custom EQ or compression per element beyond what the pre-balanced kit provides."
common_uses:
  - "Fast, already-mixed acoustic drum programming for rock, metal, and pop productions where turnaround speed matters"
  - "Groove-matched MIDI drum programming using Groove AI's audio-informed suggestions"
  - "Punchy, radio-ready drum beds for hip-hop, trap, and modern pop productions"
tags: ["steven-slate-drums", "ssd5", "sampler", "drum-sampler", "rompler", "acoustic-drums", "mix-ready", "metal", "pop"]
---

# Steven Slate Drums 5

Steven Slate Drums 5 (SSD5, Steven Slate Audio) is an acoustic drum sampler built on the premise that its kits should already sound close to a finished record: 148+ preset kits arrive pre-balanced, compressed, and tuned, drawn from a library of 84 kicks, 77 snares, 58 toms, and matching cymbals/percussion, each sampled at up to 24 velocity layers with 12 round-robin alternate hits per layer. It's the fastest-to-a-usable-mix option among this knowledge base's acoustic drum-sampler entries, trading the from-scratch multi-mic depth of Superior Drummer 3 and the ADpak-driven customization of Addictive Drums 2 for kits that need comparatively little additional mixing.

## Sound Character and Strengths

SSD5's kits are voiced to sit in a mix with minimal extra work — the 148+ presets are already balanced and compressed toward a big, punchy, radio-ready tone rather than delivered as raw, unprocessed multi-mic captures requiring a mixing pass. That's supported by real sampling depth underneath the pre-balance: up to 24 velocity layers per instrument with 12 alternate hits per layer keeps repeated hits from sounding identically triggered, and a bypassable per-mic ADSR gives attack/decay/sustain/release shaping directly on a sampled hit when further shaping is wanted. The mixer's up-to-16-stereo/16-mono discrete output routing means a producer isn't locked into the pre-balanced blend if a track needs individual kit pieces routed out to the DAW for custom processing. Groove AI — which listens to a reference audio track and recommends a matching MIDI groove from the 2,400+-groove library — is a workflow feature aimed squarely at the same speed-to-finished-drum-bed goal as the pre-balanced kits.

## Weaknesses

SSD5 is a MIDI-based sampler, not a drum-replacement/reinforcement tool for existing audio recordings — that function lives in Steven Slate Audio's separate Trigger 2 plugin, so a producer working from a recorded acoustic drum take rather than programming from scratch needs a different tool (or Superior Drummer 3's audio-to-MIDI engine) to bring that performance in. The same pre-balanced, already-processed character that makes SSD5 fast is a constraint for a producer who specifically wants to build a drum tone up from raw, unprocessed multi-mic material, since that raw layer isn't really what SSD5 is built to expose.

## Common Mistakes

Stacking further heavy bus compression on top of an SSD5 preset kit as if it were an unprocessed source — the kits are already substantially compressed, so per `knowledge_base/mixing/compression/drum_bus_compression.md`'s documented moderate glue range (roughly 2-4dB gain reduction), additional bus processing should stay light or the drum bus can end up over-compressed and pumping. Also common: reaching for SSD5 expecting drum-replacement/reinforcement functionality on an existing recorded take — that workflow belongs to Trigger 2, a separate product, not to SSD5's MIDI-triggered sampler engine.

## Cross-References

- `knowledge_base/mixing/compression/drum_bus_compression.md` — the moderate glue-compression range appropriate for SSD5's already-processed kits, versus the deeper compression a raw multi-mic source can take
- `knowledge_base/vst_database/toontrack_superior_drummer_3.md` — the raw multi-mic, build-from-scratch alternative, including audio-to-MIDI conversion of real performances
- `knowledge_base/vst_database/xln_audio_addictive_drums_2.md` — a comparably fast-workflow alternative built around genre-targeted ADpak kits with a more customizable mixer
- `knowledge_base/vst_database/native_instruments_battery.md` — the cell-based, one-shot drum sampler counterpart for chopped/programmed kits rather than a full sampled acoustic kit
