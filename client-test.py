import socket
import string

IP_ADDRESS = "127.0.0.1"
PORT = 12345
path = 'D:\\vscode\\python\\send_file_app\\test\\'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDRESS, PORT))
size = s.recv(2048)
name=2
while size:
    print(size.decode())
    data = s.recv(int(size))
    print(len(data))
    with open(str(name) + '.jpg', 'wb') as f:
        f.write(data)
    name = name + 1
    s.send(b'ok')
    size = s.recv(2048)
s.close()