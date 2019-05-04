import inputs
import threading
import math


class XboxOneController():


    def __init__(self):
        self.left_x = 'ABS_X'
        self.left_y = 'ABS_Y'
        self.right_x = 'ABS_RX'
        self.right_y= 'ABS_RY'
        self.left_x_val = 0
        self.left_y_val = 0
        self.right_x_val = 0
        self.right_y_val = 0
        self.is_running = False
        self.left_output = 0
        self.right_output = 0

    def start_controller(self):
        self.is_running = True

    def stop_controller(self):
        self.is_running = False

    def run(self):
        while self.is_running:
            events = inputs.get_gamepad()
            for event in events:
                print(event.code, event.state)
                if event.code == self.right_x:
                    self.right_x_val = self.square_input(event.state)
                if event.code == self.right_y:
                    self.right_y_val = self.square_input(event.state)
                if event.code == self.left_x:
                    self.left_x_val = self.square_input(event.state)
                if event.code == self.left_y:
                    self.left_y_val = self.square_input(event.state)
                # print("left X", self.left_x_val)
                # print("left Y", self.left_y_val)
                # print("right X", self.right_x_val)
                # print("right Y", self.right_y_val)

    def normalize(self, value):
        return value/32768

    def square_input(self, value):
        value = self.normalize(value)
        return math.copysign(value * value, value)

    def get_arcade_drive_left(self):
        return (self.left_y_val + self.right_x_val) #* 500

    def get_arcade_drive_right(self):
        return (self.left_y_val - self.right_x_val) #* 500

    def get_saturated_input(self, throttle, turn):
        greater = max(abs(throttle), abs(turn))
        lesser = abs(throttle) + abs(turn) - greater
        if greater > 0:
            return (lesser/greater) + 1
        else:
            return 1

    def calc_arcade_drive(self):
        turn = self.right_x_val
        throttle = self.left_y_val
        saturated_input = self.get_saturated_input(throttle, turn)
        turn = turn / saturated_input
        throttle = throttle / saturated_input
        self.left_output = throttle + turn
        self.right_output = throttle - turn

    def calc_curvature_drive(self, throttle_deadband):
        turn = self.right_x_val
        throttle = self.left_y_val
        saturated_input = self.get_saturated_input(throttle, turn)
        turn = turn / saturated_input
        throttle = throttle / saturated_input
        if abs(throttle) > throttle_deadband:
            self.left_output = throttle + turn * throttle
            self.right_output = throttle - turn * throttle
        else:
            self.left_output = turn
            self.right_output = -turn






# xbox = XboxOneController()
# xbox.start_controller()
#
#
# def test():
#     while True:
#         print(971, xbox.left_y_val)
#
#
# t = threading.Thread(target=xbox.run)
# t2 = threading.Thread(target=test)
# t.start()
# t2.start()
# t.join()
# t2.join()
