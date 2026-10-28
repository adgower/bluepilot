<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest Navigator drives — October 16, 2026 afternoon review

The low-speed issue remains observable. Unlike the preceding batch, these recordings include engaged low-speed steering. The installed tracking addition is almost entirely inactive, and the latest wait/catch-up revision produces exactly the same reconstructed outputs as the previous budgeted strategy on these inputs. This is not evidence that the issue is fixed or that the new revision improved road handling.

## Coverage and provenance

Downloaded all four new retained sessions after the previous review: 63 segments, 542,731,430 bytes, independently SHA256-verified against device files. Raw recordings, original route mapping and identities remain in `${USER_HOME}/CommaBackups/<private timestamp identifier>-newest-drives`. Public-facing labels are local to this report; drive-01 here is not drive-01 in the preceding report.

| Session | October 16 start, CDT | Segments | Duration | Active lateral-control time |
| --- | --- | ---: | ---: | ---: |
| drive-01 | <private clock time> | 16 | 947.5 s | 540.6 s |
| drive-02 | <private clock time> | 14 | 805.0 s | 473.2 s |
| drive-03 | <private clock time> | 1 | 38.4 s | None; stationary |
| drive-04 | <private clock time> | 32 | 1,889.2 s | 1,170.6 s |

Total active lateral control is approximately 36.4 minutes (100 Hz control samples). Active 5–25 mph angle requests without driver steering comprise 552 samples, approximately 27.6 s at 20 Hz; 112 samples/5.6 s are at 13–17 mph. Only 36 samples/1.8 s in that band meet the stricter clean meaningful-demand mask; six samples/0.3 s meet the stable subset. Adjacent samples are correlated and these are not independent trials.

All sessions identify parent9da98d0c91f0559efa976e3ffb221f2584fd0b88 and the existing tracking branch. Live source inspection confirms clean parent9da98d0c9/child18175406 at completion, offroad. Logged dirty metadata is not the live Git status. Existing 1.20/0.97 source calibration and installed Navigator configuration remain intact; all four startup records have pinion/low-speed/persistent-tracking preferences and update pause enabled, Alpha longitudinal off. The final session has ExperimentalMode preference1, which alone does not establish openpilot longitudinal operation. It has stale July init wall time; later clocks yield October16 start, and their sampled offset span is8.1ms. Analysis uses the stable clocks, not that stale init timestamp.

## Where requested turning was not achieved

Clean observations require active valid control, fresh aligned state/control/body-motion/model/vehicle parameters, no driver steering input or recent override, no blinkers/lane change, valid dynamics and no steering faults. Meaningful demand is absolute requested curvature above0.001/m. Body response is calibrated body yaw divided by speed; pinion response is a fixed-parameter wheel-angle-derived curvature proxy, not a second independent ground-truth measurement. Same-time ratios include dynamics/lag and calibration effects.

| Local time, CDT | Approx. speed | Clean weak window | Median body/request | Median pinion/request |
| --- | ---: | ---: | ---: | ---: |
| <private clock time> | 13.7 mph | 0.55 s | 50% | 34% |
| <private clock time> | 11.2 mph | 0.60 s | 18% | 48% |
| <private clock time> | 21.2 mph | 1.15 s | 48% | 96% |
| <private clock time> | 19.5 mph | 1.50 s | 57% | 87% |

These windows have body/request below70% throughout. The first13–17mph band as a whole has median body/request47% and pinion/request36%, but only1.8s of clean demand; that is too little and too unmatched to claim an improvement percentage. Median absolute lateral-acceleration discrepancy there is0.026m/s². At19.5mph it is0.084m/s². A large relative percentage at small demand is not equivalent to a large physical lane departure.

Existing continuously-clean13–17mph lag analysis still has body ratios around49% at0.25–0.5s, with fewer samples remaining; lag alone is not a demonstrated explanation. Conversely the19–21mph windows involve demand/speed changes and the wheel/body disagreement, so a same-time ratio cannot uniquely separate delay, calibration, vehicle-model mismatch and true insufficient steering. No matched before/after road/demand comparison has been established.

## Did the correction operate?

Actual-send-time reconstruction finds only three added-correction samples (about0.15s) in drive-01, all in the13–17mph band; peak pre-limiter addition is0.000791rad. No wire-level residual exceeds the prior analysis's conservative0.0015rad visibility threshold. This does not prove zero smaller physical effect. Reconstruction matches recorded commands to roughly0.00024rad at the95th percentile, within the0.0005rad wire quantization scale; it is not internal telemetry.

