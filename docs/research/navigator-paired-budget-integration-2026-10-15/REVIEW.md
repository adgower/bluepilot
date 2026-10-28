<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

Read-only reviewer confirmed the single-sample floor/reversal budget reset was unsafe for the intended episode model. Revised quiet dwell retains spend across interruptions and reversal; reviewer found no additional concrete source defect in the budget, selector or context seam.

Reviewer found two reporting issues, both corrected: the aggregate originally excluded forced/saturation cases, and aborts keyed to a count of nonzero corrections could become unreachable after lowering the budget. Aggregates now cover all312 cases; abort timing uses elapsed frames since first correction, each case asserts and records abort_triggered, and records whether the event occurs during an active pulse. Both turn signs are included in the old/new-budget comparison.

Review does not establish hardware timing or physical safety. The prelimit budget is explicitly distinct from the larger measured final-command tail. Portable regression tests were added; final test/replay runs were performed by the primary agent.
