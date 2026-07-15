---
plugin_name: "Archetype Series"
developer: "Neural DSP"
category: "amp simulation"
type: "neural-network-modeled guitar/bass amp and effects simulation (artist-collaborated plugin line)"
cpu_usage: "high"
best_genres:
  - heavy_metal
  - hard_rock
  - grunge
  - stoner_rock
  - classic_rock
strengths:
  - "Uses neural-network-based amp/cabinet modeling rather than traditional circuit-modeling or convolution IRs, aiming for a closer match to the captured amp's actual dynamic response and feel rather than a static snapshot."
  - "Each Archetype title is built around a specific artist's amp collection and signal chain (e.g. Gojira, Petrucci, Plini, Nolly), bundling amp, cabinet, and a matched set of stompbox/rack effects tuned for that artist's genre rather than requiring a separate effects chain to be built from scratch."
  - "Eliminates the need for a loud recording room, physical amp, or mic placement to get a usable, mix-ready high-gain or clean guitar tone — directly enabling the DI-guitar, reamp-later workflow documented across this KB's rock and metal genre files."
  - "Products span genre range within the line: some titles (e.g. Petrucci, Plini) emphasize articulate, high-gain clarity for complex/technical playing, while others (e.g. Gojira) are voiced for maximum low-end weight and extreme distortion."
weaknesses:
  - "Higher CPU/DSP cost than a traditional IR-loader or amp-sim plugin, since the neural modeling engine is more computationally demanding than convolution or simpler circuit models."
  - "Each title is tuned around one artist's specific rig and genre, so a metal-voiced Archetype title isn't necessarily the right tool for a clean funk or country tone — matching the specific product to the target genre matters more than with a single general-purpose amp sim."
  - "Requires purchasing (or subscribing to) individual titles or bundles rather than one universal amp-sim product, unlike a single multi-amp modeler plugin."
alternatives:
  - "Kemper-style hardware profiling (referenced alongside Neural DSP in `knowledge_base/genres/metal/heavy_metal.md` as an alternative amp-capture approach)"
  - "STL Tones amp-sim plugins (referenced alongside Neural DSP in `knowledge_base/genres/rock/grunge.md`)"
  - "Traditional IR-loader plus a separate preamp/distortion plugin, for a more manually assembled and lower-CPU signal chain"
recommended_settings:
  - "Modern high-gain metal DI reamping: a metal-voiced Archetype title (e.g. Gojira-lineage), gain pushed for the genre's wall-of-distortion character, cabinet/mic blend adjusted post-capture rather than needing a physical re-mic."
  - "Vintage-informed hard rock/classic rock tone: a more versatile Archetype title with amp voicing pulled toward a classic tube-amp character, paired with the DI-plus-amp-modeled-track layering workflow noted in `knowledge_base/genres/rock/classic_rock.md`."
  - "Technical/progressive playing: an articulate, high-gain-clarity-focused title so fast passages and complex chords stay defined rather than smearing into a wall of gain."
common_uses:
  - "DI guitar reamping and amp/cabinet tone shaping entirely in-the-box, without a physical amp or recording room"
  - "Matching a specific artist-modeled high-gain or clean guitar tone to metal, hard rock, grunge, and stoner rock production"
  - "Building a complete guitar signal chain (amp, cabinet, and matched effects) from one plugin rather than assembling separate stompbox and IR tools"
tags: ["neural-dsp", "archetype", "amp-simulation", "guitar", "reamping", "high-gain"]
---

# Archetype Series (Neural DSP)

The Archetype Series is Neural DSP's flagship line of guitar and bass amp-simulation plugins, each built in collaboration with a specific artist (titles include Gojira, Petrucci, Plini, Nolly, Rabea, Tim Henson, and others) and modeling that artist's actual amp collection, cabinet choices, and effects chain using neural-network-based amp modeling rather than traditional circuit modeling or static impulse responses. Neural DSP is cited generically across this knowledge base's metal and rock genre files as the modern go-to amp-simulation brand for achieving high-gain, mix-ready guitar tones without a physical amp or recording room — `knowledge_base/genres/metal/heavy_metal.md`, `knowledge_base/genres/rock/classic_rock.md`, `knowledge_base/genres/rock/grunge.md`, `knowledge_base/genres/rock/hard_rock.md`, and `knowledge_base/genres/rock/stoner_rock.md` (the latter specifically naming "Neural DSP Fortin/Archetype series") all reference it as the standard modern amp-sim approach. This entry documents the Archetype product line as a whole rather than a single title, since the genre corpus and the product's own positioning treat it as a series of genre/artist-specific tools sharing one underlying modeling technology.

## Sound Character and Strengths

Neural DSP's core technical differentiator is its neural-network modeling approach, which the company positions as capturing an amp's dynamic response and feel more closely than traditional circuit-modeling or convolution-based amp sims. Because each Archetype title is built around one artist's actual rig, a producer gets a complete, pre-voiced signal chain — amp, cabinet, and matched effects — tuned for that artist's genre, rather than needing to assemble amp, cabinet IR, and stompbox plugins separately and tune them to taste. This directly enables the DI-guitar-first, reamp-and-tone-shape-later workflow documented as a modern production technique across the metal and rock genre files: a guitarist can record a clean DI signal and apply (or change) the amp tone entirely after tracking, without committing to a mic'd amp sound during recording.

## Weaknesses

The neural modeling engine carries a meaningfully higher CPU/DSP cost than a simpler IR-loader or traditional circuit-modeled amp sim, which matters in sessions running many guitar tracks or heavy plugin chains elsewhere. Because each title is built around one artist's specific genre and rig, the product line requires matching the right title to the target tone — a metal-voiced Archetype title is not a general-purpose amp sim the way some competing single-product amp modelers are, and covering multiple genres may mean owning multiple titles rather than one universal tool.

## Common Mistakes

Treating any single Archetype title as a general-purpose amp sim for every guitar tone need — per the genre-specific voicing built into each title, a stoner/doom-appropriate high-gain title and a clean-toned, articulate title serve different production goals, and the genre corpus's citations (heavy metal, hard rock, grunge, stoner rock, classic rock) reflect real producers selecting a specific title to match the target genre rather than using one Archetype plugin universally.

## Cross-References

- `knowledge_base/genres/metal/heavy_metal.md` — cites Neural DSP alongside Kemper hardware profiling as a modern amp-capture technique
- `knowledge_base/genres/rock/classic_rock.md` — cites Neural DSP for vintage tube amp tone recreation and the DI-plus-amp-modeled-track layering workflow
- `knowledge_base/genres/rock/grunge.md` — cites Neural DSP alongside STL Tones for recreating classic Fender/Marshall/Mesa grunge tones
- `knowledge_base/genres/rock/hard_rock.md` — cites Neural DSP for arena-scale, modern-translating high-gain tones
- `knowledge_base/genres/rock/stoner_rock.md` — cites the "Neural DSP Fortin/Archetype series" specifically for authentic fuzz/stoner-voiced tone
