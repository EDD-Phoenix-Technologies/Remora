import serial
import  time

# ser = serial.Serial()
# ser.baudrate = 115200
# ser.port = 'COM5'
# ser.open()
# joystick_data = 0
# init_msg = 'ml0'
# init_msg = init_msg.encode()
# ser.write(init_msg)
# while True:
#     print(ser.readline())
#     # ser.write(joystick_data)
#     message = 'mr150'
#     ser.write(message.encode())
#     message = 'ml-150'
#     ser.write(message.encode())
#     time.sleep(0.001)

class SerialComms:

    def __init__(self, baud, port):
        self.ser = serial.Serial()
        self.ser.baudrate = baud
        self.ser.port = port
        self.ser.open()

    def send_data(self, leftData, rightData):
        left = 'ml' + str(leftData)
        right = 'mr' + str(rightData)
        self.ser.write(left.encode())
        self.ser.write(right.encode())

