<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Production signed-coast integration checks

Production changes are ordinary module classes/functions, imported directly by the controller. No prototype installation, monkeypatching, or class replacement is used in `production_replay.py`.

`PRECHARGE_PROTOCOL_VERSION` is 3. Requests require revision 3 and the original valid, finite, ordered and fresh planner target. Unknown/legacy requests use nominal allocator behavior. The bounded coast marker is release phase, nominal reference brake true, physical brake and precharge false, limited true, gas -5, age less than 0.300000001 seconds, and positive remaining demand-area budget at most .01. Both integral signs retain signed-control behavior only with valid fresh owner/sequence/phase/speed feedback; ordinary ramp numerical margin is unchanged. Version 1 signed-precharge integral compatibility remains as in the verified spike.

The original `BoundedPrechargeAllocator` and `RestartClearance` classes match their pre-port ASTs. The production extension matched 10,000 seeded allocator decision/state comparisons and 30 logical-clearance decision/state comparisons against the retained repair2 prototype. Focused child tests: 213 passed, 20 subtests passed; one native permission test was excluded after the macOS UBSan loader rejected its runtime under platform policy. Ruff and diff whitespace checks passed.

Two parent fixtures now import the current protocol constant instead of hardcoding revision 1. Explicit legacy versions 0/1/2 cannot admit the current command-recovery overlay. Their focused run passed all 25 tests. Only `test_command_recovery.py` and `test_low_speed_ramp_transport.py` were changed in this follow-up.

## Replay methodology and limits

The production runner is a narrowly adapted copy of the retained 237-segment harness. It imports the current paired production LongControl, request producer, pose refresh, and Ford CarController directly. It hashes its own source and nine critical production modules before replay and verifies them unchanged on completion. Input pickle hashes are checked against the unchanged manifest. Fourteen drives comprise 237 segments; the original source record identifies 225 complete input segments and 12 diagnostic prefix segments.

Producer and consumer callback clocks, software-feedback publication timing, freshness/ownership checks, original consumed planner/state, torque, pose, and driver response remain frozen. The comparator streams retained repair2 and current production traces and checks all exposed command/feedback/observer/admission/handoff/producer semantic fields, entire producer-record tuples, complete ACC packet-record dictionaries, fault lists, and summary counters. Internal allocator dictionaries are excluded because implementation representation can differ; inherited allocator state was separately checked above.

This establishes software port parity on those retained frozen inputs. It does not rerun native safety replay, prove physical comfort/pulsing benefits, close the loop on changed vehicle dynamics, recover hidden consumer receipt order, or validate installation/road behavior. Retained native safety evidence belongs to the earlier prototype run, not to this production replay. No device, CAN transmission, installation, reboot, dependency download, or firmware action was performed.

The initial focused 21-segment replay was intentionally interrupted before completion to prioritize the full corpus; its partial coast output is overwritten by the full run in the same new root. Full outputs use `${PRIVATE_CACHE}`; retained reference files are untouched.

## Completed production-bound replay

All 14 drives / 237 retained segments completed with the production source-invariance assertion passing. The streaming comparator found exact equality for 685,504 consumer trace rows and complete ACC packet records, and 1,311,408 producer records. No exposed semantic field, summary counter, fault list, producer record, or ACC packet record differed from retained repair2 output. Zero faults were added; both runs retain the same two release-timeout disengagements in the highway-pulsing sessions. See `VERIFICATION.json`, `production-parity.json`, `production-parity.log`, and `production-replay-full237.log`.

`native-applicability.json` hash-validates the retained verification-listed native summary/results/provenance/runner and reference manifest/summary, the retained compiled native binary, all 34 current safety headers, and the native C translation unit against the original provenance-bound child commit. It SHA-binds current and reference ACC artifacts, whose packet records match exactly. This is retained native applicability evidence, **not a fresh native safety replay**. The parent actual-cycle clock fix is outside the frozen replay and requires its separately recorded clock/build tests.
