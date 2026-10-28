<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Post-regression lateral road review

Local saved-log observations only. Recorded `initData.gitCommit` defines cohorts; the installed-pair receipt establishes current installation separately. No recorded dependency commit is inferred from the parent hash. No changed-road comparison establishes causal improvement, physical comfort, or closed-loop simulation.

Driver-confirmed lane repositioning explains the highlighted811.95s pressure event; it is not corrective-takeover evidence. Separate numerical40–50mph tracking mismatch remains outside that maneuver, with no demonstrated unexpected driver event. The following initial full-route metrics include that maneuver; independent exclusion results appear below.40–45mph has30.75s meaningful exposure (25.25s steady); steady body/request median1.147 and wheel/request1.153, with+.212m/s² median signed body excess.45–50mph has21.65s meaningful exposure (6.45s steady), median body/request1.130. These ratios describe measured-versus-requested tracking; they do not establish unsafe oversteer or driver dissatisfaction.

At19:04:47.54CDT (session08,811.95s,49.50mph), the driver confirms a planned lane-position change: the road widened from2 to3 lanes and they moved to the furthest-right lane for the next exit. This is excluded from problem-takeover conclusions; nearby pressure/response is not corrective-takeover evidence. Raw event counts remain unchanged. Other393.15–394.40s excess windows are entirely request unwind. The numerical tracking mismatch elsewhere is not by itself proof of unexpected or unsafe behavior.

Only candidate session08 provides driving exposure;07 is stationary and09 peaks0.55mph with no motion/parameters/model-context streams. Candidate maximum69.89mph leaves70–85mph untested by this new source. Sessions01–06 are newly downloaded pre-update recordings and must not be used as candidate-source proof.

## Cohorts and exposure

|Drive|Cohort|Recorded parent|Segments|Max mph|Active s|Qualified s|
|---|---|---|---:|---:|---:|---:|
|post-regression-session-01|pre-update|df788e02719c05595dab2f980e6fd9fb9e464006|11|71.52|459.1|267.9|
|post-regression-session-02|pre-update|df788e02719c05595dab2f980e6fd9fb9e464006|9|66.14|429.1|315.7|
|post-regression-session-03|pre-update|df788e02719c05595dab2f980e6fd9fb9e464006|9|27.73|245.0|101.6|
|post-regression-session-04|pre-update|df788e02719c05595dab2f980e6fd9fb9e464006|4|26.41|91.3|34.9|
|post-regression-session-05|pre-update|df788e02719c05595dab2f980e6fd9fb9e464006|9|28.10|357.3|144.1|
|post-regression-session-06|pre-update|df788e02719c05595dab2f980e6fd9fb9e464006|6|34.50|215.2|121.9|
|post-regression-session-07|candidate|e05e42f43d2907a4f02915a924cfd95a46197e79|9|0.00|0.0|0.0|
|post-regression-session-08|candidate|e05e42f43d2907a4f02915a924cfd95a46197e79|21|69.89|1097.7|844.6|
|post-regression-session-09|candidate|e05e42f43d2907a4f02915a924cfd95a46197e79|1|0.55|0.0|0.0|

Qualified samples require past-only fresh state/control/wire/body/parameters/model/panda, valid calibrated motion and parameters, healthy CAN/panda, active lateral for 2s, drive gear, ≥5mph, no current gas/brake, no steering pressure in the preceding1s, and no current turn signals or lane change. Requested acceleration ≥0.25m/s²; below50mph also |curvature|>0.001/m. All response ratios below use this meaningful-demand subset.

## All-speed coverage

