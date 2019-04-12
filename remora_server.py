import socket


def server():
    host = socket.gethostbyname(socket.gethostname())
    print(host)
    port = 8080  # Make sure it's within the > 1024 $$ <65535 range
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    c, adress = s.accept()
    # print("Connection from: ")
    i = 0
    data_array = []
    while True:
        i+= 1
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        # print(data + '\n')
        parse_data(data)
        # c.send(data.encode('utf-8'))
    print(i)
    c.close()

server()

def parse_data(data):
    while data.find('|') != -1:
        print(data[:data.find('|')])
