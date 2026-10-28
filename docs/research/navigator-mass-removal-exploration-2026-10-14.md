<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator mass removal exploration

Research snapshot October 14, 2026. No Comma files or settings changed.

## What upstream changed

Openpilot commit [`2713630e`](https://github.com/commaai/openpilot/commit/2713630e7950a61dc072467b5394a1043e34547f), dated October 13, removes mass from the car Kalman filter globals, supplies mass-normalized inertia and tire stiffness to paramsd, adds recorded-CarParams migration, and pins opendbc [`b3bd79a6`](https://github.com/commaai/opendbc/commit/b3bd79a659dae961af169a3baac723961f720133).

The paired opendbc change removes mass from CarSpecs and the cargo allowance calculation. It changes the model fields to `rotationalInertiaPerMass`, `tireStiffnessFrontPerMass`, and `tireStiffnessRearPerMass`, with `VehicleModel` using unit mass. The old mass field remains in the schema's deprecated group. Wheelbase, center-to-front geometry, steering ratio, and stiffness factor remain relevant. [Paired opendbc diff](https://github.com/commaai/opendbc/commit/b3bd79a659dae961af169a3baac723961f720133)

This removes a redundant input in the existing approximation: the old scaling helpers multiply inertia and stiffness by vehicle mass; dividing those quantities by that same mass cancels the mass dependence. It does not claim that actual vehicle loading has no physical effect, and does not provide new measured tire properties. [Scaling helpers and vehicle-model changes](https://github.com/commaai/opendbc/commit/b3bd79a659dae961af169a3baac723961f720133)

## Effect on the Navigator trial

The trial's `opendbc/car/ford/pinion.py` guard currently checks mass 2878 kg and absolute tire stiffness 353037.28125 / 438491.46875, along with the fixed geometry. `opendbc/safety/modes/ford.h` uses the same mass and stiffness in its pinion curvature formula. A schema update alone would break these assumptions. The port must preserve the physical curvature mapping while converting the controller guard and corresponding tests; Panda may retain an algebraically equivalent existing formula or be normalized in tandem, but the paired result must be verified.

An exploratory local numerical check used the existing trial VehicleModel with the Navigator parameters, then constructed the algebraically normalized equivalent with mass 1 and inertia/stiffness divided by 2878. Across 210 combinations of speeds 0–80 mph, steering angles −90–90 degrees, and roll −0.05–0.05 rad, the maximum curvature difference was **6.938893903907228e-18 /m**. Dynamic state matrices at nine nonzero speeds agreed within 1e-12 tolerance. Normalized tire stiffness is approximately 122.66757514 front and 152.35978761 rear.

That check establishes the algebraic equivalence for these inputs using the current model; it is not a completed upstream port, full replay, or road test. Small floating-point changes can still matter at encoded CAN boundaries and need replay verification.

## Decision

Treat mass removal as upstream maintenance, not a low-speed steering feature or remedy. Retain the Navigator wheelbase and steering-ratio customization when reconciling the Ford values file; upstream's Expedition values are not this fork's Navigator geometry. Adopt the openpilot and opendbc changes together, migrate old recorded data before analysis under the new schema, update the custom pinion guards/tests, and rerun paired safety replay before deployment. The 1.20/0.97 calibration and low-speed trial remain separate tuning decisions.
