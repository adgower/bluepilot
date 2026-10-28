<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Restart-continuity paired integration — October 24, 2026

The reviewed 6.7 mph restart prototype is integrated locally into paired branch `codex/navigator-tracking-release`: parent `49be383b2913c5cd62372f7e94222ef75592c61f`, child `d459133a3453d523f1e64b7017a444d78d111f17`. Both repositories are clean and the parent gitlink matches the child. No push, SSH, device changes, OS/firmware update or CAN activity occurred in this task.

## Change

The Ford controller constructs the new `RestartClearance` observer, whose class AST matches the frozen prototype exactly. It retains fresh measured clearance across a speed-only 3 m/s crossing, preserving an existing propulsion request. Existing observer faults, braking and reset behavior remain; no acceleration gain or handoff rise-rate change. Thirty-five permanent regressions were added, including the original controller request-continuity case.

The controller class differs from the preserved baseline only in the observer constructor. All protected steering, vehicle values, native safety and parent coordination source hashes match the prior baseline. **1.20/0.97 unchanged.**

## Fresh validation of actual integrated files

- Minimal Mac build, full development build and Panda compilation: all exit 0. Compilation only; nothing flashed.
- 75 focused/retained comparison contracts passed against actual integrated files and the preserved baseline controller.
- Complete canonical parent suite: 1,029 passed, 87 skipped, one expected failure, 281 subtests.
- Complete child suite: 4,551 passed, 1,690 skipped, 24,693 subtests. Existing Mac debug safety hooks used; no UBSan/ARM claim.
- Fresh actual-file replay: all 136,308 extracted trace rows are byte-identical to the reviewed prototype replay. Trace scope is the documented controller reconstruction; this is not complete vehicle/CAN-byte or physical equivalence.
- Ruff and Git whitespace checks passed. Independent integration review found no blocker.

## Retained replay evidence

The prototype's completed 47-segment native comparison is retained and bound by identical class AST, the narrow constructor change and fresh integrated trace equivalence: 10,914,382 RX and 328,981 TX per variant, 16 shared rejections and zero added candidate rejections. It was **not rerun** in this integration task. Original non-ACC TX and vehicle feedback are frozen; controls permission is not forced. No new full historical corpus replay is claimed.

The prototype changed propulsion slots in the selected launches without changing brake commands or the two existing release-timeout episodes. Those unresolved timeouts and highway pulsing remain outside this fix. Physical comfort, fuel economy and moving engagement after installation remain unproven.

## Delivery status

Local commits only. No new ARM build, device staging, activation, parked or road checks. The Comma remains unaffected by this integration task. Build logs, JUnit reports, source equivalence/hash receipts, `integrated-replay-comparison.json`, `REVIEW.md` and `validation-receipt.json` provide the evidence. A future installation must use the exact published pair, fresh backup and device-specific acceptance.
