<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# First post-roll-mapping drive: all-speed and intervention review

## Findings

**Follow-up correction:** the user-reported no-signal inside-bend event near83mph was excluded by this review's curvature floor. A [subsequent local investigation](../navigator-entry-highspeed-investigation-2026-10-17/REPORT.md) finds substantial excess response and estimated inward movement there. Stronger-turn improvements below65mph do not establish satisfactory gentle/high-speed behavior.

**50–65mph tracking looks better in this first drive; the clearest remaining intervention is a rising-demand turn around29mph.** One post-install session,25segments/219,415,234bytes, was downloaded and hash-verified. Recorded session runs October17,<private clock time>–<private clock time>:36CDT, with a maximum recorded83.997mph. Session duration includes parked time. The raw inventory recheck exactly matches the downloaded inventory. Comma source/settings/services were not changed; no ECU queries or CAN transmission by the analysis tools.

The session records clean parent99645f222, all trial options enabled and alpha longitudinal off. Current source is clean at published parent99645f222/child8cbc834fe; owner1.20/0.97, protected geometry/launchers/signed firmware and settings match the prior installation. Private raw/GPS-bearing data is retained at `${USER_HOME}/CommaBackups/<private timestamp identifier>-post-roll-drive-analysis`.

### Highway comparison

Steady-request50–70body response is **103.0% of request**, versus **112.1%** in18 saved baseline sessions at the immediately preceding source revision. New qualifying exposure55.8s versus baseline162.2s; new data includes33.2s positive and22.6s negative requests. Most useful new evidence is50–65mph. This is calibrated body yaw divided by requested curvature×speed, not lane-position error or a calibration factor to invert.

| Band mph | Previous median response | New median response | New steady exposure | Reading |
|---|---:|---:|---:|---|
| 50–55 | 109.7% | 108.9% | 16.45s | Little aggregate change |
| 55–60 | 113.8% | 105.2% | 13.45s | Closer to request |
| 60–65 | 112.2% | 98.2% | 25.70s | Closer to request |
| 65–70 | 111.2% | 94.5% | 0.20s | Too sparse to judge: four20Hz samples |

