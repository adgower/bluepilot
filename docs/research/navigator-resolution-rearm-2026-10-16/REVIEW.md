<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

The requesting-code-review workflow directed an independent read-only reviewer. It found no candidate dwell/refill bypass and confirmed the 0.1° resolution assumption against the DBC's StePinComp_An_Est signal.

Two material evidence/test gaps were raised and repaired:

1. Mutable baseline checkout provenance: `verify_environment.py` verifies exact expected clean parent9da98d0c9/child18175406 and hashes Ford modules, vehicle model, interfaces, tracking context, pose helpers, schemas and the safety library. Capture occurred during replay; it is rechecked at completion. Clean tracked state was also checked before replay start. This does not establish that no transient external edit happened between endpoint observations.
2. Missing reset/boundary cases: added disabled, missing context/feedback, stale/future/backward/duplicate timestamps, lane change, driver, nonfinite values and exact25mph cases. Added a whole-dwell range sequence whose individual steps pass and absolute magnitudes remain quiet.

Re-review: 29 direct rearm tests passed, no remaining material correctness finding. Inherited tests additionally cover inactive/human-turn dwell interruption; the combined suite passes87. The reviewer did not run the full native replay. One-quantum allowance admits some real adjacent motion as well as quantization jitter; unchanged total-range and quiet bounds constrain its accumulation.
