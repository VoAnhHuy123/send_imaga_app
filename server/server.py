#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import os
import threading
import time

IP_ADDRESS = "127.0.0.1"
PORT = 12345
path = os.getcwd() + '/image_storage/'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_ADDRESS, PORT)) #if the clients/server are on different network you shall bind to ('', port)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def run(socket):
    files = os.listdir(path)
   
    for image in files:
        # send image_name
        socket.send(image.encode())
        # receive ok
        name_status = socket.recv(1024)
        print(name_status)
        # get size
        size = os.path.getsize(path + image)
        print(size)
        # send image_size
        socket.sendall(str(size).encode())
        # receive ok
        status = socket.recv(1024)
        print(status.decode())
        with open(path + image, 'rb') as f:
            data = f.read()
            print(f"data len {len(data)}")
            socket.sendall(data)
            data_status = socket.recv(1024)
            print(data_status.decode())
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