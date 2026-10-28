<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Full-suite process-isolation correction

Two retained full-suite attempts stalled in `TestLeads.test_radar_fault`, waiting for a replay card fingerprint handshake. Timed Python stacks and a native child sample showed the parent waiting on a fake IPC event while the child waited for ordinary CAN input. The new pipeline test imported `card` at collection time; process modules capture REPLAY at import, and replay uses fork/import-module caching. This leaked live-mode module state into later replay startup.

The integration test now executes its actual producer/card capture loop in a separate Python subprocess with a 30-second timeout. No runtime/controller behavior was changed to accommodate the suite. The pipeline test followed by the previously blocked radar replay passes together (2 tests, 1.49 s). The complete suite is repeated after this test-only fix. Earlier attempts and stack samples remain diagnostic evidence, not passing runs.
