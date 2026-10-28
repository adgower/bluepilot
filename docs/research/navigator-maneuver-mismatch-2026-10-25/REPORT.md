<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Longitudinal maneuver mismatch investigation — 2026-10-25

## Status

Local prototype only. No installation, reboot, settings change or CAN transmission was performed for this investigation. Owner steering settings 1.20/0.97 remain unchanged. The candidate is in `candidate/longitudinal_coordination.py`; `release-progress.patch` is the reviewable diff. It has not been integrated into the paired source branches or activated.

## Download

Copied 68 completed recording segments across five sessions, 602,041,591 raw bytes. Input hashes verified; open segments excluded. Acquisition receipts and sanitized input hashes are retained alongside this report; original recordings are private local files. Work can continue without the vehicle connected.

## Cause of the two maneuver failures

Both controls-mismatch events occurred during recovery after completed minus-1 m/s² braking runs from 20 mph. The custom release watchdog expired after one second while measured brake torque was still falling normally. Actual torque reached the existing clearance threshold after approximately 1.526 and 1.494 seconds. Brake/precharge request bits were already off; inactive status bits did not establish physical clearance. Propulsion remained inactive while waiting.

## Candidate

Keep the original measured clearance rule: three distinct samples at or below 4 Nm spanning at least 40 ms. Extend only the waiting period, to a two-second timeout threshold, when fresh received torque demonstrates substantial and continuing release. Stalled, reversed, low-bias, invalid or stale feedback does not obtain that grace. Do not grant propulsion from a forecast or an inactive brake status flag. RestartClearance inheritance and existing owner/fault reset behavior remain intact.

## Validation

- Genuine recorded-fixture regression failed before the change and passed with the candidate.
- Combined local tests: 156 passed, 20 subtests passed, one excluded native sanitizer permission-boundary test; two existing pytest configuration warnings. See combined-tests.log.
- Saved-drive controller replay: 61 segments, 179,144 callbacks. The progressing-release timeout cases cleared; the older stalled-release timeout remained. No weaker strong-braking command was identified in the comparison.
- Native safety-hook replay: 14,338,901 received and 429,929 transmitted frames per variant, zero added candidate rejections. Existing recorded rejections remained identical. Controls permission was not forced; native safety source/limits were unchanged.

Recorded vehicle response remains fixed during replay. Recovery beyond an original disengagement is counterfactual, not physical road proof. ARM build and parked checks have not been run for this candidate.

## Useful partial tests

Eleven clean active runs completed: three stops, three starts, three creep sequences and two minus-1 m/s² braking runs. The latter achieved final-second mean wheel-based acceleration of -1.064 and -1.136 m/s²; observed half-response was approximately 0.346 and 0.368 seconds, including measurement filtering. These runs are useful for separating brake application from release timing. The later hard-braking and positive acceleration-at-20-mph stages were not completed.

Launch timing also contains the installed propulsion rise-rate limit, so it cannot be interpreted as pure actuator delay or vehicle gain. Do not retune gains from these partial results alone.

## Remaining

A separate normal-highway invalid_pose_or_accel fault was captured near 70.4 mph and remains a separate investigation. This release-watchdog change is not a complete highway-pulsing fix. Before retrying the maneuver tool with the candidate, finish local integration/review, then separately authorize device backup, ARM staging, activation and parked verification. Retesting the current installed code will not include this local fix.

## Local integration follow-up

The owner authorized paired local integration after this prototype. See [integration report](../navigator-release-timeout-integration-2026-10-25/REPORT.md) for current source, build and test status. The inactive-device boundary remains in effect.
