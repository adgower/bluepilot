<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator pinion feedback evaluation and integration design

2026-10-14. Offline evaluation only. No Comma files, settings, firmware, safety modes, services, or vehicle configuration were changed. No active ECU queries or live CAN access.

## Decision

Pinion feedback is a well-supported candidate to replace the biased decoded vehicle yaw input. It improves agreement with calibrated Comma motion substantially in the saved data and can be integrated while preserving the owner's exact 1.20/0.97 steering factors.

It is NOT a demonstrated complete fix for low-speed understeer/wandering. The tighter 28 mph undertracking example has identical replayed steering commands after either pinion substitution. Only around 5% of sampled newer 20–30 mph commands change meaningfully. A second low-speed command-response calibration task will likely remain; no untested numeric tuning change is recommended from this evaluation.

Recommend an opt-in, Expedition/Navigator-scoped, startup-only **fixed-geometry pinion option**, paired with corresponding Panda safety logic and default OFF. This offers a small coherent first integration. BluePilot's learned-geometry approach is more accurate against its own motion-learning input, but needs a more complex controller/safety consistency design and must not be dropped into the fixed-geometry safety path.

## Provenance and preservation

- Installed openpilot baseline: f35e6e5eb11ca9cddad3ed945d44d8f191679240, navigator-angle-v1.
- Installed opendbc baseline: eb70bef4f56d2e9e91cb5a0a8374890a6acfaf51.
- Preserved live lateral_angle.py SHA256: bc205573c3cda6b0ec77e4ec262eab11595adaaf3e0f8ace781b22992105d780.
- Candidate fixed-model reference: existing opendbc commit 0bd0763bcf88553f570b1de457ad6c0dc76fca83. Its safety source is evaluated, but its 1.15/0.98 tuning and automatic feature selection are NOT adopted.
- BluePilot alternative reference: locally cached upstream/bp-dev-expedition at 3210caa02d9e09b46d08be490f689edb23b22b20. Remote tips were not refreshed.

Evaluation loads the exact preserved live control source and overrides only its current-curvature method in offline subclasses. Assertions preserve low factor 1.20 and high factor 0.97. Low/high platform gains, 13.5/26.82 m/s gain breakpoints, curvature blend, driver override, DBC limits, and rate limits remain the original source's implementation.

Cached geometry read without ECU access: mass 2878 kg, wheelbase 3.1115 m, steer ratio 19.6, rear ratio 0, center-to-front 1.36906 m, tire stiffness front 353037.28125 and rear 438491.46875 N/rad. These match the candidate native fixed-model assumptions; this does not prove the physical Navigator geometry is exact.

## Feedback evaluation

Three saved datasets were used: two newest full-rate drives and earlier full-rate segments 26/29 for the faster comparison. Selected signals and calibrated motion come from the preceding yaw investigation, with timestamp matching, lateral-active/no-driver-press filtering, and motion/calibration validity checks. DeviceMotion is converted to calibrated vehicle frame. In these recordings controller-sign independent curvature is calibrated z yaw divided by speed; Ford CAN yaw has the opposite sign.

### Median absolute yaw-rate-equivalent error against calibrated Comma motion

| Dataset/speed | Selected samples | Existing CAN-yaw feedback | Fixed pinion model | Learned pinion model |
|---|---:|---:|---:|---:|
| Newer drive-1, 20–30 mph | 656 | 0.01587 rad/s | 0.00320 rad/s | 0.00154 rad/s |
| Newer drive-2, 20–30 mph | 531 | 0.01611 rad/s | 0.00377 rad/s | 0.00144 rad/s |
| Newer drive-2, 30–40 mph | 60 | 0.01614 rad/s | 0.00489 rad/s | 0.00253 rad/s |
| Earlier selected segments, 40–50 mph | 417 | 0.01664 rad/s | 0.00334 rad/s | 0.00130 rad/s |

Fixed pinion reduces median error by about 77–80% at 20–30 mph and about 80% at 40–50 mph. It still has a residual offset from fixed geometry/uncorrected steering zero, so it is not a perfect motion measurement.

The learned model mirrors BluePilot: live stiffness and steer ratio plus angle offset and road roll. Its parameters are themselves learned from Comma motion, so superior agreement with that source is not independent ground-truth validation. This is a same-source comparison, not proof of universal physical accuracy.

## Held-input command replay

