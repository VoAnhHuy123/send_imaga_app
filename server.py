#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import os
import threading

IP_ADDRESS = "127.0.0.1"
PORT = 12345
path = "D:\\source\\"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_ADDRESS, PORT)) #if the clients/server are on different network you shall bind to ('', port)

def run(socket):
    files = os.listdir(path)
   
    for image in files:
        # send image_name
        socket.send(image.encode())
        # receive ok
        socket.recv(1024)
        # get size
        size = os.path.getsize(path + image)
        print(size)
        # send image_size
        socket.sendall(str(size).encode())
        # receive ok
        socket.recv(1024)
        with open(path + image, 'rb') as f:
            data = f.read()
            socket.send(data)
            status=socket.recv(1024).decode()
            print(status)
    c.close()

while True:
    s.listen(10)
    c, addr = s.accept()
    thread = threading.Thread(target=run, args=(c,))
    thread.daemon = True
    thread.start()
# print(len(files))
# zip_file(files)