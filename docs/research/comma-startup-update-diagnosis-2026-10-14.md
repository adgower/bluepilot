<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Comma startup/update diagnosis — 2026-10-14

## Findings

Existing logs directly confirm that the connectivity/update startup gate has blocked on-road startup. No reboot, service interruption, active CAN operation, update attempt, or device modification was performed.

The user reports needing phone hotspot connectivity and then a reboot before driver-assistance features become available. The exact UI text remains approximate. This session did not reproduce the ignition-on failure or validate recovery while parked.

## Captured evidence

- `/data/log/swaglog.0000016207`: Startup blocked at <private wall-clock timestamp> UTC (<private clock time> America/Chicago). `up_to_date=false`; all other logged startup conditions true. Ignition, not_onroad_cycle, and device_temp_good all true.
- `/data/log/swaglog.0000015934`: same gate failure at <private wall-clock timestamp> UTC.
- `/data/log/swaglog.0000015885`: same gate failure at <private wall-clock timestamp> UTC.
- `/data/log/swaglog.0000015832`: same gate failure at <private wall-clock timestamp> UTC.
- `LastUpdateTime`: <private wall-clock timestamp> (saved value).
- `UpdateFailedCount`: 28; `UpdaterState`: idle; `UpdateAvailable`: 0 at inspection.
- UptimeOnroad=190587.63875463494 seconds; LastUpdateUptimeOnroad=4754.704342095006 seconds: 51.6203 on-road hours elapsed.
- RouteCount=214; LastUpdateRouteCount=11: 203 routes elapsed.
- DisableUpdates and SnoozeUpdate parameters absent. Offroad_ConnectivityNeeded was absent at this offroad inspection; the historical event establishes it previously blocked startup, not that it remains blocked now.
- Existing registration cache is present and not UnregisteredDevice; historical blocked events list registered_device=true.

## Update failure

Saved LastUpdateException and Offroad_UpdateFailed report:

```text
command failed: ['git', 'submodule', 'update', '--init', '--recursive']
error: Your local changes to the following files would be overwritten by checkout:
    opendbc/car/ford/lateral_angle.py
Aborting
fatal: Unable to checkout '0bd0763bcf88553f570b1de457ad6c0dc76fca83' in submodule path 'opendbc_repo'
```

Read-only Git status with GIT_OPTIONAL_LOCKS=0 confirms that file modified in BOTH `/data/openpilot/opendbc_repo` and `/data/safe_staging/merged/opendbc_repo`. The update failure is a checkout conflict involving local steering code. Do not discard, stash, reset, overwrite, or deploy over that change without preserving and reviewing it.

## Installed code behavior

- `/data/openpilot/openpilot/system/hardware/hardwared.py:345`: up_to_date requires absence of Offroad_ConnectivityNeeded, unless DisableUpdates or SnoozeUpdate is enabled. No such setting was changed.
- `/data/openpilot/openpilot/system/updated/updated.py:33`: blocking thresholds are 27 on-road hours AND 84 routes since successful update/check bookkeeping; prompts begin at 23 hours AND 80 routes.
- `updated.py:273-340`: successful checks reset counters; failed operations may set connectivity alerts. If more than 15 attempts fail while internet is available, the failure-warning branch takes precedence over the connectivity-alert branch. This can explain temporary relief when internet returns, but the exact hotspot/reboot sequence has not been reproduced.
- `updated.py:435`: failure count starts at zero per updater process, rather than loading the saved count. Reboot can alter alert bookkeeping; this is not a repair of the local source conflict.
- `hardwared.py:400-420`: logs Startup blocked and Startup after block with each gate value; those logs supplied the actual failure signal above.
- `/data/openpilot/openpilot/system/athena/registration.py`: cached registration avoids initial online registration. Current evidence does not support registration as the observed blocker.

## Clock limitation

Logs after boots jump back to 2026-07-28, then later regain current October time. This may reflect unsynchronized boot time, but its cause has not been investigated. Filesystem July timestamps previously reported for CarParams do not reliably establish acquisition age. The cached ECU data remains saved evidence, not a fresh response, regardless of its timestamp.

## Recommended next step

Preserve and review the changed lateral_angle.py and reconcile it with the intended installed branch/submodule revision in an isolated local checkout before any device repair. A durable repair should make the updater work while retaining the intended steering behavior. Hotspot availability alone cannot resolve Git refusing to overwrite the file.

For the next observation, remain parked in a ventilated location, identify the exact screen text, connect the hotspot, and record whether it recovers without rebooting. Do not run the engine in an enclosed garage, reboot while driving, or treat temporary gate relief as verified repair.

## Limits

This confirms historical startup-gate failures and a current saved updater error plus source changes. It does not establish a live reproduction, exact original boot timing, or a tested fix. No fix was applied.

## Authorized temporary pause applied

On 2026-10-14, owner explicitly authorized disabling updates temporarily. Set DisableUpdates=true using the installed Params API with blocking write and read back true. Steering file SHA256 remained bc205573c3cda6b0ec77e4ec262eab11595adaaf3e0f8ace781b22992105d780 before and after.

No reboot or service interruption performed. Installed hardwared reads this setting repeatedly, so it bypasses the connectivity startup gate without a reboot. updated.py reads DisableUpdates only at process startup; the already-running updater may continue until its next restart. A parked reboot is needed to ensure the updater exits on startup. No runtime startup recovery has been tested. Reverse the pause by setting DisableUpdates=false when the preservation/update repair is ready.
