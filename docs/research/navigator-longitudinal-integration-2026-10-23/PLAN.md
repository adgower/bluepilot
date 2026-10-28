<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired longitudinal integration plan

Authorized October23,2026: integrate reviewed brake/propulsion handoff and release fix into local paired branches, run full build checks. No push, Comma access, install, settings or firmware changes.

Reuse clean existing paired codex/navigator-tracking-release worktrees: parent24e981d6d/child01f32a6f. Apply only reviewed modules/controller block; normalize imports/names and remove duplicate pitch calculation without behavioral change. Add standalone child unit/controller tests and parent actual LongControl integration test. Capture test-first missing-module failure.

Verify production output equivalence to frozen reviewed export using original Alpha and actual RX chronology; retain cancellation edge. Check all protected files except explicitly changed controller, including1.20/0.97, all steering/safety/geometry.

Run focused checks/lint, minimal/full Mac, whole parent/child suites and Panda build with exact configured dependencies; native debug library freshly compiled without sanitizer. Independent fresh-context review; repair/recheck material findings. Commit child and matched parent gitlink/test change to paired branches only after checks. Retain exact candidate/source/verification receipts, update roadmap. No installation/road/OEM/fuel benefit claim.
