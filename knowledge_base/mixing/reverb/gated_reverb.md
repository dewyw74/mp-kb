---
technique_name: Gated Reverb
category: reverb
problem_solved: "Getting a large, room-filling reverb character on drums (especially snare) without the wash of a natural decay tail smearing into the next hit or clouding the low-mid mix"
parameters:
  gate_threshold: "Set to open on the drum transient and close abruptly once the hit's initial reverb decay drops below the threshold, typically within 100-300ms"
  reverb_source: "A large room, hall, or ambient reverb sent to the gate — the reverb itself is usually big/lush; the gate is what shapes it, not the reverb's own decay setting"
  signal_chain: "Reverb send/return followed by a noise gate keyed to the same signal (or a dedicated gated-reverb plugin combining both stages)"
signal_chain_position: "Reverb aux return, with a noise gate inserted after the reverb (or a combined gated-reverb plugin) rather than gating the dry source"
genre_applicability:
  - synth_pop
  - new_wave
  - synthwave
  - outrun
  - darksynth
  - arena_rock
  - post_punk
  - new_jack_swing
  - freestyle
  - minneapolis_sound
  - zouk
  - ebm
  - aggrotech
  - darkwave
related_techniques:
  - decay_time_tuning_by_element
  - room_plate_hall_selection
tags: ["gated-reverb", "80s-drum-sound", "snare-reverb", "noise-gate"]
---

# Gated Reverb

Gated reverb — sending a drum hit into a large, lush reverb and then abruptly cutting that reverb's tail with a noise gate — is one of the most specifically dated and specifically revivable techniques in the whole knowledge base. It is documented overwhelmingly as a mid-1980s production signature, and its modern uses are almost entirely deliberate period recreation or a direct creative borrowing of that recreation into new genres (industrial, EBM, darksynth) that want its punchy-but-huge quality without its cavernous decay.

## The Historical Signature

`synth_pop.md` is unambiguous about the effect's cultural weight: "gated reverb on the snare delivers the iconic 80s drum sound," and its production-technique notes even give the practical modern route — "Use modern gated reverb plugins to recreate the iconic 80s snare sound without needing physical gates and vintage reverb units." `arena_rock.md` cites it the same way: "Gated reverb on snare (especially 1980s productions) for the huge, cavernous drum sound." `new_wave.md` dates its adoption within the decade specifically: "Gated reverb on snare in mid-to-late-80s productions," distinguishing it from the genre's earlier, more natural plate/hall vocal reverb. `new_jack_swing.md` and `freestyle.md` both treat it as load-bearing to genre identity rather than incidental — `new_jack_swing.md`: "Gated reverb on drums (a defining late-80s production technique)... Use gated reverb on drums for an authentic late-80s sonic signature," and `freestyle.md`: "Bright digital reverb and gated reverb on drums typical of mid-1980s productions." `minneapolis_sound.md` names it as a genre-defining effect outright: "Gated reverb on snare/claps is a genre-defining effect."

## The Technique Behind the Sound

`synthwave.md`, the modern genre built most explicitly around recreating this signature, both names it as the single most identifiable element ("Gated reverb on snare is the single most identifiable mix signature of the genre") and documents how to build it without a dedicated plugin: "Building custom gated reverb chains (noise gate after a reverb send) when a dedicated gated-reverb plugin isn't available." That's the mechanism in one line — a large reverb feeding a noise gate, the gate keyed to close hard once the initial reflection decays past threshold, so the ear registers a huge room without the tail smearing into the groove. `synthwave.md`'s common mistakes section reinforces how central this is: "Skipping gated reverb on the snare, which is arguably the single most identifiable synthwave production signature."

## Beyond the Snare: Full Drum Machine and Vocal Applications

While snare is the near-universal application, several genres extend gated reverb further. `outrun.md` applies the same principle to a full mix priority — "Gated reverb on snare; shorter plate reverb elsewhere than mainstream synthwave to keep the mix tight and forward-moving" — treating the gated snare as the one exception to an otherwise tighter, drier mix philosophy. `minneapolis_sound.md` extends it to claps as well as snare, and `zouk.md` applies "Light gated reverb on drum-machine snare hits (period-appropriate 1980s production technique)" as one texture among several. `post_punk.md` documents an even earlier and more structurally important use: "Gated reverb on drums (particularly snare/toms) for a distinctive, artificially large yet controlled drum sound," recommending "Vintage gated reverb plugin emulations (SSL/AMS-style gate-reverb combos) to recreate the genre's signature large-but-cut-off drum sound" — a direct reference to the AMS RMX16 and SSL G-series gate circuits that originated the effect.

## Carrying the Technique Into Harder, Colder Genres

`ebm.md`, `aggrotech.md`, and `darksynth.md` all inherit gated reverb from the same 80s lineage but apply it with a harsher, more compressed character suited to industrial-adjacent production. `ebm.md`: "gated reverb or tight processing on drums for punch." `aggrotech.md`: "Short, gated reverb on drums for punch; vocals typically use minimal reverb in favor of direct, harsh distortion processing." `darksynth.md` explicitly contrasts its version against the smoother mainstream synthwave sound: "Gated reverb on drums, more clipped/aggressive than mainstream synthwave's," and its full reverb entry notes "Shorter, harsher, more metallic reverbs than mainstream synthwave's smooth plate/gated reverb."

## Common Mistakes

**Gating the dry drum signal instead of the reverb return.** The effect depends on the reverb tail being cut, not the transient itself — gating the dry source just makes for an oddly clipped drum hit with no reverb character at all.

**Using a small or short reverb as the gated source.** `arena_rock.md` and `synth_pop.md` both describe the underlying reverb as large/cavernous — the gate's job is to make a huge reverb sound controlled, not to make a small reverb sound bigger. A short room reverb gated hard just sounds thin.

**Applying gated reverb outside its genre-appropriate context without intention.** `outrun.md` and `darksynth.md` both deliberately vary the harshness/length of the gated effect to distinguish themselves from mainstream synthwave — treating "gated reverb on snare" as a single fixed preset rather than a tunable character misses the genre-specific distinctions the corpus draws.

## Cross-References

- `knowledge_base/genres/electronic/synth_pop.md` and `knowledge_base/genres/electronic/synthwave.md` — gated snare reverb as the defining 1980s/synthwave signature
- `knowledge_base/genres/r_and_b/new_jack_swing.md`, `knowledge_base/genres/r_and_b/freestyle.md`, and `knowledge_base/genres/r_and_b/minneapolis_sound.md` — gated reverb as a defining mid-to-late-80s R&B/dance production technique
- `knowledge_base/genres/rock/post_punk.md` — an earlier, structurally important use of gated drum reverb (AMS/SSL gate-reverb lineage)
- `knowledge_base/genres/electronic/ebm.md`, `knowledge_base/genres/electronic/aggrotech.md`, and `knowledge_base/genres/electronic/darksynth.md` — harsher, more clipped gated reverb variants in industrial-adjacent electronic genres
- `knowledge_base/mixing/reverb/decay_time_tuning_by_element.md` — the broader question of how reverb decay should be tuned per drum element, of which gating is the most extreme case
