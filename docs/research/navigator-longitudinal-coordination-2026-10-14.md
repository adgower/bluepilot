<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Expedition longitudinal coordination candidate

## Status checked October 14, 2026

Recovered from openpilot branch `codex/ford-longitudinal-coordination`, parent commit `d8123f013353bf3fb2240c78bb41c3dba2b31cdf`, which pins opendbc `d5ccadb7f9abcbee84f86dafd10e30c8e2f4e6ff`. Both branches and corresponding origin tracking refs exist locally. This check did not establish current remote publication or PR status.

The last verified Comma steering installation does not include this candidate. Its deployed controller SHA256 `fb43a80bbb4c96ac8b0a28ec5890d69e8d9591b9d9401c8b3b72a897d6fd9b43` matches the current local steering trial controller, which lacks the added brake-latch propulsion override. This is comparison with the saved deployment manifest, not a fresh SSH inspection.

The validation below is the earlier branch report, recovered verbatim; those tests were not rerun in this documentation turn. Integration into the current pinion/low-speed trial and fresh combined replay remain outstanding. Do not replace the trial with this older branch wholesale: its pinion implementation predates the optional paired implementation now installed.

Alpha longitudinal enables openpilot's gas/brake actuation path; Experimental mode changes planning behavior when openpilot longitudinal is available. They are separate concerns. This candidate changes Ford command coordination, not the experimental model's planning, cruise speed selection, or all Ford/Lincoln platforms.

## Earlier candidate report

This candidate withdraws the propulsion request while the existing Ford brake
request is latched, only for `FORD_EXPEDITION_MK4` with openpilot longitudinal
control enabled. It is intended for review on `navigator-angle-v1` and has not
been validated on a vehicle.

## Motivation

A Navigator configured as Expedition showed steering vibration during Alpha
braking. In sampled braking windows, CAN feedback reported approximately
146–174 Nm brake torque alongside +273 to +427 Nm propulsion torque. OEM ACC
comparison logs reported about 57 Nm brake torque with -128 Nm propulsion torque
in mild slowing, and 346 Nm with -95 Nm in a stronger braking window. These are
ECU-reported values, not independently measured torque or hydraulic pressure.

During the sampled OEM active-braking event, the propulsion request was inactive
(`AccPrpl_A_Rq = -5`). Alpha kept a valid propulsion request while its brake bits
were asserted. The candidate tests this one command difference. It does not
reproduce the full OEM strategy: OEM also showed precharge-only operation and a
period of inactive propulsion after releasing its brake bits.

## Behavior and limits

The override runs after the existing pitch compensation and brake hysteresis.
It sets `AccPrpl_A_Rq` to the inactive sentinel while the brake request is latched.
The reported actuator gas output reflects that transmitted value. Brake demand,
creep compensation, brake jerk limiting, acceleration bounds, precharge and
deceleration bits, predicted acceleration, steering and safety code are unchanged.
Other Ford configurations and OEM longitudinal operation retain their behavior.

Propulsion resumes when the existing brake latch releases. This introduces a
propulsion-command transition whose resulting vehicle torque is not bounded by
the unchanged brake jerk limiter. At standstill, a latched brake request can keep
propulsion inactive for small positive requests until pitch-adjusted acceleration
exceeds the existing 0.3 m/s² release threshold. Launch, grades and brake-release
response therefore need controlled vehicle validation before use.

The observed vibration was close to wheel rotational frequency. The logs do not
establish that command coordination is its sole cause or that this change removes
it. A code-level pass must not be described as a shaking fix.

## Offline validation

- Controller-to-CAN regression tests cover mild braking, both pitch directions,
  latch retention/release, disengagement/reengagement, stopping/restart, bounds,
  other Ford configurations, OEM ACC and the existing safety TX hook.
- Ford controller suite: 38 tests passed. Ford safety suite: 138 tests run,
  14 skipped, no failures. Ruff and `git diff --check` passed.
- A fixed-input differential replay used the supplied Alpha segment's recorded
  control and vehicle-state inputs with the pinned baseline and candidate
  controllers. Only the propulsion-request field changed, in 752 of 2,984 ACC
  frames; 3,550 non-ACC frames were identical. All replayed ACC frames passed the
  existing safety hook. This replay does not simulate altered vehicle response,
  reproduce original scheduling exactly, or establish road performance.
