<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Ford longitudinal coordination on the current Navigator pair

October 23, 2026, America/Chicago. **Local investigation complete; no paired-source edits, device access, settings changes, publication or installation.** Owner 1.20/0.97 retained. This is command-level diagnosis and a report-local comparison, not a validated physical shaking fix or an approved Alpha installation.

## Finding

Prioritize brake/propulsion handoff before acceleration/PID tuning or Autospeed planner changes. The currently installed-source pair still has the same longitudinal block as the pre-candidate controller: `24e981d6dd44ef11325f08846fbbba2d3ee53842` / `01f32a6f66743f63ac02f1357141e5f7359b2825`. Its block is byte-identical to the parent of old candidate `d5ccadb7f9abcbee84f86dafd10e30c8e2f4e6ff`. Upstream/AGNOS updates and the steering refinements did not add that coordination candidate.

Current behavior ties precharge and deceleration to one brake latch. Pitch-compensated brake acceleration below zero sets it; a value strictly above 0.3 m/s² or disengagement clears it. Propulsion is independently computed from the raw desired acceleration and remains a valid request while braking unless below MIN_GAS or inactive. The separate 3.5 m/s³ brake-request limiter does not bound the vehicle response to withdrawing/restoring propulsion. The inactive `-5` value is a sentinel, not a physical -5 m/s² command.

The [original discussion](../../navigator-reference/PRIVATE_ARTIFACTS.md) and original logs were recovered locally. We re-extracted four original segments using current schemas/DBC, and separately scanned 35 saved segments from five October 20 backup routes. Raw filenames/hashes, source IDs, scripts and results are retained.

## Recorded evidence

| Evidence | Result | Interpretation |
| --- | --- | --- |
| Original Alpha outgoing ACCDATA | 751 enabled active-braking frames; zero inactive propulsion requests | Simultaneous valid propulsion and requested deceleration is directly observed |
| Original OEM segment 9 | All 216 enabled active-braking frames withdraw propulsion | Clear command-strategy difference |
| Original OEM segment 8 | 634 precharge-only frames, about 12.69 s | Mild slowing is not always active brake deceleration |
| Newer saved OEM subset | 39,992 eligible commands out of 100,028 received; all 8,562 active-braking commands withdraw propulsion | Coordination difference is supported beyond one historical event |
| Newer OEM precharge-only | 1,587 commands, including five with inactive propulsion | Precharge and deceleration should not be assumed identical states |
| Original vibration subset | Alpha 0.47934° RMS / 674 samples; OEM 0.08443° / 696 samples, about 5.68× | Same 73–80 mph and −0.7 to −0.1 m/s² filters, different road intervals; association rather than causality |

Vibration uses measured steering angle, third-order Butterworth 3–15 Hz forward/backward bandpass over each whole segment, sampling frequency from median timestamp spacing. Cruise must be enabled and driver pedals released. Samples are time-correlated; road, surface and physical conditions are uncontrolled. All original logs mark source dirty; matching recorded Git IDs do not establish identical uncommitted code. No offline command replay reproduces hydraulic or wheel vibration.

Fresh ECU-reported torque extraction also reproduces the earlier observation. During Alpha +27–30 s and +31–34 s, mean brake torque is 146/174 Nm alongside reported propulsion torque +427/+273 Nm. OEM mild slowing averages brake 57 Nm / propulsion −128 Nm; stronger braking averages 346 Nm / −95 Nm. These are decoded ECU reports, not independent measurements or proof of the cause.

Newer OEM eligibility: received camera bus 2, recorded openpilotLongitudinalControl false on all five routes, longActive false, cruise enabled, neither driver pedal pressed, latest state/control ages under 100 ms. Histories reset at eligibility loss, route boundaries and command gaps over 100 ms. This is OEM evidence from older installed steering revisions, not Alpha evidence on the new 20.1 pair. No new recording was downloaded.

## Current-controller comparison

A report-local in-memory copy adds only the old Expedition brake-latch propulsion withdrawal after hysteresis. Both variants run current controller code with Navigator wheelbase 3.1115 m, steer ratio 19.6, flags 15 and Alpha enabled in memory. No paired file or setting is edited.

