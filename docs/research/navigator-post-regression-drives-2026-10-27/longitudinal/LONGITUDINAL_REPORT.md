<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Longitudinal saved-road review — 2026-10-27

This is a descriptive review of every newly acquired saved drive plus the immediately preceding 14-segment V1 baseline. Actual outgoing ACCDATA commands and received ECU brake/torque/RPM messages are decoded offline. See `metrics.json`, `cohort-summary.json`, `*-inputs.json`, and the qualified command/response CSV windows.

## Cohorts and coverage

| Acquisition | Drive | Recorded min | Recorded parent | Allocator versions in qualified samples | Qualified active min | Speed max mph |
|---|---|---:|---|---|---:|---:|
| baseline | latest-session-01 | 6.57 | df788e02719c | [1] | 4.75 | 29.20 |
| baseline | latest-session-02 | 6.43 | df788e02719c | [1] | 4.51 | 30.39 |
| new | post-regression-session-01 | 10.09 | df788e02719c | [1] | 6.22 | 71.02 |
| new | post-regression-session-02 | 8.94 | df788e02719c | [1] | 6.42 | 66.02 |
| new | post-regression-session-03 | 8.42 | df788e02719c | [1] | 3.43 | 27.67 |
| new | post-regression-session-04 | 3.44 | df788e02719c | [1] | 0.79 | 24.47 |
| new | post-regression-session-05 | 8.04 | df788e02719c | [1] | 5.76 | 27.79 |
| new | post-regression-session-06 | 5.74 | df788e02719c | [1] | 2.83 | 34.40 |
| new | post-regression-session-07 | 8.96 | e05e42f43d29 | [] | 0.00 | — |
| new | post-regression-session-08 | 20.30 | e05e42f43d29 | [3] | 16.24 | 69.22 |
| new | post-regression-session-09 | 0.29 | e05e42f43d29 | [] | 0.00 | — |

| Drive | Active, no override candidate s | Qualified s | Excluded candidate s | Candidate feedback fault s | Inactive/override s |
|---|---:|---:|---:|---:|---:|
| latest-session-01 | 285.228 | 285.090 | 0.137 | 0.000 | 99.662 |
| latest-session-02 | 270.611 | 270.517 | 0.095 | 0.014 | 105.939 |
| post-regression-session-01 | 373.160 | 373.132 | 0.028 | 0.000 | 223.367 |
| post-regression-session-02 | 385.509 | 385.492 | 0.018 | 0.000 | 141.852 |
| post-regression-session-03 | 205.608 | 205.580 | 0.028 | 0.000 | 290.232 |
| post-regression-session-04 | 47.171 | 47.171 | 0.000 | 0.000 | 150.400 |
| post-regression-session-05 | 345.801 | 345.783 | 0.018 | 0.000 | 127.391 |
| post-regression-session-06 | 169.657 | 169.609 | 0.048 | 0.000 | 165.724 |
| post-regression-session-07 | 0.000 | 0.000 | 0.000 | 0.000 | 520.182 |
| post-regression-session-08 | 975.092 | 974.621 | 0.471 | 0.000 | 233.778 |
| post-regression-session-09 | 0.000 | 0.000 | 0.000 | 0.000 | 8.432 |

Rates use qualified active exposure; inactive, faulted and driver-overridden periods are excluded and are not counted as pulse-free improvement. Candidate exposure already requires fresh matched control and state.

`installed_V3` requires every segment initData commit to equal `e05e42f43d2907a4f02915a924cfd95a46197e79` and every qualified feedback allocatorVersion to equal 3. A source-matched drive with no qualified samples has no observed active allocator version and contributes zero exposure. `prior_V1` requires `df788e02719c05595dab2f980e6fd9fb9e464006` and version 1. Other/mixed recordings remain separate. Every cohort also requires clean initData in every acquired segment. Device source receipt establishes the currently installed child; initData records the parent source for each historical drive.

## Speed-band command and physical exposure

Changes are both rising and falling edges, normalized by qualified active minutes, including stops. Combined means full-brake OR precharge; its exposure prevents treating a transfer from full brake to precharge as true coast. Tiny negative filtered standstill speed is clamped to 0 mph. A band with no qualified exposure cannot establish behavior.

