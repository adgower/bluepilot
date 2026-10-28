<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local Ford longitudinal coordination investigation

Scope: compare installed-source pair 24e981d6d / 01f32a6f with the older d5ccadb7 candidate and original Alpha/OEM recordings. No paired-source edits, device access, publishing or installation.

1. Pin source and raw-log hashes; recover earlier command/response evidence.
2. Re-extract original logs with the current schema and decode ACCDATA with current DBC.
3. Replay frozen recorded inputs through current controller and a report-local copy carrying only the earlier propulsion withdrawal. Compare emitted fields and existing native TX-hook acceptance, separately from physical response.
4. Examine real OEM brake-release timing plus current controller pitch/creep/latch transitions, disengagement, restart and other-platform/default-stock parity.
5. Record supported diagnosis, unresolved causes, missing evidence and next narrow implementation scope. Update roadmap; leave installed/current paired branches unchanged.