The broad matched-road screen finds19.85s of new samples with <=25m GPS separation, <=20deg heading difference, <=3mph speed difference and signed curvature within30% of baseline. Median absolute response error10.18%→5.57%; however, it reuses only137 distinct baseline samples. Deduplicating baseline samples leaves **6.85s**, with median absolute error **12.09%→7.20%**, also favorable. This is a small corroborating subset, not an independent causal experiment. Full pooled body medians can shift with route, road bank, demand, wind, traffic and direction. The descriptive spatial-block bootstrap does not solve the one-treated-drive limitation. [Matching details](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Results remain directionally favorable with fixed0/.25/.5s future-response checks and5/10/20% steady-demand tolerances: new response medians102.3–107.8% versus baseline111.1–112.7%. Lag-shifted comparisons are diagnostics, not estimated latency or proof of a particular gain. [Sensitivity](../../navigator-reference/PRIVATE_ARTIFACTS.md).

### The mapping actually affected recorded commands

Actual-send-time reconstruction uses recorded state, context and the actual atomic calibration packets. Every one of17,439non-driver active angle sends agrees with the mapped strategy within half a0.0005rad wire step. Highway:13,629active frames,5,805continuous commands differing from the no-map baseline;4,857also differ after wire quantization. On changed highway frames, median command magnitude is7.46% lower than the baseline. This supports delivery of the intended command adjustment; it is not a direct causal estimate of vehicle response. Mapping falls back on gentle/straight demand, invalid context, driver input or outside its speed range. Recorded40–50active mapped/baseline commands are identical. [Reconstruction](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Every speed range

The same eligibility, meaningful-demand and phase thresholds used before installation are retained. Rows with weak or absent steady turning evidence are explicitly unresolved. No proportional gain adjustment is inferred from a ratio alone.

| mph | Travel s | Active s | Clean meaningful-turn s | Steady-turn s | Steady body/request | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| 0–5 | 429.40 | 0.00 | 0.00 | 0.00 | — | Mostly parked; not steering validation |
| 5–10 | 16.65 | 0.00 | 0.00 | 0.00 | — | Manual; no assisted test |
| 10–15 | 24.80 | 0.00 | 0.00 | 0.00 | — | Manual;15mph issue not tested |
| 15–20 | 20.65 | 0.65 | 0.00 | 0.00 | — | Only0.65s assistance; no usable turns |
| 20–25 | 19.65 | 4.55 | 0.75 | 0.00 | — | Brief changing-demand response gap; no steady evidence |
| 25–30 | 58.95 | 53.50 | 10.90 | 3.05 | 91.7% | Rising-demand shortfalls and sustained driver takeover; inspect transient response |
| 30–35 | 21.75 | 17.25 | 13.15 | 13.05 | 98.4% | Near request in this subset |
| 35–40 | 24.05 | 17.45 | 9.50 | 8.45 | 114.1% | About14% above request; mapping is inactive |
| 40–45 | 28.85 | 24.95 | 22.65 | 14.60 | 114.0% | About14% above request; mapping is inactive |
| 45–50 | 64.40 | 58.50 | 25.80 | 7.60 | 113.0% | About13% above request; mapping is inactive |
| 50–55 | 125.75 | 124.60 | 57.50 | 16.45 | 108.9% | Similar to prior aggregate |
| 55–60 | 189.55 | 188.25 | 62.55 | 13.45 | 105.2% | Closer to request |
| 60–65 | 360.20 | 359.10 | 70.15 | 25.70 | 98.2% | Closer to request |
| 65–70 | 38.50 | 37.00 | 4.70 | 0.20 | 94.5% | Only0.20s steady; inconclusive |
| 70–75 | 13.95 | 13.95 | 0.00 | 0.00 | — | No qualifying turning demand |
| 75–80 | 15.30 | 15.30 | 0.00 | 0.00 | — | No qualifying turning demand |
| 80–85 | 22.95 | 22.95 | 0.00 | 0.00 | — | No qualifying turning demand |
| 85–90 | 0.00 | 0.00 | 0.00 | 0.00 | — | No recorded coverage |
| 90–95 | 0.00 | 0.00 | 0.00 | 0.00 | — | No recorded coverage |
| 95–100 | 0.00 | 0.00 | 0.00 | 0.00 | — | No recorded coverage |

Below20mph the drive does not validate the existing correction because nearly all of it was manual/inactive. At70–85mph there is travel but no qualifying meaningful assisted bend under the unchanged0.001/m threshold; gentle curves may exist below that threshold. Neither means steering is perfect in those bands. No special high-speed collection is requested.

## Interventions and response gaps

**22driver-steering-input episodes began while assistance was active. Eleven coincide with lane-change/blind-spot prompts; the other11 are not thereby proven involuntary takeovers. One additional steering interval begins after a brake disengagement and is listed as post-disengagement handling.** There were four lateral disengagements, all brake-associated. Steering threshold events do not prove why the driver touched the wheel. [Complete CSV](../../navigator-reference/PRIVATE_ARTIFACTS.md), [event source/results](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The standout is **<private clock time>.891CDT,29.4mph**, with `take control / turn exceeds limit`. Driver input continues24.87s. Actual command mode0 while lateral request remains active appears in two intervals totaling20.0s (<private clock time>–<private clock time> and22:33:44.281–<private clock time>), consistent with the retained sustained-human-turn release. This is stronger evidence of a real manual takeover than brief highway touches during lane changes.

Immediately before that input, the clean meaningful2.8s has median68.8% body/request response. The narrower rising-demand window22:33:37.43–<private clock time>.13has about62.6% simultaneous response. Request magnitude rises118%; no steady samples qualify. Comparing the earlier request with body response0.5s later gives roughly108%, before driver input. This illustrates lag during increasing demand, not a measured constant delay or proof that steady gain is37% too low. Over the clean1.95s approach, reconstructed command is not at its soft slew limit; the deviation guard binds only3/39frames. Most path commands are delivered as calculated. Mapping is inactive at this speed. [Incident detail](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Another brief24mph window at22:33:22.23has49.3% simultaneous response while request rises175%; a half-second future comparison exceeds the earlier request. At29mph,<private clock time>, response briefly exceeds130% while request unwinds54% (median156%). These paired rising/unwinding patterns argue against a blanket gain increase. The weak27mph pre-input subset also shows under-response, but clean support is short and intervention-adjacent. There are no sustained eligible<70%/>130% windows of>=0.5s above30mph in this drive under the unchanged scanner; this does not exclude smaller or shorter errors.

### Complete input/disengagement timeline

Times below are October17CDT,24-hour clock. Input events can last multiple seconds; repeated threshold pulses <0.5s apart are merged. Approximate speed is at onset.

| Time | mph | Event | Association / alert |
|---|---:|---|---|
| <private clock time> | 25.0 | Driver steering input | steering-override-associated |
| <private clock time> | 27.2 | Driver steering input | steering-override-associated |
| <private clock time> | 27.5 | Driver steering input | steering-override-associated |
| <private clock time> | 27.8 | Driver steering input | steering-override-associated |
| <private clock time> | 22.9 | Driver steering input | steering-override-associated |
| <private clock time> | 23.5 | Brake disengagement | brake-associated; steering-override-associated |
| <private clock time> | 29.4 | Driver steering input | take control; turn exceeds limit; sustained manual release |
| <private clock time> | 46.6 | Lane-change-associated steering | Changing Lanes |
| <private clock time> | 64.3 | Lane-change-associated steering | Changing Lanes; Confirm Lane Change; Steer Left |
| <private clock time> | 63.6 | Lane-change-associated steering | Car in Blindspot; Changing Lanes; Confirm Lane Change; Steer Right |
| <private clock time> | 64.1 | Lane-change-associated steering | Changing Lanes; Confirm Lane Change; Steer Right |
| <private clock time> | 55.1 | Driver steering input | steering-override-associated |
| <private clock time> | 47.4 | Lane-change-associated steering | Changing Lanes; Confirm Lane Change; Steer Left |
| <private clock time> | 54.2 | Driver steering input | steering-override-associated |
| <private clock time> | 66.9 | Lane-change-associated steering | Car in Blindspot; Changing Lanes; Confirm Lane Change; Steer Right |
| <private clock time> | 46.6 | Driver steering input | steering-override-associated |
| <private clock time> | 50.0 | Brake disengagement | brake-associated |
| <private clock time> | 80.4 | Driver steering input | steering-override-associated |
| <private clock time> | 52.2 | Lane-change-associated steering | Changing Lanes; Confirm Lane Change; Steer Right |
| <private clock time> | 57.5 | Driver steering input | steering-override-associated |
| <private clock time> | 64.0 | Lane-change-associated steering | Changing Lanes; Confirm Lane Change; Steer Left |
| <private clock time> | 59.9 | Lane-change-associated steering | Changing Lanes; Confirm Lane Change; Steer Left |
| <private clock time> | 56.7 | Lane-change-associated steering | Changing Lanes; Confirm Lane Change; Steer Left |
| <private clock time> | 76.3 | Lane-change-associated steering | Car in Blindspot; Changing Lanes; Confirm Lane Change; Steer Right |
| <private clock time> | 69.4 | Brake disengagement | brake-associated |
| <private clock time> | 38.0 | Brake disengagement | brake-associated |
| <private clock time> | 36.4 | Post-disengagement steering | brake-associated; steering-override-associated |

## Safety/health cross-check

No physicalRX-invalid or RX-check/heartbeat fault and no Chestnut supply fault was recorded. The44carState temporary-steering-fault samples occur at initial stationary startup, near1.55mph while inactive at the end, or final ignition-off; none begins during assisted road driving. Fifteen invalid-CAN samples belong to transition/startup data and are excluded by the analysis guards.

The post-initialization hardware blocked counter rises0→4→7→9 during three brake/cancel transitions. Rejected echoes identify **eight cruise-cancel frames plus one active steering frame**, rather than nine steering failures. Seven additional rejected frames occur before Ford configuration during stationary startup; two final inactive frames occur at shutdown. These are kept separately.

At22:49:07.21,69.4mph, a steering frame computed before braking reaches safety after brake input has withdrawn controls permission. The next angle send is mode0. Native offline replay reproduces that rejection with controls_allowed=false and RX valid; mapped and no-map predictions quantize to the same0.0355rad path command at that instant. This supports brake/disengagement timing rather than a roll-gain rejection. Cancel-bit payloads request cancellation after cruise has already disengaged, which the existing Ford safety rule rejects.

Offline native replay:5,881,370physicalRX frames,99,445recordedTX after Ford configuration, seven rejections (six cancel plus that one steering frame), zeroRX-invalid;490pre-FordTX separately unhooked. Hardware echoes show two additional cancellation rejections at the first brake transition that local ordering does not reproduce. Therefore replay is not claimed to reproduce transport timing or every hardware rejection. One startup invalid safety tick precedes validRX acquisition. No safety configuration or permission override was used. [Native replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [actual echoes](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Next priorities

1. Retain the successful50–65trial evidence; do not infer a universal calibration from one drive.65–70still needs ordinary sustained bend exposure.
2. Investigate rising-demand/body-response timing around24–30mph locally, using the29mph warning/manual-release scene and the24mph catch-up/unwinding pair. A blanket boost risks worsening exits; do not relax guards from this drive alone.
3. Keep35–50mph in scope: roughly13–14% over-response remains in this session's steady-request subset. Because roll mapping is inactive there, route/roll/model/response differences need separate analysis.
4. Preserve the15mph issue as unresolved: this drive supplied no useful assisted evidence there.70–85also lacks qualifying turning exposure.

No controller code, settings, services, OS or firmware was changed on the Comma during this investigation. Raw recordings and GPS remain private; public analysis tables omit location and device identifiers.
