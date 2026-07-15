---
plugin_name: "Addictive Drums 2"
developer: "XLN Audio"
category: "sampler"
type: "acoustic drum sampler/rompler with genre-focused ADpak kit expansions"
cpu_usage: "medium"
best_genres:
  - indie_rock
  - pop
  - country_pop
  - funk
  - hip_hop
strengths:
  - "The ADpak expansion model: each ADpak is a complete, fully sampled kit recorded by a professional session drummer in a specific named studio — Fairfax Vol. 1 (tracked at Fairfax Recordings, the former Sound City studio in Los Angeles) targets 'ultra-modern, radio-ready rock,' while Fairfax Vol. 2 targets indie, folk, and pop — so genre-appropriate tone comes largely pre-selected rather than built from a single generic kit."
  - "The mixer includes dedicated faders for nine drums, hi-hats, room mics, overhead mics, and an extra processing bus, plus eighteen kit-piece slots with kit-piece linking, putting a real (if more streamlined than Superior Drummer 3's) multi-mic blend within fast reach."
  - "Response and Tone Designer kit-piece controls give precise per-piece control over filter cutoff and velocity-to-volume/filter modulation, round-robin (Alternate mode) on/off, and velocity limiting/offset — shaping how a kit piece responds to MIDI without having to re-edit the MIDI itself."
  - "Runs standalone or as a 64-bit VST/VST3/AU/AAX plug-in across all major DAWs, and its lighter per-kit footprint and more streamlined mixer make it noticeably faster to get from blank track to a usable, genre-appropriate drum sound than Superior Drummer 3's deeper multi-mic signal chain."
weaknesses:
  - "The ADpak model means genre coverage is only as good as the ADpaks a producer owns — the base library covers general rock/pop territory well, but matching Superior Drummer 3's breadth (metal, jazz, Latin, orchestral percussion) requires purchasing additional genre-specific ADpaks piecemeal."
  - "Its mixer, while genuinely multi-mic (room and overhead faders, an extra processing bus), is less granular than Superior Drummer 3's per-mic-position bleed control and full 35-slot effects rack — a trade deliberately made for workflow speed over ultimate mix depth."
alternatives:
  - "Toontrack Superior Drummer 3 (see `toontrack_superior_drummer_3.md` — deeper multi-mic mixing and a larger single core library, at the cost of speed and CPU/disk footprint)"
  - "Steven Slate Drums 5 (see `steven_slate_drums_5.md` — even faster, pre-balanced kits with less mix-level customization)"
  - "Native Instruments Battery 4 (see `native_instruments_battery.md` — cell-based one-shot sampler for chopped/programmed kits rather than a full sampled acoustic drum library)"
recommended_settings:
  - "Fast genre-targeted kit build: load a genre-matched ADpak (e.g. Fairfax Vol. 1 for modern rock, Fairfax Vol. 2 for indie/folk/pop), balance the room and overhead mic faders on the built-in mixer for the desired ambience, and use Response controls to set velocity-to-tone behavior per kit piece instead of manually re-editing MIDI velocities."
  - "Round-robin realism for repetitive patterns: enable Alternate (round-robin) mode per kit piece, particularly on hi-hat and ride parts played at consistent, repetitive velocity, per the approach documented in `knowledge_base/sound_design/sampling/one_shot_layering_and_round_robin_variation.md`."
common_uses:
  - "Fast, genre-targeted acoustic drum programming where a specific named studio/session-drummer tone is the goal, selected via ADpak"
  - "Demo-to-final-mix drum production where workflow speed matters more than Superior Drummer 3-level multi-mic depth"
  - "Studio-quality drum programming across rock, indie, pop, and hip-hop productions"
tags: ["xln-audio", "addictive-drums", "sampler", "drum-sampler", "rompler", "acoustic-drums", "adpak", "rock", "pop"]
---

# Addictive Drums 2

Addictive Drums 2 (XLN Audio) is an acoustic drum sampler built around the ADpak system: complete, professionally recorded kits — each tracked by a session drummer in a specific named studio and voiced toward a specific genre — loaded into a streamlined mixer with dedicated room, overhead, and per-piece processing. Where Superior Drummer 3 hands the producer a single very deep multi-mic library to mix from scratch, Addictive Drums 2's strength is workflow speed: picking the right ADpak gets a genre-appropriate, largely pre-balanced drum tone with far less mixing decision-making.

## Sound Character and Strengths

The ADpak model is the core of Addictive Drums 2's identity. Rather than one generic core kit that has to be shaped toward every genre, each ADpak is its own fully sampled kit recorded in a specific room with a specific drummer and a specific genre target in mind — Fairfax Vol. 1, tracked at the former Sound City studio in Los Angeles, aims at "ultra-modern, radio-ready rock," while Fairfax Vol. 2 targets indie, folk, and pop. That means genre-appropriate tone is largely a kit-selection decision rather than a from-scratch mixing exercise. On top of that, the built-in mixer (nine drum faders, hi-hats, room mics, overheads, and an extra processing bus, with eighteen kit-piece slots) and the Response/Tone Designer kit-piece controls give real per-piece shaping — velocity-to-filter/volume modulation, round-robin toggling, velocity limiting — without requiring MIDI data itself to be re-edited for those effects.

## Weaknesses

Genre breadth is gated by which ADpaks a producer actually owns; the base library plus one or two ADpaks covers rock/pop/indie territory well, but matching Superior Drummer 3's out-of-the-box range across metal, jazz, Latin, and orchestral percussion means buying additional genre-specific ADpaks individually. The mixer, while genuinely multi-mic, is also less granular than Superior Drummer 3's per-mic bleed control and full effects rack — a deliberate trade of ultimate mix depth for speed.

## Common Mistakes

Staying on the stock/base kit for every project regardless of genre, rather than treating ADpak selection as the primary genre-matching decision it's designed to be — the tonal difference between, say, Fairfax Vol. 1's modern rock kit and Fairfax Vol. 2's indie/folk/pop kit is a large part of what the ADpak system is for, and skipping that choice leaves genre-appropriate tone on the table. Also common: leaving round-robin (Alternate mode) off on repetitive hi-hat or ride patterns, which reintroduces exactly the mechanical, identically-repeated-sample problem round-robin sampling exists to solve.

## Cross-References

- `knowledge_base/sound_design/sampling/one_shot_layering_and_round_robin_variation.md` — the round-robin sampling technique Addictive Drums 2's Alternate mode implements per kit piece
- `knowledge_base/vst_database/toontrack_superior_drummer_3.md` — the deeper, multi-mic alternative for full-mix-from-scratch acoustic drum production
- `knowledge_base/vst_database/steven_slate_drums_5.md` — an even faster, more pre-balanced alternative for mix-ready kits
- `knowledge_base/vst_database/native_instruments_battery.md` — the cell-based, one-shot drum sampler counterpart for chopped/programmed kits rather than a full sampled acoustic drum library
