<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# 30–50 mph: request, command and measured-response audit

October 16, 2026. Analysis uses the saved 386-segment/21-session normalized corpus; current-revision descriptive results are restricted to sessions advertising `9da98d0c9`. All 21 normalized input hashes match their previously saved artifact inventories. No SSH, vehicle queries, settings/code changes or installation. 1.20/0.97 remain unchanged.

## Finding

**30–35 mph is the strongest initial reference, but not fully validated. The next useful collection is 35–50 mph, especially both turn directions at 40–50.** An aggregate response above 100% is not enough to choose a reduced gain. Timing explains much of the 30–35 mph transient difference; at 40–50 mph, recorded roll/model effects also matter. Existing independent-route support cannot validate a new calibration in any of these bands.

The owner's earlier good 45 mph feel is subjective feedback, not an exemption. This audit includes 40–45 and 45–50 mph on the same basis as other ranges.

## Separate phases rather than pooling every bend

The predeclared diagnostic phase rule uses the preceding one second of continuously eligible samples, the same turn direction and no more than 3 mph speed spread. “Steady” means requested-curvature range within 10% of its median magnitude. Rising/unwinding have endpoint magnitude changes above/below 10%; other samples are mixed or lack qualifying history. Current samples must have absolute requested curvature above 0.001/m. Sensitivity summaries at 5% and 20% were calculated without selecting whichever threshold looked best.

These labels identify relatively steady **request**, not demonstrated settled vehicle dynamics or flat roads. Steady exposure may comprise short fragments, and sample seconds are not independent trials. Direction signs below refer to requested curvature, not an inferred physical left/right naming convention.

| Band | All clean meaningful bends | Relatively steady-request exposure | Steady body/request median | Principal gap |
| --- | ---: | ---: | ---: | --- |
| 30–35 mph | 71.30 s | 10.90 s | 101.4% | 10.85 s of steady evidence comes from one session; repeat on separate drives |
| 35–40 mph | 12.90 s | 1.30 s | 117.9% | Too little sustained evidence; no steady exposure under the stricter 5% rule |
| 40–45 mph | 11.20 s | 1.35 s | 124.8% | Steady samples from one session, all one turn sign; none under 5% rule |
| 45–50 mph | 13.10 s | 6.35 s | 112.9% | All steady samples have one turn sign, across two sessions; only one qualifying transfer-fit episode |

The 30–35 mph steady subset has 5.5 s of negative and 5.4 s positive requested curvature. The entire 40–50 mph steady subset has **zero negative-sign exposure** and 7.7 s positive-sign exposure. Even all-phase 40–50 meaningful bends are heavily skewed: 22.3 s positive versus 2.0 s negative. A single speed multiplier could hide directional offset/roll differences.

At the 5%/20% steady thresholds, 45–50 mph medians are approximately 110.5%/115.4%, but sample exposure changes from 2.9 to 9.3 s. This suggests a persistent diagnostic pattern within the selected one-direction evidence; it is not a precision gain estimate. At 40–45 mph, the 10% estimate rests on only 27 samples and cannot establish a general 24.8% over-response.

## Timing and command delivery

At 30–35 mph:

- Rising-demand body/request median is 93.6%; comparing the earlier requests with body response 0.25 s later gives 99.6%.
- Unwinding-demand median is 108.3%; the same 0.25 s diagnostic shift gives 97.7%.
- Steady-request median changes little: 101.4% contemporaneously, 101.5% at +0.25 s and 100.7% at +0.5 s.

This supports a timing contribution to the transient ratios. It does not identify exact online latency or authorize setting a 0.25 s delay. The simple shifts use later eligible body observations, not an optimized actuator model.

At 40–50 mph the steady subset remains above request under the same shifts: 114.8% at zero shift, 114.6% at +0.25 s, 113.8% at +0.5 s. Unwinding ratios fall from 128.6% to about 113.5% with +0.5 s, so turn-exit timing contributes without explaining all of the steady diagnostic difference.

