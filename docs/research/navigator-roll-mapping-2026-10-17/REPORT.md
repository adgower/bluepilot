<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator roll-aware mapping: local prototype and offline validation

This package is an opt-in, report-local sensitivity prototype. It is not selected by card, integrated into either paired branch, installed, or road validated. The Comma was not contacted. Owner 1.20/0.97 settings, installed low-speed tracking, fixed pinion geometry and native safety code are unchanged.

## What the candidate changes

`roll_mapping.py` adds `RollAwareMapping` above the existing `BudgetedTrackingPrototype`. It accepts an explicit timestamped calibration packet containing roll, learned ratio/stiffness and angle offset. It compares the standard calibrated desired wheel angle with the target reconstructed from that packet. It then converts that target through the learned vehicle model with zero roll to derive a tire-curvature feedforward adjustment, applying the model's roll contribution once.

This is a **roll-compensation sensitivity prototype with calibration-consistency gating**, not an identified steering-ratio or actuator-gain calibration. Forward/inverse conversion with the same model cancels learned ratio and angle offset for a consistent target; at zero roll the correction is zero. Three parameter-combination regressions explicitly verify that limitation. Stiffness affects the model's roll compensation. No new ratio-to-PSCM transfer function has been identified or fitted.

The application model is separate from the fixed pinion model. Desired wheel degrees are never sent as PSCM path-angle radians. The original requested curvature remains the native safety intent; the extra term enters the provisional path-angle feedforward before existing final output constraints. Native safety uses the original fixed geometry, including the fixed steering-ratio model, throughout.

## Bounds and fallback

- Speed blend: zero at/below 50 mph and at/above 70 mph, smooth onset through 55 mph, full weight 55–65 mph, smooth fade through 70 mph. The owner 1.20/0.97 factors remain inherited; the prototype deliberately changes the effective map within its stated highway scope.
- Demand blend: zero below absolute curvature 0.0007/m, smooth onset to full weight at 0.0015/m.
- Internal adjustment: at most 0.01 rad and 15% of the absolute clipped feedforward, with onset limited to 0.001 rad per 20Hz strategy evaluation. These are provisional sensitivity bounds, not validated tuning.
- Gate: Expedition pinion/low-speed flags, active control, no driver intervention, valid CAN/no steering fault, current model/no lane change, fresh state/control/model, 40–60ms strategy cadence, fresh valid calibration age 0–150ms, bounded finite parameters, and reconstructed angle target within 0.5 degrees.
- Invalid/stale/mismatched context or zero demand clears the internal correction. Requested sign reversal clears the previous correction before allowing the new bounded onset. Existing final command slew state remains intact. This permits a brief final-command difference after internal correction clears; it is measured separately rather than hidden by resetting the output state.

The default-off stream is checked against the existing feedforward implementation. Mapping-disabled with existing low-speed tracking enabled is checked against the installed budgeted-tracking implementation on every saved controller update. Existing below-25mph behavior is inherited rather than replaced. The initial highway scope does not imply that 45mph has been objectively perfected.

## Replay method and limits

`route_worker.py` consumes all retained raw sessions: the original 335 segments, the next 51 collection segments and the six new sessions' 129 segments. Every raw input is checked against its prior SHA-256 manifest. Overlapping segment tails are merged in timestamp order. Recorded physical RX frames feed independent baseline/candidate native safety-library instances; generated TX frames after the recorded Ford safety configuration are checked by their corresponding native hooks. Frames before Ford configuration are counted separately and are not claimed as hook-checked. No controls-permission override or safety-code change is used. Legacy recorded Ford configurations receive the existing paired pinion safety bit; other recorded configuration bits are retained.

Recorded vehicleParameters packets become available only at their log event time, with their actual recorded validity and fields. No future packet is used. This is publisher/log chronology, **not** proof of actual live card subscription arrival, scheduling, or end-to-end estimator freshness. The current paired card has no vehicleParameters subscription and this package does not add one. Source/dependency hashes and clean paired heads are captured in `source-provenance.json`; each worker binds its candidate/native-library hashes in its receipt.

`mapping_active_updates` in raw route receipts counts held strategy state on 100Hz controller ticks. The final verification instead counts actual 20Hz steering-TX evaluations. An accepted replay proves only that generated commands pass the tested native hooks against the saved RX trajectory. Changed commands do not regenerate the vehicle's physical response, so this cannot establish tracking improvement, physical stability, or hardware readiness.

