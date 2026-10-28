<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Installation guard review

Independent static review of `activate.py`, `prepare_install.py`, `accept_offroad.py`, `card-startup-check.py` and associated configuration identified and resolved:

1. Receipt I/O failure in the exception handler could bypass restoration. Error receipt writes are now best-effort before the recovery path.
2. Preservation checks could become stale between preflight and service shutdown. Both source trees, protected hashes, calibration hashes, selected preferences, unexpected parameter drift and exact paired heads are now rechecked after manager exit immediately before swap.
3. The recovery flag is set before attempting service stop, covering a partially successful stop that returns an error.

Follow-up review found no remaining blocker in this scoped static review. Neither review ran scripts or accessed the device. Both atomic-exchange and guarded-rename recovery paths were inspected. This is not proof of recovery from arbitrary hardware/power failure.

[Final helper hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md) were checked against the staged device copies. Full original installation and independent device/Mac backup remain the recovery basis.

Candidate preparation follow-up: preserve original upstream remotes and partial-clone/promisor metadata before Git connectivity checks. All 262 hydrated LFS files independently matched committed hashes; reindex only those verified paths and require an empty cached diff. Independent follow-up found no blocker. Removal of local alternates establishes independence from the previous directory; promised historical objects may still require their upstream remote.
