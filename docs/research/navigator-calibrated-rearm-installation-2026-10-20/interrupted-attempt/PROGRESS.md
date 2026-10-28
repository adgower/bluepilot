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
