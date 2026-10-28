<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local diagnosis: 22–25 mph entry and 74 mph excess

October 21, 2026. Local saved-log investigation only. Comma untouched: no SSH, parameter change, CAN, update or activation in this task. Paired source remains clean at parent `db584234805cf2039ee976d856a29b655188ad2a` / child `8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e`; all 85 protected child hashes and owner **1.20/0.97** remain unchanged.

## Conclusion

These are different command-policy limitations. Low-speed demand reaches the controller's fixed-pinion deviation clamp before the bounded correction can establish an episode; subsequent clipped demand fails the original wheel-target consistency check. At highway speed, the trim works but repeatedly loses permission, then reconfirms and ramps, so it changes only a small fraction of the command. Current earlier-onset coverage ends at 70 mph. Neither observation proves an EPS hardware limit, a failed yaw sensor, or that merging master caused a physical regression.

The right next work is a bounded command/reference and onset design, not a global gain increase. Fixing the low-speed calibration predicate alone would not remove the binding deviation envelope. Increasing the highway reduction cap alone would not address the observed reset/confirmation problem.

## Evidence and reconstruction

Input: the saved <private clock time> drive (`master-session-06`) from the [latest acquisition](../navigator-post-master-drives-2026-10-21/REPORT.md). Original carControl atomic calibration packets, full causal warm-up, motion/context timestamps and actual send times are replayed through the exact selected strategy. Raw logs/GNSS stay in the private cache.

All **4,466 active, unpressed, mode-1 commands** match the recorded path-angle signal within its half-step rounding tolerance (0.00025 rad). The diagnostic wrapper produces exactly the same full command array as the uninstrumented reconstruction. Each focused window also has 100% parity. This validates attribution of recorded command generation; it does not simulate counterfactual vehicle motion. Native safety and the complete controller/corpus suite were not rerun because no control-code change is proposed or made here.

Reproduction commands, using the paired checkout's `.venv/bin/python`:

- `reconstruct.py PRIVATE_RECORDING_DIRECTORY reconstruction`
- `instrumented_reconstruct.py PRIVATE_RECORDING_DIRECTORY instrumented-final`
- `layer_analysis.py`
- `verify_diagnosis.py`

The last command verifies the diagnosis facts, wire parity and unchanged sources; it is not a test asserting that physical understeer has been fixed. Physical symptoms remain in the immutable recording. CodeGraph tools were not exposed in this session; investigation used the already identified source files and runtime object state.

## 22–25 mph: the request outruns the permitted command

Window: route-relative 219.50–220.95 seconds, about **<private clock time>–<private clock time> CDT**, before driver intervention. The prior body analysis has 1.4 clean seconds at **35.1% response**, wheel feedback about **40.5%** of its target, and a turn-exceeds-limit alert.

### Verified chain

1. The application clips requested curvature to fixed pinion curvature ± **0.002 /m** above 9 m/s. This occurs in **29/29 commands** in this window. The executed update passes the **clipped** curvature into `correction()`.
2. The attached wheel target still represents the **original**, unclipped control request. Recomputing it with that original request agrees within **0.00000264 degrees**: the packet/calibration itself is consistent.
3. The calibrated-feedback helper instead recomputes the wheel target from the clipped argument. Its mismatch exceeds 0.5 degrees in **28/29 commands**, reaching **48.58 degrees**. The helper returns no feedback pair; correction state is cleared and `invalid_calibrated_feedback` is reported.
4. All 29 frames have valid CAN/fault feedback and pass the independent freshness/calibration evidence guard. This is not missing calibration, a stale snapshot, or a bad-yaw flag in this window.
5. Output equals clipped feedforward in **29/29 frames**. Added tracking and sustained terms are zero. The final slew limit is not pending; DBC range clipping is not the binding layer.

Representative endpoints (sign encodes direction, not degree units):

| Quantity | First focused command | Last focused command |
|---|---:|---:|
| Speed mph | 23.52 | 22.33 |
| Requested curvature /m | -0.004209 | -0.021511 |
| Fixed pinion curvature /m | -0.001783 | -0.008202 |
| Allowed/clipped curvature /m | -0.003783 | -0.010202 |
| Original requested wheel target deg | 15.65 | 86.29 |
| Measured wheel deg | 6.60 | 30.20 |
| Feedforward before deviation clip, path rad | -0.072924 | -0.357943 |
| Actual generated path command rad | -0.065530 | -0.169762 |

Even substituting calibrated wheel curvature leaves the original request outside the same ±0.002 band in **27/29 frames**. The discrepancy cannot be explained away solely by fixed versus calibrated pinion mapping. This does not establish that the EPS could or could not follow a different, properly validated command.

### Why it does not catch the turn earlier

Before clipping, demand is below the helper's 0.25 m/s² threshold until about route time **219.385**. Only three consecutive send-time observations pass the basic calibrated-pair predicates before clipping starts at **219.534**—about **0.15 seconds**. Existing deficit/admission history cannot be established in that interval. The low-speed fade is already small near 24–25 mph; the independent mid-speed episode only covers above 25 mph. There is no demonstrated 1.20→1.25 solution here.

