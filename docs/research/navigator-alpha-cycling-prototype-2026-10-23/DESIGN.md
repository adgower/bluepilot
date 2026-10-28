<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Throwaway brake-admission experiment

## Evidence and alternatives

The installed controller asserts brake/precharge below zero pitch-adjusted acceleration, clears a prior brake after a qualified small positive request, then withdraws/requalifies/rate-limits propulsion on every brake interval. This drive repeatedly visits that boundary. Delaying all braking, widening release hysteresis indiscriminately, or increasing longitudinal gains could conceal needed deceleration, recreate the small-positive restart deadlock, or strengthen the limit cycle. A pitch filter without a validated grade/body-motion separation could lag a real grade change.

The conservative experiment qualifies only a new weak negative-net brake entry during positive acceleration intent. It is not a general filter or a PID tune. Most recorded cycling remains outside its safely assumed brief-dip envelope, so the experiment is not considered a complete fix.

## Scope and transitions

Report-local insertion before the existing ReleaseGate, only under its current Navigator/Alpha controller branch. Existing release, propulsion handoff, acceleration computation, wire acceleration, safety limits, steering and all other vehicle branches remain unchanged.

| Condition | Admission behavior |
|---|---|
| Inactive | Preserve baseline neutral; reset local debt |
| Invalid pitch/demand/speed/time | Preserve baseline/prior brake; no suppression on that call |
| Nonpositive/backward or >100 ms cadence | Preserve baseline/prior brake on that call |
| Existing brake hold | Preserve hold; existing ReleaseGate decides any release |
| Stopping/starting/non-PID or <3 m/s | Preserve baseline, covering original stop/restart behavior |
| Raw acceleration <=0.02 or net <=−0.12 m/s² | Admit the baseline brake immediately |
| Positive raw >0.02, PID, >=3 m/s, no old brake, −0.12<net<0 | Suppress only until per-dip qualification or signed demand-area budget reaches its threshold |
| Baseline clears | Clear, reset per-dip timer; retain signed debt across brief crossings |

Per-dip qualification is 0.12 s from the first observed negative sample. Signed debt `max(0, debt - net*dt)` is capped at0.02, with admission threshold0.006 m/s. Positive net pays down debt. Existing admitted brake/disengagement or leaving eligible positive PID operation ends/reset this accounting epoch. Invalid calls preserve debt but skip integration; valid recovery is allowed, not a latched fault.

**The debt is not measured speed error and 0.006 is not a strict maximum omitted acceleration area.** Discrete sampling, current-value rectangle integration over the preceding interval (accepted cadence up to100ms), first-call zero interval and eligibility resets limit interpretation. A genuinely needed new weak grade brake can be delayed inside this envelope; only stronger demands/existing holds are immediately protected. No physical safety guarantee follows from these constants.

## Test strategy

Falsify the baseline with brief positive-intent pitch dips, then check immediate requested braking, stronger grade, persistent weak grade, alternating negative-biased pulses, exact thresholds, irregular cadence, stopping/low speed, existing holds, invalid inputs/time and recovery. Bind the candidate only in memory for retained child and actual parent stop→PID integration tests. Full-drive fixed-input comparison, exported-copy equivalence and RX-driven native ACC-hook replay are separate checks. None simulate the vehicle response or establish improved comfort.
