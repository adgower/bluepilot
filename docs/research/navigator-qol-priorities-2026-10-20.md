<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator priorities: upstream Autospeed, MADS and Ford longitudinal

Checked October 20,2026 (America/Chicago). Planning/research only. No merge, working-source edit, device connection or parameter/firmware change. Upstream refs were fetched; current paired checkouts remain clean. Last documented installed pair is openpilot f7b0c47d23de697b73f1247cd5d32021b37e19bc / opendbc 8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e; powered parked acceptance passed, latest onset road benefit unproved.

## Recommendation

Close the newly installed steering trial with its next ordinary drive review, then stabilize that configuration while adding QoL. Refresh the paired baseline from current upstream locally before adding the next feature. Best near-term feature candidate is optional MADS with stock Ford ACC; the biggest eventual capability unlock is reliable Ford longitudinal plus upstream Autospeed. These are qualitative value/effort judgments, not measured WSJF scores or an approved implementation plan.

| Workstream | Likely value | Effort/uncertainty | Recommended sequencing |
| --- | --- | --- | --- |
| Latest steering road review | Finds regressions before stacking changes | Saved/new ordinary drive evidence needed | Close current trial; retain85 mph evidence gap |
| Upstream master refresh | Maintains compatibility and adopts upstream defaults | Moderate integration, runtime timing/planner changes | Foundation before next feature; separate candidate, no device auto-update |
| MADS with stock ACC | Independent lane centering while manually managing speed or using OEM ACC | Cross-layer engagement/UI/Panda behavior; meaningful safety work | Preferred next convenience feature; opt-in/default OFF |
| Ford brake/propulsion coordination, then Autospeed | Largest eventual automation gain | Higher vehicle-response uncertainty; brakes, grade, release and restart proof | Separate main research track; retain OEM ACC until validated |
| Extra gains/automatic calibration/ICBM | Benefit depends on unresolved evidence | More coupled behavior and maintenance | Defer broad ports; target demonstrated deficits only |

## Current master and what Autospeed means

Fresh commaai/openpilot master: **1ace967a7e27d2537a956c683978f646d6b6d739**. Installed-source branch has13 own commits and is21 upstream commits behind (git rev-list HEAD...upstream/master). The two histories share base 6eb63e045469a582f4c7b406705543e891113606.

