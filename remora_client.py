import socket
import random

def client():
    host = socket.gethostbyname(socket.gethostname())
    port = 8080  # Make sure it's within the > 1024 $$ <65535 range
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    i = 0
    # while message != 'q':
    while i < 16:
        # message = input('==> ')
        message = str(getData()) + '|'
        i += 1
        s.send(message.encode('utf-8'))
        print(i)
    s.close()

def getData():
    r = random.randint(0, 254)
    print(r)
    return r


client()

