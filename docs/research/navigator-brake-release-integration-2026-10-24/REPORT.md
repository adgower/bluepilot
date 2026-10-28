<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Brake-release paired integration — October 24, 2026

The frozen brake-release prototype is integrated locally into `codex/navigator-tracking-release`: openpilot `064e086d2dc4e724df007fa66953d4f7e48f0141`, opendbc `50719b1ef987d6582e85c417adb452f098b850cb`. Both checkouts are clean and the parent gitlink matches the child commit. No push, SSH, device writes, installation, firmware or CAN activity occurred in this integration task.

The child gains `longitudinal_admission.py`, controller wiring and 31 permanent regression cases. A brief mild grade-induced negative crossing can coast instead of latching braking, with bounded dwell/exposure. Received brake torque reopens clearance qualification after prior clearance. Existing stronger braking, default-off, stop/creep, native limits and the one-second release deadline are retained. Both lateral-angle and Ford values files remain byte-identical to child baseline `d2e8d040`; owner 1.20/0.97 is preserved.

## Validation

- Actual integrated files against the preserved baseline: **40 contracts passed**. Permanent child tests: **31 passed** independently during review, also included in full suite.
- Minimal Mac build, full Mac build and Panda firmware build: **all exit 0**. Panda build is compilation only, not flashing.
- Complete canonical parent suite: **1,029 passed, 87 skipped, 1 xfailed, 281 subtests**.
- Complete child suite using existing Mac debug native hooks: **4,516 passed, 1,690 skipped, 24,693 subtests**. No ARM or UBSan claim.
- Ruff and both Git whitespace checks pass. Independent integration review found no critical/important issues.
- Controller class and all admission classes match the frozen prototype AST exactly (module docstring/import wiring excluded). The completed **1,066-segment** prototype historical replay is retained and bound to this identical implementation; it was not rerun in this task and primarily covers lateral/native/default-off regression.
- Fresh actual-file active-Alpha replay: **51 segments / 4 sessions**, **11,903,572 RX** and **352,930 TX per variant**, **31 shared rejections, zero added**, zero relay faults. All results match the frozen prototype replay exactly. **57,931** fixed-input excluded packets are exact; no owner extension or native permission forcing. The same release episode remains (baseline one fault slot, candidate two adjacent protective fault slots). See `new-drive-summary.json` and `new-candidate-native-safety.json`.

`build-results.json`, JUnit reports, `source-equivalence.json`, `integrated-source-hashes.json` and `REVIEW.md` provide receipts. The original prototype directory and hash-bound receipts were preserved. The initial external contract invocation encountered the unrelated BluePilot ancestor conftest; setting the integration folder as pytest confcutdir produced the successful isolated 40-case run.

## Limits and next gate

Recorded torque belongs to the old command stream. Against that frozen response, the original release-timeout episode remains and candidate protection can withdraw earlier; this does not prove the mechanical timeout is fixed. Command-dependent models support avoiding the trigger, but road smoothness, fuel economy and physical brake clearance remain unproven. ARM build, device staging and parked acceptance are separate future steps requiring authorization. No guard threshold was loosened to suppress the alert.
