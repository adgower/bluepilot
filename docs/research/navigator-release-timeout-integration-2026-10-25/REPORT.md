<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Brake-release timeout integration — October 25, 2026

## Scope

Integrating the measured-progress release timeout into the existing local Navigator paired branches. No device access, publishing, staging or activation is part of this task. Steering 1.20/0.97 is preserved. Final local parent `ead00c30e0f3e174130f475847b1f4a2a76e8902` pins child `d4a201251d184a446cb2db383f4bd024c93e75cb`; both working trees are clean. Neither branch was published.

## Behavior

The two maneuver failures followed completed 20 mph braking steps: the one-second watchdog expired while actual brake torque continued releasing. Actual clearance arrived about 1.49–1.53 seconds after the brake-off command. The change allows a bounded additional wait only with fresh, substantial, continuing measured release. Propulsion still requires the original three distinct samples at or below 4 Nm over at least 40 ms. Stalled/noisy/reversed feedback cannot earn the extension; the timeout threshold is capped at two seconds.

This is a targeted availability correction. It does not tune acceleration, cure highway pulsing or suppress the separate invalid-pose fault.

## Evidence

- Regression was reproduced with the original module, then corrected with the integrated module; see RED.md and final test receipts.
- Minimal and full Mac SCons builds passed. Full parent/child suites and Panda build results are recorded in build-results.json.
- Fresh integrated replay: 61 saved segments, 179,144 controller callbacks. All three routes exactly match the prototype's wire, producer and decompressed trace bytes. See integrated-replay-equivalence.json.
- The identical prototype wire streams already passed the native hooks with zero added rejections across 14,338,901 received and 429,929 transmitted frames per variant. Existing recorded rejections remained identical; permission was not forced. The stalled-release fault remained latched in the older highway case.
- Production AST equivalence, unchanged lateral/CAN/safety files and source hashes are recorded separately. The only difference from prototype production logic is explicit zip(strict=False), plus whitespace.
- Local lint and diff whitespace checks passed. The first sandboxed parent-suite invocation could not create test log folders under the home directory; the authorized local run was repeated with required filesystem access.

## Limits

Replay holds recorded vehicle response fixed. Counterfactual recovery after the original disengagement and native hooks are not hardware or road validation. ARM build and parked checks remain necessary before activation. The 11 completed maneuver runs remain useful evidence; the later maneuver stages were not completed.

## Final local checks

All five build/test steps exited zero. Parent: 1,061 passed, 87 skipped, one expected failure, 281 subtests. Child: 4,581 passed, 1,690 skipped, 24,693 subtests. Full Mac and Panda builds passed. Native child tests use the existing plain debug Mac hook library, without a sanitizer claim.