|Cohort|mph|Recorded s|Active s|Qualified s|Meaningful s|Steady s|Body/request median|Signed body excess median m/s²|
|---|---|---:|---:|---:|---:|---:|---:|---:|
|candidate|0–5|691.7|79.7|0.0|0.0|0.0|no data|no data|
|candidate|5–10|22.2|8.2|8.2|0.0|0.0|no data|no data|
|candidate|10–15|28.7|12.6|6.0|0.0|0.0|no data|no data|
|candidate|15–20|20.3|12.0|5.1|0.0|0.0|no data|no data|
|candidate|20–25|32.6|25.1|14.8|0.0|0.0|no data|no data|
|candidate|25–30|52.7|52.2|14.4|2.7|0.0|0.682|-0.161|
|candidate|30–35|6.0|6.0|3.4|0.0|0.0|no data|no data|
|candidate|35–40|11.3|11.3|9.2|6.7|5.8|1.108|0.140|
|candidate|40–45|36.2|36.2|31.7|30.8|25.2|1.147|0.210|
|candidate|45–50|60.5|60.5|49.6|21.7|6.5|1.130|0.170|
|candidate|50–55|118.9|118.9|91.6|39.5|5.2|1.121|0.071|
|candidate|55–60|289.9|289.9|259.5|154.2|30.9|1.038|0.031|
|candidate|60–65|278.4|278.4|251.6|161.8|32.4|1.067|0.046|
|candidate|65–70|106.7|106.7|99.7|39.0|5.4|1.120|0.097|
|candidate|70–75|0.0|0.0|0.0|0.0|0.0|no data|no data|
|candidate|75–80|0.0|0.0|0.0|0.0|0.0|no data|no data|
|candidate|80–85|0.0|0.0|0.0|0.0|0.0|no data|no data|
|candidate|85–90|0.0|0.0|0.0|0.0|0.0|no data|no data|
|pre-update|0–5|894.5|502.2|0.0|0.0|0.0|no data|no data|
|pre-update|5–10|246.7|99.3|82.5|0.0|0.0|no data|no data|
|pre-update|10–15|268.6|131.2|103.2|0.0|0.0|no data|no data|
|pre-update|15–20|292.4|190.4|130.0|3.1|0.0|0.593|-0.113|
|pre-update|20–25|390.4|324.1|239.4|3.1|0.0|0.686|-0.107|
|pre-update|25–30|136.9|123.3|68.7|10.5|0.3|0.752|-0.175|
|pre-update|30–35|82.4|75.2|58.2|4.4|0.0|1.091|0.069|
|pre-update|35–40|26.6|26.6|21.7|4.0|0.9|1.106|0.099|
|pre-update|40–45|21.6|21.6|15.7|1.0|0.0|1.455|0.261|
|pre-update|45–50|39.6|39.6|33.8|4.7|1.2|1.110|0.073|
|pre-update|50–55|16.5|16.5|11.9|5.8|1.7|1.207|0.133|
|pre-update|55–60|74.2|74.2|60.7|29.9|3.2|1.160|0.071|
|pre-update|60–65|113.1|113.1|106.5|48.0|10.7|1.128|0.081|
|pre-update|65–70|58.3|58.3|53.2|22.7|5.0|1.070|0.048|
|pre-update|70–75|1.5|1.5|0.8|0.8|0.0|1.297|0.337|
|pre-update|75–80|0.0|0.0|0.0|0.0|0.0|no data|no data|
|pre-update|80–85|0.0|0.0|0.0|0.0|0.0|no data|no data|
|pre-update|85–90|0.0|0.0|0.0|0.0|0.0|no data|no data|

Additional sensitivity excluding any gas/brake in the preceding1s removes zero steady samples in candidate40–45mph or45–50mph; their steady exposure and body/request medians remain unchanged. Qualification itself is unchanged. See `pedal-history-sensitivity.json`.

The final row includes85–90mph to disclose any exposure above85; actual maximum is listed by drive. Zero meaningful/steady exposure is an explicit evidence gap, regardless of recorded time.

##40–50mph excess-response screen

