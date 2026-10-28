<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Broader replay and timing work — local only

User authorized broader safety replay and local timing resolution. No SSH, device updates, CAN transmission, paired-branch edits or source publication. Candidate remains the throwaway observer-continuity implementation with owner1.20/0.97 unchanged.

## Input corpus

71recordings /1,015segments, all raw segment hashes verified against saved manifests: retained60recordings/878segments plus11new recordings/137segments. The corpus includes historical branches as regression inputs; they are not all current-tune physical evidence.

## Timing findings and correction

-Card is driven by CAN/vehicle cycles and publishes carOutput/carState before applying its already-sampled carControl. The old native harness called the controller on carControl publication. The old send-time harness could also select a newly published control between state publication and the later send, even though Card had already frozen its inputs.
-The new harness uses each actual sendcan publication as one controller invocation, including empty sends. It freezes control/model/motion/parameter inputs at the preceding carOutput publication, associates the subsequent carState, and seeds steering phase/counter from the first recorded steering request. It retains original packet publication timestamps and never substitutes the synthetic fixture clock into original packets.
-A separate latest-send/state/output anchor probe on current drives shows baseline half-step mismatches reducing11→7 and39→13with output snapshots. This is an approximation of Card's pre-publication snapshot, not recorded SubMaster receive timing. State-clock versus send-clock comparisons are retained, not fit to a response gain.
-Synthetic calibration fixtures require their own creation timestamp as control_ns. A regression test reproduced the invalid future-created packet when using the older original publication timestamp; the fixture lane now uses its own clock, separately labeled. A new assertion checks eligible positive-speed valid fixtures stay valid after transport. Stationary targetSpeed≤0.1 legitimately remains ineligible for calibration context.

## Tests and invalid runs

Six timing/snapshot tests pass, including nested Cap'n Proto packet immutability.196deterministic mixed-source timing/abort cases /15,680frames pass:40/60/45/55ms callback jitter, separate source ages, duplicates, future/stale inputs, generation changes, driver input, reversal, protected ranges, slew, shadow and low-speed exposure accounting.

The first broad attempt had synthetic fixtures rendered invalid by their original-source clock; it was stopped and its output moved to replay/route-replays-invalid-fixture-run. A subsequent overly broad fixture-validity assertion fired on expected zero-speed ineligibility; that run was stopped and moved to replay/route-replays-stationary-assert-run. These attempts do not count as successful broader validation. Logs are retained. Own local worker processes were terminated; no device process was involved.

Final restarted run uses the positive-speed fixture validity assertion and frozen runtime/test sources. Four local subprocesses feed recorded RX into independent native safety hooks; controls permission is not overridden. Original and separately stamped fixture variants compare candidate versus the current installed strategy. Default-off full-stream proof is retained from the two target-route run and67focused tests; it is not silently claimed as re-executed across this new corpus.

## Completion gates

All71routes/1,015segments must finish; each route must retain source-snapshot identity, equal reference/candidate RX outcomes and no additional native rejection. Protected ranges, budget/abort limits, phase/counter alignment, valid fixture coverage and exact-current-pair baseline/changed-frame timing ambiguity are reviewed separately. A completed native run alone does not establish physical response improvement, low-speed saturation resolution or85mph stability.

## Broader replay found scope contamination; candidate revised

The earlier frozen candidate completed39routes/545segments with no additional native rejection before the run was stopped for a scope failure: a few low-speed changes occurred below22mph and six highspeed-session-04frames changed above80mph. These were not native-protocol failures; experimental admission had modified production policy histories/shared low budgets, creating later differences outside the intended bands. Output is retained under replay/route-replays-boundary-failing-run and is not counted as a final pass.

The candidate was restructured as an output-only overlay over the unchanged installed strategy. No production admission/history/budget fields are modified. Independent wheel observation uses state-source time for prediction; current confirmation from the actually selected production body observer remains mandatory. The combined trim obeys the existing0.0003rad/frame onset cap and0.01rad/15percent total cap, with independent scope fade and final slew-controlled release. An explicit sign guard prevents added trim when production output and its untrimmed reference disagree during reversal.

New low-speed actuation was withdrawn: it produced no correction of the severe saved saturation episodes and caused shared-budget scope effects. Original-target observation remains diagnostic only; installed low-speed output and1.20/0.97 are preserved. This is an intentional narrowing after failed evidence, not a claim that23–24mph saturation is solved.

New red tests reproduced low actuation differences and admission leakage past80mph in both directions. Final71focused tests pass, including those fixes and total trim onset accounting. Final196timing scenarios/15,680frames pass with the new candidate hash. A55segment intermediate run was stopped before adding the explicit reversal guard; preserved under replay/route-replays-pre-reversal-guard. It is not final candidate validation.

The full71route/1,015segment run is restarted under a new frozen source fingerprint. Its runner now additionally rejects below70mph changes, changes outside the intended speed bands and any Card phase/counter mismatch. Final completion passed: 71 routes / 1,015 segments, 5,805,897 invocations per variant; full rejection-count/event-list, RX-outcome, source, scope and phase/counter audits passed. See [final report](REPORT.md) and [receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).
