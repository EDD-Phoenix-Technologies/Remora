from input_joy import  *
import threading
from comms import *

xbox = XboxOneController()
xbox.start_controller()
# comms = SerialComms(115200, 'COM7')


def test():
    while True:
        xbox.calc_curvature_drive(0.0045)
        print('left', xbox.left_output)
        print('right', xbox.right_output)


if __name__ == "__main__":
    t = threading.Thread(target=xbox.run)
    t2 = threading.Thread(target=test)
    t.start()
    t2.start()
    t.join()
    t2.join()