| Cohort | mph | Active min | Full changes/min | Precharge changes/min | Combined changes/min | Full duty | Precharge duty | Combined duty | Actual torque >50Nm duty | Rapid full reversals |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| installed_V3 | 0–5 | 1.33 | 4.52 | 4.52 | 4.52 | 84.7% | 84.7% | 84.7% | 85.3% | 0 |
| installed_V3 | 5–10 | 0.14 | 0.00 | 0.00 | 0.00 | 44.7% | 44.7% | 44.7% | 44.7% | 0 |
| installed_V3 | 10–15 | 0.10 | 0.00 | 0.00 | 0.00 | 44.8% | 44.8% | 44.8% | 44.8% | 0 |
| installed_V3 | 15–20 | 0.11 | 0.00 | 0.00 | 0.00 | 41.9% | 41.9% | 41.9% | 43.1% | 0 |
| installed_V3 | 20–25 | 0.27 | 11.05 | 11.05 | 11.05 | 35.9% | 35.9% | 35.9% | 30.1% | 0 |
| installed_V3 | 25–30 | 0.34 | 5.86 | 5.86 | 5.86 | 63.2% | 63.2% | 63.2% | 60.7% | 0 |
| installed_V3 | 30–35 | 0.06 | 0.00 | 0.00 | 0.00 | 100.0% | 100.0% | 100.0% | 100.0% | 0 |
| installed_V3 | 35–40 | 0.15 | 13.21 | 13.21 | 13.21 | 63.3% | 63.3% | 63.3% | 65.2% | 0 |
| installed_V3 | 40–45 | 0.56 | 19.63 | 19.63 | 19.63 | 68.6% | 68.6% | 68.6% | 67.1% | 3 |
| installed_V3 | 45–50 | 0.87 | 13.80 | 13.80 | 13.80 | 45.6% | 45.6% | 45.6% | 44.3% | 4 |
| installed_V3 | 50–55 | 1.72 | 16.24 | 15.66 | 15.66 | 41.4% | 41.7% | 41.7% | 35.2% | 8 |
| installed_V3 | 55–60 | 4.50 | 15.76 | 15.98 | 15.98 | 28.2% | 29.0% | 29.0% | 24.3% | 22 |
| installed_V3 | 60–65 | 4.41 | 16.56 | 16.56 | 16.56 | 27.6% | 28.8% | 28.8% | 23.3% | 22 |
| installed_V3 | 65–70 | 1.68 | 16.65 | 16.65 | 16.65 | 16.3% | 18.0% | 18.0% | 12.4% | 8 |
| installed_V3 | 70–75 | 0.00 | — | — | — | — | — | — | — | 0 |
| installed_V3 | 75–80 | 0.00 | — | — | — | — | — | — | — | 0 |
| installed_V3 | 80–85 | 0.00 | — | — | — | — | — | — | — | 0 |
| installed_V3 | 85–90 | 0.00 | — | — | — | — | — | — | — | 0 |
| installed_V3 | 90+ | 0.00 | — | — | — | — | — | — | — | 0 |
| prior_V1 | 0–5 | 12.12 | 2.64 | 2.64 | 2.64 | 88.8% | 88.8% | 88.8% | 88.6% | 0 |
| prior_V1 | 5–10 | 1.92 | 2.08 | 2.08 | 2.08 | 60.5% | 60.5% | 60.5% | 60.4% | 0 |
| prior_V1 | 10–15 | 2.33 | 3.44 | 3.44 | 3.44 | 60.0% | 60.1% | 60.1% | 60.0% | 0 |
| prior_V1 | 15–20 | 3.52 | 5.11 | 5.11 | 5.11 | 59.2% | 59.6% | 59.6% | 58.0% | 2 |
| prior_V1 | 20–25 | 5.75 | 17.06 | 17.06 | 17.06 | 51.7% | 53.2% | 53.2% | 46.8% | 27 |
| prior_V1 | 25–30 | 2.84 | 17.95 | 17.95 | 17.95 | 45.8% | 47.0% | 47.0% | 40.2% | 14 |
| prior_V1 | 30–35 | 1.05 | 23.71 | 23.71 | 23.71 | 39.7% | 41.1% | 41.1% | 35.2% | 5 |
| prior_V1 | 35–40 | 0.39 | 18.01 | 18.01 | 18.01 | 29.3% | 30.1% | 30.1% | 23.4% | 2 |
| prior_V1 | 40–45 | 0.27 | 0.00 | 0.00 | 0.00 | 47.7% | 47.7% | 47.7% | 47.6% | 0 |
| prior_V1 | 45–50 | 0.57 | 12.24 | 12.24 | 12.24 | 17.1% | 17.2% | 17.2% | 16.2% | 1 |
| prior_V1 | 50–55 | 0.20 | 0.00 | 0.00 | 0.00 | 42.6% | 42.6% | 42.6% | 42.6% | 0 |
| prior_V1 | 55–60 | 1.03 | 8.71 | 6.77 | 6.77 | 22.3% | 22.8% | 22.8% | 21.1% | 0 |
| prior_V1 | 60–65 | 1.82 | 12.11 | 14.86 | 14.86 | 19.2% | 20.8% | 20.8% | 16.5% | 5 |
| prior_V1 | 65–70 | 0.89 | 14.69 | 18.08 | 18.08 | 46.9% | 48.9% | 48.9% | 40.5% | 3 |
| prior_V1 | 70–75 | 0.01 | 0.00 | 0.00 | 0.00 | 100.0% | 100.0% | 100.0% | 76.5% | 0 |
| prior_V1 | 75–80 | 0.00 | — | — | — | — | — | — | — | 0 |
| prior_V1 | 80–85 | 0.00 | — | — | — | — | — | — | — | 0 |
| prior_V1 | 85–90 | 0.00 | — | — | — | — | — | — | — | 0 |
| prior_V1 | 90+ | 0.00 | — | — | — | — | — | — | — | 0 |