|Drive|Screen|Start–end s|mph p10/50/90|Body/request p10/50/90|Wheel/request p10/50/90|Phase samples|
|---|---|---|---|---|---|---|
|post-regression-session-02|body_excess|136.05–137.30|39.45/40.35/40.95|1.28/1.34/1.59|1.23/1.26/1.38|{'transition': 1, 'unwinding': 25}|
|post-regression-session-08|body_excess|393.15–393.70|47.34/47.72/47.93|1.23/1.24/1.29|1.18/1.22/1.25|{'unwinding': 12}|
|post-regression-session-08|body_excess|393.80–394.40|48.03/48.37/48.63|1.22/1.29/1.40|1.18/1.19/1.23|{'unwinding': 13}|
|post-regression-session-08|body_excess|809.05–809.75|49.45/49.50/49.62|1.25/1.30/1.34|1.24/1.28/1.31|{'transition': 6, 'unwinding': 5, 'rising': 4}|

`body_excess` requires body/request>1.2 and signed excess>0.2m/s² for≥0.5s. `coherent_excess` additionally requires same-direction wheel excess>0.2m/s² and body excess>2×reported yaw standard deviation×speed. Unwinding and transition samples are identified, not called proven overshoot. All-speed windows are in `analysis.json`.

The prior saved session05 problem windows were400–440s (speed p10/50/90:41.23/47.51/53.24mph; body/request0.934/1.168/1.303) and832–852s (49.48/49.78/53.47mph;1.043/1.206/1.348). These saved summary windows use different phase/excitation mixtures; their statistics are descriptive reference, not matched-road effect estimates. See `../../navigator-coordinated-coast-road-review-2026-10-27/focused-lateral.json`.

The candidate admission design requires independent wheel/body history, stable same-direction targets, coherent ratios and directional hysteresis. Logs here do not expose admission mode; the observation screen cannot prove the gate admitted or withdrew a correction.35–55mph is the extension; unqualified50–55mph retains exact old fallback and other bands inherit prior behavior. This review does not rerun frozen-input policy replay.

## Driver-pressure and disengagement context

