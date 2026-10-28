<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator Alpha comfort investigation — October 24, 2026

Status: investigation and offline diagnostic candidate; no new tuning installed.

## Scope and preservation

Scan all available longitudinal operation from standstill through 85 mph, including highway entry in the 50s, following, grade transitions, stops, departures and driver overrides. Five-mph bins organize evidence; they do not imply separate gains in every bin. Preserve lateral source, owner 1.20/0.97, brake clearance and fault protections. No active diagnostic ECU queries or CAN test transmission.

Installed parent 74eaa6a60d344f141d06da16f4dbe10d3de49c0e, child 3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1. One new session / 23 completed rlogs downloaded (210,676,106 bytes) and hash checked. Source/settings acquisition provenance recorded separately; raw route data private.

## New road evidence

1041.11 seconds active longitudinal; maximum recorded speed 69.33 mph. All-range scan includes stopped operation; 50–55 mph has 70.24 seconds eligible, 27 brake-request edges; 55–60 mph has 242.53 seconds, 77 edges. These are screening counts, not a claim every edge was unnecessary. Worst 20-second window: 19 brake-request edges without a detected lead. Pulsing is not restricted to following.

Planner selects e2e model acceleration for 901.65 active seconds, radar lead0 103.85, lead1 34.52 and cruise 0.90. In no-lead highway samples (at least 55 mph), more than 8 mph below a valid set speed, model is selected for 263.47 seconds, lead0 for 0.15, cruise for zero. This supports model-limited under-speed behavior rather than a fixed 62 mph speed cap. A missing radar lead does not prove an unobstructed road; model safety constraints must not simply be discarded.

One recorded release_timeout_disengage at 47.71 mph, relative 1336.13 s, with Controls Mismatch alert. No sampled active carState CAN-invalid samples. Eight longitudinal-active falling edges and three stops indexed in analysis.json; falling edges are not all emergency takeovers.

## Mode explanation from exact installed source

Radar target time gaps: relaxed 1.75 s, standard 1.45 s, aggressive 1.25 s, with additional stopping-distance terms. Aggressive halves MPC jerk/change penalties; standard and relaxed use the same factor. Personalities do not directly retune Ford's brake/propulsion handoff or the neural model. This planner selects the minimum acceleration among radar MPC, cruise and model; a high cruise setpoint is a ceiling, not a guarantee of reaching that speed. ExperimentalMode param being absent does not remove the model candidate in this source version.

## Isolated diagnostic experiment

Current-controller minimized older-drive replay exactly reproduces generated ACC wire bytes. In a 20-second ~70 mph fixture, raw acceleration is positive 98% of the time, but grade compensation and admission/release logic generate 15 brake edges / 7 rapid reversals. Several tiny negative compensated requests admit braking at the existing 0.3-second coasting deadline, then qualify release shortly after. This is a mechanism for chatter, not proof all recorded braking is unnecessary.

A one-variable sweep showed doubling the debt budget alone changed nothing. Extending only the weak-negative deadline to 0.6 seconds reduced edges 15→9 and rapid reversals 7→2. With budget 0.02 m/s and deadline 0.6 s, edges 15→7 and rapid reversals 7→1. This candidate changes no torque-clearance threshold, timeout, fault handling, strong deceleration, planner or lateral source. It remains a diagnostic subclass in this evidence folder, not integrated code. Recorded vehicle responses stay frozen; reductions do not establish physical comfort or safe stopping distances.

Broader current-controller counterfactual replay over two older sessions completed (111,457 callbacks). The same two pre-existing release-timeout episodes remain. Fresh-drive baseline and candidate reconstruction running; results must be checked before deciding whether a longer coasting admission is appropriate. No full native safety/build or physical validation claimed for this candidate.

## Remaining work

1. Compare fresh-drive candidate against current replay across every populated bin and every stop/override, with unchanged genuine braking and release protections.
2. Distinguish model-driven target oscillation from grade/handoff chatter; changing a mode alone cannot resolve both.
3. Trace initial stoplight departure separately from acceleration continuity after departure. Do not increase acceleration globally to hide model limits or measured brake-release waits.
4. Investigate the remaining measured release timeout without extending the fault deadline to suppress it.
5. Older replay inputs cover through the 70–75 bin; this new road session does not cover 70–85. Audit remaining saved high-speed Alpha recordings before requesting additional evidence. Lateral-only high-speed recordings cannot prove Alpha comfort.

## Storage cleanup completed

Additional 3,333,046,272 bytes reclaimed from validated redundant staged model copies and unused SCons cache, with process-reference/source/rollback guards. Device /data now 80% used, approximately 18 GiB available. Active source, rollback, expanded backups, settings, recordings and running service preserved. No restart. Device receipt: /data/navigator-backups/storage-cleanup-20261024-payload-cache.json. Earlier 12.46 GB archive cleanup remains separate.

## Broader result — simple timing candidate rejected

Fresh-drive reconstruction finished: 67,687 callbacks, all 67,687 matching recorded brake/gas/fault/reason feedback within gas tolerance. This is strong command-level reproducibility, not exact hidden consumed-state or physical replay. Combined with older sessions, 179,144 callbacks reconstructed.

The longer weak-negative coasting candidate is **not suitable as the overall fix**. New 50–55mph edges remain27 and rapid reversals increase7→8; 55–60mph remains76edges/23rapid. 60–65 improves84→82edges, 65–70 improves79→73. Existing release timeout remains at exactly the same replay callback. No differences in sampled raw requests below−0.2m/s² were found, but this alone is not complete braking safety proof. Older70–75mph results improve more; selecting that fixture alone would overstate the benefit.

New brake-entry classification strengthens the need to address admission scope/grade mapping and planner demand separately: 50–55mph has14entries,10with positive raw requested acceleration; 55–60 has36entries,19positive; 60–65 has42entries,24positive; 65–70 has43entries,30positive. Most entries bypass the narrow bounded-coast path and use baseline admission. Positive raw request does not itself prove braking is wrong on a downhill; grade and measured deceleration must justify the replacement. Do not simply widen thresholds or disable braking.

Evidence files: all-range-scan.json, replay-comparison.json, new-brake-entry-classification.json, speed-diagnostic.json. Five-mph bins are reporting strata, not requested separate per-bin tunes. No owner section labels are needed for automatic scanning. Initial departure and75–85mph Alpha coverage remain incomplete; this is not a release-ready0–85mph solution.
