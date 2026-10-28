<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Timing and mode selection research

Local overlays only; paired source and device remain untouched, including 1.20/0.97.

Hypothesis: requiring zero reported brake torque before requesting weak-brake release prevents a coast transition from initiating. A release/coast/drive selector should withdraw only weak requests within a measured speed-error budget. Original physical clearance and timeouts retain exclusive authority over propulsion.

Use a continuous planner-integrated speed reference, a causal acceleration filter and bounded response horizon. Retained pressure may initiate RELEASE; it never authorizes drive. Strong deceleration, lead/FCW/stopping, invalid independent radar/torque and lateral activity fall back immediately. Trial numerical limits are hypotheses, not vehicle calibration.

Compare mode-only and combined positive-integral recovery hold against actual causal baseline over all 137 cached segments. Recovery hold must expire once per transition; negative error remains unblocked. Inspect wire behavior, added faults, strong deceleration and five-mph bands. Frozen recorded vehicle response cannot demonstrate improved ride comfort.