Around elapsed86–90s in drive-01:80 active/no-driver samples, three additions,33 waiting decisions and one catch-up veto. Around105–110s:100 samples, zero additions,30 waiting decisions and seven catch-up vetoes. Most other samples fail other admission conditions and are labeled none. Thus the14mph weak response persists while the eligibility/persistence logic permits little extra output; simply describing the option as enabled is misleading.

Around elapsed298–304s in drive-02:120 active/no-driver samples, context valid throughout, zero additions,18 waiting decisions and72 catch-up vetoes. The correction uses pinion-derived feedback; its70% deficit threshold and projected-recovery veto cannot identify the full body-yaw deficit when the pinion proxy is already near target. The veto label alone is not proof of a bug.

No rising-budget exhaustion or rearm explains the gap: drive-01 spends at most0.00008736rad·s, below0.00025; drive-02 spends zero. There is zero new-versus-previous reconstructed output difference across all four sessions, including unchanged outputs above25mph. Enlarging the budget is unsupported by this evidence.

## Higher speeds

Clean40–50mph meaningful-demand exposure is24.35s combined, with median body/request about1.11 in drive-01,1.21 in drive-02 and0.98 in the much shorter drive-04 subset. At50–70mph the three moving sessions have median body/request about1.115–1.117, with no clean weak episode lasting at least0.5s. These descriptive ratios do not prove perfect tracking, causal preservation of earlier45mph behavior or persistent overshoot. Requests are small, roads/dynamics differ, and driver-intervention context is not a lane-error label. There is no evidence here to justify changing the owner's higher-speed calibration.

## Rejected messages and health

Actual returned/rejected CAN echoes identify two active-mode0x3d6 packets: drive-01 elapsed677.598s near61mph, drive-02 elapsed314.641s near43mph. Both align with brake activation and cruise disengagement; Panda permission changes from allowed to disallowed across the sampled interval. Neither coincides with the selected low-speed deficit windows.

Separate exact-recorded-TX native safety replay reproduces both active steering rejections with controls already disallowed, valid receive checks and identical payloads. Drive-01:62,923 configuredTX, seven rejected (one steering, six cancel); drive-<private clock time>,561TX, five rejected (one steering, four cancel); combined6,945,489 physicalRX, zeroRX-invalid. The actual moving configured counters/echoes show26 rejects across the three moving sessions:24 cancel and two steering. Host replay is not a complete reproduction of transport/forwarding/hardware timing and reproduces fewer cancel rejects than actual echoes. Startup/shutdown noOutput/inactive echoes are separate. Existing safety rejection protects the permission boundary; app-side send/cancel timing merits a separate local robustness task, not weakening Panda permission checks.

No sampled permanent steering faults, Panda faults, heartbeat loss, RX-invalid or reported model drops; big-model inference stays selected. Temporary steering flags never coincide with active lateral control. One Chestnut supply-fault sample occurs0.158s into the stationary drive-03 startup; none occur in the three moving sessions. These samples do not establish long-term reliability.

## What to work on next

1. Use the10:56:16 and12:40:04–07fixtures for local diagnosis. Trace the exact failed persistence/admission conditions in the former; quantify wheel/body calibration, learned offset/ratio, raw feedback and time alignment in the latter before choosing a feedback or gain change. The pinion option is operational, but the underlying yaw/response discrepancy is unresolved.
2. Add direct request/feedback/admission/correction/budget telemetry in a separately reviewed local candidate so subsequent reconstruction does not substitute for actual controller state. Keep fresh-data, override, abort/unwind, speed fade and native safety guards.
3. Independently investigate brake/cruise-edge send and redundant cancel timing; preserve native safety limits. These are not the observed15mph cause.
4. Keep1.20/0.97 and the≥25mph path unchanged. No deployment, gain change or additional installation is justified by this report alone.

No device writes, restarts, ECU queries, firmware actions or settings changes occurred. Only raw-log reads and source inventory were performed over SSH. No new controller was implemented, so the two targeted recorded-message diagnostic replays are not represented as a fresh full candidate safety/build validation.

## Evidence

[Analysis and eligibility results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [controller reconstruction](../../navigator-reference/PRIVATE_ARTIFACTS.md), [actual rejected echoes](../../navigator-reference/PRIVATE_ARTIFACTS.md), [active rejection context](../../navigator-reference/PRIVATE_ARTIFACTS.md), [drive-01 recorded replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [drive-02 recorded replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [verified coverage and checks](../../navigator-reference/PRIVATE_ARTIFACTS.md), [anonymized input hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md). Scripts and compressed derived arrays are retained alongside this report; raw identity/GPS-bearing signals remain private.
