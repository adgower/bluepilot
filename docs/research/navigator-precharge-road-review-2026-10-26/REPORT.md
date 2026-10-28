<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Bounded precharge: first road review — October 26, 2026

## Findings

Both reported symptoms are present in the saved drives. No controls-mismatch event, mismatch alert or longitudinal coordination fault was recorded. The new bounded precharge path is active, but it does not cover the worst remaining downhill-like cycle. A separate rolling restart reaches about 3,946 RPM in reported first gear before the reported shift to second completes.

All times below are America/Chicago (CDT), October 26. This is a read-only/offline investigation: no source/settings changes, service action, reboot, ECU query or CAN transmission.

## Acquisition and exact tune

Downloaded all 37 newly completed rlog segments across four sessions (305,185,728 raw bytes). No open segments deferred. Raw hashes and final remote inventory were verified; source, selected preferences, protected files and service matched before/after download. All recorded startup metadata identifies clean parent `5b301a944f40b6d3d4a490e2a2f30cbeab3a8d45`; it pins child `884c9f49167a8baffdb643559b5d341815172836`. Device inventory independently matched both.

Two sessions contain active Alpha; two contain no active longitudinal control. The active sessions provide about 13.66 minutes of qualified data across 0–65.7 mph. There is no qualified 66–85 mph validation here. Both active routes are ordinary driving, with no maneuver-tool sequence. Owner-reported slight improvement is useful context, not a measured percentage from matched conditions.

## What the new path actually did

Direct wire decoding shows 31 precharge-only entries totaling 5.914 seconds: actual brake bit OFF, precharge ON and inactive propulsion. The qualified feedback view reports 5.918 seconds; that small difference is publication/consumer timestamp timing. All 70,291 consumer callbacks across the two active routes match recorded CAN brake/precharge flags and gas requests, allowing half of the DBC's 0.01 m/s² gas quantum. Fresh-target/consumed-plan, valid CAN and no-driver-pedal gates define the analytical subset.

The largest observed held precharge-only interval is 0.3232 seconds. Returned decision ages stay below 0.3 seconds; commands persist until the next callback, as already documented in integration. Measured-clearance requirements are unchanged. This directly establishes path activation and reduced actual-brake admission in those entries, not physical comfort benefit or superiority to OEM ACC.

## Remaining pulsing: approximately <private clock time>–<private clock time>

- Speed 61.5–63.6 mph; cruise setting 70 mph throughout. The episode is not simply oscillation around the set-speed ceiling.
- Reported gear remains tenth. A lead is present in this window; minimum reported distance about 72.6 m.
- Consumed planner target is only −0.051 to +0.203 m/s². Controller raw request is +0.003 to +0.501 m/s².
- There are 20 actual transmitted brake-bit transitions in 15 seconds. These are on/off command changes, not 20 separately measured hydraulic cycles.
- ECU-reported brake torque ranges 0–260 Nm; reported propulsion torque −120 to +580 Nm. The torque variation corroborates actuator response, rather than relying on noisy wheel-acceleration spikes.
- Reconstructed pitch-based mapped gravity has median −0.342 m/s²; median Ford compensation-minus-wheel estimate is −0.260 m/s². Both are consistent with a descending section. Neither is independent absolute road-grade truth; body motion/calibration and consumer pose-refresh timing remain limitations.
- There are **no precharge-only entries in this particular window**. Existing actual-brake/release/ramp behavior governs it.

The pattern is consistent with grade-conditioned mode selection coupled to integral and actuator delay: weak planner demand becomes negative net demand for brake admission, followed by pressure clearance and rising propulsion; the next brake request interrupts that recovery. ECU propulsion torque can persist briefly after command withdrawal. The recording does not uniquely identify one dominant cause or prove that disabling grade compensation will improve it. The bounded weak-entry patch is insufficient here.

Other selected windows show 16 transitions near 59–63 mph and seven transitions near 53–59 mph, including one with entirely positive planner demand. Lead/traffic and route differences prevent treating cross-window counts as a controlled comfort comparison.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## High RPM: rolling restart near <private clock time>