`evaluate.py` runs the preserved LateralAngle.update implementation at saved 20 Hz send timestamps using nearest saved carState/carControl inputs. It compares baseline yaw, fixed pinion, and learned pinion while keeping recorded planner demands, driver flags, and motion fixed.

This is a command replay, not a closed-loop vehicle simulation. A changed controller would change vehicle response and subsequent planner demand; saved recordings cannot supply that counterfactual. Inputs were sampled at about 10 Hz, so not every original controller frame/driver transition is reconstructed exactly.

Baseline reconstructed commands match encoded path-angle commands with median absolute differences around 0.00018–0.00043 rad in meaningful bins; the encoding step is 0.0005 rad. This supports the replay's command-scale fidelity, not exact frame-for-frame equivalence.

| Dataset/speed | Replayed active/no-driver-press commands | Fixed model commands changed by >0.0005 rad | Learned model changed by >0.0005 rad |
|---|---:|---:|---:|
| Newer drive-1, 20–30 mph | 1,312 | 5.18% | 5.18% |
| Newer drive-2, 20–30 mph | 1,062 | 4.52% | 4.71% |
| Newer drive-2, 30–40 mph | 120 | 10.00% | 10.00% |
| Earlier selected segments, 40–50 mph | 840 | 0% | 0% |

Largest fixed-feedback changes in selected low-speed bins were about 0.022–0.045 rad during affected transients. Those larger individual differences warrant review; the small percentage of changed frames does not by itself establish that changes are harmless.

### Previously identified sustained examples

- Tighter turn near 27.7 mph, newer drive-2 107.5–112.7 s: fixed and learned options produce NO command change. Independent motion was about 60% of requested curvature in this example. Therefore replacing the feedback source alone does not correct this recorded undertracking through the replayed command path.
- Gentler turn near 28 mph, 162.0–168.2 s: maximum changed command about 0.00128 rad. Most of the interval remains unchanged. No new actual tracking result can be inferred.
- Faster turn near 42.6 mph in selected older segments: fixed and learned options produce NO command change. This supports preserving the recorded command behavior in that example, not guaranteed high-speed behavior on every future turn.

Changing feedback affects demand clipping and shadow-curvature safety reference; it does not automatically add low-speed steering gain. The owner’s existing 1.20 factor still applies to the high-curvature arm only.

## Native safety reference evaluation

A pristine export of candidate opendbc commit 0bd0763 was compiled into a host-native safety test library on the Mac. Production workspaces and Comma firmware were not modified. The standard sanitizer library could not load under macOS platform policy; a plain native build succeeded. Sanitizer validation was NOT performed.

Saved CAN receive frames 0x415 (speed) and 0x7E (pinion) were replayed into the actual C receive hooks in pinion mode. For each pinion frame, C's rolling curvature sample bounds were compared with exact baseline VehicleModel math using the same decoded speed and angle.

| Dataset | Saved pinion frames | Non-3 quality frames | Native RX invalid results | Maximum C/Python sample-window difference |
|---|---:|---:|---:|---:|
| Newer drive-1 | 25,996 | 0 | 0 | 1 CAN unit |
| Newer drive-2 | 36,275 | 0 | 0 | 1 CAN unit |
| Earlier selected segments | 11,997 | 0 | 0 | 1 CAN unit |

Total 74,268 frames. One curvature CAN unit is 0.00002 /m. Largest contiguous recorded pinion gaps were about 25–41 ms; deliberately omitted multi-minute recording gaps were not treated as sensor dropouts.

Controlled native probes verified:

- Active test TX denied before the first pinion sample.
- Fresh valid pinion permits a controlled valid test TX.
- Stale pinion, bad quality, stuck counter, and wrong bus deny active test TX.
- Yaw messages do not overwrite the selected pinion measurement.
- Feature flag OFF retains yaw-based measurement.

These are native reference unit probes and actual receive/geometry replay. They are NOT complete TX safety replay, full RX liveness/relay validation, verification of the currently running Panda binary, firmware flashing, or vehicle runtime proof. The pinion checksum remains unknown/ignored in the reference implementation; counter, quality, length and liveness are enforced. This limitation requires explicit review.

## Concrete integration design for navigator-angle-v1

Preserve the installed openpilot/opendbc commits and the exact live steering patch in isolated local checkouts. Integrate the pinion feature independently of the broader pending branch/tuning updates.

### Configuration and UI

