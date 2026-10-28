<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Model acceleration and grade-related switching — October 24, 2026

## Outcome

Local investigation, three diagnostic controller prototypes and replay checks completed. **No overall pulsing fix is ready to integrate or install.** A narrow neutral-intent prototype modestly reduces switching in the 50–55 and60–65mph bins, but leaves most other problem ranges unchanged and adds one rapid reversal in an older35–40mph recording. The other two prototypes did not improve the selected episodes or made some worse. No device contact, ECU queries, CAN transmission, settings changes or paired-source edits occurred. Steering and owner1.20/0.97 remain unchanged.

## Coverage and reproduction

Audited nine cached Alpha session datasets: active no-pedal exposure reaches73.787mph; none supplies valid75–85mph Alpha exposure. This does not exclude older high-speed lateral/OEM recordings, which cannot validate Alpha response.

Reconstructed the actual current controller over three Alpha input sessions /61 saved segments /179,144 callbacks, with20 selected 20-second episodes across every populated range through70–75mph. Current drive reconstruction matches all 67,687 sampled recorded brake/gas/fault/reason results within1e-5 gas tolerance. Every minimized baseline fixture also matches its reconstructed ACC wire bytes exactly. Older recordings ran older code: their counterfactual current-controller output differs from recorded output, explicitly retained as a fidelity limit.

The original fast fixture remains red on the symptom:15brake edges /7rapid reversals in20s. Fresh fixtures include50–55mph11edges/4rapid,55–60mph14/7,60–65mph21/12 and65–70mph18/5. These are command-level signatures; an edge count alone cannot establish unnecessary braking or physical discomfort. No speed bucket is assumed good because it was previously described as good.

## Model findings

Past-only model/planner/lead/control alignment confirms the model frequently limits requested acceleration, independently of cruise set speed. No-lead highway under-speed is not explained by an explicit62mph cap or forceDecel: under-speed samples have zero forceDecel exposure. This is not proof the model is reading a posted speed limit, nor proof the road is clear.

| Latest-drive speed | Model selected / eligible seconds | Brake entries with model selected / total |
|---|---:|---:|
|50–55mph|64.7/70.3|14/14|
|55–60mph|170.9/242.6|28/36|
|60–65mph|251.4/284.6|39/42|
|65–70mph|159.5/163.8|42/43|

Both relaxed (682.40 s) and aggressive (358.38 s) are represented, with 0.36 s standard during transitions. Their main differences are radar time gap and MPC cost settings. They do not directly retune this model's acceleration or Ford actuator coordination. This supports the owner's observation that switching personalities did not remove pulsing.

The model's median requested acceleration in these bins is only~0.03–0.09 m/s², with positive and negative excursions. Because the planner chooses the minimum of model/radar/cruise acceleration, a high set speed does not force acceleration toward it. Removing model slowing or increasing acceleration globally is not justified by a missing radar lead. The investigation leaves model stop/slowdown decisions intact; there is no demonstrated safe model-policy replacement or faster-launch fix in this prototype.

## Grade/admission findings

Several mechanisms overlap:

- Positive requested acceleration can still require actual braking downhill when actual acceleration exceeds demand. For example, new50–55mph entries outside the existing weak-net band have median measured acceleration0.23m/s² above requested. Blocking all braking whenever raw acceleration is positive would be incorrect.
- Existing bounded coasting requires raw acceleration>0.02m/s² and compensated net>−0.05m/s². Tiny neutral/negative model demands bypass it. Larger negative net, pending physical clearance and pressure still present also bypass it.
- Existing admission expiration, brake release and grade-threshold crossings can generate very short brake/release cycles. That fact alone does not identify the correct ECU coast response.

No interval in the latest recording meets the strict passive-coast identification screen: inactive propulsion, no commanded brake, received brake torque<=4Nm, measured propulsion torque<=0Nm and at least0.5s sustained qualification. This does **not** mean the car never coasts; it means these data do not identify a settled zero-drive/zero-brake response under that screen. In particular, a road-load/coasting map must not be invented from the short release transient or camera pitch alone.

## Local prototypes

All are explicit offline subclasses in experiment.py; the paired branches are untouched.

