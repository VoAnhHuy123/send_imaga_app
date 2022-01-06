import socket
import os
import time


IP_ADDRESS = "127.0.0.1"
PORT = 12345
path = "D:\\source\\"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_ADDRESS, PORT))
s.listen(10)
c, addr = s.accept()
print('connected')
images = ['ok.jpg', '1.jpg']
for image in images:
    with open(image, 'rb') as f:
        size = os.path.getsize(image)
        print(size)
        # c.send("ok".encode())
        c.sendall(str(size).encode())
        data = f.read()
        c.send(data)
        status=c.recv(1024).decode()
        print(status)
c.close()