# from inputs import  DeviceManager
# from inputs import GamePad
# from inputs import get_gamepad
# import

import pygame
from pygame import joystick

# joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()
print(joy.get_numaxes())
while True:
    print(joy.get_axis(0))