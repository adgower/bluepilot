<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest installed-source drive review — 2026-10-27

The new recording contains **one controlsMismatch**, immediately preceded by a V1 coordinator `invalid_pose_or_accel` fault at approximately **20.40 mph**. The exact consumed producer sequence carries a healthy fresh pose timestamp **93.749 microseconds later than its earlier sampled producer clock**, and therefore records `poseValid=false`. This is strong evidence of the producer clock/pose ordering race. Panda had not withdrawn controls permission when the coordinator fault or mismatch appeared.

Low-speed pulsing is also supported by command and received brake-torque cycling. This remains a separate control-quality finding; resolving the clock race alone does not demonstrate that pulsing is fixed.

## Provenance and limits

Read-only SSH acquired all **14 newly completed segments**, two moving sessions, **118,848,626 original bytes**. Dedup used verified hash/size manifests; there were no locked recordings in the fresh inventory. Every original and every archived segment independently matches its device SHA-256. The private durable archive is verified in [the receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md). No vehicle settings, files, services, firmware, or calibration were changed.

Fresh device manifests before and after acquisition agree on clean installed parent `df788e02719c05595dab2f980e6fd9fb9e464006`, child `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`, settings, protected file hashes, and service metadata. All 14 recorded `initData` entries also identify that clean parent. Both sessions are moving installed-source cohorts; maximum recorded speeds are 29.22 and 30.39 mph. There is no new evidence at or above 40 mph.

The local decoder checkout is concurrently receiving new integrations. This analysis decodes **recorded allocatorVersion 1** metadata and wire traffic; it does not execute the new allocator as an old baseline. Controller fixes pending elsewhere have no road validation from these recordings. Raw route names and GNSS remain private; no video was reviewed.

## Exact mismatch sequence

Times below are relative to latest-session-02 recording origin, not time since engagement.

| Event | Time | Evidence |
|---|---:|---|
| Earlier active producer pose-invalid sample | 306.646454 s | Sequence 29266; pose timestamp 318.121 us newer than producer clock; no output fault for that sequence |
| Consumed offending producer sample | 306.697289 s | Sequence 29270, producer 240272541591912 ns; pose 240272541685661 ns; poseValid false, referenceValid true |
| Coordinator fault output | 306.707964 s | Sequence 29270; `invalid_pose_or_accel`, fault true, valid false, requested −0.205257 m/s², allocatorVersion 1 |
| Immediate disable | 306.712393 s | `controlsMismatch/immediateDisable`, **4.429 ms after fault output** |
| Panda still permits controls | fault +17.710 ms | controlsAllowed true; safetyTxBlocked remains 2; RX-invalid 0 and RX checks valid |
| Panda subsequently disables | fault +118.047 ms | controlsAllowed false; safetyTxBlocked becomes 4 |

Sequence 29270's target is valid and its acceleration finite. The pose's source age relative to the earlier producer sample is **−0.093749 ms**, while the same pose is **28.091335 ms old relative to the consumer clock carried in the fault output**. The pose timestamp is thus future only relative to the producer's earlier clock sample. Recorded deviceMotion envelope, orientation, inputs, sensors, and posenet are valid. Next sequence 29271 reuses the same pose with poseValid true and a normal 26.480263 ms producer age. Both pedals and steering override are released at the fault; CAN and steering fault flags remain healthy.

The latest prior-value join would misleadingly select sequence 29271, because that message arrived before the fault output. The causal join must instead match the output's epoch and sequence, which selects 29270. The compact [clock race fixture](../../navigator-reference/PRIVATE_ARTIFACTS.md) retains these exact clocks and validity fields for a regression test. Guards rejecting truly future or stale poses should remain strict; the supported investigation is producer timestamp sampling order.

Only two active pose-invalid producer samples occur in session02, and only one is consumed into a fault. Session01 has zero active pose-invalid samples and zero faults. Panda counter order supports coordinator-first initiation; sampled Panda logs cannot resolve every intervening CAN packet or every native rejection reason.

## Below-40 pulsing

All figures below use backward-only joins, active longitudinal control, no accelerator/brake/steering override, valid streams no older than 100 ms, and fresh received torque/status. A change count is a bit transition, not a complete cycle or comfort measurement.

| Session / window | Speed | Full brake bit changes | Received brake torque changes, 4/8 Nm hysteresis | Brake torque range |
|---|---:|---:|---:|---:|
| Session01 +230–245 s | 24.26–27.53 mph | 4 | 6 | 0–64 Nm |
| Session02 +150–165 s | 23.20–27.25 mph | 11 | 15 | 0–160 Nm |
| Session02 +160–175 s | 20.62–24.59 mph | 14 | 14 | 0–148 Nm |

The session02 +160–175 s window has positive producer raw request throughout (**0.02157–0.27386 m/s²**) while planner target crosses zero (−0.26743 to +0.11297), integral ranges +0.06770 to +0.39728, and recorded mapped gradeOffset is +0.149913 m/s². Actual acceleration ranges −1.129 to +0.836 m/s² and received propulsion torque −280 to +500 Nm. This identifies a demand/integral/grade/actuator-response interaction worth retaining as a regression; it does not isolate road slope or any single term as the cause. Recorded mapped gradeOffset is not independently reconstructed road slope.

There are no positive-propulsion samples with the outgoing full-brake or precharge flag asserted in these qualified pulse windows. That invariant does not establish absence of hydraulic overlap: received brake torque is an ECU-reported quantity, not a direct pressure measurement.

The broader counts of 179/426 allocator phase transitions are **not** physical pulse counts: many are `engineRamp`/`drive` labels toggling around a limiter boundary. Actual command brake/precharge flag transitions total 23/74 across the qualified sessions. The [command/response CSV](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [fresh pulse audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) retain the relevant low-speed windows.

## Brake release and restart context

The logged `release` → `engineRamp`/`observed_clear` intervals number 8 and 26, lasting respectively 0.0608–0.1778 s and 0.0582–1.0366 s. At every observed-clear boundary, the causal prior received torque is zero and received active/precharge flags are clear; maximum sampled status/torque age is 14.19 ms and 23.24 ms respectively. These are observed log boundaries, not exact ECU-consumed clearance proof or direct pressure measurements. See [release audit](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Session01's assisted no-accelerator RPM peak is **3,340 RPM at +53.564 s, 17.63 mph**, received actual/target gear both 1. Received brake torque and outgoing brake/precharge bits are zero; wire propulsion is +0.56 m/s², planner target +0.4751, integral +0.08972. This does not show braking against acceleration at the RPM peak. Session02 has no qualified assisted sample at or above 3,000 RPM. The mismatch, pedal disables, short reengagements, and start/stop demand episodes remain separate cohorts.

## Verification

Acquisition and durable archive hashes passed; exact sequence joins and clock differences were asserted by the offline verifier. All 14 startup entries match clean installed source; recorded nonzero control metadata versions are V1. Analysis scripts process saved recordings only. No physical fix, road comfort improvement, installation, or safety certification is claimed.

Evidence: [acquisition](../../navigator-reference/PRIVATE_ARTIFACTS.md), [input hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md), [stream extraction](../../navigator-reference/PRIVATE_ARTIFACTS.md), [causal analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md), [CAN joins and Panda order](../../navigator-reference/PRIVATE_ARTIFACTS.md), [pulse audit](../../navigator-reference/PRIVATE_ARTIFACTS.md), [release audit](../../navigator-reference/PRIVATE_ARTIFACTS.md), [verification](PUBLIC_VERIFICATION.json).
