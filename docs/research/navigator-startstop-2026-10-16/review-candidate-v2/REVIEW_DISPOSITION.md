<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Review disposition

- Ordinary shutdown cancellation: implementation changed to mutex quiesce, sole-writer join, then300ms scheduling grace before NO_OUTPUT. Independent follow-up accepted ordering under nominal MCU scheduling assumptions. The full pandad/USB shutdown path has not been executed in a host integration test.
- Forwarded stock identity: firmware callback now checks actual output bus, with a native regression for stock bus0 packets forwarded to bus2.
- Ignition-off/offroad cancellation: explicitly retained as a safety shutdown boundary. DESIGN/README no longer claim arbitrary status changes cannot cancel cleanup. No ignition/offroad safety override was added.
- Hardware guarantees: deliberately unresolved by simulation. Queue failure, bus faults, reset/reconfiguration, CAN acknowledgment, genuine-publisher coexistence and PCM acceptance still need representative bench evidence. No enabled candidate is approved by this review.

Final native validation: standalone MCU transaction checks passed;130 MCU fault/tick-phase cases passed; owner activation/dwell/staleness/quiesce checks passed. Existing Ford regressions passed in both build variants:130 tests,79 skipped,12008 subtests each. These are native safety/helper tests, not full pandad/firmware builds.

All three durable patches passed git apply --check against their exact original source roots. Original parent, Panda and opendbc git status outputs were empty after validation. No source installation, device access or CAN transmission.
