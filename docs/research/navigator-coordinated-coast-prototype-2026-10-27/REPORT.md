<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordinated coast/brake selection — October 27 UTC, 2026

**The final local prototype resolves the previous weaker-strong-braking and extra full-brake-exposure replay regressions. Its smoothing benefit is modest, and physical highway pulsing is not proven resolved.** Paired branches and the Comma remain unchanged.

## What changed

The rejected independent coast-admission override is removed. The candidate uses the installed allocator's existing truthful bounded-precharge mode and its signed-braking integral role. Both full-brake and precharge requests withdraw propulsion, retain the received-torque clearance barrier and use identical native integral behavior. There is no integral repayment, copied reference I, baseline-output oracle, PID reset or fabricated actuator feedback.

The allocation allowance now has a coherent sampled-demand account:

- Earlier negative-net coast/admission deferral and prospective weak precharge both charge the existing account. Starting the clock only after nominal brake arrival was rejected because it ignored the earlier deferral.
- Existing debt is retained, but negative demand while selecting full-brake requests is not added as new weak-deferral debt. Counting those full-brake requests as omissions prevented recovery and added braking exposure in the intermediate design.
- Positive net demand can repay the account. Rearming requires it to be exactly zero, plus **100 ms** of continuous eligible, measured-clear, nominal-brake-off, positive raw/net/target qualification. The old 500 ms rule could clear an unpaid account. Overrides and invalid input do not forgive spent allowance.
- The existing **0.01 sampled demand-area allowance /0.3-second trial deadline** and strong-demand fallback remain. Trial start still includes earlier negative-net deferral, rather than granting a second clock. Budget and age feedback remain truthful under the existing protocol.

`area` is a sampled signed-demand guard, **not an exact delivered-command integral, measured brake deficit or physical speed-error bound**. It uses current demand/prospective mode over the preceding dt, and commands persist until the next consumer delivery. Selecting a full-brake request also does not prove that the vehicle delivered the requested braking.

Final code: [coordinator3.py](../../navigator-reference/PRIVATE_ARTIFACTS.md). Earlier/intermediate files remain clearly superseded research, not installation candidates.

## Why the integral regression is gone

The earlier true-coast variant changed when propulsion returned. The candidate request could reach the engine ramp sooner, unfreeze positive I growth earlier, then weaken later braking.

The final design instead retains the installed signed-braking role for bounded precharge. **Every one of 1,203,463 recomputed producer steps has identical raw demand, I, freeze decision, PID phase and rolling-recovery reduction to the installed reference.** The previously failing exact producer crossover is preserved in the audit and now has no difference. All625,238 consumer callbacks also retain identical raw demand, I, gas and combined brake/precharge request.

Only702 reconstructed ACC packets change. Each changes only the full-brake deceleration-request bit from1 to0 while precharge stays requested. Acceleration fields, propulsion request and all other packet bits are unchanged. Strong-target packets are not weakened.

