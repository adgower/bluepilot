<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Very-low-speed Navigator trial — installed October 14, 2026

**Installed and enabled. Native build, final source selection and offroad runtime acceptance pass.** User authorized installation after the local prototype/replay, requested backup first and preservation of 1.20/0.97 and good ~45 mph behavior. No new road evaluation of this revision has occurred.

## Installed paired source

- Branch on Mac and device: `codex/navigator-very-low-speed-trial`.
- openpilot: **76d78d46fc8713f2f6b1147af02e5aed07bf15a1**.
- opendbc: **f50241ca59d866af275ff6c34fb407b93094e892**.
- Previous parent/child: `6ae31161b73de2ce5043f708569759ac5f55f283` / `c09baff5c2cdd7c887e25c2d88b671f403e1ed9d`.
- Both installed Git working trees clean. Live manager GitCommit/GitBranch match the new parent/branch.

The existing low-speed-trial startup selector now constructs `VeryLowSpeedGainPrototype(..., enabled=True)` when the current Expedition/Navigator, pinion and low-speed flags qualify. Both existing Ford preference values were already enabled and remain enabled. **There is no new toggle to find.** The previous trial stays in its own module and the new strategy subclasses it. Switching the existing low-speed trial OFF removes both the preceding trial and this added correction; reverting only this increment requires the previous paired source.

Additional path-angle conversion multiplier: **1.10 through 15 mph**, smooth taper over 15–25 mph (**1.05 at 20 mph**), exactly **1.00 at/above 25 mph**. Owner **1.20/0.97** constants are byte-preserved in the base steering file. Existing pinion option, normalized Navigator geometry, inherited limits/override and 30–45 mph trial behavior are preserved. No tracking integrator, global actuator-delay change, MADS or longitudinal feature was added.

## Backup completed before source replacement

Private device backup:

`/data/navigator-backups/<private timestamp identifier>-pre-very-low-speed/`

Private Mac backup:

`${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-very-low-speed/`

Ten original artifacts totaling **981,909,647 bytes** were verified against device-side SHA256 and byte counts on the Mac. They include complete tracked parent and child source archives, full Git-history bundles, full parameter storage including calibration, the launcher and preserved steering/controller files. Nested source/parameter archives were read to EOF. These are source/settings/history backups; this task did not duplicate every ignored native/model artifact as a new full disk image. The prior full migration backup remains available.

The outer tar command reported a directory-metadata change when separately staged small Git bundles appeared during its read. Every original immutable backup file matched the original manifest, and nested archives were readable; verification did not rely on that outer command's exit code. The Mac's `verification.json` records this explicitly.

A separate private installation-evidence archive includes the build log, successful native validation, final runtime receipt, installation scripts, new commit bundles and the preserved Panda image. The saved pre-trial Panda image matches the post-install artifact SHA256. Backups and raw Params data are not committed to Git. Backup integrity is verified; restoration has not been exercised.

## Validation before activation

The final integrated selector passed **213 Ford/controller/native safety tests, 79 skips, 12,063 passing subtests** on the Mac. The new selector test first failed against the old selector and passed after wiring the new strategy. This run used the matching plain native debug safety library; the initial attempt without that loader hit the known macOS sanitizer-library restriction rather than a controller assertion failure.

Full recorded-input controller/native replay was rerun after integration, including **all 62 segments from four complete cached drives**. Both the baseline and candidate CAN stream hashes exactly match those from the preceding standalone prototype run for every drive. Results:

| Evidence | Result |
| --- | ---: |
| Controller updates per candidate | 353,029 |
| Physical received frames per safety instance | 14,084,237 |
| Candidate TX accepted after Ford configuration | **208,186** |
| Candidate / baseline generated TX rejections | **0 / 0** |
| Checked relevant RX-invalid frames | **0** |
| Compared generated messages at ≥25 mph / differing updates | **41,285 / 0** |
| Compared generated messages at ≥45 mph / differing updates | **12,425 / 0** |
| Default-OFF differing controller updates | **0** |

