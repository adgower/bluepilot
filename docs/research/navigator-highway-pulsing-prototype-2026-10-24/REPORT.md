<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# New-drive review and bounded-coast prototype — October 24, 2026

The restart improvement has supporting evidence, but Alpha still has highway cycling and three recorded coordination faults. A report-local bounded-coast prototype reduces command cycling in the new recordings without adding replay faults or sacrificing healthy coverage. It is **not ready to install**: existing faults and substantial residual cycling remain, and replay does not establish physical braking or comfort. No device settings/source/service/firmware/OS changes, active ECU queries, CAN transmission, paired edits or pushes were made. **1.20/0.97 retained.**

## Acquisition and evidence limits

All 38 newly available completed segments from two sessions were downloaded and SHA-256 verified: 341,834,841 bytes. Remote logs were rechecked, with installed source/settings/protected files/service unchanged during acquisition. Both sessions identify current parent `49be383b2` / child `d459133a`. The final read-only audit confirms unchanged selected settings, clean installed sources and protected steering/firmware hashes.

Session01 has only segments13–24 available; initial segments are absent from this acquisition. It cannot establish all initial launch behavior. Session02 has segments0–25. Embedded init messages precede the first available segment; do not count that header-to-data gap as continuous driving. Recorded carControl active coverage is about30.9minutes, maximum actual speed73.79mph. There is **no new75–85mph evidence**.

The actual production-controller reconstruction processes111,457 callbacks. Four checked feedback fields are brake/gas/fault/reason, not complete-byte identity. Session01 has587 mismatches, all within its first24.22seconds after reconstruction starts mid-drive; its first60seconds are excluded from improvement comparisons. Session02 has four mismatches out of75,706callbacks. One unmatched-request callback is excluded. Reconstruction uses latest-published carState/decoded torque, latActive disabled, vEgoRaw=vEgo, flags15 and synthetic frame=slot*2. It is not exact consumed-state reconstruction or a physical vehicle simulation.

## Restarts and takeovers

Seven selected active/no-pedal, positive-propulsion, clear-torque crossings through3m/s (6.7mph) retain a positive sent request. None has the earlier boundary dropout. This supports the reported smoother continuation after launch; it does not measure reaction to a green light or prove every restart is good. Do not raise launch acceleration simply to compensate for the remaining release faults.

All11 longitudinal active-to-inactive transitions in the extracted streams were screened: three align with coordination faults; eight have driver pedal input at the transition, some also steering. These input flags cannot establish the driver's intent or that a maneuver was unplanned. Details and context are in analysis.json.

## Three Controls Mismatch episodes

| Local time | Speed | Recorded/reproduced cause | Evidence |
|---|---:|---|---|
|<private clock time>|24.8mph|release_timeout_disengage|Reported torque156Nm at fault; pose age49.9ms|
|<private clock time>|62.0mph|invalid_pose_or_accel|Consumed pose100.120004ms old; finite acceleration/pitch and valid control request|
|<private clock time>|20.5mph|release_timeout_disengage|Reported torque236Nm at fault; pose age35.1ms|

The two release faults are not caused by stale pose at the fault. The measured-clearance observer still has non-clear reported torque and correctly reaches its existing deadline under its current contract. This channel is ECU-reported torque, not independently measured hydraulic pressure; no threshold increase or bypass is justified.

The62mph event is specifically a producer/consumer freshness race, not nonfinite acceleration: the consumed epoch/sequence was valid, requested acceleration+0.214m/s², poseValid=true, producer age5.22ms, but source pose age100.120004ms at consumption. A newer deviceMotion publication arrived3.346ms before the callback, **0.133ms after the consumed control message publication**. The following control message has fresh pose but arrives after the fault. Freshness at producer time does not guarantee freshness at consumer time. Preserve the100ms consumer bound; next work should address scheduling/coherent snapshot refresh rather than merely raising the limit or relabeling stale data.

## Highway cycling and local prototype

The new recordings reproduce highway cycling, including26brake-command edges in20seconds near70.8mph. A 20Hz context screen counts fewer edges than the full callback replay; full-rate counts are used below. These are command edges, not independently verified physical brake applications.

`coast.py` replaces only the in-memory production controller's BrakeAdmission constructor through experiment.py. Production files remain unchanged. It changes weak new entries only when raw acceleration>+0.02m/s², net residual>-0.05m/s², fresh valid torque is currently<=4Nm, the existing release obligation is clear, pose/reference/CAN are eligible, moving PID is active and callback interval<=40ms. Existing measured observer still runs. Actual braking, non-clear feedback, meaningful negative demand, stop/creep, invalid context and timing retain baseline admission. No global pose/calibration filter, acceleration-gain increase or clearance/deadline change is applied.

Instead of withdrawing propulsion for each weak-entry qualification, it permits the already clear handoff to continue. Signed residual demand accumulates toward an **experimental0.01m/s admission threshold**; positive residual pays that debt down. A continuous-negative decision deadline is **0.3seconds from its first observed negative sample**. These are sampled decision bounds: the debt can overshoot by less than one0.002m/s increment at the allowed40ms interval, and deadline admission can occur one callback late. Neither is a guaranteed physical speed-error/braking-delay bound. The candidate needs physical/closed-loop onset evidence; the numbers are not approved production tuning.

