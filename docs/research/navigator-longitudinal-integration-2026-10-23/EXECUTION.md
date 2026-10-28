<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Execution ledger

- Reused clean isolated paired codex/navigator-tracking-release worktrees. Recorded24e981d6d/01f32a6f and protected file hashes before changes.
- Added child in-tree helper tests and captured expected missing-module collection failure before integration.
- Applied reviewed export; normalized imports/locals and merged duplicate guards. Added controller/wire regressions and parent actual LongControl stopping→pid capped-demand test. No new protocol/planner/PID/safety changes.
-33focused tests/20subtests and changed-source Ruff checks pass.84protected child files retain exact hashes; all parent runtime files unchanged.1.20/0.97preserved.
- Frozen export vs integrated production:5,967updates,2,984ACC/3,889other messages byte-identical, matched stream hash0dc21b2be8ee9b62380673a0162a852c71bdce81499ef8f04533cea36f90620e. RX-driven integrated/frozen output exact-match; no added rejections, preserved driver-brake permission edge.
- Independent integration review found no actionable issues. Committed child0ac96189andparentffebc4349with matching gitlink; local only, clean. No push/device access.
- Configured incremental minimal/full Mac builds pass. First parent-suite attempt stopped at10sandbox temporary-directory PermissionErrors; preserved parent-suite-sandbox-first.log/initial-build-results.json. Ruling: use normal local test-directory/IPC permissions, not fixed shared LOG_ROOT or HOME override, to preserve OpenpilotPrefix isolation. Remaining parent/child suites and Panda build running under those permissions. No production source fix or test skip introduced for this host restriction.

Final normal-permission checks completed: parent1,022pass/87skip/1xfail/281subtests;child4,456pass/1,690skip/24,693subtests;Panda buildpass. Minimal/fullalready pass. Exact pair clean; no source changes after reviewed commits. Full local gatecomplete; no push/device action.