|Drive|Cohort|Start s|mph|Association|Prior qualified s|Prior body excess median m/s²|
|---|---|---:|---:|---|---:|---:|
|post-regression-session-01|pre-update|120.50|18.1|steering-pressure gas|0.00|no data|
|post-regression-session-01|pre-update|145.75|27.1|steering-pressure gas signal|2.80|-0.679274583261236|
|post-regression-session-01|pre-update|171.45|43.7|steering-pressure,steering-pressure,steering-pressure gas signal|0.00|no data|
|post-regression-session-01|pre-update|273.65|66.1|steering-pressure signal|0.40|-0.0048931725391508085|
|post-regression-session-01|pre-update|304.15|65.7|steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure|1.80|0.059625979568070586|
|post-regression-session-01|pre-update|342.45|15.1|steering-pressure|0.00|no data|
|post-regression-session-01|pre-update|360.20|8.8|steering-pressure|0.00|no data|
|post-regression-session-01|pre-update|436.60|30.9|lateral-disengagement brake signal|0.00|no data|
|post-regression-session-01|pre-update|448.20|27.5|steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-01|pre-update|457.25|28.5|steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-01|pre-update|525.05|23.0|steering-pressure|0.00|no data|
|post-regression-session-01|pre-update|530.50|22.9|steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure,lateral-disengagement brake|0.00|no data|
|post-regression-session-02|pre-update|47.30|25.9|lateral-disengagement brake|0.00|no data|
|post-regression-session-02|pre-update|75.10|20.4|lateral-disengagement brake signal|0.00|no data|
|post-regression-session-02|pre-update|121.00|32.3|lateral-disengagement,steering-pressure brake gas|0.00|no data|
|post-regression-session-02|pre-update|148.80|52.6|steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure signal|2.85|0.186396035000567|
|post-regression-session-02|pre-update|352.70|47.9|steering-pressure|0.00|no data|
|post-regression-session-02|pre-update|457.35|14.0|steering-pressure gas|0.00|no data|
|post-regression-session-02|pre-update|485.25|15.0|lateral-disengagement,steering-pressure brake gas|0.00|no data|
|post-regression-session-03|pre-update|146.20|21.1|steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-03|pre-update|177.40|23.6|steering-pressure|0.00|no data|
|post-regression-session-03|pre-update|180.70|21.9|steering-pressure,steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-03|pre-update|285.90|16.3|lateral-disengagement brake|0.00|no data|
|post-regression-session-03|pre-update|343.35|20.2|lateral-disengagement,steering-pressure brake|0.00|no data|
|post-regression-session-03|pre-update|369.10|20.0|steering-pressure,steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-03|pre-update|375.35|12.1|steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-03|pre-update|399.30|18.7|steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure,lateral-disengagement brake gas|0.00|no data|
|post-regression-session-04|pre-update|147.35|22.9|steering-pressure,steering-pressure,steering-pressure,steering-pressure gas|0.00|no data|
|post-regression-session-04|pre-update|179.85|22.3|steering-pressure,steering-pressure,lateral-disengagement,steering-pressure brake|0.00|no data|
|post-regression-session-05|pre-update|86.85|25.6|steering-pressure|0.00|no data|
|post-regression-session-05|pre-update|125.25|14.5|steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-05|pre-update|443.20|21.4|lateral-disengagement,steering-pressure brake signal|0.00|no data|
|post-regression-session-06|pre-update|64.15|10.2|steering-pressure,steering-pressure gas signal|0.00|no data|
|post-regression-session-06|pre-update|169.40|13.6|steering-pressure signal|0.00|no data|
|post-regression-session-06|pre-update|233.95|20.8|steering-pressure signal|0.00|no data|
|post-regression-session-06|pre-update|239.90|17.7|steering-pressure,steering-pressure gas signal|0.00|no data|
|post-regression-session-06|pre-update|256.35|31.8|steering-pressure gas|0.00|no data|
|post-regression-session-06|pre-update|264.75|33.1|lateral-disengagement brake|0.00|no data|
|post-regression-session-08|candidate|63.25|24.7|steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-08|candidate|79.65|27.6|steering-pressure,steering-pressure|0.20|-0.19237087831801924|
|post-regression-session-08|candidate|85.55|29.7|steering-pressure,steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-08|candidate|93.25|28.4|steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure gas signal|1.10|-0.17275924467016|
|post-regression-session-08|candidate|122.15|55.3|steering-pressure,steering-pressure,steering-pressure,steering-pressure,steering-pressure gas signal|0.00|no data|
|post-regression-session-08|candidate|201.05|54.0|steering-pressure signal|2.80|0.09599366145815452|
|post-regression-session-08|candidate|219.55|58.0|steering-pressure signal|2.80|0.06841712633957747|
|post-regression-session-08|candidate|288.60|50.9|steering-pressure,steering-pressure signal|0.00|no data|
|post-regression-session-08|candidate|414.85|55.4|steering-pressure signal|2.80|-0.04137004646923054|
|post-regression-session-08|candidate|417.85|54.1|steering-pressure,steering-pressure signal|0.00|no data|
|post-regression-session-08|candidate|439.30|58.0|steering-pressure|2.80|0.09145170332830976|
|post-regression-session-08|candidate|485.35|60.4|steering-pressure|2.80|0.07214586895007014|
|post-regression-session-08|candidate|496.45|60.6|steering-pressure|2.85|0.1847715133009702|
|post-regression-session-08|candidate|498.25|61.4|steering-pressure|1.05|0.2904826413624544|
|post-regression-session-08|candidate|499.65|60.9|steering-pressure signal|0.00|no data|
|post-regression-session-08|candidate|501.60|60.1|steering-pressure signal|0.00|no data|
|post-regression-session-08|candidate|529.50|61.0|steering-pressure|2.80|-0.08611234779107935|
|post-regression-session-08|candidate|552.90|66.4|steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-08|candidate|578.20|67.2|steering-pressure|0.00|no data|
|post-regression-session-08|candidate|585.30|61.3|steering-pressure,steering-pressure|0.15|-0.24973414637247338|
|post-regression-session-08|candidate|652.15|11.0|steering-pressure,steering-pressure,lateral-disengagement brake gas|0.00|no data|
|post-regression-session-08|candidate|776.55|60.0|steering-pressure|1.75|-0.07549244055930537|
|post-regression-session-08|candidate|780.30|61.0|steering-pressure|2.35|-0.030809207676909534|
|post-regression-session-08|candidate|811.95|49.5|driver-confirmed planned lane-position change|2.80|0.15214509932514492|
|post-regression-session-08|candidate|838.85|59.1|steering-pressure signal|2.80|-0.009029184716345284|
|post-regression-session-08|candidate|861.25|53.3|steering-pressure|0.90|-0.1411808521453296|
|post-regression-session-08|candidate|894.50|55.0|steering-pressure signal|0.00|no data|
|post-regression-session-08|candidate|896.25|56.6|steering-pressure,steering-pressure signal|0.00|no data|
|post-regression-session-08|candidate|1090.50|50.7|steering-pressure|2.80|0.02977791126811713|
|post-regression-session-08|candidate|1093.75|47.4|steering-pressure|0.00|no data|
|post-regression-session-08|candidate|1096.25|46.1|steering-pressure,steering-pressure,steering-pressure,steering-pressure|0.00|no data|
|post-regression-session-08|candidate|1156.45|22.5|steering-pressure,lateral-disengagement brake signal|0.00|no data|

