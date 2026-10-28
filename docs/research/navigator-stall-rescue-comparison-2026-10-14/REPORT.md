<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator 15 mph issue versus BluePilot stall rescue

October 14, 2026. **Local saved-data investigation only. No Comma connection, source/settings changes, active ECU queries, CAN transmissions or firmware operations. Owner 1.20/0.97 and the installed branch remain unchanged.**

## Finding

**The PR describes a plausible additional mechanism, but it is not established as the explanation or a fix for these Navigator events.** The strongest new evidence is a speed-dependent **EPS centering-availability status** on this Navigator itself. The PR's reactive detector does not fire with the installed fixed pinion measurement in either analyzed drive. A sensitivity calculation with the PR's learned-parameter measurement fires twice around the first latest-drive problem area, not the later event. No saved recording establishes that an injected reset would restore authority.

This changes the next investigation: prioritize the EPS availability/authority distinction and characterize true post-press attenuation before integrating a rescue pulse or increasing gains further. Keep the bounded tracking prototype local pending that review.

## Sources and coverage

BrowserOS neo refreshed [BluePilot #153](https://github.com/BluePilotDev/bluepilot/pull/153), its [commit list](https://github.com/BluePilotDev/bluepilot/pull/153/commits), [#148's prerequisite guard diff](https://github.com/BluePilotDev/bluepilot/pull/148/changes), and [#155's EPS telemetry diff](https://github.com/BluePilotDev/bluepilot/pull/155/changes). #153 remains open. Its reviewed tip is **eb36cf91d5c2e52f6a108a4f633586bccdf89241**, including original change **b2586c56bb2b50aa26028c4a45fc31679bee6af0**. The [immutable angle strategy](https://github.com/jrneulight/openpilot/blob/eb36cf91d5c2e52f6a108a4f633586bccdf89241/opendbc_repo/opendbc/sunnypilot/car/ford/lateral_angle_ext.py) was read in full via the browser; source snapshot hashes are recorded in [provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Local coverage: the **17-segment first master drive** before the added 10% very-low-speed increment, and **10-segment post-increment drive**. Both were already cached. Existing anonymous 100 Hz CarState/CarControl exports were joined causally to recorded ~20 Hz steering TX. Fresh raw extraction added lane-change state and all seven relevant main-bus EPS status fields. **53,625 raw status frames** were cross-checked bit-for-bit against the installed native DBC parser. No GPS, VIN, account or device identifiers are exported. This is a targeted two-drive diagnostic comparison, not another full 72-segment controller/native safety replay.

## What the PR actually does

#153 extends an existing reactive 300 ms mode-0 release pulse down from above **9 m/s (~20.1 mph)** to above **5 m/s (~11.2 mph)** when pinion measurement is enabled. Between those gates it charges on raw desired-versus-measured curvature gap, because the deviation clip cannot bind there.

For this analysis the inspected constants and guards are:

- Desired/measured curvature gap **greater than 0.004 m⁻¹** (twice CURVATURE_ERROR=0.002).
- No detected driver press or lane change; active angle control.
- With prerequisite #148: measured magnitude **less than 65% of requested magnitude**.
- Sustained accumulation of **0.5 s**, then a **six-frame/300 ms** pulse, **2 s cooldown**, at most **three pulses per episode**. Source Python float accumulation reaches its >=0.5 comparison on the eleventh 0.05 s update; that boundary is retained and tested.

The inspected strategy also contains a separate proactive pulse after a sufficiently sustained press. That pre-existing mechanism is not the low-speed gate change. Despite the reactive detector's “post-override” description, its predicate **does not require a recent driver press**. A trigger therefore does not diagnose the cause as press-induced attenuation. The author explicitly requires #148 first to reduce ordinary curve-entry misfires and says pulses cannot fix every low-speed availability/authority limitation. [PR discussion](https://github.com/BluePilotDev/bluepilot/pull/153)

Our installed vanilla port contains its human-turn override but **no reactive stall-rescue or proactive falling-edge pulse**. #153 is not a standalone drop-in feature. Its surrounding fork controller also has different prediction/gain logic; importing that controller wholesale would not preserve the current steering map.

## New EPS evidence: availability differs from limit status

The earlier `[2,0,2]` tuple meant:

| Field | Value in the problem windows | DBC meaning |
| --- | ---: | --- |
| LatCtlSte_D_Stat | 2 | Continuous lateral control in progress |
| LatCtlLim_D_Stat | 0 | Limit not reached |
| LatCtlCpblty_D_Stat | 2 | Capability code, not the separate availability field |

The newly decoded fields, from the **same 0x3CC message**, show in all three selected weak-steering windows:

| Field | Value | DBC meaning |
| --- | ---: | --- |
| **LaActAvail_D_Actl** | **0** | LCA/LKA/LDW suppressed |
| LaActDeny_B_Actl | 0 | Not denied |
| LaHandsOff_B_Actl | 1 | EPS reports hands off |
| TjaHandsOnCnfdnc_B_Est | 1 | Confidence flag code |

Thus an “in progress” control state and a “limit not reached” code **do not establish centering availability**. The earlier analysis omitted this field; its implication that the tuple excluded an availability policy was too strong. This is new direct Navigator evidence, not an assumption transferred from #155's Q3 vehicle.

Across both drives, using raw status-frame timestamps and fresh causal CarState/CarControl:

| Speed / steering request | Valid status frames | Availability |
| --- | ---: | --- |
| 5–20 mph, lateral requested active | **6,378** | **All 0** |
| 5–20 mph, lateral not requested active | **8,738** | **All 0** |
| 25–45 mph, lateral requested active | **6,788** | **6,785 code 2; 3 code 0** |

Code 2 advertises LCA/LKA available with LDW suppressed. **83 of 94 total availability transitions** occur at 24–25.2 mph; the per-drive median in that interval is approximately **24.72 / 24.74 mph**. Brief high-speed transitions also exist, so this is not a claim of a perfect single-threshold rule. The status pattern exists while lateral is not requested, supporting a vehicle-side availability policy rather than solely a reaction to our commanded steering. [Numeric policy summary](../../navigator-reference/PRIVATE_ARTIFACTS.md)

**Interpretation limit:** this bit is not a measurement of available motor torque, maximum path angle or delivered authority. The vehicle still steers with code 0. The pattern is consistent with the policy discussed in #155, and fits the speed dependence of the complaint, but does not prove that the policy causes the measured undertracking or defines an unavoidable physical wall. A mode-0 pulse is not evidence of a way around that policy.

## Does the rescue predicate match the weak turns?

Causal joins use the latest preceding sample; no future feedback is used. Primary measurement is the installed **fixed geometry, no learned offset/roll** pinion model, preserving controller/Panda consistency. Sensitivity uses the same Navigator geometry but recorded learned ratio/stiffness, angle offset and roll, mirroring the PR's measurement formula. Current `vehicleParameters` substitutes for the older fork's `liveParameters`; this is not a complete BluePilot runtime replay. These measurements must not be swapped into the installed paired controller/safety independently.

| Drive window | Median speed | Time since last press at window start | Median fixed-model delivery/request | Fixed-model gap >0.004 frames | Longest qualifying streak |
| --- | ---: | ---: | ---: | ---: | ---: |
| Before increment, 934.03–938.03 s | 14.77 mph | 7.84 s | 0.497 | 12/80 | ~0.50 s; no fire under inspected accumulation |
| Latest, 105.43–107.43 s | 13.79 mph | 20.97 s | 0.555 | 4/40 | ~0.20 s |
| Latest, 510.48–512.48 s | 14.93 mph | 11.51 s | 0.474 | 3/40 | ~0.15 s |

All admitted gap frames in this table also satisfy the fractional guard. None of the windows has a lane-change state; all have fresh EPS hands-off, suppressed availability, in-progress state and no limit flag. Hardware TX-block counter stays constant inside each window; this does not reconcile unrelated historical blocked messages.

**With installed measurement:** zero reactive candidate fires across either full numeric drive, with either the speed extension alone or extension plus fractional guard. Repeating on all five possible phases of the 100 Hz CarControl stream sampled every fifth update still produces **zero** low-speed fires in both drives.

**With PR-style learned measurement:** two candidate fires in the latest drive, approximately **100.53 s and 105.38 s**, at about **14.9 / 13.6 mph** and about **45% measured delivery**. The five sampling phases consistently produce those same two episodes, within ~0.04 s. Neither the earlier drive nor the later latest-drive event around 511 s triggers. The second event's prior delay analysis also showed substantial response catch-up when comparing later motion; this is not a uniform persistent-stall signature. [Per-window and detector results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [phase sensitivity](../../navigator-reference/PRIVATE_ARTIFACTS.md)

The latest preceding press episodes are only **0.21 s / 0.15 s**, below the source proactive hand-off threshold of 0.5 s. For the first latest event, a long recorded mode-0 interval ends **after** that last press (84.98 s), before the weak turn. This weakens a simple “last press left attenuation that needs a release” account if the PR's reset mechanism applies. The earlier drive has a longer ~2.06 s press, making press-associated attenuation a plausible separate case there, but candidate triggering and recovery remain unestablished.

## No demonstrated recovery from a reset

Recorded mode-0/resume intervals were checked for clean low-speed before/after demand of the same sign, within 25% magnitude and 1 m/s speed. **Neither drive supplies a comparable brief 0.25–1.5 s reset/resume pair** under that gate. A longer 11.3 s disengagement has a loose before/after match and changed response, but road/demand evolution and driver action prevent attribution to a short reset. The latest intervention near 513 s changes requested turn direction across the release, so its response cannot validate the pulse. [Natural reset checks](../../navigator-reference/PRIVATE_ARTIFACTS.md)

A hypothetical predicate trigger is an offline eligibility result. It does not demonstrate factory acceptance, beneficial response, safe re-engagement or recovery. This investigation does not implement a sender, alter safety permissions, or exercise the pulse on a vehicle.

## Roadmap decision and next steps

1. **NAV-01:** retain the bounded tracking candidate locally. Analyze the EPS availability/authority relationship, transient versus persistent deficits, and post-press history before considering another steering change. Do not describe the 15 mph issue as simply missing gain.
2. **NAV-15:** prioritize read-only EPS availability/deny/hands/status telemetry alongside requested/measured curvature, stale-data indication and active-limit/reset reason. The previously omitted availability field materially changes diagnosis.
3. **Stall rescue:** keep as a separate, unproven NAV-01 alternative. A future design must distinguish ordinary lag, policy-associated deficits and true post-override attenuation; retain #148-style guarding and assess driver re-engagement. No blanket reset pulses or firmware-policy bypass are justified by this data.
4. **Preserve owner settings and 45 mph behavior.** Do not replace fixed feedback with learned feedback, widen bounds, merge the full fork controller, or deploy this analysis as a steering fix. No additional data collection is required to begin the remaining local analysis; a future physical recovery claim would need its own evidence.

## Reproduction and validation

Run the pinned master integration `.venv/bin/python` on `extract_context.py`, `analyze.py`, `sensitivity.py`, `natural_resets.py`, `policy_summary.py`, then `verify.py`. These scripts read existing private caches and produce anonymous numeric outputs. The detector helpers do not import vehicle interfaces or send CAN. Synthetic tests check the inspected speed/gap/fractional/hold/cooldown/episode and driver/lane guards; they validate analysis bookkeeping, not real controller or vehicle behavior.

The full source controller's prediction blend, proactive pulse and human-turn state machine are not simulated. Primary bookkeeping resets on recorded inactive/mode-0 periods; a hypothetical pulse's changed physical feedback is unknowable. Results therefore support **whether conditions resemble the proposal**, not exact future wire output. The previous 72-segment native safety replay remains evidence for the bounded tracking prototype only, not for a newly integrated rescue pulse.

## Follow-up interpretation

The [availability/authority investigation](../navigator-eps-authority-investigation-2026-10-14/REPORT.md) confirms no application/Panda gate uses the availability field and finds nonzero, varying response with code 0. It finds no adequately matched boundary experiment, so EPS firmware derating remains unresolved. The speed-linked field remains useful context, not established causation or a measured authority wall.
