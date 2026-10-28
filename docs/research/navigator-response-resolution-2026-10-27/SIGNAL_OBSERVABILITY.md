<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Known brake observation scope

A literal audit of the current paired Ford DBC found named brake torque and brake/precharge status signals. It did not identify a named hydraulic wheel/cylinder-pressure signal in this DBC. `BrkBstrVac_P_Actl` is explicitly booster vacuum in millibar; it must not be used as hydraulic pressure. `BrkTot_Tq_Actl` is a torque signal in Nm and does not by its name/DBC alone establish hydraulic pressure or directional acceleration authority. This does not prove the vehicle broadcasts no other useful signal: unmapped messages and physical semantics remain unexamined.

No clearance threshold was changed. The existing measured-torque barrier remains authoritative in these prototypes; signal absence is not permission to bypass it. The source hash and exact selected lines are bound in `signal-observability-audit.json`.
