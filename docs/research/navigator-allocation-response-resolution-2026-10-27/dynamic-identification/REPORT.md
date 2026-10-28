<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Dynamic identification addendum: forecast value exists; causal authority remains unverified

**The short original records do contain useful transient prediction information. Absence of a settled 0.6-second Alpha coast window does not show that transient dynamics are unlearnable.** This assessment improves that earlier limitation statement: current/past state predicts much of the observed trajectory, and command history adds a smaller repeatable improvement in held-out Alpha highway data. It does **not** identify a trustworthy actuator Jacobian for a new brake/coast/propulsion policy. No controller is changed or newly cleared by this fit.

## Original data and causal forecast scope

Input inventory: **175 unique original recording segments**, 35 OEM and 140 Alpha, across 17 sessions (96 prior OEM/Alpha plus 79 newly saved segments). Fourteen sessions contribute **53,356 forecast anchors**. OEM03 has no eligible owned-active commands; new07/09 have no active Alpha examples. They contribute zero cases, not easy stationary prediction success. Every forecast origin is moving at least 3 m/s; Alpha requires original active longitudinal control, while OEM eligibility uses original OEM-owned commands with Alpha disabled. This is a subset assessment of the available original data, not a fresh 316-segment controller replay or an exhaustive proof that no stronger identification is possible in any retained recording.

Primary splits preserve whole sessions: OEM trains on two usable sessions, calibrates on one and tests on one; Alpha trains on one, calibrates on one and tests on the older comfort session plus seven usable newly saved sessions. New07/09 are empty. No random-window split is used. The old/current sessions have been examined in other work; this is retrospective held-out modeling, not prospectively blind validation. Adjacent 0.1-second anchors overlap in their response windows and are not independent trials.

The transparent direct ridge/ARX-style forecasts use only state/status/torque/gear/gravity-proxy and command information available at the origin or at past 0.1/0.2/0.4-second lags. State-only baseline has 55 variables; adding command lags, past mode duration and gas×speed has 77. Missing-value flags, imputation and scaling are learned on training sessions only. Ridge strength and nominal 90% residual bands use calibration sessions only. Previously built feature matrices that included future command prefixes were deliberately **not reused**.

Targets are original reported aEgo, observed speed-change mean acceleration, actual brake/propulsion torque and received brake/precharge status at nominal 0.1/0.2/0.3/0.6-second horizons. Mean acceleration uses observed Δv divided by the actual state-sample elapsed time, not a planner or candidate trajectory. All audited state labels are later than the forecast origin; label samples can precede the nominal target by up to 41 ms. These are not exact 100-ms actuator-delay measurements. Future missing/override records are censored for valid labels; no future command, gear stability or response is used as a feature or an event-selection success condition.

These forecasts include whatever future commands the original closed-loop controller/driver actually issued. They are **not** predictions for holding the origin command fixed after changing the control policy. Vehicle pitch is a gravity proxy, not independently measured road grade; aEgo/Δv are recorded estimates, not independent cabin acceleration truth.

## Primary held-out result, relevant moving regime

Newest installed session08 has 8,670 forecast anchors at 40–70 mph. Reported-acceleration RMSE (m/s²):

|Horizon s|Persistence|State lags|State + command lags|Paired command−state ΔMSE, 95% block interval|
|---:|---:|---:|---:|---|
|0.1|0.314|0.241|0.239|[-0.00162, -0.00044]|
|0.2|0.396|0.254|0.250|[-0.00272, -0.00116]|
|0.3|0.418|0.251|0.245|[-0.00396, -0.00194]|
|0.6|0.371|0.286|0.279|[-0.00639, -0.00158]|

The intervals resample paired 10-second blocks within this held-out session; they are not cross-session causal confidence intervals. Added command information improves this Alpha highway forecast modestly; most improvement over persistence comes from measured state history. The older held-out comfort session also shows modest incremental command value. In the held-out OEM highway session the command−state intervals include zero at all horizons, and adding commands is slightly worse at 0.3 seconds. Ownership/regimes therefore remain separate.

This is not a stationary/easy-row headline. Session08's other origin subsets contain 1,132 moving-below-40 anchors, 364 recent-brake-release anchors and 1,140 valid-propulsion-ramp anchors. At 0.3 seconds, command-model reported-a RMSE is .291 / .247 / .269 respectively (mean-Δv acceleration .203 / .187 / .196). They are different conditional populations; detailed state, persistence, torque/status and episode counts remain in the evaluation files. For session08 at 0.3 seconds, actual brake-torque RMSE improves 48.7→35.5 Nm and propulsion-torque RMSE 95.3→60.8 Nm against persistence. These torque forecasts do not imply physical pressure calibration.

Nominal 90% reported-acceleration residual bands cover only **82.7%, 82.4%, 83.2%, 84.4%** of all 9,802 moving session08 anchors at the four horizons; half-widths are approximately .287/.298/.297/.359 m/s². Thus even their descriptive uncertainty does not transport as a 90% guarantee to this session. Mean-acceleration bands also under-cover. They are not hard response bounds suitable for spending a control-error budget.

## Explicitly secondary seven-session robustness

