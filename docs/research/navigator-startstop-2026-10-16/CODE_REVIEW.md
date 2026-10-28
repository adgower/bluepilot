<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Ford start/stop transmit source review

Read-only inspection of `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014`; paths below are relative to that absolute checkout. No device access or mutation performed by this reviewer. This establishes source behavior, not the running Panda firmware identity or receiver acceptance.

## Findings

1. **The existing Ford safety configuration rejects host transmission of 0x461.** `opendbc_repo/opendbc/safety/modes/ford.h:457-480` lists all common, CAN-FD-stock, CAN-FD-long-debug, and non-CAN-FD-long transmit messages. None includes 0x461. `opendbc_repo/opendbc/safety/safety.h:230-252` checks exact address, bus, and length and only calls the vehicle transmit hook when allowlisted. Adding a Python controller message alone therefore does not enable transmission under this source configuration.

2. **Forwarding is separate from host transmit authorization.** `opendbc_repo/opendbc/safety/safety.h:255-287` forwards physical bus 0 to 2 and 2 to 0 unless relay malfunction, configuration disable, static blocking, or a vehicle hook blocks it. Ford has no forwarding hook (`opendbc_repo/opendbc/safety/modes/ford.h:514-522`). 0x461 is absent from the static blocking list. Seeing forwarded stock 0x461 therefore does not mean openpilot may inject it. Nor does forwarding prove which destination ECU actually consumes the bit.

3. **Ford bus selection:** `opendbc_repo/opendbc/car/ford/fordcan.py:4-18` defines main = offset, radar = offset+1, camera = offset+2. `opendbc_repo/opendbc/car/__init__.py:114-123` derives offset from safety configuration/fingerprint, in blocks of four. `opendbc_repo/opendbc/car/ford/interface.py:48-60` selects Ford safety, adding noOutput for preceding hardware when appropriate and enabling CANFD/longitudinal flags. Must verify running CarParams and actual firmware before interpreting bus 0 as an unconditional vehicle-wide address.

4. **Existing button API does not cover start/stop.** `opendbc_repo/opendbc/car/ford/carcontroller.py:75-85` emits cruise cancel/resume and TJA toggle through `create_button_msg`. `opendbc_repo/opendbc/car/ford/fordcan.py:295-343` copies stock SCCM values and sets cruise/TJA bits in `Steering_Data_FD1` (0x83), not 0x461. No start/stop handling was found in the Ford source directory.

5. **DBC confirms candidate is currently unnamed and shares a message with drive-mode functions.** `opendbc_repo/opendbc/dbc/ford_lincoln_base_pt.dbc:2602-2605` declares 0x461 (`AllTerrainControlData_FD1`) as 8 bytes, sender GWM; byte 0 bits 1-7 hold selected-drive-mode switch/count fields. Byte 0 bit 0 is undefined. This is strong reason not to zero/reconstruct the entire frame. The DBC lists HS2_CAN gateway metadata (`:5437-5440`), not definitive physical button source or recipient for the unnamed bit. The declaration contains no named checksum/counter for the remaining bytes; that does not prove no protection exists.

6. **State indicator definition supports the earlier interpretation.** `opendbc_repo/opendbc/dbc/ford_lincoln_base_pt.dbc:2363-2370` defines Stop_Start 0x166 and StopStrtDrvMde_D_Indic; `:11918` labels 0 Selected, 1 Deselected, 2 IndirectDeselect, 3 NotUsed. Thus this is a 2-bit field rather than a universal boolean. It is preferable for independent state confirmation versus assuming the button bit itself represents disabled state.

7. Other explicitly named request candidates exist in the dictionary: `StopStrtDrvMde_B_RqBtn3` at `opendbc_repo/opendbc/dbc/ford_lincoln_base_pt.dbc:2501` (message 261/0x105), and `StopStrtDrvMde_B_RqBtn` in Compressor_Req_FD1 806/0x326 (`:3037-3042`). Their presence does not prove this Navigator uses them. Correlate raw logs rather than prefer their names over observed evidence.

## Assessment

Technically plausible CAN button input, but no current supported controller API or allowlisted 0x461 host transmission path. Existing stock module/GWM keeps ownership of the message; arbitrary parallel injections may be overwritten or interpreted inconsistently. A source change would need explicit narrow safety support, payload preservation, rate/duration bounds and independent status feedback, plus bench/unit validation before any separately authorized stationary vehicle test. No suggestion to switch to unrestricted safety mode or disable existing protections.

Unknown: actual flashed firmware hash, exact installed CarParams, unnamed-bit physical producer/consumer, required cadence/edge semantics, receiver arbitration/acceptance. Source review cannot establish these or guarantee a transmit will toggle the feature.
