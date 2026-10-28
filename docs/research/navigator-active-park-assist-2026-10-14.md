<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# 2023 Navigator Active Park Assist investigation

## Initial conclusion

Uncertain — more information required. SSH access is established, but no vehicle ECU identification or parking hardware compatibility has been verified.

## Mac SSH access

- No ~/.ssh/config was present. An existing ~/.ssh/id_rsa key authenticated successfully with strict host-key checking against the existing known_hosts entry.
- Current working endpoint: comma@<private host>.
- Repository scripts reference comma@<private host>; that endpoint timed out.
- The SSH agent had no loaded identities; the explicit existing key worked.
- No credentials, SSH configuration, or known_hosts entries were changed.

## Passive device evidence

Read over SSH on 2026-10-14:

| Item | Observed value |
|---|---|
| Device-tree model | comma mici |
| Linux | 4.9.103, aarch64 |
| OS release | Ubuntu 24.04.4 LTS |
| /VERSION | 19.7 |
| Cached Version parameter | 0.11.2 |
| Cached GitBranch parameter | navigator-angle-v1 |
| Cached GitCommit and actual checkout HEAD | f35e6e5eb11ca9cddad3ed945d44d8f191679240 |
| Checkout commit date | <private wall-clock timestamp> UTC |
| Checkout path | /data/openpilot |
| Matching process | pandad, PID 29760 |
| USB product string | custom ed4e39b7-CLEAN |

The USB product string alone does not establish the active Panda firmware version or interface inventory. The process-name filter does not establish the complete openpilot service state. Device model marketing name and Chestnut presence are not independently verified yet.

## ECU inventory and retrofit status

IPMA, PAM, PSCM, BCM, ABS, APIM, gateway, sensor count, switch wiring, As-Built data, and retrofit part numbers remain unverified. No ECU requests have been transmitted.

## Source evidence

- Local scripts/device_health_check.sh and scripts/debug_ui_performance.sh contain the older connection address.
- Local docs/how-to/connect-to-comma.md documents SSH using the comma account.
- Installed utility paths observed: tools/scripts/test_fw_query_on_routes.py, tools/scripts/car/ecu_addrs.py, tools/scripts/car/disable_ecu.py. These were not executed; presence does not establish safety or compatibility. In particular, disable_ecu.py is outside this read-only investigation.

## Next gate

Continue passive source and cached-data inspection. Before any active vehicle diagnostic request, obtain confirmation that the vehicle is stationary, parking brake applied, and driver present; verify the exact request and Panda safety implications. Do not open Panda directly, change safety modes, stop services, execute programming or diagnostic routines, or transmit control/button messages.

No VIN, device serial, SSH key material, or dongle identifier is included.

## Passive source and cache inspection — 2026-10-14

Vehicle off in garage; owner in kitchen; Comma powered through Comma Power/OBD. All findings below came from files or USB sysfs metadata. No CAN interface was opened and no diagnostic request was sent.

### Cached platform and safety settings

Installed `launch_env.sh` explicitly exports `FINGERPRINT="FORD_EXPEDITION_MK4"`. Decoded CarParams confirms `fingerprintSource: fixed`, `carFingerprint: FORD_EXPEDITION_MK4`, brand ford, flags 1 (CANFD), networkLocation fwdCamera, dashcamOnly false, openpilotLongitudinalControl false, and Ford safetyParam 2 (CANFD). Previous-route cache has the same selected fields. This is a forced platform selection, not proof of natural firmware fingerprint matching or current Panda safety state.

CarParams, CarParamsCache, and CarParamsPersistent have identical SHA256 `5be94f007391551d35ec80c2ccaa65d8a06848b7a6d094cca1ed6c88571ac7b6`. CarParamsPrevRoute differs: `b4694181de4982baea815954eb7d622266a7002cf0f7907d7d26fff1f7448001`. Filesystem modification times report 2026-07-28 around <private clock time> UTC; this does not establish actual acquisition time or that the data belongs to the current vehicle. VIN association was not inspected or exported.

### Historical ECU software inventory

These are decoded saved manufacturer-software responses for request `22 F1 88`, with trailing NUL padding removed for readability. They are not hardware service part numbers or fresh responses.

| Saved ECU label | Diagnostic request address | Cached identifier | Evidence confidence |
|---|---|---|---|
| fwdCamera / IPMA candidate | 0x706 | RJ6T-14H102-BAH | High for cache content; physical identity and park compatibility unverified |
| eps / PSCM candidate | 0x730 | NL14-14D003-AE | High for cache content |
| abs | 0x760 | PL14-2D053-AB | High for cache content |
| fwdRadar | 0x764 | ML3T-14D049-AL | High for cache content |
| engine / PCM | 0x7E0 | PL7A-14C204-DE | High for cache content |

The five identifiers appear in saved bus 0 and bus 1 records, mostly marked obdMultiplexing true. This does not prove current OBD routing or access to every vehicle network. No PAM, BCM, APIM, or gateway identification response was established. Absence from this cache does not establish absence of hardware.

Additional cached `22 F1 10` entries are ambiguous: combinationMeter at 0x7C6 and fwdCamera at 0x7C4 both contain `f11044534d4c33542d3134483033312d41480000000000000000`; adas at 0x730 contains `f11044534e4c31342d33463936342d4142000000000000000000`. Cross-brand/utility labels must not be treated as independently identified modules.