- 2,984 ACC outputs compared; **751 differ only in AccPrpl_A_Rq**.
- 3,889 non-ACC outputs are byte-identical for the supplied frozen inputs.
- All 2,984 candidate ACC frames pass the current native debug TX hook, Ford parameter 11, with recorded longActive permission. This is a TX-hook check, not a full physical RX/forwarding/timing/permission replay.
- Existing recovered eight command contracts: baseline has four expected withdrawal-contract failures and zero errors; the report-local candidate passes all eight. Contracts cover brake demand, both pitch directions, latch/release, low-speed restart, disengagement/reengagement, bounds, two other Ford configurations, OEM mode and allowed/disallowed TX behavior. These tests demonstrate command semantics, not a shaking cure.
- Twelve additional settled sequences (0/2/15/33 m/s × negative/zero/positive pitch) expose release behavior, with OEM-mode and two other-platform parity checks.

Replay limitations: synthetic 100 Hz update schedule, 50 Hz ACC cadence, explicit historical initial accel/latch seed, and latest preceding state without lookahead. One control before the first state is skipped. Original log has 2,983 outgoing ACC frames; this constructed schedule produces 2,984, so it is not an exact original-wire replay. Earlier candidate reporting used 752 changed frames; this fresh replay uses 751 and does not silently reuse that older count. Only selected state/control fields are reconstructed; full modern atomic steering/context replay is not claimed. Native hooks were freshly compiled on Mac without sanitizers; sanitizer loader failure is retained in the investigation history, and no UBSan/ARM/hardware claim follows.

## Why the old candidate is not sufficient for installation

1. **Release and launch:** after a flat-road brake latch, +0.20/+0.25 m/s² requests still leave propulsion inactive; +0.31 releases it. With pitch contributing −0.3 m/s², +0.50 still holds the latch and +0.70 releases it. These are synthetic command outcomes, not measured launch delay. Creep compensation further couples low-speed brake behavior.
2. **Handoff:** original OEM holds propulsion inactive about 2.00 s after releasing brake bits. Newer saved complete eligible release periods vary about 0.018–2.228 s. A universal two-second hold is not justified. The old candidate resumes as soon as its existing latch clears; vehicle torque response to that transition is unvalidated.
3. **Mild braking:** the candidate retains tied precharge/deceleration bits and therefore does not reproduce observed OEM precharge-only slowing.
4. **Other semantics:** predicted acceleration remains inactive and target-speed field remains fixed. Their effects are unresolved; do not change them simultaneously or infer a cure from OEM differences alone.
5. **Physical outcome:** there is no candidate Alpha road recording, grade/restart validation or closed-loop vehicle-response model proving that withdrawing propulsion removes vibration. Current stock-ACC drives cannot establish Alpha behavior.

## Next narrow scope

Design an Expedition/Navigator-only, explicit brake/propulsion coordination state machine, preserving the existing stock-ACC/default-off path and all steering behavior. Establish the mutual-exclusion contract for active brake deceleration; separately define brake release, propulsion resumption, pitch validity and low-speed restart. Use real OEM transitions to test proposed states, without copying a fixed timer or unsupported thresholds. Preserve demanded braking, existing limits and all disengagement/permission behavior. Treat precharge-only selection as a separate testable change; leave predicted acceleration, target-speed semantics, planner behavior and PID gains fixed initially.

Required next local gates: production controller-to-wire tests for grades, pitch changes/dropout, standstill/starting, modest positive demands after braking, aborted/reversed requests, brake/cancel/disengagement, transition timing and non-target/default parity; input provenance and native RX/TX replay; retained steering regression/build checks after actual integration. Vehicle acceptance and a separately scoped supervised Alpha evaluation remain later steps. No road exercise is needed to finish this local design.

## Evidence and reproduction

- [Pinned sources and four original files](../../navigator-reference/PRIVATE_ARTIFACTS.md), [unchanged longitudinal block](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- [Original logs, current-controller comparison and transition matrix](../../navigator-reference/PRIVATE_ARTIFACTS.md), [ECU torque results](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- [Newer saved OEM subset](../../navigator-reference/PRIVATE_ARTIFACTS.md), [35 file hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- [Baseline contract result](../../navigator-reference/PRIVATE_ARTIFACTS.md), [candidate contract result](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- Run `investigate.py`, `response_check.py`, `scan_saved_oem.py` using the pinned integration venv. `check_contract.py baseline` intentionally exits 1 on the four missing candidate contracts; `check_contract.py candidate` exits 0. Private decoded caches are under `${PRIVATE_CACHE}`; scripts do not access the vehicle. All paths are pinned inside the scripts.
