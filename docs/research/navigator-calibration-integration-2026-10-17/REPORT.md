<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator atomic calibration integration and release follow-up

The local candidate now implements calibration delivery, freshness/order validation and bounded release with rearm blocking. It is staged separately under `stage/` with paired patches; the original paired source trees remain clean and the Comma was not contacted. Owner **1.20/0.97**, vehicle geometry and native safety code remain unchanged.

## Calibration integration and timing

The previous prototype consumed the latest calibration topic alongside a recorded control. That did not establish which input produced the angle target. The staged producer now captures an optional `CarControl.navigatorCalibration` snapshot immediately after computing/sanitizing that control's actuators, using the exact vehicleParameters/carState already held by `Controls.state_control`. The snapshot carries validity, source/state/computation monotonic timestamps, target speed, roll, learned ratio/stiffness, offset and copies of the requested curvature and angle target. `publish` sends it atomically with the control. No new independent publisher or card calibration subscription is needed.

The staged card feeds that same received control into the calibration bridge before applying it. Checks reject invalid/default/missing legacy snapshots, source/state timestamps beyond computation, computation after publication, future/expired/reordered controls, stale producer inputs and changed target anchors. Matching uses the producer's speed, avoiding consumer-speed skew in reconstructing its angle target. Repeated held controls expire rather than refreshing their original source timestamps; future controls cannot poison the valid high-water timestamp. Numerical model/parameter bounds, target consistency and current state/model/cadence gates remain in place.

Time limits: received control and producer computation at most100ms old, producer carState at most80ms old at computation, calibration source at most150ms old at use. Existing receiver state/model checks and40–60ms strategy cadence remain. These are explicit fail-closed trial limits, not measured real-vehicle latency guarantees. Atomic provenance removes the separate-topic race; it does not identify the estimator's physical sensor latency or make its learned roll ground truth.

## Release and rearming

An unmodified budgeted-tracking baseline now advances independently on every strategy evaluation. Its original factors, feedback, state and intent metadata are preserved. The candidate adds the bounded roll adjustment to that baseline's final command and constrains the actual candidate result with the existing DBC range and speed-dependent output rate limits. This replaces the previous shared-output-state approach, where candidate slew history could obscure the baseline and carry into rearming.

Invalidation, request reversal or correction-direction reversal clears the prior correction and latches release while a final-output difference remains. Release chooses the closest rate-legal baseline value; new calibration cannot rearm the correction until that output difference is gone. A new correction then starts with the original bounded onset. Default-off and legacy/missing-snapshot operation preserve baseline behavior.

A universal instantaneous or fixed-duration release is impossible if baseline moves away at the same maximum rate as the candidate: jumping onto baseline would violate the unchanged rate bound. A dedicated adversarial regression holds that condition, verifies bounded difference/no rearm, then stops baseline motion and verifies rejoin. This is an explicit contract and test, not a hidden rate-limit relaxation. Original inactive/human-turn neutral behavior remains inherited.

The initial map remains50–70mph only, up to0.01rad/15%of feedforward with0.001rad/frame onset. It remains **roll-compensation sensitivity with calibration consistency gating**, not an identified physical steering-ratio/actuator-gain map. Same-model forward/inverse conversion still cancels ratio/offset at zero roll. No new universal gain calibration or road improvement is claimed.

## Selection and compatibility

`FordPrefRollAwareMapping` is a separate persistent bool with default0. The factory requires the existing persistent-tracking selection and eligible platform/pinion/low-speed flags, then selects the new map only when this additional opt-in is true. No parameter was written outside an owned temporary test store. No UI toggle or device activation is added by this package.

The key is registered in the staged actual header. The read helper also tolerates older native parameter libraries by leaving the option false. The staged Params C ABI was rebuilt separately and exercised with the real Python wrapper and a temporary store. Both staged patches pass `git apply --check` against pinned paired bases. They are not applied to those bases; submodule pointer/commits/install remain separate work.

## Integration evidence