Every detected pressure interval with lateral activity in its preceding1s and each lateral-active falling edge at≥5mph is retained; events within1s are grouped. These flags do not establish driver intent or safety-critical takeover. Pre-context excludes the final0.2s and uses the same qualified meaningful-demand guard; missing context is not normal tracking. Alerts/onroad events and full preceding body/wheel/wire distributions are in `analysis.json`.

## Measurement and provenance

Applied wire field is Ford path-angle command decoded to a yaw-like control quantity; multiplying it by speed expresses an equivalent acceleration for comparison, not independently measured wheel/body yaw. Body yaw uses calibrated device angular velocity. Wheel curvature is derived from steering angle minus learned offset with contemporaneous steer ratio, stiffness, speed and roll through VehicleModel. It remains a model-derived estimate rather than direct tire or road authority. Steering rate is the backward difference of measured steering angle at20Hz; repeated angle messages may quantize it.

Zero-demand/straight-like results use absolute acceleration and wheel-rate distributions (`quiet_demand_5s` windows), never response percentages. Heading, roll mapping, phase lag, model/path demand and request unwind can create instantaneous discrepancy; no same-time ratio alone establishes unstable steering. Motion yaw uncertainty is retained in every meaningful-window table. No fitted lag correction is used, so transient response remains phase-dependent.

Raw receipt: `../acquisition-provenance.json`; input hashes: `../input-manifest.json`. Local extraction and normalized-array SHA256 are in `analysis.json`. Only saved files were decoded; no device/ECU queries or CAN transmission.

## Controller-basis speed and publication sensitivity

All lateral speed bands and maxima above use `carState.vEgoRaw`, matching the controller observation basis. Candidate maximum69.892mph is raw speed; the main health review uses filtered `vEgo` and reports69.233mph. These are different measurements. Neither provides candidate70–85mph coverage.

The baseline body diagnostic aligns `deviceMotion.timestamp` (physical source time), while controls/state/wire/parameters are aligned by publication time. Backward source-time alignment alone does not establish that that body sample had arrived online. It can include delivery lookahead relative to publication; transient windows therefore are physical timing diagnostics rather than exact controller-available observations. Parameters are fresh learned estimates, not direct physical tire measurements.

