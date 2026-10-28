<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibrated tracking and resolution-aware rearm integration plan

> Execute inline using the executing-plans skill; one fresh independent review at the end.

**Goal:** Integrate the accepted combined calibrated feedback,25–30mph bounded correction,60–70mph unwind and resolution-aware rearm without device changes.
**Architecture:** Add a child policy subclass retaining the installed policy as an independent reference. Select it through the existing parent prerequisite/default-off factory. No new parameter or producer.
**Tech stack:** Python, pytest, Ruff, SCons, native Panda safety hooks.
**Spec:** ../navigator-mid-rearm-controller-prototype-2026-10-20/REPORT.md and frozen prototype.py.

## Constraints and review focus

Preserve1.20/0.97, geometry, pinion/native limits, old policy modules and device settings. Check invalid/non-finite/duplicate evidence, no refill on reset/abort/turn, default-off parity, boundary/abort residuals and factory prerequisite selection. Carry the accepted766-segment replay only through exact code/actual-factory equivalence; distinguish that from a fresh integrated full corpus replay. No push or installation.

## Tasks

- [x] Preserve clean paired heads and protected hashes; retain existing integration checkout.
- [x] Add factory regression expecting CalibratedMidUnwind; observe expected failure against old factory.
- [x] Port frozen prototype into opendbc/car/ford/lateral_angle_calibrated_mid_unwind.py; export Candidate as CalibratedMidUnwind, rename private ratios helper and normalize formatting/zip only. Add accepted behavioral tests in child and portable saved-episode fixture.
- [x] Switch parent factory; verify class/helper AST and actual-factory returned-command equivalence against frozen prototype, including noisy rearm history.
- [x] Run focused tests, transition/abort screens, full parent/child suites, minimal/development/Panda incremental Mac builds, scoped Ruff and whitespace checks.
- [x] Independent review, fix material findings, locally commit child then pin/commit parent; verify clean paired heads and rerun incremental builds at committed revisions.
- [x] Passively acquire new rlogs, verify hashes and installed revisions/settings; analyze observational tracking/takeover windows using the installed-policy baseline. Keep raw identities private.
- [x] Update report, roadmap and feature inventory with results and remaining device/road gates.

Ruling: user explicitly authorized execution of the already-designed integration; proceed without another plan-approval pause. Reuse the clean established paired branches. Prior prototype tests already provide behavioral red/green; new factory regression covers integration red/green.

Completion: clean local paired commits and all configured build/test gates pass; no push/install. Full receipts inREPORT.md and final-verification.json.
