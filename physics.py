from pyfrc.physics import core, drivetrains
import wpilib


class PhysicsEngine(core.PhysicsEngine):

    def __init__(self, physics_controller):
        self.physics_controller = physics_controller
        physics_controller.add_gyro_channel(0)


    def update_sim(self, hal_data, now, tm_diff):
        front_left_wheel = hal_data["pwm"][2]["value"]
        rear_left_wheel = hal_data["pwm"][4]["value"]
        front_right_wheel = -hal_data["pwm"][5]["value"]
        rear_right_wheel = -hal_data["pwm"][3]["value"]

        vx, vy, vr = drivetrains.mecanum_drivetrain(rear_left_wheel, rear_right_wheel, front_left_wheel, front_right_wheel, 2, 1.5, 13)
        self.physics_controller.vector_drive(vx, vy, vr, tm_diff)
