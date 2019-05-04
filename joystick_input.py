# from inputs import  DeviceManager
# from inputs import GamePad
# from inputs import get_gamepad
import inputs
import time
import pygame
from pygame import joystick

joystick.init()
joy = pygame.joystick.Joystick()
print(joy.get_name())
joy.init()
# print(joy.get_numaxes())
# print(joy.get_init())
print(joystick.get_count())
while True:
    time.sleep(1)
    # print(joy.get_axis(0))

    # for x in range (joy.get_numaxes()):
    print(joy.get_axis(0))
    # print("--------")
    # print(joy.get_button(0))

# while True:
#     events = inputs.get_gamepad()
#     for event in events:
#         print(event.ev_type, event.code, event.state)