# 4A. Forking/ Threading (Concurrent Server)

import socket
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 11597
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(1024)
while True:
    Input = input('Client Say Something: ')
    if Input == "[e]":
        message = "Left chat room!"
        ClientSocket.send(message.encode())
        print("\n")
        break
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print('From Server : ' + Response.decode())
ClientSocket.close()