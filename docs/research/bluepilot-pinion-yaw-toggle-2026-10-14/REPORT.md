<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# BluePilot Use Pinion Yaw Sensor investigation

2026-10-14. No changes to the Comma.

## Result

Yes: newer locally cached BluePilot upstream branches contain a setting titled **Use Pinion Yaw Sensor**, key `FordPrefSteerAngleCurvature`. It replaces yaw-based measured curvature with a steering-pinion/vehicle-model estimate. It does not select another physical yaw-rate sensor, repair the original sensor, recalibrate an ECU, or use Comma's gyro as the direct steering-feedback source.

This is a relevant candidate workaround for the decoded yaw baseline mismatch found in this Navigator's recordings. It is not proof of a defective RCM or a complete low-speed tracking fix.

## Source provenance

Read-only local Git snapshots:

- upstream/bp-dev-expedition: 3210caa02d9e09b46d08be490f689edb23b22b20.
- upstream/bp-dev: 501a7c0e911245044196fcc90cb077a69fa0749b.

Both cached refs contain the key and UI label. Remote branch tips were not refreshed in this pass. The currently checked-out local bp-dev is an older/different source layout; the toggle was found by reading cached newer refs without switching or changing the checkout. Source snapshots are saved alongside this report for inspection.

## UI and behavior

- `selfdrive/ui/bp/mici/layouts/settings/vehicle_mici.py:24`: MICI vehicle panel labels the setting Use Pinion Yaw Sensor.
- `selfdrive/ui/bp/layouts/settings/bluepilot.py:126`: other settings layout has the same label and describes steering-pinion measurement as a workaround for faulty vehicle yaw feedback. Examples in the UI include weak curve tracking and steering-limit warnings. Those descriptions are the authors' intended use, not an independently diagnosed hardware fault for this vehicle.
- `common/params_keys.h:327`: persistent/backed-up BOOL, default 0; read at car initialization.
- `opendbc_repo/opendbc/sunnypilot/car/interfaces.py:139`: initialization converts the setting into a separate Sunnypilot safety parameter flag plus platform geometry-table index.
- `opendbc_repo/opendbc/sunnypilot/car/ford/values_ext.py`: Expedition platform has geometry index 4; Edge is excluded because its relative-angle path lacks the required absolute measurement.
- `opendbc_repo/opendbc/sunnypilot/car/ford/lateral_curv_ext.py:246`: when enabled, controller curvature is derived from pinion angle, learned angle offset, roll and VehicleModel. Otherwise it uses -yawRate/speed. Learned ratio and stiffness are applied to the control-side model.
- `opendbc_repo/opendbc/safety/modes/ford.h`: the paired safety flag selects pinion-based measurement and appropriate pinion receive checks/geometry. This is a different feedback source while retaining safety checks; do not emulate it by setting an unrelated flag in the owner's fork.

The source documents activation at the next car initialization/restart, not a live mid-drive toggle. The controller and safety estimators are intended to use the same source, but their geometry and calibration details are not identical; their consistency requires review/tests.

## Installed Comma distinction

Read-only SSH confirms owner is running openpilot/adgower navigator-angle-v1 at f35e6e5eb11ca9cddad3ed945d44d8f191679240, not the inspected BluePilot branch. Installed source search of params keys, UI, Ford control code, and safety code found no FordPrefSteerAngleCurvature, Use Pinion Yaw Sensor, or PINION_CURVATURE references. The saved parameter key is absent.

Therefore this setting cannot simply be switched on in the currently installed software. Creating that parameter by hand would not enable the missing code. Moving branches or porting the feature would be a separate implementation/deployment task, with existing steering changes preserved and compatible safety firmware verified. Nothing was installed, toggled, flashed, rebooted, or changed here.

The previously observed pending navigator-angle-v1 pinion-curvature changes are related in concept but differ from BluePilot's user-toggle/SP-safety-parameter implementation. Do not assume the key or geometry bits are interchangeable.

## Does it address this vehicle's problem?

The recorded raw yaw baseline persists while stopped and the independent motion estimate is near zero. Pinion-based feedback would avoid using that biased yaw measurement for the relevant controller feedback. That makes it a reasonable first candidate to evaluate before additional gain tuning.

It would not remove the original yaw offset, prove the underlying vehicle module healthy, or automatically improve every low-speed turn. The two selected sustained low-speed turns were not curvature-clipped, so replacing feedback alone would not change their command through that limiter. Separate low-speed gain/response issues can remain.

Recommended next step is an offline comparison of the applicable pinion implementation against the already-saved recordings, including geometry, driver overrides, low/high speed, both turn directions, and paired safety checks. Preserve the current tuning and successful high-speed behavior. No direct jump to a new branch or firmware is justified by UI presence alone.

## Existing diagnostic utility

The cached branch includes `tools/ford_yaw_health_check.py`, which compares CAN yaw, steering geometry and Comma motion across recorded routes. It was read but not run. Its documented historical example is a different Explorer with variable yaw gain; it must not be conflated with this Navigator's measured baseline offset. It expects older livePose/liveParameters message names, whereas the owner's current recordings use DeviceMotion/VehicleParameters. An adaptation or careful schema compatibility review is needed before using its output on these logs.
