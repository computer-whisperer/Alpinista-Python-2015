import yeti
import wpilib
import asyncio

from yeti.interfaces import gamemode
from yeti.wpilib_extensions import Referee

class Arm(yeti.Module):

    def module_init(self):
        self.referee = Referee(self)

        self.joystick = wpilib.Joystick(0)
        self.referee.watch(self.joystick)

        self.motor = wpilib.Victor(2)
        self.referee.watch(self.motor)

    @asyncio.coroutine
    @gamemode.teleop_task
    def teleop_loop(self):
        while gamemode.is_teleop():
            out = 0
            if self.joystick.getRawButton(2):
                out = 1
            elif self.joystick.getRawButton(3):
                out = -1
            self.motor.set(out)
            yield from asyncio.sleep(.05)