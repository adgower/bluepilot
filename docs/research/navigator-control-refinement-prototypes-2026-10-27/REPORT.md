<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local control-refinement investigation — October 27, 2026

User scope: investigate pulsing, high-RPM rolling restart and40–50 mph excess turning; prototype locally and run full saved replays. No integration, publication, SSH access, device changes, settings changes or CAN transmission occurred. Paired source remains df788e027 /1d29e6e7 with1.20/0.97 preserved.

## Longitudinal pulsing: candidate rejected

A unified bounded true-coast/phase-consistent integral prototype completed237 segments / 14 routes / 685,504 controller callbacks, including the latest21-segment drive. It worsens the city fixture17→27 brake changes, produces1,620 weaker encoded strong-target samples and a new simulated release-timeout near55 mph on the latest route. The later68mph and restart windows lose activity after that fault; their zero switching cannot be credited as smoothness.

Native replay completes237segments,685,398 replacement ACC slots with zeroaddedTXrejections/relayfaults. That native acceptance does not override failed controller-history gates.26 focused/budget/protocol tests pass; recorded-feedback producer reproduction matches all 107,945 newest-route producer steps within 1e-5. Coupled consumer reconstruction has disclosed receive-drain uncertainty and is not bit-exact installed-road reproduction. One12-segment historical input-prefix route remains diagnostic-only.

The observed mechanism is history-dependent: broader engineRampIholding changes raw/net demand and nominal brake-release timing, even before the first true-coast intervention. True coast plus limited feedback can then reinforce the hold and exhaust the finite allowance. More coasting cannot be selected from switch counts alone. [Detailed report and failed gates](../navigator-pulse-authority-prototype-2026-10-27/REPORT.md).

## High RPM: protocol hypothesis explored, no runtime policy selected

The received second-gear target appears at18.885 mph, then actual second2.381 s later;3,946 RPM lies between. SavedOEM examples target second near8.75–9.13 mph despite larger acceleration commands. This contradicts a simple universal acceleration-cap explanation but does not identify TCMinternal causality. StoredIatRPMpeak is only~.081 versus planner~.770m/s².

A shadow-only target-speed packet helper and18 paired syntheticnative unit cases demonstrate field isolation, not correct OEMsemantics or shifting improvement. Literal cruise-setpoint copying fails the prior OEMsemantic comparison. Five exact-observation diagnosis tests pass. There is no installable restart fix from this experiment; no gearcommand or unsupportedCANsemantics selected. [Restart evidence and shadow experiment](../navigator-restart-response-prototype-2026-10-27/REPORT.md).

## 40–50 mph steering: bounded mapping candidate with performance limits

Wheel-model and calibrated body response both indicate excess turning; current roll-aware mapping is zero below50mph. The isolated candidate extends that existing bounded target mapping over35–55 mph and retains the exact installed ObserverContinuity policy, inherited freshness/override/slew/authority guards and owner1.20/.97.106 targeted checks pass, including14 independent full-controller55–85 mph packet-parity cases.

The full saved replay completed all 637 historical segments plus 21 new segments: 33 routes / 658 segments, with zero added native safety rejections in both recorded-context and separately labelled causal-calibration-fixture comparisons. Even a clean native replay cannot prove physical correction, lane keeping or85mph stability. In one42 mph window the roll-derived target difference is only2.3% versus~29% observedbodyexcess, so this mapping extension cannot be claimed to resolve every episode. [Steering investigation and current full replay status](../navigator-midrange-mapping-prototype-2026-10-27/REPORT.md).

## Decision boundary

Do not install the longitudinal candidate. No new RPM cap, cruise-target policy, timeout suppression, weaker braking, Ireset or enlarged decision allowance is authorized by these results. Steering is a separate bounded experiment with full saved-corpus completion; hardware and road response remain unproved. The installed Comma has not been accessed or changed during this local work.


### Final steering command audit

On the latest recorded-context replay, requested path-angle magnitude is about 2% lower in the 42 mph episode and 7% lower near the 50 mph intervention. This is changed command evidence, not a predicted reduction in body yaw. Owner factors remain unchanged. All observed changed path-angle slots are between roughly 35 and 53 mph; 55–85 mph comparison packets and default-off behavior remain identical in the tested histories.

A directional screening flag remains: 16 eligible 40–50 mph slots reduce command while recorded body response is below 80% of request, and two increase command while recorded body response is above 120%. These are rising/transition samples, with wheel/body disagreement and possible response lag, rather than demonstrated steady-state regressions. They still require explanation before selecting a production policy. The extension does not explain all excess at 42 mph, where the target correction is much smaller than the observed response excess.

**No candidate is installed or represented as a complete physical fix.** The longitudinal candidate fails the controller gates. The steering candidate clears the saved native comparisons but remains a diagnostic prototype with transition and efficacy limitations. The high-RPM work provides reproducible timing and protocol hypotheses, not a new runtime tune. Full details and receipts are linked above.
