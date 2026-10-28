<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator EPS availability and the 15 mph steering issue

October 14, 2026. **Local investigation completed; no Comma connection or changes. Owner 1.20/0.97, installed steering behavior and clean paired source remain intact. No ECU queries, CAN transmissions, source deployment, reset pulses or firmware/configuration operations.**

## Result

**The availability flag is not proven to limit steering below 25 mph. It does not reduce commands in our application or Panda code, and it is not a binary steering shutoff in the saved data. A speed-dependent reduction inside the EPS remains possible, but cannot be established from this flag alone.**

The 15 mph problem contains at least two different response patterns: a persistent shortfall and a turn-entry response that catches up later. The current added-gain trial is reaching the wire; a local clipping bug is not swallowing the request in these windows. The next useful local correction needs to distinguish persistent tracking error from ordinary delay, rather than treating the availability bit as an actuator setting or applying one larger multiplier to both cases.

The existing bounded tracking prototype remains an experiment, not a demonstrated fix. A new assumption-only plant screen finds both incomplete correction and potential overshoot under different hypothetical dynamics. Do not install that prototype on the strength of its earlier safety replay alone.

## What the flag means—and what we can actually establish

The native DBC labels `LaActAvail_D_Actl` as an LCA/LKA/LDW availability matrix. The previous investigation verified its strong speed correlation directly on this Navigator: all 15,116 valid raw 5–20 mph status frames reported 0, usually changing to 2 near 25 mph. That is a useful diagnostic observation. **A DBC availability name is not a calibration table for steering torque or a quantitative authority measurement.**

Source audit of the pinned installed tree:

- `carstate.py` uses the separate `LatCtlSte_D_Stat` for CAN-FD temporary steering faults, not `LaActAvail_D_Actl`.
- `carcontroller.py` selects angle-mode output, limits and active mode without reading availability. Mode 1 is generated whenever lateral is active at both low and higher speeds.
- `lateral_angle.py` and the installed low-speed subclasses do not read availability. Their measured-curvature deviation clip begins above 9 m/s, not at 25 mph; it is inactive in the analyzed 15 mph turns.
- `ford.h` does not read this status field or0x3CC to reduce steering authority. Existing permission, signal, rate, curvature and pinion-validity checks remain the relevant application/safety bounds.
- The source distinguishes Lane_Assist_Data1 departure-aid commands from LateralMotionControl2 continuous lane-centering commands. Neutral departure-aid action is retained; our source does not activate departure aid to steer.

Therefore there is no application setting for “make this availability bit true.” Changing a decoded receive value would not establish a change in the EPS firmware's actual policy. The source's mode 1 label is “limited mode”; that wording does not prove mode 2 is an appropriate low-speed fix. No mode, hands-off confirmation, enablement or as-built setting was changed or recommended for bypassing a limitation.

### OEM context checked

The exact **2023 Navigator** HTML owner manual is available as Ford variant 9224. Its [lane-keeping limitations](https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?variantid=9224&languageCode=en&countryCode=USA&Uid=G2216809&ProcUid=G2182052&div=l&vFilteringEnabled=False&buildtype=web) describe a 40 mph/64 km/h minimum for departure aid. Its separate [lane-centering requirements](https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?variantid=9224&languageCode=en&countryCode=USA&Uid=G2287427&ProcUid=G2277643&div=l&vFilteringEnabled=False&buildtype=web) list ACC, hands, markings and initial lane position. Those sections do not map the CAN availability field to a 25 mph torque limit. It would be incorrect to equate the departure-aid minimum with our continuous-control command path.

The [lane-centering limitations](https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?variantid=9224&languageCode=en&countryCode=USA&Uid=G2287428&ProcUid=G2277644&div=l&vFilteringEnabled=False&buildtype=web) do document finite steering effort and difficulty with tight curves. That establishes general limits, not the numerical EPS limit in these recordings. Owner documentation describes factory assistance, not validation of this custom controller.

## Saved response: same flag, different outcomes

The two relevant cached drives cover 27 complete raw segments. Existing 100 Hz CarState/CarControl, calibrated motion and recorded 20 Hz command exports were joined causally, with fresh EPS/model data, no driver press for the preceding second, no faults, no lane change and valid motion. The raw status decode was already checked against 53,625 native DBC frames in the preceding investigation.

