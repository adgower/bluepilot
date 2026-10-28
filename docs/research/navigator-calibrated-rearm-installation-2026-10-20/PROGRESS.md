<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Installation progress

User authorized paired publication, backup and installation, confirmed parked ignition off, power/Wi-Fi, screen/recovery access.

- Exact child de70d4f945b2bb1472e5207b92d2276137d8c5a1 and parent f750d756caf772c36c01a97be4c03501de8851db pushed non-force; remote heads verified.
- Fresh device backup20261020T162111Z-pre-calibrated-rearm:843,593,091bytes,66params; Mac archive SHA/size,143manifest members and both nested archives verified.
- Separate exact-pair stage /data/navigator-validation/<private timestamp identifier>-f750d756c;262LFS assets hash checked; current active pair remains0171b8972/4167433e.
- Independent installer review found no material blocker; explicit714transition/128abort receipt gates included.
- Isolated ARM build/native checks started in navigator-calibrated-rearm-<private timestamp identifier>.service. Read validation-current.json for latest phase. No activation yet. Keep ignition off.

Next: require successful device build/replay and live preservation; prepare self-contained Git/launchers/firmware; atomically exchange full tree with guarded rollback; ignition-off acceptance; then ask user for ignition-on stationary Park to run passive powered checks. No OS/firmware update.

Runtime progress: isolation probe and full ARM build pass; Ford/native690tests/79skips/12,063subtests pass. Retained320case roll transition screen passes. Further480case sustained screen,714case calibrated screen,128abort cases and Card/pipeline still pending. No activation.

Retained480case/172,800frame sustained/unwind screen passed. New714case calibrated screen now running, followed by128abort cases and Card/pipeline checks. Still no activation.

Connectivity correction: last fresh validation-current.json was2026-10-20T16:55:16Z (480case screen passed). Subsequent shell display commands mistakenly printed that cached JSON after failed SSH. Corrected reporting with poll_once.py, which fails closed. At17:05UTC SSH192.168.1.87unreachable; requested user check power/Wi-Fi/IP. No activation helper has been run. New714/128/Card/pipeline completion unverified.

Fresh SSH recovery: prior unit had aborted after vehicle went onroad (elapsed1707s); source/head hashes preserved, onroad-selected state/manager PIDs changed. User returned and authorized retry with ignition off. Preserved interrupted-attempt and remote evidence-interrupted; new backup/config/unit timestamp in config.json. Reuse same compiled exact-pair stage but rerun full probe/build/replay under fresh parked preservation snapshot. New backup includes intervening learned settings. No activation yet.

Fresh181002Zbackup verified:843,593,059bytes,143manifest members. New unit full ARM build,690tests/79skips/12,063subtests and320case screen pass.480/714/128/Card/pipeline pending. Active old pair unchanged.

Fresh480case sustained/unwind screen passed;714case calibrated screen running. Confirmed via fresh unit status, resource usage304MiB of3GiB. No activation.

Fresh validation complete2954.236s: all probe/build/replay phases0 and live preservation true; onlyUptimeOffroad/LastAthenaPingTime hashes changed. Preparation initially stopped for archived staging manifest; restored only input manifest after rehashing all262assets/exact pair, then prepare passed. Both repos clean/self-contained, firmware/launchers unchanged. Guarded atomic activation and201sample offroad acceptance pass; allselectedpreferences and5learned hashes equal fresh181002Zbackup. Full previous tree retained. Await user ignition-on stationary Park for passive powered acceptance.

Powered acceptance complete:55s passive stationary Park check passed;1,101big-model samples,20.001fps,zero reported drops. Core learned ratio/offset/delay/profile/geometry/flags/safety/extrinsics/torque payload retained. Normal stiffness reset1.048793→1.0and outer torque timestamp refreshed; no stale params restored. Installation and parked acceptance complete; physical tracking improvement remains unproved.
