<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator body-confirmed high-speed integration plan

> Execute inline with test-first gates and one fresh source reviewer. Continue through authorized local integration and checks; do not contact the Comma or publish.

Goal: integrate the validated wheel/body, unwind and driver-release fixes into the existing paired `codex/navigator-tracking-release` branches.

Spec: `docs/research/navigator-highspeed-release-2026-10-17/DESIGN.md` and its final84-test/540-segment verification.

Constraints: preserve1.20/0.97, geometry, native safety, existing settings/default-off behavior and below60mph commands. New preference is persistent/default0. Existing pinion, gain, persistent tracking and roll mapping are prerequisites. Keep standalone opendbc free of parent imports. Reuse clean paired checkout; no device access, firmware or push.

Review focus: source versus actual receipt time; conflated calibration/motion ordering; stale/invalid cache revocation; default-off/prerequisite matrix; real card path preserving native slew and final-release join.

- [x] Preserve exact baseline HEADs, selected source copies, protected-source SHA256 and settings snapshot.
- [x] Write factory/preference/motion-adapter tests red. Port controller to child `lateral_angle_high_speed.py` and portable84 regressions; preserve all controller-method ASTs. Add parent `motion_context.py`, receipt-aware SubMaster adapter, separate `FordPrefHighSpeedTracking` key and card wiring. Keep motion extras optional for old strategies/test doubles.
- [x] Verify focused tests, actual card/producer/local-IPC pipeline and invalid/stale/order/future cases. Review applied changes. Format/lint only scoped files and prove method equivalence against retained prototype.
- [x] Run full minimal/development SCons builds, project-scoped parent suite, complete child suite, local Panda firmware build. Run retained540-segment native replay through integrated factory/module and exact-recorded-timing check. Resolve failures and repeat affected checks.
- [x] Commit child, pin parent to it, commit parent with integration docs; verify exact paired HEADs and repeat commit-sensitive build checks. Update roadmap/inventory with concrete results and remaining physical validation limits.
