<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

Report-local prototype, baseline installed parent f750d756ca / child de70d4f945. Reviewer received explicit source paths and constraints without full conversation history. No source edits, vehicle access or heavy replay by reviewer.

Initial material finding: a canValid=False sample could remain in the credit history because the lower observer's basic_evidence does not include canValid. Inherited fraction rejects that sample, but subsequent valid frames could borrow it. A red recovery regression reproduced this. Candidate now clears credit history on invalid CAN; five fresh valid updates must rebuild credit. A second red regression caught a currently rising demand below the recent five-sample peak; current rising demand now receives no credit.

Second review reported no further material findings after inspecting stale/duplicate sources, generation changes, direction, driver/fault/release and speed boundaries. Reviewer independently ran the same60 focused cases successfully. Independent review and local tests do not establish hardware behavior or road improvement.

Reviewed corrected prototype SHA256: b8b1d434833331044e13f1a4eacfd7042663181a4cbe7acef892c6e42066f5f5.

Harness review found no material proof gaps: installed CalibratedMidUnwind baseline, four independent native copies, identical physical RX/original timers, no controls-permission override, expanded53/819 input SHA validation, source snapshots and final rejection/protected/default-off audits. Default-off proof uses recorded calibration; the separate causal fixture compares enabled reference/candidate. Full acceptance remains contingent on completed replay and final audit.
