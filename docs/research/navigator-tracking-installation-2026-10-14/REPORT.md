<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator persistent tracking correction installation

Installed and enabled. Native build, isolated startup, ignition-off and powered parked checks pass. Road evaluation of this revision remains pending.

## Paired source

Branch on Mac and Comma: `codex/navigator-tracking-release`.

- Parent: `74f66e7a0bf1dc0718431532948ece2c4fb0041c`.
- Child: `1b965caadd4a6aea4d09985532bf7cca6c0873ca`.
- Previous parent/child retained on `codex/navigator-very-low-speed-trial`: `76d78d46fc8713f2f6b1147af02e5aed07bf15a1` / `f50241ca59d866af275ff6c34fb407b93094e892`.

Existing owner1.20/0.97 and low-speed feedforward remain intact. New opt-in `FordPrefPersistentTracking=1` selects the bounded release-aware strategy at the next onroad initialization when Expedition identity, pinion and low-speed flags qualify. No new UI toggle was added. [Candidate design and limits](../navigator-tracking-release-2026-10-14/REPORT.md) remain applicable: zero added term by25mph, original range/rate limits, freshness/lane-change/driver guards, no stall-rescue pulse or safety-limit expansion.

These commits are local and installed through verified SSH Git bundles; no remote push/PR was performed.

## Verified backup before source replacement

Private device backup: `/data/navigator-backups/<private timestamp identifier>-pre-tracking-release/`.

Private Mac backup: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-tracking-release/`.

All12 original files,1,037,386,553bytes, matched device SHA256 and byte counts on the Mac. Source archives were read to EOF (1,260 parent files,476 child files); parameter archive68 files. Backup includes tracked source, full Git history bundles, parameter storage/calibration, original launcher, steering modules and signed Panda image. Ignored build/model assets were not duplicated as a new disk image. Integrity verified; restoration has not been exercised. Earlier complete migration recovery material remains separate.

Private Mac installation evidence additionally preserves native build/validation/runtime receipts, guarded scripts and the new paired Git bundles. No private parameter dump or raw drive data is copied into this report.

## Validation before enabling

The actual committed portable modules passed24 integrated tests. Full native replay across five drives/72 complete cached segments reproduces the prior prototype's baseline and candidate command hashes exactly for every drive. All242,250 configured generated TX accepted, zero rejected, defaultOFF parity and recorded≥25/45mph parity. This establishes saved-input behavior, not vehicle handling.

Fresh live preflight verified expected clean source, AGNOS19.9, offroad, ignition flags false, controls disallowed and Panda noOutput. After backup verification, stopped the app, imported/switched the paired source and ran full target-native `scons -j4`: passed. No OS or firmware updater/flasher was invoked; signed Panda image remains byte-identical.

Native isolated validation passed: exact installed commits, clean trees, original seven selected preference states and four calibration/persistent-data hashes,1.20/0.97,3.1115m wheelbase/19.6 ratio, safety parameter10, high-speed strategy parity and trial feedback/blinker reset. Trial stayedOFF throughout these checks.

The exact installed Car constructor was then exercised with in-memory Params and stubbed IPC: disabled selects original VeryLowSpeedGainPrototype; enabled selects ReleaseTrackingPrototype. No actual CAN I/O or parameter writes occurred in that constructor test.

TrialOFF offroad runtime passed before activation. Enabled the new preference synchronously, restarted the app, restored the captured original absent/off ExperimentalMode state after upstream manager default initialization, and observed the final15-second offroad window:

- Device, manager and Panda topics alive and valid.
- Trial enabled; live Git metadata matches the exact installed pair; both trees clean.
- IsOffroad true, device not started; no ignition or controls allowed; Panda noOutput.
- Zero TX blocked, no invalid RX checks, no unexpected stopped required process (intentionally paused updater excluded).
- All seven selected existing preferences and all four captured calibration/persistent-data hashes match backup.
- Original1.20/0.97 source and signed Panda image unchanged. Existing update pause, pinion and low-speed preferences preserved; Alpha/Experimental settings retain baseline states.

See `runtime-summary.json`. This does not establish full-power Chestnut inference, onroad CarParams/context freshness or driving improvement for this revision.

## Installation notes

The first detached preflight used root; Git's repository-ownership guard stopped it before any source switch or app stop. Reran as the comma user without adding a safe.directory exception. Review also tightened exact target-SHA assertions and source/firmware verification before any rollback restart. Successful native installation completed with status0; rollback was not needed or exercised.

The first attempt to enable the preference used an asynchronous write and its immediate read assertion stopped the restart chain. Repeated with `block=True`, verified durable state, and completed the actual offroad restart. Final receipt above is after that completed restart.

Upstream manager startup repopulates previously absent ExperimentalMode, as on the preceding installation; restored its captured absent/off state after each restart. No unrelated manager-default-policy patch was added. This initialization behavior can recur on later app restarts.

## Rollback

To disable only the added correction, while ignition off/offroad set `FordPrefPersistentTracking` false using a blocking Params write, then restart the app. The existing low-speed/pinion options and1.20/0.97 remain. Original paired source branches and verified backups are retained for a separate source rollback if needed. Do not reset/clean future local modifications. Full parameter restoration and OS recovery are separate procedures.

## Powered parked acceptance completed

The user confirmed ignition on. A fresh preflight verified Park/0m/s, valid CAN, Ford safety10 and controls disallowed. A55.01-second passive observation then passed, with no diagnostic injection, engagement requests or steering-command tests:

- All12 observed topics alive/valid, including actual live CarParams; all captured state fault/timeout/invalid-CAN counts zero. Vehicle stayed in Park at0m/s with selfdrive disabled and no alerts.
- Live forced Expedition profile retains Navigator geometry3.1115m/19.6, flags15 including pinion/low-speed, stock longitudinal and Ford safety10. New tracking preference enabled, both Ford options enabled, update pause preserved; Alpha and Experimental remain off.
-1,101 big-model samples:20.000fps,39.44ms mean execution, zero reported frame drops in sampled messages. Final Chestnut GPU48C/memory68C,29W,13.346V and no supply fault.
-550 Panda samples: zero RX-invalid/TX-blocked, no invalid RX checks, heartbeat loss, SPI errors or faults; controls remained disallowed.
- Model/control context valid throughout sampled observation; lane-change state off, no blinkers. Maximum observed subscriber ages: state18.0ms/control27.3ms/model28.9ms. These are subscriber observations, not direct internal strategy cadence/guard instrumentation. Correction is speed-ineligible while stationary.
- Actual source pair still exact and clean; calibration reports calibrated. Earlier native checks preserve owner1.20/0.97 and high-speed command parity.

`powered-parked-summary.json` saves the receipt. Full passive samples/script are preserved privately on device and Mac in the existing backup. This establishes powered stationary health, not steering response, engagement behavior, full closed-loop stability or road improvement.

## Next comparison

A supervised road comparison remains. Use a familiar route and note speed/time/location context of any understeer or intervention so later analysis can identify the exact segment; do not intentionally seek the steering limit. The correction is bounded below25mph and existing45mph recorded-command parity remains the offline reference. No road result has been claimed.