## Overall and contextual splits

- **installed_V3:** 16.24 qualified active minutes; 236 full-brake changes (14.53/min), 236 precharge changes (14.53/min), 236 combined changes (14.53/min). Full/precharge/combined exposure 36.9%/37.7%/37.7%. Positive raw request >0.1 while full brake: 81.15s; abs(plan)<0.2 while full brake: 212.97s. Received ECU active brake 31.1%, ECU precharge 37.7%.
- **prior_V1:** 34.71 qualified active minutes; 294 full-brake changes (8.47/min), 300 precharge changes (8.64/min), 300 combined changes (8.64/min). Full/precharge/combined exposure 62.0%/62.6%/62.6%. Positive raw request >0.1 while full brake: 114.53s; abs(plan)<0.2 while full brake: 806.16s. Received ECU active brake 35.1%, ECU precharge 62.6%.

| Cohort | Context | Active min | Full changes/min | Combined duty |
|---|---|---:|---:|---:|
| installed_V3 | below40_lead | 2.09 | 5.74 | 77.6% |
| installed_V3 | below40_no_lead | 0.40 | 2.47 | 29.9% |
| installed_V3 | below40_deficit_gt2mph | 2.28 | 5.27 | 69.0% |
| installed_V3 | below40_deficit_lte2mph | 0.22 | 4.58 | 78.7% |
| installed_V3 | below40_neutral_request_plan | 0.25 | 15.88 | 57.9% |
| installed_V3 | 40to85_lead | 10.46 | 15.40 | 36.5% |
| installed_V3 | 40to85_no_lead | 3.29 | 18.82 | 17.0% |
| installed_V3 | 40to85_deficit_gt2mph | 13.66 | 16.33 | 31.4% |
| installed_V3 | 40to85_deficit_lte2mph | 0.09 | 0.00 | 100.0% |
| installed_V3 | 40to85_neutral_request_plan | 8.89 | 16.76 | 23.9% |
| installed_V3 | 85plus_lead | 0.00 | — | — |
| installed_V3 | 85plus_no_lead | 0.00 | — | — |
| installed_V3 | 85plus_deficit_gt2mph | 0.00 | — | — |
| installed_V3 | 85plus_deficit_lte2mph | 0.00 | — | — |
| installed_V3 | 85plus_neutral_request_plan | 0.00 | — | — |
| prior_V1 | below40_lead | 18.20 | 6.87 | 71.1% |
| prior_V1 | below40_no_lead | 11.72 | 10.07 | 63.3% |
| prior_V1 | below40_deficit_gt2mph | 29.34 | 8.01 | 68.1% |
| prior_V1 | below40_deficit_lte2mph | 0.58 | 13.69 | 67.6% |
| prior_V1 | below40_neutral_request_plan | 6.30 | 24.15 | 48.7% |
| prior_V1 | 40to85_lead | 3.64 | 11.26 | 33.7% |
| prior_V1 | 40to85_no_lead | 1.14 | 8.76 | 12.5% |
| prior_V1 | 40to85_deficit_gt2mph | 4.61 | 10.42 | 28.5% |
| prior_V1 | 40to85_deficit_lte2mph | 0.18 | 16.80 | 30.3% |
| prior_V1 | 40to85_neutral_request_plan | 2.85 | 12.63 | 17.5% |
| prior_V1 | 85plus_lead | 0.00 | — | — |
| prior_V1 | 85plus_no_lead | 0.00 | — | — |
| prior_V1 | 85plus_deficit_gt2mph | 0.00 | — | — |
| prior_V1 | 85plus_deficit_lte2mph | 0.00 | — | — |
| prior_V1 | 85plus_neutral_request_plan | 0.00 | — | — |

