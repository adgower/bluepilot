<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local longitudinal release correction

October23,2026. Authorized local correction/prototype and replay only. Paired branches/device/settings/1.20/0.97 unchanged. Builds on the earlier reviewed handoff; preserve that report as historical evidence.

## Reproduced cause

Ford get_pid_accel_limits caps requests at0.2m/s² near cruise speed. Existing brake latch requires pitch-compensated acceleration>0.3to release. A positive0.2flat-road demand can never clear it. Current LongControl transitions stopping→pid, so a starting-state-only correction would miss the actual path.

## Options and selected spike

Do not globally replace0.3withzero or clear braking after a timeout. Instead add a conditional release gate: when the baseline remains latched, qualify sustained **raw desired acceleration>0.02 AND processed brake acceleration plus pitch>0.02**, with active pid/legacy starting state, finite three-axis orientation, finite demand and valid monotonic50Hz ACC-update timestamps. Require60mselapsed and consecutive controller samples no more than100msapart. The0.02m/s²positive margin is an exploratory near-zero noise band (two propulsion wire steps/about five brake-request steps), not an OEM calibration.±0.01net-demand noise must never qualify release. Positive demands inside this band remain conservatively latched. This dwell is an exploratory noise qualifier, not copied OEM hydraulic release timing. Baseline negative net demand immediately relatches; zero/net-negative demand, stopping/off phase, invalid data/time or lost positive intent resets qualification. A previously latched brake must not clear because missing pitch was replaced by zero or a timestamp gap. Preserve baseline release when already unlatched/normal old>0.3rule clears on valid inputs.

Preserve processed brake acceleration and its limits. Changed wire fields may be propulsion and paired precharge/deceleration bits; only clear those bits under qualified positive demand, never under demanded net braking. No change to predicted acceleration/target speed/steering or safety. Other Ford/OEM modes bypass correction. Stop requests remain propulsion-inactive. Upstream existing stopping/brake logic is retained, not replaced with a new hill-hold algorithm.

Reuse bounded propulsion handoff after release. Sweep0.25/0.5/1.0positive rise and20/60/100msbrake-clear qualification. Original0.5default remains exploratory; publish command delay, do not declare a vehicle calibration. Infinity/NaN/missing orientation are screened before target-platform math.sin; retain last brake latch when pitch invalid, inhibit propulsion. Other-platform behavior is unchanged.

## Required checks

Test-first persistent0.2cap/restart cause, actual stopping→pid transition, grades where positive raw demand still means net braking, exact-zero boundary, request noise/reversal, stop/off/disengagement, invalid pitch/numeric/timestamps, reset lifecycle and non-target parity. Current controller-to-wire comparison permits only justified brake bits/propulsion changes; all brake acceleration/stop fields and non-ACC messages identical. Differential original Alpha replay plus current native RX/TX replay with real recorded RX chronology, separately classify any baseline rejection/ambiguity. Full scoped native Ford longitudinal test matrix; no bypass or forced permission in RX-driven replay.

No offline result proves hydraulic release, rollback prevention, shaking cure, fuel savings or road equivalence. Integration/build/ARM/device and stationary checks remain separate gates before low-speed supervised evaluation; no highway trial authorized.

Invalid target-demand fallback retains the last processed finite brake acceleration while active and bypasses creep/rate processing. Disengagement emits neutral acceleration0. Persistent invalid input is not a new braking request. Integration regression holds the previous processed value for100updates at standstill; no silent ramp toward minimum braking.
