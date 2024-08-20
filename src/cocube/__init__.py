# SPDX-FileCopyrightText: 2024-present wwj718 <wuwenjie718@gmail.com>
#
# SPDX-License-Identifier: MIT
from microblocks import MicroblocksClient


class CoCube(MicroblocksClient):

    @property
    def battery(self):
        return int(self.request("CoCube Battery Percentage", []))

    @property
    def on_the_mat(self):
        return bool(self.request("CoCube On The Mat", []))

    @property
    def card_id(self):
        return int(self.request("CoCube Card ID", []))

    @property
    def position_x(self):
        return int(self.request("CoCube position_X", []))

    @property
    def position_y(self):
        return int(self.request("CoCube position_Y", []))

    @property
    def position_direction(self):
        return int(self.request("CoCube position_Direction", []))

    def set_tft_backlight(self, flag=0):
        self.request("CoCube set TFT backlight", [flag])

    def draw_aruco_marker_on_tft(self, id=0):
        self.request("CoCube draw Aruco Marker on TFT", [id])

    def draw_apriltag_on_tft(self, id=0):
        self.request("CoCube draw AprilTag on TFT", [id])

    def move(self, direction="forward", speed=40):
        self.request("CoCube move", [direction, speed])

    def rotate(self, direction="left", speed=30):
        self.request("CoCube rotate", [direction, speed])

    def move_millisecs(self, direction="forward", speed=40, duration=1000):
        # self.request("CoCube move at speed for millisecs", [direction, speed, duration], callType="call", timeout=3+duration/1000)
        self.request("CoCube move for millisecs", [direction, speed, duration], callType="blocking_call", timeout=100)

    def rotate_millisecs(self, direction="left", speed=30, duration=1000):
        # self.request("CoCube rotate at speed for millisecs", [direction, speed, duration], callType="call", timeout=3+duration/1000)
        self.request("CoCube rotate for millisecs", [direction, speed, duration], callType="blocking_call", timeout=100)

    def move_by_steps(self, direction="forward", speed=40, step=50):
        self.request("CoCube move by step", [direction, speed, step], callType="blocking_call", timeout=100)

    def rotate_by_degree(self, direction="left", speed=30, degree=90):
        self.request("CoCube rotate by degree", [direction, speed, degree], callType="blocking_call", timeout=100)

    def set_wheel_speed(self, left_speed=40, right_speed=40):
        self.request("CoCube set wheel", [left_speed, right_speed])

    def wheels_stop(self):
        self.request("CoCube wheels stop", [])

    def wheels_break(self):
        self.request("CoCube wheels break", [])

    def rotate_to_angle(self, angle=0, speed=30):
        self.request("CoCube rotate to angle", [angle, speed])

    def rotate_to_target(self, target_x=0, target_y=0, speed=30):
        self.request("CoCube rotate to target", [target_x, target_y, speed])

    def move_to_target(self, target_x=0, target_y=0, speed=50):
        self.request("CoCube move to target", [target_x, target_y, speed])

    ###### module ########

    def power_on_module(self):
        self.request("Power on module", [])

    def power_off_module(self):
        self.request("Power off module", [])

    def gripper_open(self):
        self.request("Gripper Open", [])

    def gripper_close(self):
        self.request("Gripper Close", [])

    def gripper_degree(self, degree):
        # degree: -70-0
        self.request("Gripper degree", [degree])

    def attach_NeoPixel(self):
        self.request("attach NeoPixel", [])

    def set_all_NeoPixels_color(self, r, g, b):
        color = r << 16 | g << 8 | b
        self.request("set all NeoPixels color", [color])

    def clear_NeoPixels(self):
        self.request("clear NeoPixels", [])

    @property
    def ultrasonic_distance(self):
        return self.request("Ultrasonic distance (cm)", [])

    @property
    def ambient_light(self):
        return self.request("Ambient Light", [])
