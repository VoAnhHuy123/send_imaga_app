#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import os
import threading

from client import IP_ADDRESS

IP_ADDRESS = "127.0.0.1"
PORT = 12345
path = "D:\\source\\"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_ADDRESS, PORT)) #if the clients/server are on different network you shall bind to ('', port)

def run(socket):
    files = os.listdir('D:\\source\\')
    socket.sendall(str(len(files)).encode())
    for file in files:
        f = open(path + file, "rb")
        l = os.path.getsize(path + file)
        socket.sendall(str(l).encode('ISO-8859-1'))
        m = f.read(l)
        socket.sendall(m)
        print("Done sending...")
        f.close()
    socket.close()

while True:
    s.listen(10)
    c, addr = s.accept()
    thread = threading.Thread(target=run, args=(c,))
    thread.daemon = True
    thread.start()
# print(len(files))
# zip_file(files)