- Add persistent BOOL `FordPrefSteerAngleCurvature`, default false, in openpilot/common/params_keys.h.
- Add a restart-required Ford-specific toggle to openpilot/selfdrive/ui/layouts/settings/toggles.py, explaining steering-angle-derived curvature rather than another physical yaw sensor.
- Read it once in openpilot/selfdrive/car/card.py during initialization. No mid-drive mode changes.
- Pass an optional keyword-only setting into opendbc/car/car_helpers.py:get_car (default false). Apply a pure Ford configuration helper to freshly computed CP BEFORE CarInterface/CarController construction.
- Scope eligibility to FORD_EXPEDITION_MK4 with CANFD and the verified fixed geometry. Leave every other platform unchanged.
- Existing CarParamsCache supplies fingerprint/firmware information, while get_params recomputes CP; apply the option after that step. Do not delete cached vehicle data merely to change this option. Test toggling against a cache from the opposite prior mode.

### Controller and paired safety

- Add distinct flags to opendbc/car/ford/values.py, using the reference's proposed CP flag 2 and main safety flag 8; existing CANFD safety flag 2 yields safetyParam 10 when enabled. These main-field bits are NOT BluePilot's separate CP_SP safety bits.
- Add a fixed private VehicleModel in opendbc/car/ford/lateral_angle.py only when enabled. Use pinion-derived curvature for all measured-feedback/shadow-reference reads; leave raw CarState.yawRate untouched for diagnostics.
- Keep `_FORD_LOW_SPEED_FACTOR_ANG=1.20`, `_FORD_HIGH_SPEED_FACTOR_ANG=0.97`, Expedition-only factor application, and all existing gain/blend/rate/driver behavior exactly as preserved.
- Pair it with the reviewed flag-gated pinion receive path in opendbc/safety/modes/ford.h. Keep existing curvature/rate limits. Enforce quality/counter/liveness and fail closed on invalid pinion; do not silently fall back to biased yaw while pinion mode is selected.
- Confirm the candidate geometry constants remain equal to the CP used by the Python model. Do not add learned parameters to one layer only.
- Verify compatible compiled Panda firmware before enabling the option on device; a parameter on old firmware must not be treated as sufficient. Installed Panda binary provenance remains to be established without opening a conflicting interface.

### Required acceptance before any device transition

- Default OFF produces baseline controller output, CP flags, and safety config across recorded fixtures, including driver override and mode transitions.
- Enabled option does not alter the stored gain constants or unrelated Ford/non-Ford platforms.
- Controller/safety geometry and sign match across speed/angle ranges and saved recordings.
- Invalid/missing/stale/wrong-bus pinion fails closed; yaw cannot replace the selected source; switching configuration clears relevant history.
- Cached CP from prior mode does not retain obsolete flags after restart.
- Full raw-CAN paired controller/TX safety replay, including blocked timestamps and transitions, supplements the limited native probes performed here.
- Publish an opendbc commit containing both the preserved steering change and optional pinion feature, then an openpilot commit pinning it and adding the UI/init option. Verify both SHAs and checks. Do not use a device-only commit or reset over the live steering diff.
- Keep updates paused until a separately authorized, reviewable device transition is prepared. No firmware installation, restart, settings change, Git commit/push, PR, or deployment occurred in this evaluation.

## Expected effect on the owner’s issue

Likely benefit: remove reliance on the biased vehicle yaw measurement for feedback, reduce one-sided clipping/false-limit behavior, and use a consistent pinion reference in both layers.

Unproven benefit: reduced real lane wandering after changed feedback. A small number of changed commands can affect subsequent closed-loop trajectories, but recorded inputs cannot prove that improvement.

Not established: cure of sustained low-speed understeer. The strongest tighter-turn example receives unchanged commands, so a separate low-speed command-response/gain investigation remains. Do not combine that tuning adjustment with the feedback change; otherwise any improvement/regression becomes difficult to attribute.

## Artifacts

- evaluate.py: feedback comparison and held-input controller replay, with gain-preservation assertions.
- evaluation.json / command-replay.json: numeric results and selected replay commands.
- extract_rawfeedback.py / rawfeedback.json: saved CAN receive-frame extraction.
- native_probe.py / native-safety.json: native reference RX/geometry replay and failure probes.
- vehicle_model.reference.py / ford-safety.candidate.h: exact source snapshots.
- cached-geometry.json: identifier-free geometry used in evaluation.
- manifest.json: artifact checksums.

Best next step: implement and review this optional fixed-geometry feature locally, then perform full paired safety replay before discussing any Comma transition. This report is an evaluation/design, not a deployed fix.
