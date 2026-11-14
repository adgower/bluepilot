"""Navigator wheel-target unwind adapted to BluePilot's angle controller."""

from collections import deque
import math
import time

import numpy as np

from opendbc.car import DT_CTRL
from opendbc.car.ford.values import CarControllerParams

_MPH_TO_MS = 0.44704
_STEER_DT = DT_CTRL * CarControllerParams.STEER_STEP
_MAX_TRIM = 0.0009  # radians of path angle
_MAX_AREA = 0.0003375  # rad·s per curve


class NavigatorUnwind:
  def __init__(self):
    self.samples = deque(maxlen=5)
    self.last_time = None
    self.quiet_since = None
    self.area = 0.0
    self.trim = 0.0

  def reset(self):
    self.samples.clear()
    self.last_time = None
    self.quiet_since = None
    self.trim = 0.0

  def update(self, state, curvature, path_angle, vm, params, params_age, lane_change):
    now = time.monotonic()
    dt = now - self.last_time if self.last_time is not None else _STEER_DT
    self.last_time = now
    speed = state.vEgoRaw
    if (params is None or not 0 <= params_age <= 0.15
        or not (params.valid and params.sensorValid and params.steerRatioValid
                and params.stiffnessFactorValid and params.angleOffsetValid)
        or not state.canValid or state.vehicleSensorsInvalid or state.steeringPressed
        or state.brakePressed or state.gasPressed or state.leftBlinker or state.rightBlinker
        or state.steerFaultTemporary or state.steerFaultPermanent or lane_change
        or not all(math.isfinite(value) for value in (speed, curvature, path_angle, state.steeringAngleDeg,
                                                      state.yawRate, params.roll, params.angleOffsetDeg))
        or not (10 <= params.steerRatio <= 35 and 0.2 <= params.stiffnessFactor <= 3
                and abs(params.roll) <= 0.15 and abs(params.angleOffsetDeg) <= 10)
        or not 0.04 <= dt <= 0.06 or speed <= 0.1):
      self.reset()
      return path_angle

    target = math.degrees(vm.get_steer_from_curvature(-curvature, speed, params.roll))
    actual = state.steeringAngleDeg - params.angleOffsetDeg
    if abs(curvature) < 0.00015 and abs(actual - target) <= 0.5 and abs(state.yawRate * speed) < 0.1:
      if self.quiet_since is None:
        self.quiet_since = now
      if now - self.quiet_since >= 1.0:
        self.area = 0.0
    else:
      self.quiet_since = None

    mph = speed / _MPH_TO_MS
    demand = abs(curvature) * speed ** 2
    no_roll = vm.get_steer_from_curvature(-curvature, speed, 0.0)
    if not (62 < mph < 75 and demand >= 0.25 and abs(target) >= 1.5
            and target * actual > 0 and target * no_roll > 0 and curvature * path_angle > 0):
      self.samples.clear()
      self.trim = 0.0
      return path_angle

    error = math.copysign(1.0, target) * (actual - target)
    excess = math.copysign(1.0, -curvature) * state.yawRate * speed - demand
    if (error <= 0.5 or excess <= max(0.1, 0.1 * demand)
        or (self.samples and (curvature * self.samples[-1][1] <= 0
                             or abs(curvature) > abs(self.samples[-1][1])))):
      self.samples.clear()
      self.trim = 0.0
      return path_angle

    self.samples.append((now, curvature, error, excess))
    if len(self.samples) < self.samples.maxlen:
      return path_angle

    start, initial_curvature, initial_error, _ = self.samples[0]
    duration = now - start
    projected_error = min(error, error + 0.3 * (error - initial_error) / duration)
    if (projected_error <= 0.5 or abs(curvature) > 0.95 * abs(initial_curvature)
        or (self.trim == 0 and (excess < 0.25 or np.median([row[3] for row in self.samples]) < 0.25))):
      self.trim = 0.0
      return path_angle

    weight = float(np.interp(mph, [62., 64., 72., 75.], [0., 1., 1., 0.]))
    requested = min(_MAX_TRIM, 0.05 * abs(path_angle)) * weight
    self.trim = min(requested, self.trim + 0.0003, max(0.0, (_MAX_AREA - self.area) / dt))
    self.area += self.trim * dt
    return path_angle - math.copysign(self.trim, path_angle)
