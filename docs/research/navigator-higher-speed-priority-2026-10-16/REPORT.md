<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Higher-speed investigation priority — October 16, 2026

Owner redirected the next investigation toward 30–85 mph. The unresolved below25mph issue remains open; the low-speed rearm prototype is not installed and did not correct the target episode. Existing settings, 1.20/0.97 and paired/device code remain unchanged.

The table uses only sessions advertising current revision9da98d0c9, from the existing normalized335+51segment corpus. Eligibility and meaningful-turn selection are unchanged. Ratios are contemporaneous descriptive medians, not steady-state gain estimates, independent trial counts or tuning recommendations. Revision labels do not prove recorded dirty-source identity.

| Band | Eligible exposure | Meaningful bends | Sessions with bends | Median body/request |
| --- | ---: | ---: | ---: | ---: |
| 30–35 mph | 244.40 s | 71.30 s | 3 | 99.7% |
| 35–40 mph | 31.20 s | 12.90 s | 4 | 110.6% |
| 40–45 mph | 117.75 s | 11.20 s | 3 | 118.3% |
| 45–50 mph | 59.30 s | 13.10 s | 3 | 118.2% |
| 50–55 mph | 139.35 s | 19.15 s | 3 | 109.5% |
| 55–60 mph | 338.45 s | 29.30 s | 3 | 116.4% |
| 60–65 mph | 1019.50 s | 111.65 s | 4 | 110.6% |
| 65–70 mph | 634.30 s | 14.40 s | 3 | 110.6% |
| 70–75 mph | 83.05 s | 8.35 s | 1 | 115.3% |
| 75–80 mph | 0.00 s | 0.00 s | 0 | — |
| 80–85 mph | 0.00 s | 0.00 s | 0 | — |

Sequence: **30–50 mph first**, explicitly including 40–45 and 45–50 mph; **50–70mph second** using existing highway logs; **70–85mph last**, subject to available ordinary legal driving data. The raw corpus peaks around74mph, and75–85mph performance remains unassessed. No dedicated85mph collection is required.

Use5mph bins to track evidence, with a smooth speed-dependent model only if route-held-out validation supports it. Separate rising, steady and declining demand; align signals, compare both turn directions, and trace requested curvature→transmitted path angle→wheel/body response. The owner clarified that good subjective feel around 45 mph is not verified requested-versus-applied performance. Audit that range equally and allow evidence-supported improvements; assess handling and stability for regressions rather than requiring its existing output to stay unchanged. Ratios above100% may reflect timing, unwind, bias or sparse turn selection; do not invert them directly into reduced gains.

30–35mph has the best initial mid-speed bend coverage and a median near100%, but is not certified perfect.35–50mph has only11–13seconds of meaningful turning per bin; this is a useful diagnostic gap, not evidence that a precise gain is identified.60–65mph has much better coverage.70–75mph meaningful bends come from one session;75–85mph has no current-corpus exposure.

Next action is the local phase/route-separated30–50mph audit, before selecting a code change or requesting further drive coverage. This priority update and coverage summary change documentation/analysis only.


## Clarified acceptance criteria for 45 mph

No range is presumed optimal from subjective feel. For40–45and45–50mph, establish a time-aligned request→transmitted-command→measured-wheel→body-response baseline, separating turn entry, sustained demand and exit in both directions. Evaluate absolute error, response delay, overshoot and repeated corrections on separate whole drives, alongside owner feedback. The descriptive medians near118% are a diagnostic prompt, not a calibrated gain estimate. Earlier≥45mph byte parity proves preservation only, not performance. Retain1.20/0.97 and all device settings during investigation; any proposed change remains subject to local validation and separate deployment authorization.