- **54 focused tests pass**, including prior sign/neutral-scope/parameter tests, atomic wire snapshot, producer-speed skew, source/state/computation ordering, stale/future/reordered/repeated controls, default/legacy behavior, independent-baseline release and rearm latch, and rebuilt registry behavior.
- **320 transition/abort cases /115,200 frames pass**: final range/rate limits, unchanged intent and settled trace ends. Synthetic speed85mph cases are not85mph road evidence.
- `pipeline_screen.py` calls the actual staged `Controls.state_control`, transports a real cereal Event over an owned unique local msgq endpoint, and calls actual staged `Car.controls_update` with capture-only CI/PubMaster objects. The snapshot remains unchanged after later producer parameters change. Controlled50ms calls establish active correction, reject an expired snapshot and verify final baseline rejoin. No CAN/USB/vehicle interface or sendcan socket is opened by the test.
- C++ code for the additive car schema was regenerated and compiled; a native serialization round trip passes. The actual staged key header compiles and verifies persistent bool/default0. A private rebuilt Params C ABI passes real temporary-store enable/disable checks.
- Independent review caught and resolved the initial registration and stale-test-claim gaps. See `REVIEW.md`.

This is targeted Python/C++/IPC integration evidence. The whole vehicle application, on-device build, H7 firmware, real USB/CAN timing and road response are not validated here.

## Full replay interpretation

All515retained raw segments are used. Independent baseline/candidate native safety instances consume recorded physical RX and test generated TX after Ford safety configuration, without controls-permission override or native changes. Pre-configuration generated frames are counted separately. Input hashes bind raw files to prior manifests.

Old recordings have no atomic producer snapshot. Therefore each controller update also checks a strict legacy path using the original control: it must remain byte-identical to the installed baseline. The candidate replay additionally creates **synthetic causal snapshot fixtures** from preceding logged parameters/state, preserving recorded validity and chronology with no future input. These fixtures exercise changed command/native safety behavior, but cannot prove historical producer consumption, reproduce actual live scheduling or show what the vehicle would do with new commands. The actual staged producer/consumer and IPC tests cover the newly implemented atomic path separately.

## Results

- **27sessions /515segments complete**, 2,986,854 controller updates, 118,905,779 saved physical RX frames and 597,382 steering-TX evaluations.
- **1,904,757 native TX checks accepted per variant, zero rejections**. 9,983 generated frames before Ford configuration are separately counted/unhooked. Baseline/candidate native counts match, including27startup/configuration-invalid ticks. 212,444 active angle TX frames per variant.
- **Strict original legacy controls match the installed baseline byte-for-byte** on every controller update. Default-off matches the original feedforward stream. Synthetic-snapshot mapping runs on23,440 steering evaluations; 17,528 generated controller updates change after wire quantization. Maximum internal/final command difference remains0.01rad; maximum mapped packet age53.79ms.
- **No saved final-command differences≤50mph or≥70mph**, including45mph. This is baseline preservation on these recordings, not a finding that those ranges are optimally calibrated.
- **Five final-output release-tail frames remain**, peak0.00570527rad and aggregate absolute area0.000469680rad·s. Counts/peak/area are effectively unchanged from v1; no claim of release-tail reduction. The improvement is an explicit independent baseline and no-rearm-until-rejoined contract, not a concealed output reset. The509`releasing` status evaluations include frames already rejoined and must not be interpreted as509nonzero residual frames.
-54focused tests,320transition/abort cases, actual staged producer/card+IPC screen, compiled C++ schema/key header and rebuilt Params runtime checks pass. Patches apply-check and Python compilation pass; paired heads/dependency/native-safety hashes unchanged. Full application/hardware/road validation remains unrun.

Evidence: `verification.json`, `full-replay.json`, `input-manifest.json`, `source-provenance.json`, `green.txt`, `transition-results.json`, `pipeline-results.json`, `native-integration-results.json`, `params-runtime-results.json`, and per-route receipts/traces. `openpilot.patch` and `opendbc.patch` are reviewable local changes against openpilot`9da98d0c91f0559efa976e3ffb221f2584fd0b88` /opendbc`18175406d0cc5af8233afde70a5d121aedf8de44`. Neither patch was applied to those clean original trees.

Reproduction: paired `.venv/bin/python`; focused `pytest -c /dev/null -p no:cacheprovider --confcutdir=<package> <package>/test_integration.py <package>/test_mapping.py -q`; `pipeline_screen.py`; `transition_screen.py`; `native_build.py`; `build_params.py` then `params_registry_screen.py`; `parallel_replay.py` and `summarize_replay.py`; `package_candidate.py` checks immutable candidate/base hashes and patch application. The staging overlay reuses unchanged local dependencies, so it is not a standalone distribution.

## Disposition

The software integration, explicit timing guards, baseline release and rearm contracts are implemented locally with reviewable paired patches. Physical actuator/ratio identification, roll-estimator uncertainty and hardware/road validation remain separate. Saved-input native acceptance alone is not evidence that tracking improved. Keep the existing35–50mph collection plan and all-range objective tracking work open; no special high-speed driving is requested.
