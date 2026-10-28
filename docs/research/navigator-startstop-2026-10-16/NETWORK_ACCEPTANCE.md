<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Network path and receiver acceptance follow-up

2026-10-16. Local recording/source and publicly accessible Ford primary-source research only. No device commands, changes, firmware updates, diagnostic requests, or experimental CAN transmissions in this follow-up.

## Result

A candidate injection direction can be identified: logical main/vehicle bus 0, rather than the isolated camera-side bus 2. Receiver acceptance is not established and cannot be inferred from passive data alone. The unknown is not simply which bit to set: it is whether the bit is a routed command to the PCM or a mirrored indication on the camera network, and how the gateway/receiver handles competing same-ID publishers.

## Confirmed path

In captured segment 63, 66 received 0x461 frames on bus 0 have exactly the same ordered payload sequence as 66 returned-TX frames on bus 130. Echo timestamp delay is 0–9.60 ms. No corresponding received bus2 sequence exists in that segment. With the reviewed Panda forwarding and returned-bus encoding, this supports vehicle/main bus0 -> Panda forwarding -> camera bus2, with transmitted bus2 frames reported as130. The UI's bus130 is not a third physical network. Normal idle intervals in the inspected sample are approximately1 second; press/release adds event frames.

Logical bus0/2 are openpilot wiring roles, not Ford HS-CAN network numbers. See NETWORK_SOURCE.md for exact citations. DBC FrameGatewayNetwork HS2_CAN for0x461 is a dictionary attribute; it does not identify the currently connected camera network, prove routing direction, or prove the PCM consumes this ID. The DBC's named drive-mode fields list ABS_ESC as receiver; the button candidate bit has no defined recipient. Thus a definite button->FCIM->HS2->GWM->PCM path cannot be asserted for this vehicle.

## OEM evidence and its applicability

Ford's own diagnostics index:
https://www.fordtechservice.dealerconnection.com/vdirs/diagnostics/default.asp?gutsid=diagsheet&pageid=diagnostic_theory

This links the2018 gasoline summary:
https://www.fordservicecontent.com/Ford_Content/catalog/motorcraft/OBDSM1802-2018.pdf

Printed page227 describes a momentary start/stop-disable switch read by FCIM, a CAN button-state message to PCM, and low-to-high detection by PCM. This establishes a Ford architecture precedent, not the2023 Navigator's exact ID/bit/routing. The section was available through indexed primary-source excerpts; full-PDF retrieval hit the web tool's size limit.

The same official index links the2020–2023 gasoline summary:
https://www.fordservicecontent.com/Ford_Content/catalog/motorcraft/OBD_System_Operation_Update.pdf

Opened and searched this172-page primary document: stop/start diagnostics at printed page115; no matching FCIM or button-edge section. It does not validate the older switch topology for the owner's2023 vehicle or specify 0x461 gateway/receiver acceptance. Third-party workshop mirrors and forum posts were not used as verified wiring evidence.

Important discrepancy: the older generic Ford summary describes a rising-edge toggle; the owner's repeated capture shows status changes following the candidate falling edge after sustained holds. This further prevents treating the older document as an exact receiver specification. Observed edge correlation is repeatable, but may reflect upstream processing or a different platform implementation.

## Implications

* Sending to camera bus2 would place a message on the isolated camera side. There is no evidence that this side relays the request back to the powertrain controller; do not choose it merely because bus130 appears.
* Bus0 reaches the vehicle-side segment, but may only expose a gateway mirror of a request originally delivered on another Ford network. Gateway reverse-routing and receiver acceptance are unknown.
* Camera-harness forwarding rules can block a message from reaching the camera, but cannot remove a stock message that already reached another ECU on the main-side segment. Parallel same-ID transmission requires assessing normal publisher traffic; changing Panda forwarding alone does not replace the main-side source.
* CAN transport acknowledgment or Panda's transmit echo would establish transmission, not that the PCM acted. Independent0x166 state change would be required to demonstrate functional acceptance.
* Current Ford safety still rejects0x461. This follow-up does not change that finding or authorize bypassing safety checks.

## Remaining evidence needed

A model/build-correct Ford wiring/network and message description identifying the console-switch input module, gateway route, PCM network and any translated request ID. If that is unavailable, an isolated representative bench or a separately authorized narrowly bounded stationary injection experiment is needed to answer actual receiver acceptance. No amount of extra passive presses alone establishes it. No current evidence supports promising a working openpilot toggle.