[Current pinned release notes](https://github.com/commaai/openpilot/blob/1ace967a7e27d2537a956c683978f646d6b6d739/RELEASES.md) describe Autospeed under 0.11.3 with a placeholder release date. This is development-master behavior, not proof of a shipped stable0.11.3 release. Scene-aware model speed planning previously exposed through Experimental mode becomes the default on supported cars; the cruise setting is treated as a maximum. Current source removes ExperimentalMode and obsolete Chill selection. [A New Dawn commit](https://github.com/commaai/openpilot/commit/f50108b4a), [planner at checked master](https://github.com/commaai/openpilot/blob/1ace967a7e27d2537a956c683978f646d6b6d739/openpilot/selfdrive/controls/lib/longitudinal_planner.py).

AlphaLongitudinalEnabled remains a separate development-only vehicle actuation opt-in. Autospeed planning, Ford gas/brake actuation, MADS engagement independence and ICBM cruise-button emulation are separate layers. With OEM ACC controlling speed, merging the planner does not grant openpilot control of Ford braking or turn OEM ACC into traffic-light-aware Autospeed. Removing ExperimentalMode also means preserving an old off value is not a way to retain the old Chill behavior after a stock-default update.

Master still pins upstream opendbc b3bd79a659dae961af169a3baac723961f720133 and Panda a59195163c32a3a375ea6c86715dc08fd0984c1b. Those pins match the prior upstream base; the custom child must remain8ccc6cf0..., not be replaced with upstream's child pin. The checked update changes msgq and runtime scheduling; no AGNOS manifest or driving-model asset changes were found in this21 commit interval. No OS/firmware update requirement is established by this diff alone.

Suggested maintenance: merge upstream in an isolated local candidate, preserve custom child/forkURL/1.20/0.97/settings, review Card/schema/planner/Ratekeeper changes, run affected tests plus the existing regression/replay checks once at final candidate. Keep upstream refresh separate from a new longitudinal or MADS experiment. There is no urgent need to replace a just-installed build merely because21 commits exist.

## The earlier shaking investigation and candidate

Read the actual [Analyze Alpha Long shaking](../navigator-reference/PRIVATE_ARTIFACTS.md) final discussion and current [draft PR #3](https://github.com/adgower/openpilot/pull/3). It targets the old navigator-angle-v1 branch; parent d8123f013353bf3fb2240c78bb41c3dba2b31cdf pins child d5ccadb7f9abcbee84f86dafd10e30c8e2f4e6ff. It is still draft and unmerged in the checked page, with zero reported checks there.

That Expedition-only candidate forces propulsion to the inactive sentinel while the existing brake latch is asserted. Earlier38 controller tests and safety/replay passed;752 of 2,984 ACC frames changed only the propulsion field. These are prior candidate results, not rerun here or proof of a judder cure. Brake release, launch and grades remain unvalidated. Current installed-source carcontroller still lacks that brake-latch propulsion override. Do not install the old branch over the modern paired steering branch: port and reassess only the narrow candidate on the current baseline. [Existing detailed evidence](navigator-longitudinal-coordination-2026-10-14.md).

The old OEM/Alpha comparison's approximately 5.7 times vibration difference was a speed/deceleration subset from different intervals, not a randomized causal test. It justifies investigating command coordination before blindly changing PID gains, smoothing or an entire speed map. Distinguish requested acceleration, emitted Ford fields, actual acceleration and vibration; first test mutual exclusion and proper release, then jerk/delay/response, then upstream scene-aware planning behavior. On newest master there is no stock Chill toggle for the public road stage, so any staged planner comparison should be local/replay or deliberately scoped rather than a claim of stock mode availability.

## What BluePilot already improves

[Full cited BluePilot review](navigator-qol-priorities-2026-10-20-bluepilot.md) pins bp-dev d27bc20a7c13eed7ec1947d4c59b98835facea87. Its [LongitudinalExt](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/opendbc_repo/opendbc/sunnypilot/car/ford/longitudinal_ext.py) separates precharge/deceleration thresholds, suppresses propulsion whenever braking is requested, and adds lead-aware highway coasting. It retains inactive predicted acceleration and a fixed maximum target-speed field; the highway overlay is not a general stop/go repair. [Maintainer README](https://github.com/BluePilotDev/bluepilot/blob/d27bc20a7c13eed7ec1947d4c59b98835facea87/README.md) still recommends stock Ford ACC. It does not establish a Navigator road-proven fix. Open PR #212 changes Lightning/Mach-E EV behavior and leaves ICE Fords unchanged.

MADS exists in the sunnypilot-derived BluePilot implementation and can work with OEM ACC; bringing it to vanilla requires independent application/lateral state, clear button/brake/cancel/DM/fault semantics, UI and matching Panda permission/heartbeat behavior. DefaultOFF and explicit driver opt-in preserve vanilla behavior for normal use. Use current source/reference behavior, not a guessed one-line enable change. ICBM is separate Alpha stock-ACC speed-button automation; defer it as a first QoL port because it adds another speed-control path and has a history of Ford mapping/speedCluster defects.

## 85 mph confidence

Do not equate near100percent wheel/body request tracking with lane stability. Lane-edge errors, path choice, curvature onset/unwind, calibration/roll mismatch and driver interventions also matter. The latest earlier-onset correction operates strictly60–70 mph; its accepted >=75 mph replay parity preserves previous output rather than newly validating85 mph.

Use saved83/85 mph bends and prior lane-edge/takeover windows for replay, timing and path review now; ordinary legal-speed drives can still expose timing/calibration weaknesses before the trip. Fresh representative road evidence near85 mph remains absent for the new installation and cannot be manufactured by extrapolating65mph response or passing safety hooks. No high-speed gain or safety-limit increase is recommended. Record road condition, curve context and intervention times on naturally occurring drives within posted limits; keep this evidence requirement open before claiming the behavior stable.
