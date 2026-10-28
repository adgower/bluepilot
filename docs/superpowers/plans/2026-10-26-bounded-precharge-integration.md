<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Bounded precharge paired integration plan

**Goal:** Port the validated bounded-precharge allocator into the existing Navigator parent/child pair, with real versioned IPC and full local build/replay checks.
**Architecture:** Child owns allocator, split request encoding and signed-precharge feedback interpretation. Parent stamps the consumed plan target and source time into the existing CarControl request and uses returned typed feedback. Existing epoch/freshness/torque guards and all steering behavior remain unchanged.
**Spec:** docs/research/navigator-allocator-contract-resolution-2026-10-25/DESIGN.md

## Constraints and execution ledger

- Use the existing clean dedicated `.navigator-master-integration-20261014` feature checkout and paired child, on `codex/navigator-tracking-release`; user explicitly requested those branches. No new checkout or dependency reinstall.
- Keep early coasting, downhill toggle and BP follow overrides disabled. No device access, publishing, reboot, OS/firmware updates or CAN transmission.
- Keep exact 1.20/0.97, lateral files, vehicle geometry, calibration and safety limits unchanged. Local child/parent commits and exact gitlink update follow passing checks.
- Execute inline; final fresh-context review per executing-plans workflow.

## Tasks

- [ ] 1. Add RED real-wire request/feedback/version tests, then append schema fields and versioned target/context helpers; old/malformed context must fall back to nominal.
- [ ] 2. Port allocator and integral phase handling, integrate controller/split precharge encoding, preserve reference history and measured release rules; run focused/retained child contracts.
- [ ] 3. Wire parent actual consumed plan target and feedback transport; run parent producer/consumer/version/freshness tests and minimal schema build.
- [ ] 4. Replay all 137 cached longitudinal segments through integrated source with real encoded fields, not prototype metadata, and prove expected actuator/I/wire equivalence and nominal fallback.
- [ ] 5. Run full Mac builds, parent/child suites, Panda build, lint and source preservation checks; address actual blockers. Review complete pair.
- [ ] 6. Commit paired child and exact parent pin locally, update integration docs/roadmap and report checks/limits. No publication or device change.

Completion: all six integration/validation/commit steps complete. See research integration REPORT.md and LEDGER.md for exact pair, test counts, native results and retained failed-attempt history. No publication/device work.
