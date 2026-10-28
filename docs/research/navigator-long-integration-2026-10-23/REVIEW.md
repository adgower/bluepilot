<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Fresh review and resolutions

A fresh reviewer examined both working trees, including untracked implementation and tests. Three Important findings were reproduced in the actual Ford controller, then fixed by the author with failing/passing regression tests:

1. Override erased pending brake-release history. The observer now retains the obligation across a pedal override, resets qualification and pauses the deadline; true owner disable remains the reset boundary. `review-override-red.log` and `review-override-green.log` preserve the first reproduction/repair.
2. Missing local history on moving entry/restart permitted propulsion without actuator clearance. Moving entry and return from stop/creep now require the same distinct fresh brake-clear observations. Missing/invalid feedback faults, high torque waits, elapsed time never grants permission. Stop/creep packets remain unchanged.
3. In-window reversed producer/pose timestamps remained accepted. The controller now retains producer order and GradeLease retains pose order; genuinely reversed context faults even when nominal age remains below100ms. Cached equal-time samples remain allowed within their freshness window. `review-entry-order-red.log` preserves both failing tests; final contracts cover the repairs.

Final: fixed all three Important findings through RED/GREEN contracts and broader replay/suite checks. No Critical findings, no deferred minor findings. The review was not rerun after repairs; the fresh review plus author-run regression tests is the verification boundary.

Author-found integration defect: optional CAN125 was initially read before the lazy parser registered it. Actual CarInterface tests exposed this. It is now explicitly preregistered only for the enabled trial, with cached timestamp/Unknown rejection and default-off RX-dependency tests. Initial failed suite logs remain preserved.

Ruling: require moving entry clearance in addition to post-brake clearance. Local brake history cannot survive process restart or a quick owner off/on; fresh qualification closes that gap. Cost: a bounded initial qualification delay, or a visible disengagement when required feedback is unavailable. Do not relax clearance to preserve the earlier replay's exact edge count.

Test isolation defect: the new live-mode pipeline test initially imported card/controlsd in the parent pytest process. Later process-replay tests fork and reuse module globals; card captures REPLAY at import. The full suite stalled in TestLeads.test_radar_fault, while the same test passed alone. The live pipeline now runs in its own subprocess, matching the existing high-speed pipeline convention. The corrected broad suite advances past that replay test. No production control logic was changed to accommodate this test.
