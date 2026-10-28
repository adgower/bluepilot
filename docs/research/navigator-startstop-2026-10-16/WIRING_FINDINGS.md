<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# 2023 Navigator wiring and gateway path

2026-10-16. Public documentation research only; no device interaction, changes, diagnostic queries or CAN transmission.

## New evidence

Located Ford-attributed original wiring diagrams reproduced in a third-party2023 Navigator Black Label workshop collection. These are primary technical diagrams hosted by a mirror, not an authenticated VIN-filtered Ford session; build applicability and reproduction integrity are not independently certified. Distinguish these model-year-specific diagrams from the earlier2018 generic Ford description.

### Start/stop switch wiring

[2023 Navigator Auto-Start-Stop OEM wiring page](https://lemon-manuals.la/Lincoln/2023/Navigator%20Black%20Label/Repair%20and%20Diagnosis/Electrical/Wiring%20Diagrams/OEM%20Wiring%20Diagrams/Auto-Start-Stop%20System/).

Visually inspected both diagrams. Figure1/GFDWR184841 is explicitly EXPEDITION and is not the Navigator switch wiring. Figure2/[GFDWR184842](https://lemon-manuals.la/images25/GFDWR184842/) is explicitly NAVIGATOR: Start/Stop switch and indicator are integral to All Terrain Control Module(ATCM); its microcontroller connects to HS2 CAN. ConnectorC3393: pin3 HS2CAN+ circuitVDB25 GN-OG, pin2 HS2CAN- circuitVDB26 GY-BU, pin1 power, pin4 ground. This is documentation only, not instructions for probing or modifying wiring. The generic FCIM circuit description from prior research is not the model-specific switch implementation shown here.

### Network membership

[2023 Navigator network system diagram and module chart](https://lemon-manuals.la/Lincoln/2023/Navigator%20Black%20Label/Repair%20and%20Diagnosis%20%28Single%20Page%29/Accessories%20%26%20Equipment/Communication%20Devices/Controller%20Area%20Network%20%28Can%29%20Module%20Communications%20Network%20%28Description%20%26%20Operation%29/Description%20And%20Operation/Controller%20Area%20Network%20%28CAN%29%20Module%20Communications%20Network%20-%20System%20Operation%20and%20Component%20Description/System%20Diagram/).

The chart places ATCM on HS-CAN2 and PCM/IPMA/GWM on FD-CAN; GWM also connects HS-CAN2. This establishes the documented physical network relationship. It does not give a numeric0x461 receive specification for PCM.

[Reproduced Ford network-message table](https://www.linavigator4.com/lincoln_navigator_controller_area_network_can_module_communications_network_system_operation_and_component_description_description_and_operation-770.html) lists stop/start mode status originating PCM on FD-CAN and gateway copies onto other networks. This collection spans multiple years; do not promote it above the year-specific wiring. Searched relevant rows; no explicit start/stop-button0x461-to-PCM routing entry was found. It describes semantic messages, not a complete CAN-ID/filter/acceptance specification.

## Path synthesis: supported inference, not fully decoded routing

Physical button -> ATCM on HS2-CAN -> GWM -> FD-CAN vehicle segment -> PCM and the vehicle side of the IPMA camera harness.

IPMA is the forward camera module. The openpilot Ford logical main0/camera2 split corresponds to vehicle side versus isolated camera side; the recording receives0x461 on0 and echoes the identical forwarded payloads on130(returned physical2). Its dictionary marks GWM and HS2 provenance. Together, wiring, dictionary and capture strongly support0x461 being an already-gatewayed ATCM-related frame on FD-CAN. The numeric ID/unnamed bit linkage to ATCM is inferred from those combined observations, not stated in the wiring diagram.

This materially refines NETWORK_ACCEPTANCE.md: if the documented harness/network applies, an injected vehicle-side bus0 frame would already share the physical network with the PCM. A reverse gateway route FD-CAN->HS2->PCM is neither the relevant topology nor a necessary prerequisite. Injection on camera-side bus2 is not equivalent to direct vehicle-side delivery.

## What is still not established

The diagrams and tables do not say that PCM consumes0x461 byte0bit0, what validation/debounce it applies, or whether it acts on a parallel publisher. A broadcast observed on the shared PCM network can be informational only. Acknowledgment/echo cannot prove semantic acceptance. The original gateway keeps publishing; Panda at the camera connector cannot remove frames already delivered on the shared vehicle network. The existing Ford transmit safety still rejects0x461. No software control or on-road suitability is proven.

The most useful next evidence is a model-correct PCM/ATCM message definition or controlled representative bench/vehicle acceptance evidence, separately authorized. Further passive recording alone cannot settle injected-frame acceptance.

## Official source access

[Motorcraft technical resources](https://www.motorcraft.com/us/en_us/home/technical-resources.html/1000) points to official service information, including wiring and repair manuals; some require subscription. The Motorcraft service purchase page did not render usable content in the available browser session. No purchase, sign-in or account change was made. Official VIN-filtered wiring verification remains outstanding. Publicly located diagrams substantially narrow topology, but are not a replacement for Ford's proprietary CAN acceptance specification.
