<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest master /AGNOS 20.1 merge — October 23,2026

Merged upstream `ff47f484e606ce5a2c3f8768ba5f5bf01b81e90e` into paired branch `codex/navigator-tracking-release` without conflict. Parent **`24e981d6dd44ef11325f08846fbbba2d3ee53842`**; child **`01f32a6f66743f63ac02f1357141e5f7359b2825`** unchanged. All 91 protected Ford/safety/Card/context files, owner 1.20/.97, highway observer correction, geometry and settings seams unchanged. Source checkouts clean and gitlink matched.

Four upstream commits cover AGNOS 20revert/reapplication as20.1, Panda debug-read correction and HITL robustness. Net11files change; runtime encoder subscription/debug reading changes included. Relative to installed20manifest, only system image changes, but the inactive19.9/B slot still needs boot plus system to become 20.1. New launch_env requires20.1; no bypass or activation on20.

Fresh configured incremental minimal/full Mac and Panda builds pass. Full parent:1021passed,87skipped,1expected failure,281subtests. Full child:4424passed,1690skipped,24673subtests. Skips are existing/upstream configuration; no local skips introduced. Independent merge review found no material findings. This is Mac/source proof, not20.1device proof.

Previous highway pair38172286f/01f32a6f was published and staged on20with verified private backup, but never activated. Its isolated native run is superseded for deployment. Live source remains26b3416/fe59e503 on 20/A. Activation is paused while20.1images, inactive Btargets and rollback/source staging are prepared. OS writes/reboot need explicit20.1authorization after preparation; previous20authorization is not reused for20.1.

Upstream primary sources: [AGNOS 20.1PR](https://github.com/commaai/openpilot/pull/39149), [pinned master](https://github.com/commaai/openpilot/commit/ff47f484e606ce5a2c3f8768ba5f5bf01b81e90e). [Build receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [review](REVIEW.md), [final verification](../../navigator-reference/PRIVATE_ARTIFACTS.md).
