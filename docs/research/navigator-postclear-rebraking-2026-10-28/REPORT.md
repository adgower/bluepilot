<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Post-clear rebraking: grade, integral and planner investigation

October 28, 2026. **The bounded grade-filter prototype is rejected; remaining pulsing is not resolved.** It reduces some repeated software brake selections but adds braking exposure and changes later strong requests. No controller change is selected for integration. Paired sources, Comma, original recordings and 1.20/0.97 remain unchanged.

## What drives the 13 events?

These are the 13 previously identified road release/rebrake pairs with a qualifying raw received torque-clear sequence available before rebraking. Availability is not proof the consumer had acknowledged clearance. Original consumed CarControl epoch/sequence binds each returned request to its recorded PID I, consumed planner timestamp and referenced carState. Request values match exactly at all endpoints. Producer orientation plus recorded GradeOffset provides a **grade-decision proxy**, not independently measured road slope or proof of the refreshed consumer orientation.

Twelve pairs have an intervening brake-off callback after the clear sequence. Their largest negative contribution to the change in `raw request + grade proxy` is:

| Largest negative contribution | Events |
|---|---:|
| Pitch-gravity proxy | 5 |
| Integral I | 4 |
| Planner target | 3 |
| No intervening released callback to decompose | 1 |

The static GradeOffset is unchanged at all endpoints. This pass does not support retuning the OEM-derived 0.149913 m/s² relative mapping. The contribution ranking describes software signals; it is not independent physical causation, and the contributions can oppose one another.

In the four I-dominated pairs, I falls by about 0.066–0.209 m/s². Mean consumed target-minus-actual acceleration is negative in all four (−0.046 to −0.143 m/s²), with negative error in roughly 59–74% of the producer samples. Actual acceleration is therefore above the requested acceleration on average: reducing I is a normal signed-error response. These observations do **not** justify clearing I or suppressing its negative updates.