Normalized-grid transmitted command agrees closely with the current feedforward map: steady median wire/feedforward ratios are about 100.1%, 100.1%, 99.5% and 100.1% in the four bands. Calculating the existing deviation clip against aligned state finds no affected samples at 30–35, 40–45 or 45–50 mph, and two at 35–40 mph (one in its tiny steady subset). This is a past-aligned 20 Hz diagnostic, **not exact send-time limiter telemetry or a fresh native safety replay**. It gives no evidence of a broad command-delivery shortfall in these ranges.

## Wheel, roll and independent OEM yaw

The learned-ratio/offset wheel model without roll is close to requested curvature even where body response is higher. Adding recorded roll brings wheel-model estimates closer to body yaw:

| Steady subset | Learned wheel/request, without roll | Learned wheel/request, with roll | Body/request |
| --- | ---: | ---: | ---: |
| 30–35 mph | 101.5% | 101.3% | 101.4% |
| 35–40 mph | 101.5% | 121.2% | 117.9% |
| 40–45 mph | 95.0% | 125.7% | 124.8% |
| 45–50 mph | 104.5% | 113.3% | 112.9% |

Stationary-debiased OEM CAN yaw broadly corroborates body yaw (for example ~113.6% in the 45–50 steady subset). Thus body response is not contradicted by the OEM signal. However, recorded roll and learned vehicle parameters are estimates, not independent ground truth about road banking or causal actuator gain. These comparisons support investigating roll/model/road effects, rather than concluding that a speed gain is uniformly too high. Driving comparable ordinary bends in both directions is particularly useful for separating directional effects. No roll, yaw, steer-ratio, offset or native safety parameter was changed.

## Calibration validation still abstains

The existing episode selector and estimator gates were reused. Source-diverse historical sessions train the model; all current-revision sessions are held out whole. Current-only whole-route cross-validation is also reported separately. No adjacent-frame split or new gain recommendation is introduced.

- 30–35 mph: 3 historical / 16 current episodes. Historical training lacks required episode/duration support; current qualifying episodes come from only two sessions.
- 35–40 mph: 1 historical / 1 current episode; inadequate support.
- 40–45 mph: 1 historical / 5 current episodes; inadequate historical support and current route coverage.
- 45–50 mph: 6 historical / 1 current episode; inadequate independent held-out episodes/routes/duration.
- Broad 30–50 mph: 8 historical / 21 current episodes. The fitted model fails residual-input dependence, per-route dependence and across-route gain-consistency checks. Current-only CV has just three qualifying routes, below the existing four-route minimum.

No precise speed map, gain adjustment or optimal delay is validated. These limitations do not erase the descriptive observations; they limit which control changes can be justified by them.

## What to collect next

**Two or three more ordinary drives on a suitable 35–50 mph route**, where those speeds are legal and natural. Prioritize gentle marked bends in **both left and right directions**, especially around 40–45 and 45–50 mph. Repeat a familiar route in the opposite direction where practical. Prefer ordinary roads over heavily banked ramps for the next comparison, while recognizing that visual appearance does not prove flat banking.

Include normal bend entry, a sustained middle and exit. Naturally steady speed helps distinguish timing from gain; exact speed holding is not required. A few normal 30–35 mph bends on the same drives would add independent confirmation of the stronger existing reference. Several usable bends per direction per drive is a collection goal, not guaranteed estimator support.

Four-to-twelve-second segments are useful to the offline selector **only when naturally available**. Maintain supervision and intervene/brake normally; never extend a turn, avoid braking or delay intervention to meet a data criterion. After parking, an approximate timestamp/location for any noticeable shortfall or repeated correction helps identify the scene.

No dedicated 75/85 mph collection is needed. The next gap is mid-speed directional/repeatability evidence, not maximum speed. Existing 50–70 mph logs remain available for the next highway audit without waiting for this collection.

## Evidence

`audit.json`: phase/route summaries, threshold sensitivity and abstaining fit/CV results. `chain-check.json`: diagnostic transmitted-command and wheel/roll comparisons. `lag-check.json`: fixed timing-shift summaries. `input-provenance.json`: verified normalized hashes and source labels. `analyze.py` and `chain_check.py` reproduce the analysis. Recorded startup dirty flags can be true, so advertised revision labels alone do not prove exact recorded source contents. No claim of matched-road causal improvement or optimal calibration is made.
