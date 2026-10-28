<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local review candidate

Goal: prepare, never deploy, an experimental Ford safety mode and one-shot local tool. Snapshot base: opendbc18175406d0cc5af8233afde70a5d121aedf8de44.

1. Write failing host tests for normal-build rejection and experimental permit/limits.
2. Add a compile-time AND debug-build AND safetyParam0x4000 gate. Test mode has its own TX list containing only0x461/bus0/8; normal Ford lists unchanged. Fresh raw speed/gear/standstill/parking-brake/cruise/status and stock context required. Permit one100–200ms press/release pair per initialization; unexpected attempts consume the trial. No controller/firmware installation changes.
3. Write failing pure tool tests; implement a transport-free one-shot core plus a JSONL input / JSONL intent-output CLI. It emits at most two transmission intents, never opens CAN, Panda, SSH or messaging sockets. A live adapter is present for source review and mock testing, but its CLI execution is disabled pending separate review/authorization and real transport/recording verification. This makes the review tool usable offline without pretending an unvalidated hardware adapter is ready.
4. Compile normal and experimental safety host harnesses; test constraints and run existing Ford regression tests. Independent code review; fix findings.

Unresolved: PCM consumption, duplicate sequence tolerance and coexistence. Payload strategy copies latest observed stock context and patches only bit0; no invented counter progression. No claim of successful vehicle control. Timing bounds are experimental test policy derived from brief captured pulses, not OEM limits.