## Qualified dense 15-second windows

Relative times begin at the first acquired event for that pseudonymous drive, and are not wall-clock chronology. Every exported window has at least 95% qualified samples and continuous active ownership/no pedal or steering override/no allocator fault throughout. Missing/failing samples are excluded from counts and exposure. CSVs retain backward join ages and actual requests/response. Window rankings use full-brake plus precharge edge counts, not a comfort score.

| Cohort | Drive | Relative seconds | mph | Qualified | Full/pre/combined changes | Combined s | Actual accel range m/s² | abs jerk p95 m/s³ | Actual torque range Nm | Integral range | Pitch range ° | Raw/plan zero crossings | CSV |
|---|---|---|---:|---:|---|---:|---|---:|---|---|---|---|---|
| prior_V1 | latest-session-01 | 227.889–242.868 | 24.162..26.870 | 100.0% | 4/4/4 | 2.47 | -0.454..0.601 | 1.493 | 0.000..64.000 | -0.067..0.147 | -1.467..0.206 | 4/0 | [baseline-latest-session-01-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | latest-session-01 | 43.515–58.492 | 2.260..19.313 | 100.0% | 2/2/2 | 7.90 | -1.489..2.166 | 2.202 | 0.000..940.000 | -0.009..0.766 | -4.684..-2.017 | 7/7 | [baseline-latest-session-01-below40-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | latest-session-01 | 179.716–194.688 | 0.414..24.840 | 100.0% | 2/2/2 | 13.32 | -2.206..1.273 | 2.035 | 0.000..1784.000 | -0.049..0.236 | -1.736..0.256 | 2/4 | [baseline-latest-session-01-below40-3.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | latest-session-02 | 158.405–173.386 | 21.160..24.588 | 100.0% | 15/15/15 | 9.23 | -1.129..0.834 | 2.081 | 0.000..148.000 | 0.068..0.378 | -2.496..-0.953 | 0/6 | [baseline-latest-session-02-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | latest-session-02 | 111.083–126.043 | 27.390..30.388 | 100.0% | 10/10/10 | 5.81 | -1.523..1.022 | 2.052 | 0.000..176.000 | -0.145..0.330 | -3.620..0.002 | 7/5 | [baseline-latest-session-02-below40-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | latest-session-02 | 132.529–147.529 | 25.570..28.191 | 100.0% | 7/7/7 | 7.09 | -1.573..1.875 | 2.715 | 0.000..120.000 | 0.003..0.468 | -3.031..-0.441 | 2/10 | [baseline-latest-session-02-below40-3.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-01 | 499.146–514.132 | 21.437..24.213 | 100.0% | 10/10/10 | 9.76 | -1.084..0.969 | 1.986 | 0.000..264.000 | -0.071..0.294 | -2.840..-0.919 | 10/7 | [new-post-regression-session-01-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-01 | 402.507–417.502 | 22.765..30.992 | 99.9% | 3/3/3 | 6.66 | -1.248..1.607 | 2.456 | 0.000..720.000 | -0.391..0.186 | -4.935..-0.303 | 5/3 | [new-post-regression-session-01-below40-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-01 | 83.463–98.442 | 0.000..19.457 | 100.0% | 2/2/2 | 6.75 | -1.794..2.018 | 2.228 | 0.000..1540.000 | -0.174..0.316 | -1.967..0.255 | 2/2 | [new-post-regression-session-01-below40-3.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-01 | 251.703–266.663 | 64.535..66.291 | 100.0% | 11/13/13 | 9.50 | -1.687..1.375 | 4.045 | 0.000..88.000 | -0.077..0.393 | -3.812..-0.056 | 6/4 | [new-post-regression-session-01-highway-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-01 | 193.120–208.092 | 52.617..66.547 | 100.0% | 1/1/1 | 12.00 | -0.884..0.738 | 1.224 | 0.000..680.000 | -0.010..0.136 | -1.918..-0.169 | 1/1 | [new-post-regression-session-01-highway-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-02 | 93.516–108.500 | 31.006..34.936 | 100.0% | 11/11/11 | 4.74 | -1.123..1.149 | 2.099 | 0.000..456.000 | -0.074..0.259 | -3.066..-0.346 | 0/4 | [new-post-regression-session-02-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-02 | 395.677–410.671 | 0.000..20.445 | 100.0% | 2/2/2 | 6.01 | -1.750..2.133 | 3.296 | 0.000..868.000 | -0.183..0.492 | -1.033..2.829 | 2/2 | [new-post-regression-session-02-below40-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-02 | 298.678–313.660 | 12.662..35.639 | 100.0% | 1/1/1 | 2.98 | -0.727..1.520 | 1.412 | 0.000..460.000 | -0.101..0.211 | -3.163..-2.143 | 1/1 | [new-post-regression-session-02-below40-3.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-02 | 189.643–204.642 | 57.594..61.128 | 100.0% | 6/6/6 | 4.82 | -0.880..0.897 | 1.668 | 0.000..92.000 | -0.111..0.271 | -1.166..0.267 | 5/3 | [new-post-regression-session-02-highway-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-02 | 250.545–265.519 | 58.254..62.236 | 100.0% | 6/6/6 | 6.35 | -1.338..1.475 | 3.786 | 0.000..148.000 | -0.092..0.273 | -1.603..0.882 | 13/12 | [new-post-regression-session-02-highway-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-02 | 335.017–350.016 | 47.610..49.149 | 100.0% | 6/6/6 | 2.86 | -0.367..0.522 | 1.024 | 0.000..180.000 | -0.103..0.155 | -1.543..0.165 | 2/7 | [new-post-regression-session-02-highway-3.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-03 | 194.147–209.146 | 6.729..23.080 | 100.0% | 3/3/3 | 12.24 | -1.529..0.728 | 1.677 | 0.000..1760.000 | -0.063..0.285 | -5.599..0.611 | 8/0 | [new-post-regression-session-03-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-03 | 304.525–319.522 | 0.000..23.028 | 100.0% | 2/2/2 | 4.83 | -1.556..2.125 | 2.346 | 0.000..1688.000 | -0.148..0.648 | -2.491..0.476 | 2/2 | [new-post-regression-session-03-below40-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-04 | 90.750–105.731 | 4.020..22.354 | 100.0% | 2/2/2 | 11.54 | -1.621..0.638 | 1.573 | 0.000..792.000 | -0.011..0.515 | -0.271..1.234 | 7/0 | [new-post-regression-session-04-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-05 | 260.906–275.876 | 15.658..21.637 | 100.0% | 5/5/5 | 8.56 | -1.304..1.327 | 2.142 | 0.000..972.000 | -0.183..0.181 | -1.880..-0.292 | 5/3 | [new-post-regression-session-05-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-05 | 203.605–218.576 | 15.275..23.063 | 100.0% | 3/3/3 | 10.68 | -0.669..1.510 | 1.576 | 0.000..264.000 | -0.154..0.354 | -2.085..-0.077 | 5/1 | [new-post-regression-session-05-below40-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-05 | 137.876–152.834 | 0.000..11.274 | 100.0% | 2/2/2 | 10.77 | -1.285..1.572 | 2.505 | 0.000..1564.000 | -0.096..0.452 | -4.275..-1.518 | 2/2 | [new-post-regression-session-05-below40-3.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-06 | 90.785–105.748 | 22.812..25.989 | 100.0% | 5/5/5 | 5.13 | -1.049..1.631 | 2.041 | 0.000..60.000 | -0.098..0.172 | -1.805..0.400 | 2/1 | [new-post-regression-session-06-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-06 | 204.305–219.304 | 10.168..24.794 | 100.0% | 4/4/4 | 12.48 | -1.438..0.929 | 1.776 | 0.000..708.000 | -0.247..0.101 | -1.704..-0.081 | 4/6 | [new-post-regression-session-06-below40-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| prior_V1 | post-regression-session-06 | 132.605–147.583 | 6.215..24.798 | 100.0% | 1/1/1 | 12.02 | -1.326..2.453 | 1.622 | 0.000..1248.000 | -0.173..0.099 | -1.766..-0.345 | 1/3 | [new-post-regression-session-06-below40-3.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| installed_V3 | post-regression-session-08 | 634.985–649.973 | 0.000..7.605 | 100.0% | 3/3/3 | 7.67 | -0.620..1.376 | 1.321 | 0.000..900.000 | -0.069..0.183 | 0.410..0.852 | 3/4 | [new-post-regression-session-08-below40-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| installed_V3 | post-regression-session-08 | 1131.235–1146.198 | 0.000..7.501 | 100.0% | 3/3/3 | 7.84 | -0.826..1.043 | 1.379 | 0.000..1004.000 | -0.162..0.252 | -1.216..-0.843 | 3/7 | [new-post-regression-session-08-below40-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| installed_V3 | post-regression-session-08 | 180.068–195.057 | 52.237..53.813 | 99.7% | 14/14/14 | 7.13 | -0.950..0.930 | 2.731 | 0.000..56.000 | -0.091..0.268 | -2.721..-0.074 | 8/14 | [new-post-regression-session-08-highway-1.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| installed_V3 | post-regression-session-08 | 383.137–398.118 | 40.635..49.804 | 99.3% | 14/14/14 | 7.17 | -0.632..1.350 | 2.364 | 0.000..332.000 | -0.103..0.170 | -3.670..-2.088 | 0/0 | [new-post-regression-session-08-highway-2.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |
| installed_V3 | post-regression-session-08 | 316.067–331.047 | 56.992..58.789 | 100.0% | 12/12/12 | 4.66 | -0.865..0.977 | 1.752 | 0.000..160.000 | -0.012..0.205 | -2.210..-1.126 | 0/9 | [new-post-regression-session-08-highway-3.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |

## V3 bounded true-coast activation

The exact marker requires reason `bounded_coast_pending`, feedback release phase, referenceBrake=true, brake=false, precharge=false, gas=-5, limited=true, version=3, valid/nonfaulted feedback, finite prechargeAge in [0,0.300000001), and budgetRemaining in (0,0.01]. This follows the installed allocator deadline=0.3s and observer lease guard. Ordinary release clearance is excluded.

| Drive | Raw marker rows | Unique consumed epoch/sequence | Marker runs | Feedback interval integration s | Strict backward-anchor exposure s | prechargeAge min/max s | Budget min/max | Actual request bits at past-marker anchors |
|---|---:|---:|---:|---:|---:|---|---|---|
| post-regression-session-08 | 166 | 83 | 18 | 1.703757 | 1.340413 | 0.057..0.299 | 0.00006657..0.00853848 | full=0.273645s, pre=0.292471s, both clear=1.047942s; [new-post-regression-session-08-bounded-coast.csv](../../../navigator-reference/PRIVATE_ARTIFACTS.md) |

The marker proves the bounded true-coast path activated: all matching feedback rows requested both flags clear. The feedback-interval integration and past-only CAN-anchor exposure use different clocks/publication phases and are not interchangeable. Current outgoing bits can differ from the preceding feedback cycle; the CSV shows those differences. The both-clear overlap is a descriptive request-bit observation, not an exact corresponding-packet receipt or measured physical-coast duration. Full/precharge edges can remain equal when the new path clears weak precharge intervals without eliminating separate full-brake transitions.

## Observed moving true-coast runs

These are runs of outgoing full brake=0 AND precharge=0 at >=5mph, with continuous qualified samples. They include normal propulsion as well as neutral coast; short duration alone does not identify the V3 bounded-coast mechanism.

| Drive | Runs | Duration median/p95/max s | Runs <=0.3s | Runs <1s |
|---|---:|---|---:|---:|
| latest-session-01 | 17 | 2.76/9.74/11.50 | 3 | 5 |
| latest-session-02 | 35 | 1.23/6.37/10.32 | 6 | 16 |
| post-regression-session-01 | 34 | 2.95/14.96/24.38 | 4 | 10 |
| post-regression-session-02 | 40 | 1.93/16.10/39.34 | 7 | 17 |
| post-regression-session-03 | 20 | 0.80/10.90/17.38 | 10 | 10 |
| post-regression-session-04 | 8 | 0.16/5.81/7.07 | 5 | 5 |
| post-regression-session-05 | 23 | 1.28/8.34/8.88 | 9 | 11 |
| post-regression-session-06 | 15 | 3.67/7.75/8.24 | 1 | 3 |
| post-regression-session-07 | 0 | —/—/— | 0 | 0 |
| post-regression-session-08 | 170 | 1.18/14.64/26.48 | 46 | 77 |
| post-regression-session-09 | 0 | —/—/— | 0 | 0 |

## RPM/restart observations

A restart observation is received RPM below 100 then above 400 within 10 seconds, with the running-threshold sample qualified. It is an observed engine-speed transition, not proof of why the engine restarted. The ±2/+3 second context is filtered to qualified samples; no sensor-causal or fuel claim is made.

- latest-session-01: 0 qualified restart observations.
- latest-session-02: 0 qualified restart observations.
- post-regression-session-01: 0 qualified restart observations.
- post-regression-session-02: 0 qualified restart observations.
- post-regression-session-03: 0 qualified restart observations.
- post-regression-session-04: 0 qualified restart observations.
- post-regression-session-05: 0 qualified restart observations.
- post-regression-session-06: 0 qualified restart observations.
- post-regression-session-07: 0 qualified restart observations.
- post-regression-session-08: 0 qualified restart observations.
- post-regression-session-09: 0 qualified restart observations.

## Method and limits

- Each compressed raw segment SHA-256 is checked against its acquisition manifest before decoding. One drive is streamed into numerical arrays; no GNSS, VIN, full-message pickle, raw log copies, or route identities are published. Numeric array SHA-256 and field layouts are in `*-inputs.json`.
- Anchor: actual bus-0 outgoing `sendcan` ACCDATA (390). Brake/precharge bits are `AccBrkDecel_B_Rq`/`AccBrkPrchg_B_Rq`. Received bus-0 DesiredTorqBrk (531), BrakeSnData_4 (125), RPM (516), and engine status (357) are separate physical observations. Sent commands are intent; received ECU states/torque are response, not direct hydraulic pressure.
- Every core join is backward-only and at most 100ms old: carState, carOutput, exact consumed output epoch/sequence -> carControl, preceding controlsState, and the exact planner timestamp named by that controlsState. Future rows are rejected. CarState must be valid/CAN-valid; control enabled and longitudinal active; feedback valid and nonfaulted; no brake/gas/steering override. Maneuver recordings are excluded. Radar/ECU/torque/RPM context has its own past-only <=100ms validity mask and is not imputed.
- An edge counts only when adjacent samples both qualify and their positive time gap is <=100ms. Exposure is the next outgoing-CAN interval capped by that same gap criterion. Rapid reversal means consecutive qualified full-brake edges less than 0.6s apart with uninterrupted qualification. Edges across gaps are omitted.
- Measured aEgo jerk is the derivative across 200ms of a causal trailing-200ms mean, avoiding differentiation of duplicated CAN-anchor state samples. It remains filtered sensor response with road/grade/driveline effects. It is not a cabin-comfort or physical jerk validation.
- Set-speed deficit uses recorded carState vCruise (kph), converted to mph; unset/sentinel >=250kph and nonpositive values are excluded from deficit splits. Lead-present/no-lead splits require fresh radar; neutral_request_plan additionally requires speed>=5mph, raw request -0.1..+0.3m/s², and abs(plan)<=0.2m/s². Split differences are descriptive and confounded by traffic and route. Source and controller changes, different route/grade, set speed, traffic, driver overrides, stops, and missing speed-band exposure prevent causal improvement, comfort, or fuel conclusions.
- The older `navigator-coordinated-coast-road-review-2026-10-27` road table is background: its 1044.54 healthy active seconds and 69.37mph maximum used producer/consumer telemetry and brake *onsets*. Those onsets are not mixed into this actual-CAN two-edge rate comparison; its other historical sources are not silently relabeled as installed V3.

## Conclusion and remaining issues

**The brief true-coast fix activated, but full-brake cycling persists in the installed road recording.** Clean V3 session08 supplies 974.621 qualified active seconds (16.24 minutes), reaching 69.22mph; sessions07/09 have zero active exposure. The exact bounded marker appears in 166 raw feedback rows, 83 distinct consumed requests, 18 runs, with 1.704s feedback-interval integration and 1.340s strict backward-anchor overlap. This verifies activation, not a general road cure.

- **Remaining repeatable activity is strongest at 40–70mph.** Across the installed recording there are 236 full-brake changes (14.53/min), 236 precharge/combined changes, 67 rapid full-brake reversals, and 367.095s combined requested exposure (37.67%). At +180.068–195.057s, 52.24–53.81mph, there are 14 full-brake changes, actual aEgo -0.950..+0.930m/s², and 200ms-filtered abs jerk p95 2.731m/s³. At +383.137–398.118s, 40.64–49.80mph, another 14 full-brake changes occur while raw and plan acceleration both remain positive; actual brake torque spans 0..332Nm. At +316.067–331.047s, 56.99–58.79mph with no fresh lead, there are 12 changes despite entirely positive raw request, so a lead is not required for every observed cycle. These are concurrent road observations; they do not isolate the physical cause of acceleration variation.
- **Below-40 cure is unproven.** V3 below40 has only149.640 qualified seconds, including79.699s at0–5mph. Moving5–40 exposure is69.942s with7 full-brake changes and no observed <0.6s reversal, compared with1068.143s moving5–40 in the V1 comparison cohort. V3 has only36.789s in20–30mph and15.117s of below40 moving neutral-request/plan context. The prior dense21–25mph event is not comparably reproduced; fewer unmatched pulses cannot establish a cure. Combined requested exposure moving5–40 is52.96% V3 versus53.96% V1, also not a causal improvement measure.
- **Do not infer improvement from mixed-route totals.** V3 overall14.53 full-brake changes/min versus prior V1 8.47/min comes from very different speed/traffic distributions: V1 has29.92 active minutes below40, V3 only2.49. Even neutral-request/plan highway context has different exposure (533.37s V3 versus171.00s V1). The speed table and fresh-lead splits show the actual denominators. Source labels alone do not control grade, traffic, set speed or route.
- **Coverage stops below70mph for V3.** There is no qualified installed-source70–85mph or85+ exposure; V1 reaches71.02mph only. Five-mph rows through85 and beyond remain explicitly empty where not recorded. The installed candidate retains974.621/975.092s of fresh matched active/no-override candidate exposure;233.778s of inactive/override exposure is excluded.
- **Restart/fuel conclusion remains open.** No qualified received-RPM <100 to >400 within10s restart is observed. This cannot prove restart behavior fixed, and neither command/coast counts nor filtered aEgo prove fuel economy or cabin comfort. Source and measured-response questions remain separate from the main controlsMismatch/fault audit.
