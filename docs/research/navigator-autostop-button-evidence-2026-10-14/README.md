<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator Auto Start/Stop button evidence — 2026-10-14

Preserved locally from the ten cached post-correction drive segments. No device access or CAN transmission. The user identified the A/circular-arrow Auto Start/Stop disable button and estimated about five presses near the beginning of this drive.

Six rapid **status transitions** were observed near 90.88–94.78 seconds, alternating selected (0) / deselected (1). Numeric context puts speed near15mph and engine state1 throughout. Six status transitions do not establish exactly six physical presses, and these were not ignition-button events.

`main-bus-evidence.jsonl.zst` contains all70,808 recorded main-bus frames for0x166 (status),0x167 (engine bits),0x326 (request),0x105 (alternate request) across the complete drive. Rows contain relative time, segment index, address, exact payload, decoded value and native-DBC-check indicator. No location, images, VIN, route/account identifiers or parameter dump is included. The engine-bit extraction was not independently native-DBC checked by this preservation script.

`raw-transition-frames.json` preserves the exact six transition payloads and the explicit time-origin difference from `button-transitions.json` (previously verified speed/engine context). `manifest.json` records source segment sizes/SHA256, counts and limits. `provenance.json` pins source/DBC. `preserve.py` reproduces extraction from the private local cache.

**Missing actuation evidence:** all5,901 main-bus0x326 request bits and both main-bus0x105 request bits are0. Thus a physical button-request pulse was not captured at these addresses. Bus1 same-address frames are excluded because their semantics differ. No factory acceptance, safe timing, echo policy or sender implementation is established.

The earlier [packet hypothesis and negative native safety test](../navigator-response-and-autostop-investigation-2026-10-14/REPORT.md) remains research only: the proposed one-bit packet is rejected by current safety, and no sender/allowlist was added. Future work starts with passive capture/mapping of the actual request source, not transmitting the hypothesis.

`SHA256SUMS.json` verifies package files. `evidence.zip` is a portable copy of these files with its own checksum in `evidence.zip.sha256`.
