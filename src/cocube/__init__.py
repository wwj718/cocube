# SPDX-FileCopyrightText: 2024-present wwj718 <wuwenjie718@gmail.com>
#
# SPDX-License-Identifier: MIT
from microblocks import MicroblocksClient


class CoCube(MicroblocksClient):

    @property
    def battery(self):
        return int(self.request("Battery Percentage", []))

    @property
    def position_x(self):
        return int(self.request("position_X", []))

    @property
    def position_y(self):
        return int(self.request("position_Y", []))

    def set_tft_backlight(self, id=0):
        self.request("set TFT backlight", [id])

    def draw_aruco_arker_on_tft(self, id=0):
        self.request("draw Aruco Marker on TFT", [id])

    def control_left_motor(self, speed=50):
        self.request("ControlLeftMotor", [speed])

    def control_right_motor(self, speed=50):
        self.request("ControlRightMotor", [speed])

    def move_forward(self, speed=50):
        self.request("Move Forward", [speed])

    def move_backward(self, speed=50):
        self.request("Move Backward", [speed])

    def turn_left(self, speed=10):
        self.request("Turn Left", [speed])

    def turn_right(self, speed=10):
        self.request("Turn Right", [speed])

    def motor_stop(self):
        self.request("Motor Stop", [])

    def motor_break(self):
        self.request("Motor Break", [])

    def rotate_to_angle(self, angle=0, speed=10):
        self.request("Rotate to Angle", [angle, speed])

    def rotate_to_target(self, x=10, y=10, speed=10):
        self.request("Rotate to Target", [x, y, speed])

    def move_to_target(self, x=10, y=10, speed=50):
        self.request("Move to Target X _ Y _ Speed _", [x, y, speed])
