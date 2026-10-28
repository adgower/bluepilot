<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Authorized highway correction installation

User explicitly authorized push, backup and install; confirmed parked, ignition off, stable power/Wi-Fi, screen/recovery access. Publish exact paired branches to existing authorized adgower origins. No OS/firmware updates, ECU query or longitudinal changes.

1. Verify current sources/live OS20, ignition-off passive telemetry and clean sources. Push child then parent without force, verify remote heads.
2. Fresh private source/settings/launcher/firmware backup and hash-verified Mac copy. Preserve whole existing install for rollback. Source staging is separate.
3. Isolated ARM build and native/controller/pipeline tests in separate staged checkout, private params/cache, no network/device access; retain active runtime. Verify settings/source identity.
4. Preserve firmware and launcher, prepare self-contained Git stage. Offroad guarded source swap with rollback to whole previous install if acceptance fails. No reboot/OS operation.
5. Passive ignition-off acceptance, then request ignition-on in Park/disengaged for passive powered checks. No road readiness/physical benefit inferred from static or parked checks.
