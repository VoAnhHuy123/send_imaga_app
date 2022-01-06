#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import string
import random

IP_ADDRESS = "127.0.0.1"
PORT = 12345
path = 'D:\\vscode\\python\\send_file_app\\test\\'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDRESS, PORT)) # here you must past the public external ipaddress of the server machine, not that local address
letters = string.ascii_uppercase
image_name = s.recv(1024).decode()

while image_name:
    s.send(b'ok')
    print(image_name)
    # receive size
    size = s.recv(1024)
    # send ok
    s.send(b'ok')
    data = s.recv(int(size))
    print(len(data))
    with open(path + image_name + '.jpg', 'wb') as f:
        f.write(data)
    s.send(b'ok')
    image_name = s.recv(1024).decode()
    # size = s.recv(2048)
s.close()