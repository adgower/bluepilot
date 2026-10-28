<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Newer saved-drive coast signals — October 26, 2026

**Signal recovery complete: relevant sustained OEM highway coast examples were found in existing saved recordings.** The newer Alpha drives alone still lack the sustained regime. Recovered received gear, torque, RPM, brake status, pose and radar from all 37 saved segments across four sessions. The controller, Comma and archived response model were not changed or trained.

## What was recovered and verified

- Rehashed all 37 raw segments before and after extraction. Original acquisition provenance identifies source parent `5b301a944` / child `884c9f491`; these recordings do not road-validate the newer local low-speed guard.
- Two sessions contain active Alpha driving: 40,977 sent-command observations, approximately 819.56 seconds of sampled active exposure. The other two are retained in the inventory with zero active Alpha observations.
- All 40,977 active observations have backward-looking fresh radar publication and referenced model times within 150 ms, with valid radar context. This resolves the missing-radar extraction gap for these newer sessions; it does not repair the old model's uncertainty.
- Reconciled all 284,854 actual-brake, actual-propulsion and requested-propulsion torque observations from the two active routes against the previously verified joint caches: original timestamps, values and validity flags match exactly.
- Retained nanosecond timestamps, validity, duplicate counts, field ages and raw pose/calibration messages in new private caches. Did not replace the old source arrays, model files or train/calibration/evaluation roles. New routes remain previously inspected, unassigned development evidence.

## What the highway pulsing episode shows

In the same 15-second 62–64 mph window:

| Signal | Observed result |
|---|---|
| Sent actual-brake transitions | 20 |
| Received actual and target gear | Both 10 throughout |
| Received clutch engagement state | 6, DBC `Fwd_Clutch_Fully_Engaged` |
| Fresh radar context | All 751 command observations |
| Observed decoded RPM | 1,552–1,834, with unresolved quality flag below |
| Received actual wheel propulsion torque | −120 to +580 Nm |
| Received actual brake torque | 0–260 Nm |
| Positive propulsion request while received brake torque exceeds 4 Nm | Zero observations |
| Qualifying coast episode at least 200 ms entirely within this window | Zero |

This supports **mode cycling in a steady reported gear, rather than gear hunting in this episode**. Brake-bit cycling and changing received torque coexist with only brief release/propulsion periods. The no-positive-request/received-pressure overlap result is specific to these samples; it does not prove no physical drivetrain/brake overlap, safe following behavior or improved comfort. It does not explain away the separate earlier first-gear high-RPM restart.

## Coasting coverage after quality filtering

A provisional episode requires fresh received state, torque, gear and status; active owner and PID state; no driver pedals; speed at least 3 m/s (6.7 mph, outside creep); actual/target forward gear equality and fully engaged clutch; no commanded brake/precharge; received actual/arbitrated brake torque no greater than 4 Nm; no received brake/precharge status; modest yaw; valid raw producer pose; and a stable command regime/gear/gravity-proxy band. Gaps over 60 ms and gas-request span over 0.025 m/s² split episodes. These are observational selection rules, not new vehicle permissions.

There are 366 provisional episodes at least 200 ms long; 317 are positive engine requests and **49 are coast-like candidates**:

| Candidate command regime | Episodes ≥200 ms | Combined known span |
|---|---:|---:|
| Valid negative engine request | 38 | 15.39 s |
| Near-zero engine request | 11 | 3.44 s |
| Inactive propulsion with received brakes clear | 0 | 0 s |

Only five coast-like episodes last at least 600 ms; one lasts at least a second. These longer episodes are below the relevant highway range. At **60–70 mph there are only six candidates**, one near-zero and five negative-request episodes, lasting **0.239–0.378 seconds**. None reaches 600 ms and none occupies the negative-gravity-proxy band used in the investigation. Maximum active speed in the new sessions is about 65.72 mph, so this extraction adds no 70–85 mph validation.

These are contiguous episodes and separately reported nonoverlapping duration slices, not independent experiments. Counts are not directly interchangeable with the previous model's overlapping fixed-time case counts. The strict stable-command selection does not prove that no other closed-loop data could be useful; it shows that this extraction does not supply sustained, settled, relevant coast response. It does not identify a causal coast step response.

