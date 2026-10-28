<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Ford longitudinal forks and saved OEM coasting evidence

Read-only research, 2026-10-23. No device contact, CAN queries, source activation, or controller changes. Owner 1.20/0.97 and paired branches remain unchanged.

## Conclusion

BluePilot contains directly relevant Ford coasting and brake allocation ideas, but no examined source proves this Navigator's cycling is solved. Saved OEM ACC recordings provide a better vehicle-specific reference than copying another vehicle's thresholds. Prior pitch/grade discrepancy remains unresolved; command replay alone cannot prove comfort or fuel economy.

## Source provenance and comparison

Live GitHub metadata and pinned source copies are in `fork-provenance.json` and `sources/`. BrowserOS neo returned “No browser window available”; read-only GitHub connector access was used instead.

| Repository | Inspected default head | Finding |
|---|---|---|
| BluePilotDev/bluepilot, bp-dev | d27bc20a7c13eed7ec1947d4c59b98835facea87 | Ford LongitudinalExt adds follow/coasting behavior, separate brake/precharge outputs, brake thresholds and optional disabling of negative-pitch compensation. |
| dustin-decker/bluepilot, bp-exp | 691a38cde77c959ee895212c63c47bc44ba9613b | Examined Ford controller and extension match BluePilotDev; not an independent longitudinal fix. Controller blob e08e24bc327e7dce176f1977a97a4cadce16967c. |
| sunnypilot/sunnypilot, master | 8e740e0ac680d9a960489c04436a701dd491505c | Pinned sunnypilot/opendbc e3f1487de42c4f6de7229ef53da70673f1091b42 retains baseline Ford pitch/brake allocation in inspected controller. No Navigator-specific coasting fix found there. |
| firestar5683/StarPilot, StarPilot | 823a5d5674ec6635b51dd989884dfbd661f90dc4 | Mach-E-specific creep/brake-rate changes; other Fords retain baseline behavior in these paths. Not Navigator validation. |

Primary sources:

- [BluePilot longitudinal extension](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/opendbc_repo/opendbc/sunnypilot/car/ford/longitudinal_ext.py)
- [BluePilot Ford controller](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/opendbc_repo/opendbc/car/ford/carcontroller.py)
- [Dustin Ford controller](https://github.com/dustin-decker/bluepilot/blob/691a38cde77c959ee895212c63c47bc44ba9613b/opendbc_repo/opendbc/car/ford/carcontroller.py)
- [Sunnypilot pinned Ford controller](https://github.com/sunnypilot/opendbc/blob/e3f1487de42c4f6de7229ef53da70673f1091b42/opendbc/car/ford/carcontroller.py)
- [StarPilot Ford controller](https://github.com/firestar5683/StarPilot/blob/823a5d5674ec6635b51dd989884dfbd661f90dc4/opendbc_repo/opendbc/car/ford/carcontroller.py)

BluePilot's follow strategy latches above 50 mph and releases below 45 mph, with lead-speed and pedal gates. It caps propulsion for pacing/gaining leads and uses brake engagement below -0.14 m/s²/release above -0.06. Precharge uses separate thresholds. These are source constants, not recommended Navigator calibration. Actual braking forces propulsion inactive; precharge alone does not. Disabling downhill compensation clamps negative pitch contribution rather than calibrating sensor alignment.

Porting requires review: the no-lead branch zeros its BP braking target; old lead.status schema differs from current lead.present; BP-local brake/precharge flags reset per update despite hysteresis comments. Do not copy this entire behavior without planner demand, emergency braking, grade, timing and release validation.

[BluePilot PR 212](https://github.com/BluePilotDev/bluepilot/pull/212) is OPEN and unmerged at inspection. It describes similar brake/accel hunting and changes regen/friction handoff and actuator delay for Lightning/Mach-E EVs only. The author's reported improvement is not independently validated here and does not establish an ICE Navigator fix. [Sunnypilot PR 428](https://github.com/sunnypilot/sunnypilot/pull/428), Custom Stock Longitudinal Control: Ford Support, is CLOSED and unmerged; it is not evidence of a shipped Alpha actuator fix.

## Fresh saved OEM analysis

`oem_scan.py` re-read and SHA-256 verified 35 saved segments across five routes; every route's carParams confirms openpilot longitudinal false. 40,544 received OEM ACC commands qualify: cruise enabled, no driver pedals, openpilot long inactive, camera-bus ACC active, past-only state/control under 100 ms. Torque/motion samples are also past-only under 100 ms. Stable per-segment timestamp ordering changes eligibility from the older unsorted 39,992-command analysis; do not combine counts.

| Command state | Eligible samples | Moving samples, >5 mph |
|---|---:|---:|
| Actual brake request | 8,674 | 7,177 |
| No propulsion request, no brake/precharge | 3,032 | 1,088 |
| Valid negative propulsion request, no brake/precharge | 3,371 | 3,368 |
| Near-zero propulsion request, no brake/precharge | 2,687 | 2,679 |
| Positive propulsion request, no brake/precharge | 21,170 | 20,605 |
| Precharge only, valid propulsion request | 1,605 | 1,605 |
| Precharge only, propulsion inactive | 5 | 0 |

Every eligible actual-braking sample has propulsion inactive. OEM distinguishes precharge from actual braking and also uses mild negative propulsion commands without brake activation. Valid propulsion means the command is not the inactive sentinel; it does not necessarily mean positive engine torque.

Example observed OEM runs, zero median reported brake torque:

- 2.23 seconds near 62.6 mph, propulsion inactive, median acceleration -0.419 m/s².
- 6.10 seconds near 57.5 mph, propulsion inactive, median acceleration -0.004 m/s².
- 9.06 seconds near 65.8 mph, mild negative propulsion request, median acceleration -0.098 m/s².

This proves available OEM brake-free slowing states, not neutral gear, fuel cut or zero engine braking. Negative acceleration requests can coexist with positive reported propulsion torque because the vehicle must overcome road load. Near-zero requested acceleration is not zero physical throttle.

The current paired `opendbc/car/ford/fordcan.py:142-143` derives both precharge and deceleration bits from one brake_request. It cannot encode the observed OEM precharge-only state. That is a concrete representation gap; whether it causes this drive's cycling still requires isolated replay and actuator timing evidence.

Artifacts: `oem-inputs.json` (hashes and source versions), `oem-results.json` (counts, signals and examples), `oem-scan.log`. Raw rows remain in a private temporary cache. Runs can be censored at eligibility/segment boundaries; duration summaries are observed lengths, not complete physical maneuvers. This is not matched-route comfort or fuel-economy comparison. No new pitch calibration was estimated in this scan.

## Recommended next local work

1. Use OEM records to specify distinct propulsion, brake-free slowing, precharge and actual-braking transitions. Preserve actual-brake/propulsion exclusion while testing OEM-like precharge semantics.
2. Resolve pitch/gravity frame alignment before tuning brake thresholds. The prior diagnostic pitch offset is not an approved calibration.
3. Replay each change independently against Alpha cycling, saved OEM transitions, lead loss, grades, urgent braking, stop/hold/restart, pedal overrides and stale torque feedback. Verify packed bytes and native safety, not only controller flags.
4. Consider BluePilot's relevant concepts selectively. Do not import EV regen thresholds or suppress planner braking to manufacture fewer brake edges.
5. Keep installation gated on integration/build/native replay and a separately authorized staged vehicle test. Offline command changes do not establish smoother physical response.