[Every-producer audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Changed-packet audit](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Full controller replay

All **216 segments /13 routes /625,238 callbacks** processed: the prior197-segment corpus plus the latest19-segment moving drive. One older12-segment route has five missing active prefix inputs and remains diagnostic-only. The204segments with complete active atomic inputs clear the declared comparison gates.

| Complete-input route check | Result |
|---|---:|
| Raw/I/gas differences | **0 /0 /0** |
| Weaker raw strong-target requests | **0** |
| Weaker encoded strong-target requests | **0 /35,375 checked** |
| Extra full-brake samples | **0** |
| Full-brake changes | **1,655→1,637** |
| Full-brake command exposure | **2,783.745→2,769.615 seconds (-14.130)** |
| Combined brake/precharge exposure | **unchanged, 2,845.254 seconds** |
| Added fault sequences /lost or gained active callbacks | **0 /0** |
| Gas under commanded brake/precharge or retained received torque | **0** |
| Disabled-owner wire changes | **0** |

Including the diagnostic-only route, full-brake changes are1,664→1,646; the18-change and14.130-second reductions are the same. Two preexisting reference release-timeout sequences remain unchanged, including one in the diagnostic-only route. No new timeout is introduced; this is not a claim that every historical controls-mismatch cause is resolved.

### Named road regressions

| Window | Full-brake changes, reference→candidate | Full-brake exposure, seconds |
|---|---:|---:|
| New58–62mph /15s |14→14|7.703→7.325|
| New62–64mph /15s |12→12|4.500→4.159|
| New~74mph /15s |10→10|3.564→3.564|
| Earlier city~25mph |17→17|21.533→21.448|
| Earlier63mph /15s |20→20|9.914→9.914|
| Earlier highway response window1 /20s |22→20|14.325→14.060|
| Earlier highway response window2 /20s |12→12|12.340→12.340|

Named high-RPM rolling-restart and normal stopped-launch windows retain their brake counts/exposure, and all raw requests and integral history remain identical. Actual RPM and shifting are frozen; this is preservation evidence, not a prediction of further RPM improvement.

[Full comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Source/input receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## What this does and does not improve

The previous +51-second full-brake-exposure penalty and2,071 weaker encoded strong-target samples are absent. Some brief weak full-brake requests become bounded precharge. That is a limited command-level improvement.

**The final three new highway windows still have14/12/10 full-brake changes.** Gas withdrawal and combined brake/precharge timing remain unchanged. This does not remove the underlying propulsion-withdrawal cycling or establish smooth physical coasting, reduced nausea, fuel savings, following performance or a cure across0–85mph. The earlier isolated12→10 and10→8 results belonged to the rejected early-start variant and must not be advertised for this final candidate.

The next larger improvement needs response evidence for true coast versus precharge and a delivered-authority model that preserves braking and recovery. Do not enlarge the allowance or substitute favorable packet counts for physical evidence.

## Rejected intermediate variants

- `prototype.py` /`coordinated`: producer/exposure comparisons improved, but it started the clock only after nominal brake arrival and ignored earlier legacy deferral. Rejected on accounting grounds.
- `coordinator.py` /`coordinated2`: kept the earlier start and required zero debt, but charged full-brake demand as unserved weak demand. Full replay added1,127 full-brake samples /15.512 seconds exposure despite identical I. Rejected; its focused strong-braking debt test is retained red.
- `coordinator3.py` /`coordinated3`: final reviewed candidate described above.

## Tests, review and scope

18focused tests pass, including real LongControl braking/precharge/release/ramp equivalence, debt retention, strong braking, measured clearance, overrides, clock gaps and20,000 seeded allocator transitions. The202installed longitudinal contract tests and20subtests also pass using an explicit local unsanitized native test build; macOS denies this runtime loading the normal UBSan library. No sanitizer proof is claimed.

An isolated read-only reviewer found no blocking issue and independently passed the then-current15-test suite. Three further debt-retention tests were added afterward. [Review and accounting caveat](REVIEW.md).

The installed source pair remains clean at openpilot`1dbbc01892616c4b1a5c7c841d132f724ea5132c` /opendbc`beb10c25770471534261606072c131db5eefa117`. Steering1.20/0.97 is unchanged. No SSH, device install/staging, settings change, CAN transmission, reboot, branch integration, publication or OS/firmware action occurred. This is a local prototype, not hardware or road acceptance.

## Final native replay and verification

Fresh final-candidate native replay completed all **216 segments /13 routes /625,140 replacement ACC slots** with original received CAN, original non-ACC sends and timers retained. It added **zero TX rejections and zero relay faults**, with no forced permission. The141 preexisting TX rejections remain equal on both sides; both sides process50,044,658 RX packets with zero RX rejections. Binary/header/source/input hashes and clean paired source state were verified.

The final verification checks every producer step and every changed packet, source/manifest bindings, declared performance gates, native receipts,18focused tests and202installed contract tests plus20subtests. The earlier first-crossover case no longer diverges. Road comfort, actual grade, brake torque under the new commands, RPM and fuel consumption are still unproved because physical response is frozen in replay.

Final status: **local prototype clears the saved replay gates; not integrated, installed or road-validated.** The main highway gas-withdrawal cycling remains a separate unresolved comfort problem.

[Final verification](PUBLIC_VERIFICATION.json) · [Final native summary](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Final native source provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md)
