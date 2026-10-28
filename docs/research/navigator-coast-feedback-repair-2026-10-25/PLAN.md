<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coast feedback repair — local only

Preserve the rejected experiment as evidence. Use the recorded 21.39 mph first divergence and chronological actual-controller replay, not a new PID gain. No device access, paired-tree edit, CAN transmission or deployment.

Ranked hypotheses: (1) latched model lock changes the baseline qualifier long after a trial; (2) coasting continues into positive planner demand and changes honest actuator-limited feedback/integral recovery; (3) the short forecast misses response lag. Test one logical policy change at a time. Forecasts remain scoring only; actual pressure clearance and timeout remain authoritative.

Regressions must fail on the rejected policy: retired trials preserve baseline qualifier semantics; recorded acceleration +0.733 m/s² with target −0.044 m/s² must not initiate coast. New trials require measured tracking within +0.05 m/s² of target, negative compensated intent and nonpositive planner target. Positive recovery may rearm only after 0.5 s of real fresh, clear, positive demand and measured tracking; waiting alone cannot rearm. Recovery eligibility must be separate from negative-demand coast eligibility. Preserve the measured-error budget and lock for new trials while falling back to the exact original qualifier.

Validate actual coupled replay including the first sample and entire subsequent integral trajectory, all five-mph bins, deceleration regressions, original faults and inactive behavior. Native acceptance is a separate check. Matching baseline means the introduced regression is removed; it does not mean original pulsing is fixed. No active Alpha 75–85 mph proof exists.

Final constraint: PID raw request must also be nonpositive; do not let model coast fight requested propulsion. A feedback-intent marker was probed, then removed after full replay showed identical wire output without it. Preserve the original PID/anti-windup/schema.