After the primary result was frozen, a separately labelled retrospective check adds all six pre-update new Alpha sessions to the original Alpha training session: seven development sessions / 16,376 anchors. The original Alpha calibration session and fixed primary ridge strengths remain unchanged. The older comfort session and installed08 remain outside training. Previously primary-held-out new01–06 are development in this secondary check, so this is not a second independent validation on them.

Newest08 40–70 mph reported-a RMSE:

|Horizon s|State lags|State + command lags|
|---:|---:|---:|
|0.1|0.246|0.244|
|0.2|0.254|0.251|
|0.3|0.250|0.245|
|0.6|0.283|0.274|

The result again supports modest command information over state history; it does not remove the prediction-band under-coverage or causal limitation.

## Local sensitivity: observed command directions versus invented perturbations

In secondary training, 4,862 valid-propulsion anchors with at least one gas quantum of past change show gas/brake-numeric-request changes correlated .826. The observed regression direction is **Δbrake numeric request ≈ .675 × Δgas**, with residual scatter. A gas-only partial derivative holds a normally co-varying command channel fixed; an arbitrary +1/+1 coissued perturbation is also not this measured direction. Both are reported for diagnosis, not as causal interventions.

At 25 m/s, secondary 0.1-second partial reported/mean acceleration slopes are −.138/−.294 for gas-only, +.047/−.004 for unit coissued change, and **−.013/−.098 along the observed command-change direction**. Leaving each training session out makes the observed-direction reported-a slope range **−.051 to +.092** and the mean-a slope **−.180 to +.138**. The short-horizon sign is not robust even on that observed direction.

At 0.2/0.3/0.6 seconds, observed-direction slopes are positive across those seven jackknife fits (reported-a ranges .563–.767 / 1.218–1.496 / .888–1.076). These are conditional forecasts of the original closed-loop trajectory, including later policy actions and context. They do not establish a causal gain for changing a request while preserving other future inputs. The primary one-session Alpha fit cannot estimate a leave-training-session-out interval at all; its block bootstrap is explicitly within that one training session. OEM has two usable training sessions and a very limited two-fold jackknife.

## Quiet coast support and future input continuation

The quiet-origin proxy requires an inactive command-mode prefix of at least 0.1 seconds, received torque ≤4 Nm at the origin and its 0.1-second lag, clear current received brake/precharge statuses and low current lateral demand. It is an origin/past qualification, not proof of continuously absent hydraulic pressure or future coast.

Newest08 supplies only **one anchor / one episode** under that proxy; the older Alpha comfort session supplies three. The held-out OEM session supplies 21 anchors. No Alpha quiet-origin anchor in those two external Alpha sessions remains under the same inactive/no-brake command through even the following 0.1 seconds. These tiny subsets cannot validate an inactive-coast response map.

The broader newest08 inactive/no-brake, torque-clear origin subset has 123 anchors: only 12 remain in that command mode through 0.1 seconds, one through 0.2, and zero through 0.3 or 0.6. In contrast the held-out OEM session has 30 such origins and nine remain inactive through 0.6 seconds. This is a **retrospective support audit only**—future continuation was not used for fitting or selecting successful prediction examples. An accurate 0.6-second forecast after an Alpha inactive origin can chiefly describe its naturally returning propulsion, not the response to holding inactive propulsion for 0.6 seconds.

## What this narrows, and what remains missing

Existing short records can support offline trajectory prediction and release/ramp diagnostics; it would be too strong to infer otherwise merely from the old 0.6-second settled selection. The remaining blocker is narrower: validated **causal directional achieved-authority** over mode transitions, with transferable uncertainty, suitable for deciding integral updates after a changed control action. The controller's delayed I crossover and 212 weaker strong requests remain a real rejection. These predictor fits do not clear it.

Before such a rule is admissible, the identification evidence must distinguish natural feedback-policy response from actuator-input innovation: original command ownership/timestamps; separate actual/arbitrated brake torque, propulsion torque and received statuses; gear/engagement/RPM; pose/gravity proxy and actual acceleration/speed; and comparable whole-session held-out transition regimes. Demonstrating sufficiently independent natural command excitation and defensible closed-loop noise/model assumptions in remaining original records could narrow this without new actuation. This assessment does not prove that every retained record or stronger identification method is incapable of doing so.

If existing records cannot provide that overlap/excitation, independently distinguishable release/clear-coast/propulsion transitions would require a separate validated, explicitly authorized identification plan. A 0.6-second window is a prior research selection convention, not a physical safety constant or runtime timeout. No parked/offline replay or guessed synthetic plant can create missing physical force observations. No new controlled command or physical test is authorized or performed here.

## Inspectable artifacts

- [Original-source/case manifest](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [preparation](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [primary fitting](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [frozen primary models](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [per-session/per-regime evaluation](../../../navigator-reference/PRIVATE_ARTIFACTS.md).
- [Paired command information check](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [primary sensitivity](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [secondary robustness/parameters](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [future-command support](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [label timing](../../../navigator-reference/PRIVATE_ARTIFACTS.md).
- [Verification](PUBLIC_VERIFICATION.json) independently checks source/case hashes, past command/state feature bindings and reconstructed forecast errors/coverage. It does not turn prediction into causal validation.

All previous controller source and rejection receipts are unchanged. No controller integration, fresh full/native candidate replay, device/network access, calibration change or CAN transmission occurred in this assessment.