## Transition, abort and review evidence

`transition_screen.py` screens 320 deterministic cases / 115,200 final-command frames: both turn signs; 45, 52, 55, 60, 65, 68, 75 and 85mph; speed fades/jumps; request and roll reversals; roll withdrawal/step; turn abort; disengage/reengage; driver intervention; invalid, stale and future calibration; lane change; faults; mismatched target; stale model; and cadence interruption. All final range/slew constraints and unchanged shadow intent are asserted, and all traces settle back to baseline. The 85mph fixture is synthetic, not evidence of an 85mph drive.

The focused suite adds explicit freshness, parameter, neutral-scope and established-mapping abort assertions, including cadence/stale-state/stale-control/invalid-model tests. Independent review found a real reversal gap when the deviation clip retained the old turn sign; requested-sign tracking fixes it. `clipped-reversal-red.txt` reproduces the failure against an isolated old version. See `REVIEW.md` for review findings, fixes and scope caveats.

## Decision and next work

This package evaluates a bounded roll-aware map, not a solution to the remaining calibration problem. The earlier approximately 47% wheel-to-body prediction-error reduction remains a measurement-model result and is not a claimed steering improvement from this prototype.

Before any deployment proposal: inspect the complete replay's command sensitivity and release tails; resolve live publisher/subscriber integration and timing; evaluate model/roll-estimator errors and causal actuator behavior. Native acceptance alone is insufficient. Keep the ordinary supervised 35–50mph evidence collection and broader objective tracking work open; no special high-speed collection is requested by this prototype.

## Results

- **Full replay complete: 27 sessions / 515 raw segments**, all verified against prior input hashes. 2,986,854 controller updates, 118,905,779 recorded physical RX frames and 597,382 steering-TX evaluations.
- **1,904,757 native TX checks accepted per variant, zero rejections**. 9,983 generated frames per variant occurred before Ford safety configuration and were not hook-checked. Both variants have identical native receipt counts, including 27 startup/configuration-invalid safety ticks; these are not hidden or treated as valid-configuration checks. 212,444 active angle TX frames per variant.
- Mapping actually evaluated as active on **23,477 steering frames**; 23,470 pre-wire final floating outputs and 17,520 generated controller updates changed. These counts differ because of wire quantization. Maximum internal/final difference: **0.01 rad**. Maximum accepted calibration packet age at mapped steering evaluation: 53.79ms.
- **No saved-drive final-output differences at/below 50mph or at/above 70mph**, including the 45mph region. This establishes preservation against the existing controller on these logs, not optimal tracking in those speed ranges.
- **5 steering frames** retained a final-output difference after the internal mapping term became zero; peak 0.00570527rad, total absolute area 0.000469680rad·s across the corpus. This explicitly measured release tail remained accepted by native safety. Synthetic transitions/aborts additionally assert final range/slew and eventual baseline return.
- **35 focused tests pass; 320 transition/abort cases / 115,200 frames pass.** Mapping-disabled matches the installed baseline byte-for-byte on every saved controller update; default-off matches the original feedforward byte-for-byte. Reviewer independently passed the then-current 26 tests; expanded coverage was run by the implementer.
- Paired source remains clean at openpilot `9da98d0c91f0559efa976e3ffb221f2584fd0b88` / opendbc `18175406d0cc5af8233afde70a5d121aedf8de44`; source/dependency/native-library hashes unchanged through replay. Owner **1.20/0.97** and all device state unchanged.

Machine-readable evidence: `verification.json`, `full-replay.json`, `input-manifest.json`, `source-provenance.json`, `transition-results.json`, `green.txt`, and per-route receipts/command traces under `route-replays/`. `parallel_replay.py` reruns all raw sessions offline with four independent workers; `summarize_replay.py` verifies/aggregates receipts. Use the paired checkout's `.venv/bin/python`; focused tests require `pytest -c /dev/null -p no:cacheprovider --confcutdir=<this package> <this package>/test_mapping.py -q` to avoid the unrelated root checkout's configuration.

**Disposition:** local prototype and requested replay/testing complete; no deployment readiness or observed steering improvement claimed. General calibrated actuator mapping and real-time publisher/subscriber integration remain open.