Initial tests failed on the baseline (3failed/14passed), then the bounded-coast contracts passed. Actual-controller constant-demand/pitch-oscillation reproducer goes from repeated braking/withdrawal to zero edges/withdrawal with the candidate. Meaningful deceleration, stop/creep/inactive packets and non-clear-torque fault contracts are retained. The final suite has23passing contracts, including irregular sampled-bound tests.

### New recordings, joint-healthy active samples

| Measure | Current reconstruction | Prototype |
|---|---:|---:|
|60mph through observed maximum: brake edges|348|246|
|First drive worst selected highway20s near70.6mph|20|16|
|Second drive worst selected highway20s near70.8mph|26|12|
|Second window inactive-propulsion fraction|37.8%|20.6%|
|Existing fault episodes|3|same3, same reproduced times|

The aggregate edge reduction is29.3%, **not29.3%better comfort or fuel economy**. First-drive warmup is excluded. Healthy coverage is identical per variant. No output changes occur in the new samples classified raw<=0.02 or net<=-0.05. The candidate still cycles; these results do not resolve the full complaint.

Two older Alpha sessions add136,308callbacks, for247,765callbacks across four moving sessions. The retained59.7mph worst window goes39→23edges; both older release timeouts remain. Twelve older slots differ when raw<=0.02, all with **positive net** residual and history-dependent prior-brake state; they are not new meaningful-negative-braking onset suppression. Five retain small valid propulsion requests and seven remain inactive. Preserve these as integration-review cases rather than claim exact outside-scope parity.

OEM saved protocol/state comparisons remain a historical reference. OEM does not log this Alpha planner, so no equivalent OEM candidate-response/comfort claim is made. No new closed-loop parent/vehicle-response run is claimed; frozen recorded torque/vehicle response can differ from what changed commands would produce.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Lateral straight-proxy oscillation

12-second screening requires active lateral, valid context/CAN, no driver steering/pedals/blinkers, lane-change off, lane confidence>0.5,60–85mph and requested curvature magnitude<0.00015m⁻¹. It identifies194overlapping low-curvature windows (75/119 by session), with no qualifying data above75mph. This is **not verified straight-road geometry or lane-position ground truth**.

Selected windows around69–73mph show repeated requested wheel-target oscillation and larger measured wheel motion. Example14:42:45 near72.6mph: measured95–5percentile span2.39°, requested span1.16°, offset-corrected error span1.86°; the causal amplitude screen finds14measured versus11requested swings in12seconds. The0.4°/0.2s swing screen is a diagnostic selection rule, not a tuning target. A first-drive example also has strong requested oscillation. Thus neither pure controller hunting nor pure planner noise is established; target, mapping/offset, actual response and concurrent longitudinal cycling must be separated.

Reported steeringRateDeg is zero in these samples; it cannot be used as rate evidence. Rate/swing screening is derived from angle with causal smoothing and explicit amplitude/time thresholds; missing values reset the filter. Tiny derivative sign changes alone are not counted as physical ping-pong cycles. No lateral gain or high-speed tuning changes were made. Next local lateral work: replay saved oscillation episodes through the existing mapping/unwind path, separate requested-path variation from wheel amplification and contemporaneous calibration-offset/roll changes, and retain no-override/no-lane-change constraints. No blanket60–85mph gain reduction is justified, especially without75–85mph coverage.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Verification and remaining blockers

-23focused candidate contracts pass; initial baseline failures retained.
-226existing guard/native Ford tests pass,79skipped,12,028subtests pass. These verify retained guards; they are not a full candidate production integration suite.
-Fresh debug native ACC-hook replay covers8,920,477raw RX packets per variant and111,444reconstructed-clock ACC TX slots. Baseline/candidate share five TX rejections (1+4); **zero added candidate rejections**, zero relay faults, no forced controls permission. Thirteen earlier callback slots precede logged Ford11 eligibility. This exercises **ACC TX only**, with raw buses0–3 and timers; excludes lateral TX, forwarding, heartbeat injection, actual actuation and changed vehicle response.
-Independent read-only review found no blocker to retaining the research prototype, and specifically required sampled-bound wording and installation limitations. Final device read-only audit passed; no selected setting changes.

Remaining before any integration/installation: resolve release-request/feedback ownership semantics while retaining clearance/deadline protection; fix coherent pose freshness scheduling without accepting stale pose; reduce residual cycling with explicit actual braking-onset and coverage checks; parent/vehicle-response and full controller integration/transition/abort/default-off/safety/build validation. Current prototype has no new ARM, powered parked or physical road acceptance.

Evidence: acquisition-provenance.json, input-manifest.json, extraction.json, analysis.json, fault-inputs.json, pose-fault-probe.json, replay-comparison.json, old-replay-comparison.json, native-results.json, contracts.log, guard-tests.xml, lateral-screen.json and final-device-audit.json. Raw route identities/GNSS remain private.
