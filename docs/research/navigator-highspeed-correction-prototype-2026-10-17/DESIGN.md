<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local high-speed reduction experiment

Authorized scope: local prototype and complete retained-drive/native safety replay. No device connection, installation, firmware, CAN transmission, branch publication, or production integration.

Reference: installed `RollAwareMapping` from parent `99645f2222ea2ba1fd4124808774bcd6381f8154`, opendbc `8cbc834fe534a248a3bc6d56ce964106c0f49503`. Composition keeps an independent instance of that exact strategy; 1.20/0.97, fixed pinion model, low-speed tracking and existing roll mapping are unchanged.

## Hypothesis and bounds

The reported 83 mph bend has coherent measured wheel angle above its learned-model desired angle, corroborated by excessive body response. Test a reduction-only feedback term; do not add steering or directly retune speed gains from observational ratios. Wheel excess is not by itself proof of a plant calibration error, and frozen replay cannot establish improved vehicle response.

Only fresh, valid, coherent control/calibration/model/state context may start a correction. Require active assistance, no driver input/brake/blinkers/lane change/fault, Navigator-associated Expedition pinion+gain flags, bounded learned model parameters and agreement between recomputed and supplied angle target (0.5 degree tolerance).

Speed weighting rises smoothly from zero at 60 mph to full at 70 mph. Gentle curvature is fully eligible through 0.001/m and fades to zero at 0.0015/m. Requested lateral acceleration ramps from 0.25 to 0.5 m/s² so gentle high-speed curves are retained while near-zero demand ratios are excluded. Desired offset-corrected wheel angle must exceed 1.5 degrees; actual and desired direction must agree. Signed wheel excess beyond 0.5 degree must persist for five 50 ms frames.

Use excess/actual wheel magnitude as a bounded reduction fraction, capped at 15% of the **installed strategy output** and 0.01 rad. Onset is limited to 0.0003 rad/frame. Neither owner factor is changed. The final output intersects the inherited native slew envelope with a same-sign reduction-only envelope; it cannot amplify or countersteer relative to the installed reference. A missing intersection is a hard offline failure, never a silent relaxation.

Meaningful demand withdrawal (>10% retreat from the six-frame demand window), reversal, stale/mismatched calibration or context clear the internal term and release to reference. Small demand jitter is not interpreted as an aborted turn. Re-arm is blocked until final output rejoins the reference; persistence restarts after joining. Driver input/inactive control immediately uses the exact reference path. A moving reference may create a bounded release tail; elapsed release time is not universally guaranteed.

## Verification plan

1. Test-first steady excess in both directions; default-off exact output; lower-speed parity; ineligible inputs; transition, withdrawal, driver, reversal, invalid-message and re-arm cases.
2. Compare strategies at actual recorded steering-send timestamps with untouched atomic packets on the latest 25-segment route. Verify reference fidelity within half wire step before interpreting candidate changes. Include the predeclared 1011–1017.5s reported 83 mph bend and gentle curves using acceleration criteria.
3. Replay every retained route: 28 sessions / 540 segments, physical recorded RX, independently generated TX through independent unmodified native Ford safety hook instances. Run original atomic packets and separately labelled past-only synthetic calibration fixtures. Never enable controls by override.
4. Require unchanged source hashes from worker startup to completion and identical source snapshots across workers. Report shared baseline rejections separately from candidate-specific regressions, pre-Ford unhooked frames and native timing limitations.
5. Independent review and durable report/roadmap. Production integration, on-device build, physical actuation and closed-loop performance are out of scope and remain unvalidated.

Legacy recordings lack the new atomic snapshot. Their original-packet pass must stay at installed-reference behavior; the synthetic fixture pass is a causal input reconstruction, not historical evidence of actual packet production. No recorded body response is replaced or rescaled to claim a tracking improvement.