[Recorded endpoint attribution and per-event errors](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Reproducible attribution](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## OEM comparison

Fresh hash checks cover saved derived signal caches for **131 original unique segments / 12 previously inspected routes**, comprising five OEM and seven Alpha routes. No new recording acquisition or fresh raw-rlog extraction is claimed. Under the declared active-owner, 35–75 mph, gear/engagement, CAN, no-pedal and orientation screens, two OEM routes contribute 304 nonoverlapping half-second windows and five Alpha routes contribute 3,375. The other routes contribute no complete eligible windows; they are retained as exclusions rather than silently counted as supporting evidence.

Pitch-variation distributions overlap. For example, OEM route 04 has a half-second pitch-gravity span p90 of 0.078 m/s²; the usable Alpha routes span roughly 0.048–0.080 at p90. OEM has eight zero-brake-edge windows with proxy span above 0.1 m/s². Thus ordinary pitch variation alone does not establish a sensor defect or require every Alpha brake selection. The 304 OEM windows contain 11 within-window brake-bit edges versus 569 across the much larger Alpha exposure. These unequal route/lead/grade/request cohorts are **descriptive**, not a causal comfort comparison or an identified OEM threshold/plant law. Exact tenth-gear results are reported separately in the artifact; engaged code 6 is not sixth gear.

[Source-qualified OEM/Alpha comparison and exclusions](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## One bounded local diagnostic

The research-only prototype applies a causal 250 ms grade filter, capped at 0.05 m/s² correction, only within a faded 35–75 mph active weak-positive-demand scope. Negative or stronger planner demand, FCW, invalid/stale context, pedals and stopped/creep phases bypass it. The original GradeLease offset/slew, numerical raw/brake request, PID implementation, shared allocator, torque-clearance chain, native safety and handoff logic are not replaced. These parameters were declared once; no tolerance sweep or second filter variant was used.

This is a hypothesis test, **not a validated physical grade estimate**. Changing the decision reference can omit an original brake selection even though the allocator's internal budget code is unchanged. The audit explicitly treats such changed-reference omissions against a locked original account as unsupported, rather than claiming that unchanged account code proves preserved authority.

Seven filter tests follow an observed failing passthrough regression. Seven additional adapter/context checks pass against actual GradeLease/request contracts. Their 14 passes prove the bounded software properties, not highway comfort.

[Design and limits](DESIGN.md) · [Prototype](prototype.py) · [Tests](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Fresh producer/consumer replay results

Both sides run actual current LongControl and CarController at retained producer/consumer clocks. Vehicle state, torque, pose, planner and driver response are frozen. The current-source assisted session covers **21 segments, 60,424 callbacks and 114,018 recomputed producer steps per variant**, with no active atomic-input gaps. Its reconstructed raw request differs from recording by median 0.00156 / p95 0.01848 m/s²; hidden receipt order remains unknown. Comparisons are paired reconstructed software behavior, not changed road behavior.

| Focused assisted-session measure | Baseline | Filter diagnostic |
|---|---:|---:|
| Full-brake bit changes | 280 | 246 |
| Full-brake exposure | 389.587 s | 399.403 s |
| Brake/precharge union exposure | 397.180 s | 408.308 s |
| Weaker encoded strong-request rows | — | 218 |
| New faults / active-row losses / retained-torque positive gas | — | 0 / 0 / 0 |

The 218 weaker encoded requests differ by at most **one 0.0039 m/s² encoding increment**. That small magnitude is disclosed; it does not negate the extra exposure or unsupported omissions. There are 497 full-brake omissions against a locked original baseline account, including 362 with a direct positive filter correction at the callback. No new coast authority was established to justify those omissions.

| Named road window | Brake-bit changes, baseline → diagnostic |
|---|---:|
| 53 mph | 14 → 14 |
| 40–50 mph | 15 → 11 |
| 58 mph, no lead | 12 → 6 |
| Separate retained 25 mph city regression | 17 → 17 |

The separate city comparison covers **eight segments, 22,988 callbacks and 44,283 producer steps per variant**, with no active atomic-input gaps. The filter never changes grade there; wire, raw, I, activity and fault histories remain identical. It is a preservation control, not a city pulsing improvement. Total fresh coupled coverage is 29 unique segments / two routes. The city originals are already included in the 131-segment descriptive corpus; with the 21 newer assisted segments, the combined evidence union is 152 unique originals, not 160.

[Focused comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [City comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Failing acceptance gates](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Why simple filtering fails the joint loop

Fresh paired software traces establish this chain (times relative to the replay's first carState, distinct from the earlier acquisition time origin):

1. Around +127.361 s, about +0.0202 m/s² selected grade correction advances a release. Baseline still commands braking; candidate waits for observed clear.
2. At +127.380 s, candidate positive integration freezes during the limited release while baseline signed braking continues to integrate. I begins to diverge without any direct PID modification.
3. Around +131.581 s, roles reverse: baseline waits for clearance and freezes, while candidate actual braking permits positive integration.
4. At +361.038 s, the filter is bypassed for a strong negative target, but accumulated I differs (about 0.04027 baseline versus 0.04118 candidate). Later encoded braking can therefore be weaker despite the immediate strong-demand bypass.

This is a **software feedback interaction on frozen vehicle response**, not proof of physical counterfactual acceleration. It shows why an isolated grade smoother or an immediate bypass cannot by itself preserve subsequent integral behavior. I also differs at 1,067 below-35-mph callbacks later in this session, despite the filter's speed gate; instantaneous scope does not erase state history. None of the weaker encoded strong-request rows are below 35 mph in this run.

[Exact first-divergence snapshots](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Decision and remaining work

`check_gates.py` correctly exits 1: extra full/combined exposure, weaker strong encoding, and unsupported original-account omissions reject this diagnostic. The 40–50 and 58 mph edge reductions are not credited as physical improvement. No full 316-segment expansion, native drive replay, ARM build, installation or road validation follows this failed focused gate.

The remaining problem involves **joint near-zero demand selection and integral/actuator authority**, with planner slowdowns preserved. This evidence does not justify eliminating grade compensation, zeroing I or extending a coast account. A next design must explain actual acceleration response through that transition and preserve signed tracking, measured clearance and later strong braking across its state history; another independent grade-only filter does not satisfy that requirement. This is not proof that all further local designs are impossible or that every observed rebrake is erroneous.

[Artifact and source verification](PUBLIC_VERIFICATION.json) · [Scope](PLAN.md)
