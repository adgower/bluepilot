<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator tracking correction: overshoot and context guards

Local candidate only. No SSH, vehicle access, ECU query, CAN transmission or Comma/settings change. Existing parent/child branches remain untouched. This report supersedes the prior prototype for future trial preparation, not the currently installed controller.

## What was wrong

The prior persistent-error correction treated a delayed steering response as sustained understeer. In the known failing hypothetical case (unit response gain,0.15s response constant,1s delay), it added effort before the normal response arrived; the later response peaked at1.1907 times requested. This is a reproducible controller/plant simulation failure, not evidence that the Navigator actually overshot19% on the road. The real15mph under-response cause is still not uniquely identified.

One-variable comparisons showed reducing gain alone still overshot, and a long persistence hold avoided overshoot but suppressed the actual selected drive event. The final design waits for observed response and releases while the wheel is catching up, rather than relying on a long blind wait.

## Final local design

- Preserve1.20/0.97, pinion curvature model, installed low-speed feedforward, original range and rate limits. Added term remains zero at25mph; existing command-history caveat below applies.
- Retain the prior same-direction stable-demand admission:11 samples (nominal0.5s window), request range≤25% of median request, speed range<0.5m/s, six stable weak-response observations. No integrator.
- Require observed same-direction response≥10% of request before admission. A silent actuator is not eligible; this is explicitly not an EPS stall-rescue/pulse feature.
- Stop adding effort if measured curvature plus its positive response slope projected1s ahead reaches70% of request. Slope uses actual sample timestamps. This is a conservative veto, not an identified vehicle predictor.
- Halve the prior feedback strength:Kp0.25, cap min(0.0075rad,12.5% of feedforward), original0.30s feedback filter. Smooth speed weight is full through15mph and zero by25mph.
- Require one fresh context per evaluated steering frame: state age≤80ms, control age≤100ms, model age≤150ms, no future timestamps, model/control valid, model lane-change state off, neither blinker set. Accept40–60ms evaluated steering cadence; discontinuities reset admission. Missing context disables extra correction only. State CAN validity/steering faults and driver override retain their reset guards.

These thresholds are experimental bounds, not a fitted Navigator control law. The more conservative design trades correction size for reduced delayed-response risk.

## Local integration prepared

`parent-integration.patch` registers defaultOFF `FordPrefPersistentTracking`, selects the new strategy only at process startup for the existing Expedition identity with both pinion/low-speed flags, subscribes to model lane-change context, and feeds actual CAN/control/model timestamps and validity before the normal controller apply call. `child-integration.patch` supplies portable controller modules. The original controller continues to own20Hz command scheduling and native safety remains unchanged. No toggle is installed or changed on the device.

`staged/` contains exact proposed source copies. Both patches pass `git apply --check` against the pinned pair. Python syntax and the parameter header's C++ syntax compile. Report-local tests use the same context bridge as replay; staged tests import the portable modules and execute the exact patched card controls_update method with mocked IPC/apply endpoints. Startup/state_update are source-reviewed; this is not a whole running-stack or hardware build claim.

## Verification and practical limits

Final validation:23 behavioral/regression tests and24 portable staged tests pass. Ford suite213 passed,79 skipped,12,063 subtests passed. Five drives/72 segments replay410,939 controller updates and16,377,999 physical RX frames per hook. Of244,093 generated TX,1,843 precede Ford configuration; all242,250 configured TX accepted, zero rejected, zero invalid required RX. DefaultOFF byte parity holds across all updates. All50,567 generated messages at≥25mph and12,425 at≥45mph are byte-identical to baseline.154 generated update streams differ below25mph.

Latest persistent event105.43–107.43s:14/40 encoded angle commands changed, maximum0.0075rad. Later catch-up event510.48–512.48s:0/40 changed. This demonstrates targeted command action, not a corrected vehicle response.

Final exact counts are in `summary.json`, `verification.txt`, `test-green.txt`, `staged-tests.txt` and `ford-native-tests.txt`. Full replay covers the same five complete drives/72 segments, with independent native hooks and no forced controls permission. Input manifests are checked against all72 raw segment hashes; provenance includes inherited report modules, source revisions and native library.

Original96 hypothetical gain/lag/delay cases: unit-gain peak no longer exceeds requested response,45mph commands identical. Expanded210 stress cases cover gains0.25–1.25, response constants0.05–3s and delays0–3s. For assumed gain≤1, peak remains≤requested; gain1.25 baseline overshoot is unchanged. These are simple independent-feedback plants, without a full planner or identified vehicle dynamics. They do not establish stability for every real steering system, nonlinear friction, road condition or delay.

In the original grid, an assumed50% steady response improves to about55%, versus about60% with the stronger prior candidate. This is only a hypothetical tradeoff, not a predicted percentage of road improvement. The expanded stress screen's late-plateau ratio is not a steady-state estimate in the slowest cases.

The overly conservative hold20 variant passed safety replay but changed zero commands in the latest weak-response window. Its files are explicitly prefixed `hold20-` and are historical comparison evidence. `window-diagnosis.json` and `hold-sensitivity.json` explain choosing the prior six-observation hold with the new response-onset/projection guards. Final full replay must demonstrate nonzero selected-window action before candidate readiness is claimed.

At/above25mph the added term is zero. An artificial instantaneous speed/demand jump can retain a small previous-output difference through the unchanged slew limiter; discarding that history would alter the existing rate guarantee. Recorded≥25/45mph parity is the concrete verification target, not a universal arbitrary-jump equivalence claim.

## Next step

The local overshoot regression and context-handling gaps are addressed, with reviewable paired patches and a default-off trial. Actual Navigator handling remains unproven. A later authorized deployment needs a fresh backup, paired source/parameter build verification on the device, startup/parked checks with the trial initially off, and then a controlled driving comparison if those checks pass. No firmware/OS or update-policy change is part of these patches. This work does not claim to repair an unidentified EPS physical limit.

The saved [Auto Start/Stop evidence](../navigator-autostop-button-evidence-2026-10-14/README.md) is unchanged and remains available for its separate roadmap task.