The alert is software evidence of desired-versus-actual turning plus lateral saturation. It is **not an ECU report proving hard EPS torque/angle saturation**. Similarly, application clipping is not a Panda TX rejection: no rejected command echo occurs in the focused window. The host starts clipping above 9 m/s; the native shadow-curvature check uses its own 10 m/s speed threshold and min/max measured-curvature window. Preserve both protections and do not equate those distinct predicates.

### Next local design

Separate **original intent**, **validated wheel/body feedback**, and **feasible/clipped command** in the correction interface. Validate the atomic target using original intent; classify deviation limitation explicitly rather than treating it as corrupt calibration. Keep the permitted command envelope authoritative. Then evaluate whether fresh, bounded rising-demand evidence can act **before** the clamp binds, without reducing safety margins, dropping freshness/driver checks, or replenishing budgets improperly.

The severe clipped part has no additional outward headroom under the existing controller envelope. A prototype must show useful pre-clip command changes and preserve shadow intent; merely making the feedback predicate pass is insufficient. If bounded onset cannot help this request, report that limitation and investigate model/reference/path feasibility rather than promise that extra gain will make the vehicle follow it.

## 74 mph: reduction exists, but is intermittent and small

These steering inputs are **user-reported tire-debris avoidance**, not confirmed tracking-failure takeovers. The input windows and following second are excluded from tracking attribution. Excess before the inputs is a separate observation, not the established cause of intervention. No video/lane-crossing conclusion is made.

| Pre-input window | Body response median | Nonzero trim commands | Maximum actual command trim |
|---|---:|---:|---:|
| Before <private clock time>, 2.8 s | 110.7% | 4/56 | 2.15% |
| Before <private clock time>, 2.8 s | 127.3% | 19/56 | 3.39% |

The second window also has **127.1% wheel-target response**. Shifting the body reference back 0.25/0.4 seconds leaves **123.6/121.3%** response, so simple delay does not explain all of it. Yaw covariance is correlated and these percentages are observational estimates, not confidence bounds or safe gain recommendations.

### Verified command causes

- No curvature-deviation clipping in either highway window. Final prototype slew is not binding. Target consistency is good; this is not stale calibration or the low-speed target-mismatch mechanism.
- Current body excess and sustained-body margins, wheel deadband/direction, and predictive wheel closure can withdraw permission. That resets the five-frame persistence counter; readmission restarts the 0.0003 rad/frame onset ramp. The first window has six candidate confirmation bursts of 4, 1, 7, 1, 3 and 1 observed frames; most cannot build a reduction. The second is less fragmented but still spends half its observed commands at zero actual trim.
- The **15% maximum reduction is not reached**: measured trim remains below 3.4% in the second window. Raising that cap is not the first issue to solve.
- `EarlierUnwindOnset` explicitly requires **60 < mph < 70**. It gives **zero earlier-onset credit** in these 74 mph frames. Its independently validated history is therefore not used to accelerate this band.
- The 70–75 mph region blends independently maintained branches. Extension weight ranges **3.8–13.2%** in the first window and **9.0–23.5%** in the second; the older upper policy remains dominant. Do not diagnose the newest branch's reason string alone as the actual transmitted effect.

### Separate mapping hypothesis, not yet a validated fix

Roll-aware feedforward mapping is explicitly faded out by **70 mph**, so it is inactive here. The atomic wheel target still incorporates learned ratio, stiffness, offset and roll. Converting that recorded target back through the same calibrated model with zero roll gives a tire-curvature target about **15% smaller** than the request in the second window (about 27% smaller in the first). This is a **static model/reference difference**, not a recommended path-angle reduction or a proven vehicle transfer function. The existing 15%/0.01 rad map bounds and all safety predicates would still apply to any separately evaluated extension.

### Next local design

First evaluate earlier bounded onset in **70–75 mph** using already independently confirmed wheel/body history, while retaining immediate withdrawal when current evidence or predictive closure fails. Do not simply hold an old correction across unsafe evidence. Exercise 70/75 mph transitions, reversal, driver/brake takeover, aborted turns, residual release and budget/state independence.

Keep a possible mapping-scope extension as a separate comparison so its benefit and side effects can be attributed. Do not combine it with a global gain retune or infer performance at 85 mph from this one bend. No new 75–85 mph evidence exists in this acquisition.

## Source pointers

- [Executed deviation clip and correction ordering](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Calibrated target/feedback validation](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Invalid-feedback reset](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Low-speed fade](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [High-speed permission reset, confirmation and ramp](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Earlier-onset speed coverage](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Roll-map speed coverage](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [70–75 mph independent-branch blend](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Software saturation-alert condition](../../navigator-reference/PRIVATE_ARTIFACTS.md)

Artifacts: `reconstruction/`, `instrumented-final/`, `layer-analysis.json`, `low-onset-predicates.json` and `verification.json`. No prototype/control-code edits, gain change, full-corpus safety replay, hardware test or physical improvement is claimed.