The vehicle slows from roughly 24 mph to about 3 mph, then accelerates again while Alpha remains active and no gas/brake pedal input is recorded. Selector is Drive. The valid propulsion request ramps to about 1.82 m/s², then falls as the planner target approaches zero and becomes negative.

RPM exceeds 3,000 for about 3.96 seconds. Peak is **3,946 RPM at 20.9 mph**, with reported actual gear first and target gear second. Target first→second is reported at monotonic 136111.104857931; reported actual second arrives at 136113.344765163, about **2.24 seconds later**. RPM is already falling during the reported transition. At the peak, the valid propulsion request is only about +0.09 m/s² and actual-brake bit is OFF. Later automatic braking and recorded driver brake input follow; driver input begins after the high-RPM peak.

The reported shift completes. This is evidence of an undesirable rolling-restart/shift sequence, not proof of a permanently stuck transmission, direct gear command from openpilot, or a mechanical diagnosis. The ordinary Ford command builder supplies acceleration/brake/mode fields rather than selecting a specific gear.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Saved OEM comparison and a concrete protocol lead

Existing hash-verified OEM caches contain about 15.1 seconds of qualifying positive-command first-gear exposure on two routes. Their observed first-gear peaks are 2,542 and 2,636 RPM, with maximum speeds about 15.9 and 16.7 mph. The routes, loads, grade and demand histories are not matched to the new Alpha event; these observations justify comparison, not a causal conclusion or an earlier-shift tuning target.

The same OEM subsets use varying valid `AccPrpl_A_Pred` values (including +1.17 to +2.31 m/s² on one route). In the new Alpha restart, that field is always −5, decoded as the existing inactive value. Alpha also sends `AccVeh_V_Trg=145 km/h` and resume-enable=1 throughout the active window; the OEM subsets vary these fields. Source confirms the prediction/target/resume behavior existed before this precharge update, so it is not a new change introduced by the allocator.

These are **specific protocol differences to investigate**, especially for anticipation/shift behavior. Their labels do not establish their effect on the TCM. Do not simply copy OEM values, force a gear, or transmit exploratory requests based on this correlation. The next local comparison should match speed, load/torque, brake clearance, gear and restart phase, and separate the prediction, target-speed and resume fields.

## Next work

1. Prioritize the remaining downhill brake/propulsion cycle. Use the selected 15-second window as a regression; investigate consumer mode admission/release, measured torque-response delay and integral recovery together. Preserve urgent braking and the existing received-torque clearance rule. Avoid a blanket gas-gain increase or deleting grade compensation on this evidence.
2. Investigate the rolling-restart load/shift sequence separately against OEM command fields and earlier starts. This is a useful reverse-engineering lead; a causal shift response is not established by frozen-state replay.
3. Keep current source/settings unchanged while designing any next candidate. A normal-drive comparison is more relevant to the pulsing than repeating the whole maneuver suite, which does not reproduce these descending lead-following conditions.

## Verification, limits and reproduction

`verification.json` rehashes all 37 segments, verifies exact startup tune, ordered decoded streams, target/source identity and all 70,291 wire/feedback callback matches. The source receiver is never instantiated: all CAN parsing operates on saved arrays/messages on the Mac. Intermediate analysis corrected two harness issues: the gas comparison now respects its 0.01 m/s² wire quantum, and original unpadded segment names required numeric ordering. Decoded rows were sorted without removing or changing values; `ordering-correction.json` retains hash provenance. Final monotonicity and identity checks pass. No physical improvement percentage, fuel-economy conclusion, new tune or high-speed validation is claimed.

Reproduce using the paired checkout Python: `quick_inventory.py`, `health_extract.py`, `quick_health.py`, `thin.py`, `scan_can.py`, `road_metrics.py`, `analyze.py`, `protocol_window.py`, `compare_oem_gear.py`, `verify.py`. Run `plot.py` with the retained temporary plotting dependency path. Raw routes, coordinates, original logs and full extracted rows remain private. Charts and selected CSVs are deidentified. `acquisition-provenance.json`, `input-manifest.json`, `analysis.json`, `wire-precharge-summary.json`, `protocol-window.json`, `oem-gear-comparison.json` and verification receipts retain the evidence.