As before, 1,477 messages before recorded Ford configuration are excluded, and each drive has one initial RX-check warmup invalid tick. The intervening trial lacks complete locally cached raw logs and is not claimed as fully replayed. See the [prototype report](../navigator-very-low-speed-prototype-2026-10-14/REPORT.md) for replay limitations and the separate broad-suite MISRA bootstrap failures. No safety C code changed. Recorded-stream transition rejections in the earlier analysis are not claimed fixed by generated replay.

After backup verification and fresh ignition-off/offroad checks, the app was stopped and both local Git bundles were imported over SSH. The previous branches/commits were retained. On-device full **scons -j4 passed**. Actual installed imports verified strategy selection, both curvature signs, 10/15/20/25/45/55 mph factors, geometry **3.1115 m / 19.6**, safety parameter **10**, preserved settings/calibration and unchanged base steering source. This is an on-device isolated startup/strategy check, not live steering actuation.

The Panda signed image remains byte-identical:

`5a10a6119110b3c41a03d381c4bdd3bea4e05c3a7164bef515b42df7054c466e`

No OS or firmware update/flashing operation was performed.

## Startup and final acceptance

The first app restart encountered the OS launcher's tap-triggered reset prompt. Inspection showed `/usr/comma/reset --tap-reset`; the launcher's cumulative touch-count condition had triggered its one-time boot check. No reset was confirmed. A subsequent normal service restart, after the launcher had created `/tmp/booted`, closed that prompt and launched openpilot normally. Calibration/settings hashes afterward match the backup. No reset or reinstall was performed.

Manager initialization also populated previously absent ExperimentalMode from its upstream default. Its original **unset/off** state was restored after startup, and the final native Params API check confirms both absence and get_bool false. Stock longitudinal/Alpha remain disabled as before. Current upstream removes that key for stock-longitudinal operation; a later manager start may populate defaults again before normal cleanup. This task did not add an unrelated manager/UI default-policy patch.

Final 15-second offroad observation:

- deviceState, managerState and pandaStates all **alive and valid**.
- Live Git metadata agrees with the installed new parent and branch; parent and child source clean.
- IsOffroad true; device not started; ignition line/CAN flags false; controls disallowed; Panda **noOutput**.
- TX-blocked counter **0**, RX checks valid; no unexpectedly stopped required process. The intentionally disabled updater remains excluded from failure reporting.
- All seven selected preference states match the backup: update pause, both Ford preferences, Alpha/Experimental state, openpilot enable and accelerator disengagement preference.
- CalibrationParams, CarParamsPersistent, LiveParametersV2 and LiveTorqueParameters hashes all match the backup.
- Owner 1.20/0.97 constants and Panda image unchanged. Original boot launcher remains unchanged.

The app has already restarted; a new full device reboot is not required to load this source. The correction will be selected at the next normal onroad initialization using the already-enabled preferences. This offroad acceptance does not establish onroad recognition, powered Chestnut inference, live command acceptance or improved handling for the new revision. Earlier inference/road evidence belongs to the previous revision.

## Rollback and artifacts

`ROLLBACK.sh` records an application-only rollback to the exact preceding child commit and parent branch, guarded by ignition-off/offroad and clean-source checks. The child is restored by commit rather than assuming it was previously on a named branch. The script passed shell syntax checking; **it was not executed and is not a tested restoration procedure**. OS/firmware rollback and full parameter restoration are separate operations. Preserve the backups; do not reset or clean over future source changes.

Reviewable local artifacts: paired install patches; final-selector `full_replay.py`, `full-replay.json`, `replay-console.txt` and `provenance.json`; `local-tests.txt`; [sanitized runtime receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md). Private Mac installation evidence was separately read and validated against the expected installed SHAs, native test result and unchanged Panda image.

Actual steering benefit remains untested. The new command is a modest 10% experiment rather than a proven cure for the large previously observed 15 mph response deficit. Recorded ≥45 mph parity preserves the covered commands, not a universal guarantee about future closed-loop vehicle behavior or arbitrary limiter-history transitions.