## RPM-quality issue kept explicit

`EngAoutNActl_D_QF` is **zero in every newly extracted RPM message**. The current DBC labels 3 as `OK` and 0 as `Faulty`. Older saved OEM and Alpha arrays also have this flag constantly zero across all eight routes. Consequently this is not evidence of a newly introduced update/controller problem, nor a diagnosis of an engine fault. Whether the field is applicable/populated on this Navigator remains unresolved.

All 49 coast candidates are therefore **RPM-quality-unqualified**, despite plausible changing RPM values. The fully RPM-flag-qualified inventory is zero. We keep the candidates and their torque/speed/gear evidence for investigation, but do not relabel zero as OK, claim certified RPM, or manufacture support by silently dropping the flag. A future model must validate the RPM interpretation or represent RPM as unresolved/missing. Source pose is likewise a vehicle-pitch proxy; it is not surveyed road slope or the exact refreshed consumer grade term.

## Older OEM highway recovery: useful evidence already exists

Rather than stop at the newer-drive gap, inspected the original OEM caches and found highway ACC activity in `oem-04` and `oem-05`. Their original roles were calibration and test, respectively; the OEM routes assigned to training never reached 50 mph. This is a training-coverage/split issue as well as a shortage of sustained Alpha coast intervals—not proof that useful OEM data was never saved.

Re-extracted **19 additional raw segments** from those two OEM routes, retaining event validity, radar and motion/calibration messages. Stock command ownership is incoming CAN bus 2; outgoing Comma commands remain a separate channel. OEM eligibility requires Alpha off, Comma longitudinal inactive, stock cruise enabled and an enabled stock command. Alpha-only PID/feedback metadata is not incorrectly required for stock operation. Fresh measured motion and a calibrated reference are checked independently for the old records.

The raw re-extraction confirms the initial cache reconnaissance:

| OEM highway coast evidence (60–70 mph) | Count |
|---|---:|
| Provisional episodes at least 200 ms | 34 |
| Episodes at least 600 ms | 10 |
| Episodes at least 1 second | 6 |
| Negative-gravity-proxy episodes at least 600 ms | 8 |

All 25,114 active stock-command observations have fresh radar context. Reconciled another 454,730 command/torque/gear/RPM/brake-status stream observations against the old numeric arrays: decoded values and timestamps match, while original event validity is newly retained. The old RPM quality flag is still unresolved; these remain provisional rather than certified physical-response trials.

The 27 highway coast episodes in `oem-04` retain their original calibration label; the seven in `oem-05` retain their original test label. No rows or roles were moved into training. All were already inspected, so none is new blind validation.

## What this means for the next fix

There is now a concrete local path forward **without collecting another drive yet**: build a separately versioned coast-response research experiment using the recovered OEM evidence, consistent pose/grade frames, and explicit RPM missingness/quality handling. The current archived model must remain immutable. Any new route allocation must be declared honestly; repurposing old calibration data for development cannot preserve its old evaluation claim. Keep separate retrospective route evaluation and reserve independent future evidence for road-readiness claims.

This recovery makes that next modelling experiment possible; it does not prove that a new coast selector or back-calculation policy will be stable. The approved controller prototype remains stopped at its feasibility gate until a model supports a conservative coast decision and the full coupled regression checks pass. No mode selector, integral back-calculation, gain increase, brake suppression, precharge extension, safety-limit change or device test is introduced here. Local pair `2ca969e45` / `bcd706d0` and 1.20/0.97 remain unchanged.

## Reproduction and artifacts

Using the existing paired checkout's `.venv/bin/python`, run `extract.py` then `inventory.py`; add `--older-oem` to both for the separately stored two-route OEM recovery in this research directory. Scripts only read saved local inputs and write the new research/private-cache directories. No package installation or network access is required.

`inputs.json` includes field schemas and per-stream missingness/duplicate/validity profiles; `extraction-provenance.json`, `reconciliation.json`, `historical-rpm-quality.json`, `INVENTORY.json`, `episodes.json`, `downhill-signals.json` and `RESULTS.json` preserve the evidence. Raw data and pose messages remain private. The `older-*` artifacts retain the reconnaissance, raw re-extraction, inventory and reconciliation separately. Contract tests and final verification/review are recorded alongside the results.
