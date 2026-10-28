<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Model/grade comfort diagnostic prototype

User-authorized local spike, October 24, 2026. No device access, source integration or steering changes.

Use exact-current actual-controller fixture/reconstruction as the baseline. Test separately: (1) grade-decision chatter; (2) model-target variability; (3) measured release interruptions. Do not remove model/radar/stop constraints, enlarge brake-clearance thresholds, lengthen release fault deadlines, or infer vehicle comfort from frozen-input command replay.

1. Reproduce current rapid reversals with the existing fast actual-controller fixture (already red: 15 edges/7 rapid in 20s).
2. Select additional reproducible episodes in every populated range, especially 50–60mph; preserve baseline snapshots and command bytes.
3. Attribute baseline brake admission bypasses and measured tracking errors; test a bounded measured-tracking coast decision only where weak predicted braking conflicts with acceleration feedback. This is a hypothesis, not an established remedy.
4. Analyze model/planner acceleration fluctuations, selected source and lead/stop context per five-mph reporting bin. Keep command/planner/physical layers separate. Do not force cruise past model slowing to meet a setpoint.
5. Run candidate versus baseline over all available Alpha replay sessions; compare every bin, stops, strong braking, clearance/faults and speed transitions. Reject localized improvement with broader regression. Native safety replay where raw CAN coverage permits.
6. Save provenance, result and roadmap gates. Preserve paired branches and owner1.20/0.97. Explicitly report missing75–85mph Alpha evidence.
