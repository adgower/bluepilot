<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator steering speed screen — 2026-10-14

Owner reports understeer/wandering with steering engaged between 20–40 mph, near-ideal at 45 mph, and cannot identify a specific drive or curve. Latest saved drive was screened offline over SSH. No vehicle requests, tuning changes, or device modifications were made.

Filtered qlog carControl/carState pairs within 150 ms, lateral active, no steeringPressed, requested curvature magnitude >=0.00015 /m:

| Speed mph | Pairs | Gentle requests (<=0.0007 /m) | Potential software deviation clipping |
|---|---:|---:|---:|
| 20–30 | 783 | 36.9% | 12.8% |
| 30–40 | 197 | 49.2% | 0.0% |
| 40–50 | 199 | 54.8% | 0.0% |

Potential clipping reconstructs the installed +/-0.002 /m band around -yawRate/vEgoRaw when speed>9 m/s; it is not a measured count of actually clipped or rejected CAN commands. qlogs are sparse, asynchronous, and not controller-frame aligned. The sampled route may not contain the owner's exact symptom.

Measured/requested curvature ratios were inconsistent, with frequent sign disagreements. They are not reliable tracking metrics without time alignment, steady-curve selection, and verification of sign conventions through the full call path. Do not interpret them as understeer percentages.

This screening does not confirm a general clipping explanation for 30–40 mph: no potential clipping appeared there in these selected samples. Gentle-curve gain remains a source-derived candidate, not a demonstrated root cause. The preserved 1.20 factor affects the high-curvature arm only; installed low-curvature gain remains 1 below 13.5 m/s (about 30.2 mph), increasing toward 1.425 at 26.82 m/s (about 60 mph).

Next useful analysis: time-aligned rlog comparison of sustained curves at 20–40 and 40–50 mph, separating planner demand, limited demand, encoded path-angle commands, measured response, driver input, and path/lane tracking. Existing recordings allow this without asking for a deliberate test drive. No fix or road validation is claimed.
