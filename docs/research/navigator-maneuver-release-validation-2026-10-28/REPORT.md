<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Recovered maneuver brake-release validation — October 28, 2026

**Narrow brake-release behavior is supported; remaining pulsing is not resolved.** This work adds an offline release-state observer and source-bound regressions. It selects no controller change. Paired branches, Comma, original recordings and owner 1.20/0.97 remain unchanged.

## Actual maneuver evidence

The two recovered original sessions supply 14 negative-reference phase windows, evaluated separately from the prior descriptive acceleration templates. The replay primes the **current complete CoastClearance / RestartClearance / ObservedClearBarrier / ReleaseBarrier chain**, including precharge as braking. It does not replay only the base class. Actual outgoing command clocks and prior original torque receive, state, longitudinal activity and published post-update mode clocks are retained. These public clocks do not establish the exact historical consumed frame or historical callback schedule. No bounded-coast lease is invented for these old recordings.

Three completed-session −1 m/s² / 20 mph releases remain clean, active, moving PID observations through qualification:

| Repeat | Observed qualification after command release |
|---|---:|
| 1 | 1.5596 s |
| 2 | 1.5809 s |
| 3 | 1.5837 s |

The existing progress-dependent wait permits all three without a timeout; propulsion permission still requires the existing distinct received torque samples at <=4 Nm spanning at least 40 ms. The confirmation time, rather than the first sample's time, is reported. Across these traces there are **223 callback rows with brake/status clear while reported torque remains above 4 Nm**. A status-only clearance hypothesis fails the retained regression and is rejected. This is not discovery of an installed status-only bug: the installed policy already requires torque.

Of the other 11 windows, seven leave the moving PID domain, three are interrupted by quality/driver/ownership conditions, and one has no release request within the bounded search. They are censored, not successful clearance tests. The first three usable releases occur in actual gear positions 4/3/3; engaged code 6 is a separate engagement-state code and does not mean sixth gear. The earlier session's clean active braking phases do not imply clean ensuing release intervals.

Applying an artificial 20 ms prior-receipt margin retains all three qualifications at 1.5831–1.6159 s. A 50 ms margin causes all three to hit the progress timeout: the progress criterion requires receipt age <=50 ms although basic feedback freshness permits <=100 ms. This is a timing sensitivity, **not evidence of a real current timeout or justification to widen that limit**. Reported torque is the ECU signal used by the guard, not independently measured hydraulic pressure or tire force.

[Full observation traces](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Reproducible runner](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## What that means for the road pulsing

A fresh audit binds the three saved post-regression-session-08 road windows to original raw torque receipts and recorded feedback consumer clocks. It reproduces the previously documented **14 / 15 / 12 brake-bit edges**; these are recorded feedback transitions, not a newly generated controller replay or independent count of every original wire edge.

Among 18 within-window release-to-rebrake pairs, **five lack a new qualifying received torque-clear sequence before rebraking; 13 have one**. Only two of the five actually have torque >4 Nm at the rebrake sample. The remaining three must not be described as proven retained pressure. Received sequence availability also does not prove the consumer had acknowledged it. In the 13 qualifying pairs, raw receive confirmation occurs 0.0469–0.2263 s after release, much faster than the stronger low-speed maneuver releases. A fixed 1.58-second highway release assumption would therefore be unsupported.

Across 2,364 valid recorded release-feedback rows, the latest possible prior raw torque receipt age has median 10.06 ms, p95 16.77 ms and maximum 25.24 ms. Exact consumed samples can be older, but this audit provides no observed basis for applying the artificial 50 ms timeout change as a pulsing treatment.

The five interrupted releases warrant coordinated transition investigation; the other 13 show that release delay alone cannot explain all repeated selection. Existing traces also show changing grade-adjusted demand and integral state near the brake-entry boundary. Correlation does not establish how much friction braking is physically necessary. The recovered low-speed braking tests do not identify inactive-propulsion highway coast response, grade/engine-drag authority, or the counterfactual acceleration after suppressing a brake request. Changing optional integral recovery based on that assumption would repeat the previously rejected weaker-braking failure.

[Road edge and receive-clock audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Prior coupled failure chain](../navigator-allocation-response-resolution-2026-10-27/REPORT.md)

## Prototype and verification

`release_observer.py` is an **observation-only research prototype**, delegating to the actual current clearance chain. It distinguishes commanded braking/precharge, requested release, qualified measured clearance, quality gaps, faults and out-of-domain stopped/creep behavior. It neither changes actuator requests nor invents a response gain, and is not imported by the paired branches. No controller pulsing benefit is claimed from it.

- The intentionally unsafe status-only hypothesis fails its recorded-torque regression; it remains clearly labeled `status_only_rejected.py`.
- Ten focused behavioral tests pass, including duplicate/reversed/stale samples, 40 ms confirmation, precharge, late progressing release, timeout retention and reapplication of torque.
- The existing Ford longitudinal/coast suite reports **210 passed, 20 subtests passed, one failed**. The failure is `TestLongitudinalCoordination.test_native_permission_boundary_unchanged`: macOS rejects loading the UBSan runtime. This run is not called fully green.
- A separate explicitly unsanitized build runs that unchanged native permission-boundary contract. See its receipt and log for the result. It is not sanitizer coverage or full native drive replay.
- No new full 316-segment coupled controller replay, native drive replay, ARM build, hardware check or physical comfort validation was run: there is no accepted new controller candidate to test that way.

[Tests](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Original suite outcome](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Separate native contract](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Artifact/source verification](PUBLIC_VERIFICATION.json)

## Remaining prerequisite

Retain the current measured-clearance and bounded progress policy. Do not substitute status bits, a fixed maneuver delay, a larger coast allowance or an integral reset. The next controller design needs independently supported coast/engine-braking response through the near-zero demand region, separated by operating regime, together with the saved post-ramp stronger-braking regression. Existing controlled data support active braking and its release, not that counterfactual. No additional vehicle experiment, instrumentation installation or road test is authorized by this report.
