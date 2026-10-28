<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local upstream merge

User authorizes latest master merge into existing paired branch locally and checks. No push, SSH, install, OS/firmware or settings changes. Preserve1.20/0.97, exact child8ccc6cf0 and custom Ford source/safety/geometry, all parent calibration/motion/selection interfaces and fork submodule URL. Adopt stock upstream Autospeed/ExperimentalMode removal; keep Alpha actuation opt-in. Existing installed pair stays unchanged.

1. Snapshot clean heads/submodule states/custom patch and protected child hashes. Create local backup ref.
2. Merge pinned fresh upstream without committing; resolve actual conflicts minimally; update only changed upstream dependency checkouts after verifying clean starting state.
3. Run configured minimal/full/Panda Mac builds, full parent/child suites and fork integration/factory pipeline tests. Reuse accepted unchanged-child full-corpus evidence by source identity; do not rerun the slow ARM matrix or connect to Comma. Runtime Ratekeeper change requires targeted stall/freshness scrutiny.
4. Fresh-context review of final merge diff and preservation, fix genuine blockers with regressions, record local merge commit and exact pin; verify committed pair and save report/roadmap.

Ruling: reuse existing clean feature checkouts as specifically requested. New upstream planner defaults intentionally replace ExperimentalMode behavior; preserving an obsolete parameter as a mode selector would defeat the requested upstream merge. No new feature design or unrelated tuning.
