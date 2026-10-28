<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Original maneuver evidence inventory

Read-only first pass over all 42 routes / 737 compressed original segments from the existing frozen corpus manifest. No controller import, replay, generated-reference commands, or CAN transmission. CAN event frame-list lengths are counted without iterating individual frames. Only selected mode parameters are retained; no GNSS or private route identifiers are published.

Current paired source semantics: manager starts longitudinal maneuversd when started and LongitudinalManeuverMode is true, suppressing plannerd. Lateral daemon starts when started and LateralManeuverMode is true. Automatic lateral suite requires manual ACC speed selection and two seconds of readiness in code (README says one second). It emits lateralManeuverPlan at 20Hz, valid only during active action; alertDebug records setup, action, abort, completion. Longitudinal uses longitudinalPlan and alertDebug; engagement plus initial-speed readiness for three seconds begins actions, disengagement pauses/resets readiness.

Enablement snapshots, observed running process, active valid plan and completion alerts are separate evidence dimensions. Missing parameters are unknown. Explicit false parameter is a snapshot only; manager-not-running applies only observed publication coverage, with gaps/startup unknown. Historical source commits are inventoried separately: current definitions must not silently be attributed to all historical recordings. Contradictions remain visible.

Stage 1 metadata/event inventory is approved by parent and reviewer. Stage 2 per-address original command/response extraction requires review of Stage 1 candidates first. Missing exact marker semantics or historical source availability will be reported as limits rather than inferred experimental intent.