1. **Pending-release continuity:** retain a weak release while measured acceleration is below demand, bounded by0.3s/0.01m/s demand debt and existing measured clearance. No meaningful improvement across selected latest-drive episodes. Not selected.
2. **Tracking-aware coast entry:** short bounded coast only with fresh measured under-acceleration and no visible lead/FCW. It worsened the selected50–55and60–65mph episodes. Not selected.
3. **Neutral-intent admission:** reuse the existing0.3s/0.01m/s bounds and−0.05m/s² net boundary for raw requests between−0.1and0.02m/s², only without visible lead/FCW. Does not modify model, PID acceleration, brake acceleration value, torque-clearance checks, timeout or lateral code. The narrow scope produces modest changes, not an overall solution.

### Neutral-intent full-route screening

Aggregate eligible command results across the three replay inputs; this is not a count of proven unnecessary braking.

| mph | Brake edges, baseline→candidate | Rapid reversals, baseline→candidate |
|---|---:|---:|
|0–30|unchanged|unchanged|
|30–35|32→32|10→10|
|35–40|63→61|24→25|
|40–45|2→2|0→0|
|45–50|14→14|3→3|
|50–55|28→26|7→5|
|55–60|94→94|25→25|
|60–65|132→130|39→37|
|65–70|172→172|26→26|
|70–75|116→116|43→43|
|75–85|no Alpha exposure|unvalidated|

Only 281 ACC packets change among179,144 callbacks. No changed packets occur when inactive, below3m/s, during stopping/starting phases, or with raw deceleration<=−0.1m/s². All brake-acceleration numerical values remain identical. No new coordination-fault samples appear. The same three pre-existing release_timeout_disengage episodes remain at the same replay callbacks. Retaining those faults is not resolving their ECU-response cause.

## Checks

- Nine focused contracts pass, including preserved lead/strong-demand braking, stale/invalid tracking fallback, bounded pending exposure and no elapsed-time-only rearming. Red contract/fixture outputs retained.
- Twenty minimized baseline fixtures reproduce reconstructed ACC bytes; candidate comparisons recorded.
- Full native hooks replay recorded RX, all original non-ACC TX and native timers, replacing 179,133 reconstructed ACC slots. 14,338,901 received packets and 429,929 transmitted packets per variant; **zero added candidate rejections**, no relay faults, no forced controls permission. Existing recorded/baseline rejections are retained in results; zero added does not mean zero absolute rejections.
- Native test library freshly compiled from current child 3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1 with debug hooks matching the existing Ford parameter 11 path. macOS denied loading the UBSan runtime; normal unsanitized native compilation was used, recorded in provenance. No sanitizer coverage is claimed.
- Research comfort acceptance remains **red**: incomplete benefit and the35–40mph rapid-transition regression. This prevents treating native-hook success as proof of smoothness.
- No ARM/full product rebuild, hardware validation or physical counterfactual response claimed. These are research-only adapters, not integrated code.

## Next engineering work

The remaining problem needs a combined planner/PID/ECU-response investigation, rather than another brake-bit delay increase. Trace consumed planner acceleration, integral state, requested acceleration and measured wheel/brake torque through the same release/acceleration episodes. Establish which response is natural coast versus retained pressure and drive torque before selecting a brake/coast map. Do not turn the fixed grade-reference correction into a road-load fit, force speed past model slowing, or mask release timeouts by extending deadlines.

No additional uncomfortable high-speed Alpha drive is needed to establish that the present prototypes are insufficient. Existing lower-speed/OEM recordings can be used for the next passive response analysis.75–85mph remains an explicit future validation gap.

## Reproduction and artifacts

Use the paired checkout's `.venv/bin/python`. Run `fixture_check.py` for episode comparisons, `test_experiment.py` with pytest`-o addopts=''`and this folder as `--confcutdir`, `compare_full.py` for preservation checks, and `acceptance.py` for the intentionally failing overall research gate. Raw recordings, fixture payloads and reconstructed traces stay under `/private/tmp`; public JSON artifacts contain counts, relative analysis and cache pointers. Input source/settings provenance is linked from `navigator-alpha-comfort-investigation-2026-10-24`.