|Candidate steady mph|Seconds|Wire/request median|Wheel/wire median|Body/wire median|Body/request median|
|---|---:|---:|---:|---:|---:|
|35–40|5.80|1.5416|0.7231|0.7261|1.1096|
|40–45|25.25|1.4893|0.7780|0.7729|1.1472|
|45–50|6.45|1.4439|0.7800|0.7859|1.1319|
|50–55|5.20|1.3645|0.8408|0.8431|1.1172|
|55–60|30.90|1.2251|0.8350|0.8380|1.0351|
|60–65|32.35|1.2383|0.8288|0.8288|1.0285|
|65–70|5.40|1.3326|0.8279|0.8250|1.0878|

Publication sensitivity re-aligns candidate motion by event publication and additionally requires both source and publication timestamps≤analysis time, physical source age<120ms, no current pedals, no steering pressure in preceding1s,2s active, and all other original qualification guards. It contains zero eligible future publication/source samples. This checks delivery availability, without fitting a dynamics lag or changing recorded demand.

|mph|Publication-aligned steady s|Body/request median|Signed excess median m/s²|
|---|---:|---:|---:|
|35–40|5.80|1.1067017813172786|0.14081155553653946|
|40–45|25.25|1.147193558226769|0.21394412999669754|
|45–50|6.45|1.1333534867037982|0.21887543627460326|
|50–55|5.20|1.1118182671372674|0.08299541427401161|
|55–60|30.90|1.0358524159935287|0.036581611455268837|
|60–65|32.35|1.029557968588977|0.029873515537410134|
|65–70|5.30|1.0874951094390353|0.0826635284281258|

Qualified motion delivery delay p0/p10/p50/p90/p100 seconds: [0.015675957005100827, 0.0204688295051767, 0.024651765997447228, 0.028056403505898688, 0.031974603000207935]. The complete stream has 15 stale-source delivery samples over120ms, including startup timestamps; these cannot qualify in the publication sensitivity. Full stream maximum is retained in JSON. See `publication-sensitivity.json`.

## Driver-context exclusion sensitivity

The driver-confirmed planned maneuver supersedes the original unattributed pressure interpretation. Excluding805.95–817.95s (±6s) or801.95–821.95s (±10s) removes those bounded intervals around the planned maneuver from independent tracking comparisons. Source-time and publication-time checks are separate.

|Exclusion|mph|All meaningful s|Steady s|Source-time steady body/request median|
|---|---|---:|---:|---:|
|±0s|40–45|30.75|25.25|1.1472|
|±0s|45–50|21.65|6.45|1.1319|
|±6s|40–45|30.75|25.25|1.1472|
|±6s|45–50|15.70|4.65|1.1229|
|±10s|40–45|30.75|25.25|1.1472|
|±10s|45–50|15.30|4.65|1.1229|

After both exclusions40–45mph retains25.25s steady at1.1472 body/request median;45–50mph retains only4.65s steady at1.1229. Those are remaining numerical tracking observations, not demonstrated unexpected maneuvers. The planned event cannot support a corrective-takeover or unsafe-oversteer diagnosis.

Publication-aligned exclusion sensitivity:

- ±6s,40–45mph: 25.25s steady, body/request median 1.1472.
- ±6s,45–50mph: 4.65s steady, body/request median 1.1272.
- ±10s,40–45mph: 25.25s steady, body/request median 1.1472.
- ±10s,45–50mph: 4.65s steady, body/request median 1.1272.

Before maneuver exclusion, publication timing leaves40–45mph steady median body/request unchanged at1.1472 (25.25s), and45–50mph at1.1334 versus source-time1.1319 (6.45s). The remaining steady mismatch is not materially changed by accounting for delivery availability. Transient event ratios remain phase/lag sensitive. The applied wire command is consistently larger in magnitude than requested in steady40–50mph; measured wheel/body equivalents are below that wire equivalent yet remain above requested. Thus the excess relative to requested is already present upstream in command mapping, rather than evidence of the plant amplifying the applied wire command. Wire is a path-angle-derived equivalent and includes calibrated mapping, so these ratios are not direct physical actuator gains or a unique causal diagnosis. Unwind and body-delivery timing still affect transient windows.
