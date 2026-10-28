<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Regression repair installation complete — October 27, 2026

**Exact new pair is active; ignition-off and powered stationary Park acceptance both passed.** This final report supersedes the pending powered status in the immutable [offroad activation checkpoint](ACTIVATION_REPORT.md).

Active parent `e05e42f43d2907a4f02915a924cfd95a46197e79` pins child `5097b993965b2b65ea3fcca7e3769cfa9403d49c` on `codex/navigator-tracking-release`. Complete previous install remains at `/data/openpilot.pre-regression-repair-<private timestamp identifier>`. Fresh68parameter device/private-Mac backup was verified before the whole-install switch. Current selected settings, Alpha ON,1.20/0.97, geometry, firmware, launchers and AGNOS20.1slotB were carried through. No OS/firmware update or test/custom CAN/ECU commands were issued. The app service was restarted only for activation; no device reboot.

## Powered passive check

Owner confirmed home-screen response, ignition ON, stationary Park and assistance disengaged. Observed55.00seconds of the actual new running stack:5,496carState/control/output samples,550Panda samples, all required topics alive/valid. Vehicle remained stationary in Park; assistance never became active. Ford safety parameters matched Alpha longitudinal. No board/receive/transport/heartbeat fault, coordination fault, controlsMismatch alert, new blocked TX increment or unexpected stopped process was observed. Historical blocked-TX values were0through this observation.

Big-model cadence was**19.99979Hz**, with0reported frame drops. All1,100observed pose samples were healthy; maximum observed source age was39.44ms. These are current-stream samples, not proof of the consumed moving-speed producer snapshot. See `parked-powered.json` and its raw log.

## Final source and owner-state audit

Exact active and retained rollback pairs are clean; active gitlink matches the child. Candidate source manifests and7protected source/firmware/launcher hashes match. Service is active, settings differ only by the owner-requested ignition/offroad transition, and Alpha/coordination remain ON. See `final-activation-audit.json`.

Some serialized learned caches refreshed at normal onroad startup, so raw hashes changed after the earlier offroad preservation check. A read-only numeric comparison shows learned steer ratio**22.0367298**, average angle offset**−1.8592135degrees**, and lateral delay**0.26231572s** retained exactly. Torque cache numeric values/status are unchanged. Vehicle configured wheelbase3.1115m, steer ratio19.6, actuator delay0.2s, control flags and longitudinal mode are unchanged. `CarParamsPersistent` differs only in`carFw`metadata; no firmware programming occurred. Existing per-route filter initialization resets stiffness to1and transient roll/instantaneous offset; the installer did not manually write learned parameters. See `learned-after-start.json` and the existing `paramsd.retrieve_initial_vehicle_params` behavior.

## Evidence limits

1304ARM/Ford/native/context tests plus12083subtests and both parked checks passed. Local237segment longitudinal and658segment scheduled steering port comparisons remain recorded in the integration report; there is no fresh full route-native replay here. **Road-level pulsing, tracking and controls-mismatch improvement are not established by these parked checks.** Two historical release-timeout replay faults remain part of the known evidence.

Original staging and offroad manifests remain immutable. `ACTIVATION_COMPLETE_VERIFICATION.json` binds the final powered/source/numeric receipts and both earlier verification checkpoints. The new runtime is installed, not merely staged.
