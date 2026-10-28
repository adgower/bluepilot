<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# BluePilot longitudinal and MADS evidence, 2026-10-20

Read-only primary-source review using BrowserOS Neo. No source changes, branch operations, device operations, or road tests. GitHub pages and GitHub API read from the browser supplied the provenance below.

## Snapshot

- BluePilotDev `bp-dev`: **d27bc20a7c13eed7ec1947d4c59b98835facea87**, Oct 12, 2026. [Branch](https://github.com/BluePilotDev/bluepilot/tree/bp-dev), [pinned README](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/README.md).
- Dustin Decker `bp-exp`: **691a38cde77c959ee895212c63c47bc44ba9613b**. Its [pinned README](https://github.com/dustin-decker/bluepilot/blob/691a38cde77c959ee895212c63c47bc44ba9613b/README.md) describes an experimental, best-effort fork combining bp-dev with newer models, download reliability, angle auto-calibration, anti-weave smoothing, gauges, steering-delay indication, and takeover guards. It does not advertise a separate longitudinal repair. `BluePilotDev/bluepilot/tree/bp-exp` returned invalid ref/404; do not conflate the repositories.

## What current BluePilot actually changes

The [pinned Ford LongitudinalExt implementation](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/opendbc_repo/opendbc/sunnypilot/car/ford/longitudinal_ext.py) contains:

- Separate precharge and deceleration requests: precharge threshold −0.12 m/s²; brake threshold −0.14; release −0.06. The BP follow path recomputes local booleans each update; the stock fallback uses the stored brake latch for both requests. Thus this is not evidence of a complete OEM-equivalent precharge state machine.
- Whenever `brake_actuate` is true, final propulsion is forced to `INACTIVE_GAS`. This directly addresses the *class* of simultaneous live propulsion plus requested brake deceleration observed in Alex's supplied Alpha comparison, but does not prove it removes Navigator vibration.
- `accel_pred_send` remains `INACTIVE_GAS`; the extension does **not** supply a dynamic predicted-acceleration signal. The CAN builder accepts an argument, but the caller still supplies the inactive sentinel.
- Lead-aware coasting: gaining/pacing/trailing classification, pacing gas capped at 0.2 plus pitch, no gas while gaining inside 1.5 s, downward accel slew limited to 0.002 per update unless TTC ≤8 s or following time ≤0.5 s.
- The BP follow overlay enables above 50 mph, disables below 45 mph, excludes pedal input, and requires no lead or lead speed above 40 mph. It is therefore principally highway following behavior, not a stop/go solution. Mutual exclusion and final clipping still run outside that overlay and even with the BP-follow bypass.

The [pinned controller](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/opendbc_repo/opendbc/car/ford/carcontroller.py) passes `target_speed = V_CRUISE_MAX`, not an OEM-like dynamic speed target, and obtains `stopping` from openpilot's long-control state. Pitch compensation can be disabled. The [pinned CAN builder](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/opendbc_repo/opendbc/sunnypilot/car/ford/fordcan_ext.py) maps these to ACCDATA propulsion, predicted propulsion, brake total accel, target speed, precharge, decel and stop-status fields.

The README says BP softens gas/brake switching but cannot fully fix it; it recommends stock Ford ACC and Alpha Long off. Its stop/go FAQ attributes hard braking to loss of a too-slow lead and subsequent AEB, and suggests DEC/downhill-compensation changes for users choosing Alpha Long. These are **maintainer documentation claims**, not independent proof of the mechanism or a Navigator cure. [Pinned README](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/README.md).

## PR status and applicability

[PR #87](https://github.com/BluePilotDev/bluepilot/pull/87), coasting/downhill compensation, was merged Feb 27, 2026 into `bp-6.0-dev`; merge **27c956f1770a7bf86947c51ffb7e69d97bae021c**. Current source above is stronger evidence of today's behavior than that historical PR title.

[PR #212](https://github.com/BluePilotDev/bluepilot/pull/212) remains **open**, head **a140aa48b600d1a7131091b74bd3b964e513a990**, targeting `bp-dev`. It changes only Lightning/Mach-E EV thresholds (brake −0.5/release −0.4, precharge −0.45/−0.35) and delay 0.25 s. Its author reports smoother Lightning following, requested-vs-actual acceleration improvement and no Mach-E road test. **ICE Fords are explicitly unchanged**, so this is neither merged BluePilot behavior nor a 2023 Navigator remedy. Different propulsion/regen behavior makes blind transplant inappropriate.

## MADS, ICBM, and Autospeed are distinct

MADS already exists in current BluePilot through sunnypilot: it separates steering engagement from cruise/longitudinal engagement. The [pinned MADS implementation](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/sunnypilot/mads/mads.py) reads main-cruise coupling, unified engagement, and steering-on-brake modes; its state machine handles active/paused/disabled steering independently. The README exposes Remain Active / Pause / Disengage on brake. This is useful with **stock ACC** and does not require resolving experimental Ford longitudinal feel. Porting it into a vanilla fork is an integration across state, events, car interface, UI and safety, not a single engagement toggle.

ICBM emulates cruise-button inputs to adjust stock ACC's set speed; it is the documented path for curve/speed-limit assistance while retaining Ford ACC. It does not directly replace the brake/propulsion controller. [Merged PR #28](https://github.com/BluePilotDev/bluepilot/pull/28), Nov 14, 2025, merge **3a4b8841425f4f183d8728470278fb691d22960a**, fixed Ford-specific reversed button mapping and missing `speedCluster` that caused unbounded increase commands. The README still labels ICBM Alpha and its recommended settings leave it off. This calls for separate careful validation even if MADS is adopted.

Autospeed's new upstream longitudinal/model behavior is a separate feature from MADS engagement architecture and from ICBM set-speed button emulation. Nothing in this BluePilot review establishes that a recent openpilot model/default change repairs ACCDATA actuator coordination.

## Recommendation for the paired vanilla fork

Retain stock Ford ACC for the near-term QoL path; prioritize a deliberately scoped MADS integration after the current baseline is pinned and verified. Treat a BluePilot-inspired brake/propulsion coordination experiment as a separate higher-upside research track. Alex's supplied 5.7× vibration subset and simultaneous-precharge/decel/live-propulsion observation justify testing that hypothesis, not claiming it causal. Validate gas suppression, distinct precharge/decel states, stale/disengagement behavior, sentinel prediction and target-speed semantics in replay/contract tests before any device or road decision. Do not copy EV thresholds into Navigator or describe source/PR evidence as Navigator road proof.
