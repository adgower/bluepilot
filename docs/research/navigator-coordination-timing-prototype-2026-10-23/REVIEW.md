<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

Read-only reviewer found a P1 in the initial prototype: an independent late subscriber can lag the main subscriber, rolling a healthy newer motion or calibration backward. Reproduction accepted990ms, main advanced1010ms, late cache980ms; old implementation published980ms and real Ford consumer faulted. Added failing regressions before repair (`ordering-red.log`).

Repair selects each topic by publication `logMonoTime` across main and late subscribers, then builds calibrated orientation/angular velocity/source timestamp/validity together. Source timestamp is deliberately not the ordering key: newly published reversed-source data must remain a fault, rather than be silently ignored. Primary invalidity and reference withdrawal stay authoritative. Unseen late cache falls back to seen primary; it is not a health revocation.

Reviewer independently reran37pose cases and reported no remaining implementation blockers. Combined focused suite44passed. No child/safety/steering changes. This review is local source/test evidence; no ARM scheduling, hardware or road proof.

Earlier test-first refinements also preserve known main invalidity (`known-invalid-red.log`) and withdrawn reference (`reference-red.log`). Partial broad runs were stopped and retained because production source changed. Only the final reviewed-source run can substantiate completion.
