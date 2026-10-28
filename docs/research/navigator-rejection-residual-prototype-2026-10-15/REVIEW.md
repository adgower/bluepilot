<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

Reviewed the report-local controller adapter, limiter, inherited ramp code and tests. Initial review found a P2: inherited eligibility resets cleared the episode budget, allowing an invalid model sample followed by same-sign steady demand to bypass the cap. Reproduction accumulated `.024693834 rad*s` after the intended `.001` budget.

Added failing `test_invalid_context_does_not_replenish_same_turn_budget`, then retained the latch/spent area across temporary resets. Reviewer confirmed the bypass is closed and found no additional concrete defect. Review of saved replay outputs does not replace the corrected-code replay rerun.

Remaining caveats: demand floor/sign reversal is assumed to identify a new episode; the cap is on the pre-limiter term, not physical response. Marker traffic changes require hardware timing validation. No device access or source edits by reviewer.
