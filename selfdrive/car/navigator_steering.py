"""Feed BluePilot 7.0's calibrated pose and fresh control context to the Navigator tune."""

import math

from openpilot.selfdrive.car.navigator_calibration import feed_calibration_context
from openpilot.selfdrive.locationd.helpers import Pose, PoseCalibrator


class NavigatorSteeringContext:
  def __init__(self):
    self.calibrator = PoseCalibrator()
    self.motion = None
    self.generation = 0
    self.calibrated = False

  def feed(self, strategy, sm, control, state, now_ns, state_ns, replay, control_ns, control_valid):
    model = sm['modelV2']
    model_ns = sm.logMonoTime['modelV2']
    model_valid = sm.all_checks(['modelV2'])
    lane_change = str(model.meta.laneChangeState) != 'off' or state.leftBlinker or state.rightBlinker
    strategy.set_path_preview(model if control_valid and model_valid and not lane_change else None, model_ns)
    strategy.set_context(now_ns=now_ns, state_ns=state_ns, control_ns=control_ns, model_ns=model_ns,
                         model_valid=control_valid and model_valid, lane_change=lane_change)
    feed_calibration_context(strategy, control, now_ns=now_ns, control_ns=control_ns, control_valid=control_valid)

    rpy = sm['liveCalibration'].rpyCalib
    calibrated = sm.all_checks(['liveCalibration']) and len(rpy) == 3 and all(math.isfinite(v) for v in rpy)
    if calibrated and (sm.updated['liveCalibration'] or not self.calibrated):
      self.calibrator.feed_live_calib(sm['liveCalibration'])
    calibrated = calibrated and self.calibrator.calib_valid
    if self.calibrated != calibrated:
      self.generation += 1
      self.motion = None
    self.calibrated = calibrated

    if sm.updated['livePose'] and calibrated:
      pose = sm['livePose']
      published_ns = sm.logMonoTime['livePose']
      received_ns = published_ns if replay else int(sm.recv_time['livePose'] * 1e9)
      yaw = self.calibrator.build_calibrated_pose(Pose.from_live_pose(pose)).angular_velocity
      self.motion = dict(sample_ns=pose.timestamp, received_ns=received_ns, yaw_rate=float(yaw.z), yaw_std=float(yaw.z_std),
                         valid=(sm.valid['livePose'] and pose.inputsOK and pose.sensorsOK and pose.posenetOK
                                and pose.angularVelocityDevice.valid and 0 < pose.timestamp <= published_ns <= received_ns))
    motion = dict(self.motion or dict(sample_ns=0, received_ns=0, yaw_rate=0., yaw_std=0., valid=False))
    motion['valid'] = motion['valid'] and calibrated and sm.all_checks(['livePose'])
    strategy.input_state_valid = bool(state.canValid and not state.vehicleSensorsInvalid and state_ns)
    strategy.set_motion(now_ns=now_ns, generation=self.generation, **motion)