### Saved IPMA configuration payloads

| Saved request | Cached response payload hex |
|---|---|
| 22DE00 | ce53a0152a0000000000 |
| 22DE03 | 0a03081e058a05070a03 |
| 22DE0F | 124b0000000000000000 |
| 22DE11 | 08834084000000000000 |
| 22DE13 | 100928000a0c80050505 |
| 22DE14 | 14eb0c28062c050207e5094f06ac07d406b407dbff0b000000665228 |

These are stored response data, not complete raw CAN/UDS frames. Installed Ford source classifies these DIDs as As-Built block reads. No authoritative mapping of these bytes to Active Park Assist has been established. Saved EPS blocks DE00–DE02 and ABS blocks DE01–DE02 also exist. Do not infer enabled/disabled park features from undocumented bits.

### Chestnut correction and bus limitations

USB sysfs reports vendor/product 3801:0001 and `custom ed4e39b7-CLEAN`. Installed `openpilot/common/hardware/usb.py` lists that VID/PID as Chestnut and that product string as the expected Chestnut firmware string. The earlier report's unidentified USB product is therefore evidence for Chestnut, not Panda firmware. This confirms enumeration and descriptor agreement, not accelerator operation.

Installed Ford CanBus definitions assign main=offset, radar=offset+1, camera=offset+2. Installed Ford safety source defines main bus 0 and camera bus 2 and chooses allowlists based on safety flags. Source configuration and historical bus records do not establish the presently connected Panda interface count or current gateway reachability. No safety mode was changed.

### Installed source references

Remote paths, read directly without execution:

- `/data/openpilot/launch_env.sh`: forced Expedition selection.
- `/data/openpilot/opendbc/car/ford/values.py`: Expedition CANFD platform; Ford query configuration; F188 manufacturer software query; As-Built DIDs beginning DE00; APIM extra address 0x7D0 and PCM 0x7E0.
- `/data/openpilot/opendbc/car/ford/interface.py`: Ford safety and feature selection; EPS DE01 handling relates to lateral-control prerequisites, not an Active Park Assist decoder.
- `/data/openpilot/opendbc/car/ford/fordcan.py`: logical bus assignment.
- `/data/openpilot/opendbc/safety/modes/ford.h`: Ford safety hooks and transmit allowlists.
- `/data/openpilot/openpilot/common/hardware/usb.py`: Chestnut VID/PID and expected product string.
- `/data/openpilot/opendbc_repo/opendbc/car/car.capnp`: schema used to decode the saved buffers.

System python lacked capnp; the existing `/usr/local/venv/bin/python` successfully decoded the files. No packages were installed, and bytecode writes were disabled. Remote CodeGraph index and executable were absent; no index was initialized or remote files modified.

### Revised conclusion

Uncertain — more information required. We now have a specific historical IPMA software identifier and saved configuration payloads to guide OEM research. Neither the IPMA hardware assembly, semiconductor content, park-sensor inventory, switch wiring, nor factory Active Park Assist 2.0 compatibility has been established. The missing button cannot yet be classified as the only missing component.

## Startup investigation and timestamp correction

Passive startup logs show boot-time clock jumps to 2026-07-28 before later October timestamps. Therefore the July modification dates above must not be treated as reliable evidence of ECU-cache acquisition age. All ECU findings remain cached, not newly queried.

A separate [startup diagnosis](comma-startup-update-diagnosis-2026-10-14.md) documents confirmed historical update/connectivity startup blocks and a Git submodule update failure involving locally modified Ford lateral_angle.py. No repair or reboot was performed.

## OEM research result — 2026-10-14

Classification remains **Uncertain — more information required**. No independently verified OEM source in this pass maps RJ6T-14H102-BAH to an APA 2.0-equipped 2023 Navigator's hardware assembly. No replacement IPMA, sensor, switch, or harness part number is justified yet.

OEM evidence establishes:

- Ford's [2023 Navigator L equipment sheet](https://content.fordpro.com/content/dam/fordpro/us/en-us/pdf/showroom/specialty-vehicles/livery/2023_Lincoln_NavigatorL.pdf), page 1, lists APA 2.0 and front/side/rear parking sensors for the advertised 200A configuration. It does not establish the owner's equipment or individual sensor quantities.
- The [2023 Navigator owner manual](https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?ProcUid=G2095740&Uid=G2213974&buildtype=web&countryCode=USA&div=l&languageCode=en&moidRef=G2068573&userMarket=USA&vFilteringEnabled=False&variantid=9224) describes activation by the physical parking button then touchscreen icon, and a hold/release role. Adding a button alone is not proven sufficient.
- Public OEM FordDirect reference stickers include actual 2023 Reserve builds with APA 2.0 delete credits. Indexed sticker text was retrieved, but direct PDF rendering failed; these are different vehicles. They do not prove the owner's delete option, semiconductor-shortage cause, or exact removed hardware.

See [the detailed OEM comparison](navigator-ipma-oem-comparison-2026-10-14.md) for sources, access limitations, and unresolved questions. Public reference sticker URLs include reference-vehicle VINs, not the owner's VIN.

The lowest-cost next evidence is the owner's original window sticker/build record and a Ford/Lincoln parts/service applicability comparison against a confirmed APA-equipped 2023 Navigator. A compatible hardware assembly and software association must be established before buying components. No active ECU queries were performed.
