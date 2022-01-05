#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import string

IP_ADDRESS = "127.0.0.1"
PORT = 12345
path = 'D:\\vscode\\python\\send_file_app\\test\\'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDRESS, PORT)) # here you must past the public external ipaddress of the server machine, not that local address
letters = string.ascii_uppercase
image_num = s.recv(1024)
image_num = int(image_num.decode())
# create_zip = zipfile.ZipFile(path + "images.zip", "w")

for i in range(image_num):
    image_len = s.recv(1024)
    # file_name = ''.join(random.choice(letters) for i in range(5))
    
    # print(image_length.decode('utf-16'))
    try:
        image_len = int(image_len.decode("ISO-8859-1"))
        f = open(path + str(i) + '.jpg', "wb")
    except:
        continue
    image_data = s.recv(image_len)
    f.write(image_data)
    