At 10–20 mph while availability remained 0:

| Drive | Clean frames | Motion response 80–120% of request | Motion response 0–60% of request |
| --- | ---: | ---: | ---: |
| Before extra 10% increment | 882 | 60 | 519 |
| After extra 10% increment | 666 | 45 | 431 |

These are correlated samples, not independent turns. Most near-requested stretches are short and can include delayed curve exit. A latest-drive example around 85.63–85.93 s has approximately 88% delivery by both motion and fixed pinion measurement at 18.4 mph while availability is still 0. This contradicts a complete no-steering interpretation, but **does not rule out reduced maximum authority or establish steady-state unity gain**.

A stricter comparison around the transition found **zero** speed/input-magnitude/direction/entry-exit cells with at least 10 clean frames in each availability state, and **zero** stable 1 second before/after boundary events with comparable command. Speed and flag are closely coupled and the drives contain different turns. Consequently these logs cannot isolate the flag's causal effect or give a trustworthy “percent authority lost below 25 mph.” [Detailed analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md)

### Speed units checked independently

Saved GNSS speed with a valid fix and velocity uncertainty below 1 m/s was compared to fresh preceding CAN speed above 5 m/s. The two drives admit **2,402 / 2,875** samples; median GNSS/CAN ratios are **1.0029 / 0.9966**. This rules out a gross mph/km/h conversion error as the explanation for the apparent 25 mph boundary. It is not an exact instantaneous-speed calibration. Camera odometry has a different scale and is not used as the calibrated speed reference. Only speed and quality values were extracted, with no coordinates. [Speed check](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## What is limiting the selected 15 mph turns?

The correct installed map was used for each drive: the earlier low-speed trial before the increment, and VeryLowSpeed afterward. In all three windows, actual wire path-angle is close to the unbounded requested conversion; median absolute reconstruction discrepancy is about 0.00010–0.00012 rad, below half a wire LSB. This is a timing-tolerant comparison, not a byte-exact runtime reconstruction.

| Window | Maximum path magnitude | Maximum observed path step | Deviation clip active by speed? |
| --- | ---: | ---: | --- |
| Before,934.03–938.03 s | 0.102 rad | 0.015 rad/frame | No |
| Latest,105.43–107.43 s | 0.089 rad | 0.006 rad/frame | No |
| Latest,510.48–512.48 s | 0.107 rad | 0.012 rad/frame | No |

These are well inside the existing DBC range and approximately 0.055 rad/frame soft rate bound at these speeds. Model-to-controller demand is also essentially unchanged in the first latest window; requested lateral acceleration is only about 0.30/0.36 m/s² in the two latest windows, below the upstream 3 m/s² nominal limit. The preceding audit found no local command-safety reject near these events and constant hardware blocked counters inside them. This does not claim unrelated hardware blocks are resolved.

The same-base-sample delayed-response comparison, using only future samples before intervention and with valid clean motion:

| Latest event | Base frames shared across delays | Now | +0.5 s | +1.0 s |
| --- | ---: | ---: | ---: | ---: |
| First weak turn | 19 | 0.532 | 0.519 | 0.516 |
| Later weak turn | 20 | 0.158 | 0.579 | 1.096 |

Values are median future actual curvature divided by the original requested curvature. They are not identified actuator transfer functions. The first shortfall persists; the second largely catches up and may overshoot the earlier reference. **The same instantaneous tracking error therefore cannot automatically justify the same extra command.**

## Recorded delay: a useful new constraint

Both drives carry an estimated lateral delay fixed at **0.262153 s**, status estimated,50 valid blocks and 100% calibration. CarParams nominal actuator delay is 0.2 s. No valid maneuver-plan override was present in these recordings. The current model uses the recorded lateralDelay input; controlsd also reads it, while the angle conversion itself does not add lead compensation.

The current upstream lag estimator's admission floor is **50 mph**, so these slower drives do not identify a new 15 mph delay. The loaded estimate is already marked calibrated and remains unchanged. That does not make it wrong, but **100% calibration does not establish low-speed accuracy**. The selected turn's 1 s catch-up is likewise not proof that the correct model delay is 1 s. Changing a global delay would alter the good higher-speed behavior and is not justified here. [Recorded delay analysis](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Local screen of the existing bounded prototype

The existing prototype's 1.20/0.97 and feedforward remain unchanged. It adds filtered P feedback with gain 0.5 and 0.30 s filter, caps the additional term at 0.015 rad and 25% of feedforward, and fades it out by 25 mph.

An offline screen ran **96 assumed cases**:15/45 mph, response gains 0.25/0.5/0.75/1, first-order time constants 0.15/0.4/0.8 s and delays 0/0.3/0.6/1 s. Each controller receives its own hypothetical measured response. The physical plant is *not identified from the Navigator*; the flag is not modeled as a limiter. Step, reversal and release inputs exercise feedback memory. Baseline low-speed steady response is checked against the assumed plant gain.

Findings:

- For the assumed half-response plant, steady delivery improves from about 50% to **60%**, not 100%. The small bounded correction cannot recover an arbitrarily large persistent deficit.
- Some assumed full-response/delayed cases overshoot. The worst tested peak is about **1.207 times the reference**; see [synthetic-screen.json](../../navigator-reference/PRIVATE_ARTIFACTS.md). This is a sensitivity finding, not a prediction of the Navigator's overshoot or a certification of other cases.
- All 45 mph synthetic baseline/prototype command sequences match. The earlier 72-segment real-recorded-input replay also retains its documented ≥45 mph parity; this screen does not replace native safety replay.
- The screen omits openpilot's outer lane-policy/model feedback, real EPS nonlinearities, firmware and driver intervention. It cannot establish stability on the road.

This is why simply raising feedback gain/caps until an offline example reaches 100% is not a supported fix.

## Concrete direction for the next local correction

**Separate two experiments rather than widen one gain curve:**

1. **Persistent deficit correction:** evaluate a bounded tracking term admitted only after demand and tracking error persist long enough to reject normal entry lag; reset on driver input, inactive/invalid state, reversal and speed exit. The existing prototype supplies a starting implementation, but its admission logic and useful correction envelope need further design. Availability should initially be diagnostic context, not an automatic on/off or boost switch. Keep 1.20/0.97 and zero added term by 25 mph.
2. **Transient timing:** independently assess low-speed anticipation/reference timing against held-out turn entries and reversals. Do not assign a 1 s global delay from these examples or change the model's delay input without corresponding model/runtime validation. The model already consumes a delay estimate; extra lead could double-count compensation.
3. **Identify authority before adding force:** fit response only where sufficiently steady, direction-balanced demand and valid independent motion exist. Prior strict coverage found no full-second steady qualifying windows in the relevant 10–20 mph bands, so these recordings do not justify a best new gain or deadband table. A physical reduction remains unresolved without an adequate reference experiment or validated independent actuator telemetry.
4. **Keep boundaries:** unchanged mode/permissions/safety bounds, paired fixed pinion geometry, driver override and≥25/45 mph regression checks. Do not manipulate the received flag, introduce release pulses, or select extended mode based only on this diagnosis.

An admission-only diagnostic grid tested a trailing 0.5-second stable-demand check, maximum relative request variation of 15/25/40%, less than 70% fixed-model delivery, and holds of 0.3/0.5/1.0 seconds. In the latest selected first window, the 0.3-second holds admit 13–14 of 40 frames; the later transient window admits none in all nine cases. Increasing the hold to 0.5 seconds admits only 3–4 first-window frames, and a 1-second hold admits neither selected window. This supports separating transient and persistent error, but **does not select a robust threshold or prove useful early intervention**. It also shows why a persistence gate alone is not yet a completed fix. [Admission sensitivity](../../navigator-reference/PRIVATE_ARTIFACTS.md)

These are now explicit NAV-01/NAV-15 acceptance gates. No revised controller has been claimed fixed, integrated or installed. The investigation resolves the software-gate question and narrows the correction design; it does not claim to reverse-engineer the closed EPS firmware from a status bit.

## Reproduce and inspect

Scripts: `analyze.py`, `extract_delay.py`, `delay_analysis.py`, `check_speed_units.py`, `synthetic_screen.py`, `admission_screen.py`, `verify.py`. Run with the pinned integration tree's `.venv/bin/python`; private cached numeric/raw logs are prerequisites. [Verification receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md) records fresh source/artifact checks. This task does not rerun the entire native suite because no production controller/safety source changed.
