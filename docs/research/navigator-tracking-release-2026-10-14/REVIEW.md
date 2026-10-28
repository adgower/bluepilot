<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review

Initial review found two issues: replay bypassed control-message validity in the bridge, and accepted sample cadence was broader than the response-slope timing assumption. Added invalid-control and fast-cadence regression coverage; observed the latter fail against the earlier candidate. Replay now uses the bridge with recorded control validity. Cadence is constrained to40–60ms and slope uses actual timestamps.

Reviewer rechecked paired staging, defaultOFF parameter, startup selection, CAN timestamp capture and delivery before apply; independently ran23 staged tests successfully at that review point. No additional concrete blocker to local candidate testing was found. Final tests subsequently added a delayed-plant regression and the hold decision retained the prior six-observation admission with new onset/projection guards; final results are in the adjacent logs.

Limits explicitly retained: init/state_update source reviewed; exact controls_update executed with mocked IPC/apply, not a whole live stack. Final full native replay and source/dependency provenance verified separately. No road or device validation performed.
