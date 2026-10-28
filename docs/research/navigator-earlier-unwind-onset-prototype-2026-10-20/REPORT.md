<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Earlier bounded unwind onset — local prototype

October20,2026. **Full controller/native replay accepted locally.** Report-local only, not paired-integrated or installed. No device access.1.20/0.97 and native limits preserved.

## Change

Candidate subclasses the installed CalibratedMidUnwind without editing the paired source. During60–70mph withdrawal only, it credits the existing five-update persistence after independent input histories have already confirmed the evidence. Current inherited wheel/body agreement, atomic target/context validation,0.5° wheel deadband, body margin, predictive wheel release and all native bounds remain mandatory.

Credit requires five strictly increasing now/state/control/motion stamps, each spanning160–300ms across the window; valid CAN and lower observer evidence; a current validated wheel target; at least five fresh body-history observations spanning160–300ms; positive inherited fraction with confirmed predicted wheel excess; no pending release; and demand withdrawn at least2% from the five-sample peak without rising on the current update. Invalid/duplicate/timing/generation breaks prevent borrowing old credit. Magnitude, onset slew and release rules are inherited: at most15% /0.01rad high-speed reduction and0.0003rad per20Hz update onset. No minimum quantization-step push is added.

No credit at/below60mph or at/above70mph. Protected lower-speed and>=75mph behavior is subject to whole-stream replay checks, not assumed from constants.

## Saved-road command evidence

Original-send replay keeps actual measured motion fixed. In the exact-parity session05 reference:

| Episode | Installed first encoded reduction | Candidate first encoded reduction | Earlier |
| --- | ---: | ---: | ---: |
|~69mph, recording seconds351–352|351.635462s|351.534600s|0.101s|
|~67mph, recording seconds411–412|411.485156s|411.236201s|0.249s|

The quoted67mph command is now about0.100s after the first body excess margin crossing, versus0.349s previously. This is command timing on recorded inputs, not a measured vehicle delay or physical tracking prediction.

Across the two saved moving sessions,99/76 packed requests differ, with maximum absolute encoded difference0.0015rad.98/72 have additional reduction;1/4 have less reduction than installed during release/reconfirmation. Those small opposite differences are explicitly retained: earlier admission arms the inherited bend lifecycle sooner, and prediction still withdraws correction while wheel error closes. They are not a claim that extra steering or physical overshoot improved. The28mph32-update clipped window is unchanged. Session04's reference wire parity is5705/5742 active/unpressed updates, with quoted28mph window exact; session05 reference is exact on all3340. No mechanism claim is made for unmatched reference updates.

## Verification

- Red before implementation: six earlier-onset cases failed,23 guards/protected cases passed.
- Corrected candidate:60 focused tests pass. Review-recovery regressions first failed as expected, then pass.
-714 transition cases /228,480frames pass range, slew, exposure and settling checks.
-128 abort cases pass; maximum additional neutral command tail0.0s relative to installed policy in these cases. This is not physical yaw settling time.
- Independent second review reports no further material findings.
- Full **53-recording /819-segment** generated-controller/native comparison passed: **4,735,309 controller updates per compared variant**, zero additional native rejections. The766-segment corpus is extended with18 previously reviewed segments and all35 latest segments. Four independent native streams compare recorded-control reference/candidate and separately labelled causal-calibration-fixture reference/candidate. Default-off byte parity covers the whole evaluated recorded-control stream. Enabled reference/candidate comparison covers both calibration contexts. Replayed outputs below60mph, including40–50mph, and at/above75mph remain byte-identical. Original RX/timing, exact rejection identities, source/input hashes and calibration contexts pass the final audit.

An initial replay was interrupted after review found the CAN recovery gap. Its results are not acceptance evidence; the corrected replay restarts all routes with frozen corrected source.

## Scope and next gate

No gain changes, native deviation-limit changes, steering-mode changes, firmware, settings, paired commits or Comma changes. This prototype does not fix the28mph authority/model issue. Full replay, comparison audits and source preservation passed. Paired integration/build checks and separately authorized hardware/road validation are still outstanding. Offline changes cannot prove improved lane tracking, actuator response or reduced takeovers.

## Full replay totals and limits

188,238,622 configured physical RX frames are supplied to each independent native stream. The compiled native library exactly matches the prior accepted library; safety headers are unchanged since that accepted pair. This task reruns the corpus, not a new native-library build. Legacy recordings use the paired pinion flag while retaining their other safety bits. Current forced-Expedition/Navigator steering configuration is exercised; this is not validation of every longitudinal mode or vehicle variant.

| Native stream | Generated TX | Accepted | Rejected | Before Ford configuration |
| --- | ---: | ---: | ---: | ---: |
| recorded_reference | 3,068,406 | 3,048,834 | 2 | 19,570 |
| recorded_candidate | 3,068,406 | 3,048,834 | 2 | 19,570 |
| fixture_reference | 3,068,406 | 3,048,834 | 2 | 19,570 |
| fixture_candidate | 3,068,406 | 3,048,834 | 2 | 19,570 |

Rejection lists match exactly in each reference/candidate context; there is no controls-permission override. Shared rejections are retained, not counted as newly introduced. Details are in acceptance.json.

Recorded calibration: 2,051 generated updates differ from installed. Causal fixture: 4,129. These are command differences, not improved vehicle-motion percentages. Original-send episode counts above use a different timing seam and must not be mixed with generated-controller counts.

A separate stored-output envelope audit passes on 266,934 active/unpressed60–70mph frames across both contexts, with peak floating residual 0.004649rad, preserving the0.01rad absolute and15% relative reduction envelope (relative reconstruction includes explicit half-wire-step uncertainty). Shadow intent remains identical in14,000 synthetic updates. Of128 abort cases,32 have the new additional correction active before interruption. These checks do not prove wire delivery, receiver acceptance or physical steering recovery.
