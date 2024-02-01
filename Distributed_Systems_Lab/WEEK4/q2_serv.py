# 2. Write a UDP simple chat program for message send and receive.
# Sample Output:
# Client Side
# Do Ctrl+c to exit the program !!
# Type some text to send =>Hi
# 1. Client Sent : Hi
# 2. Client received : Hello
# Server Side:
# Do Ctrl+c to exit the program !!
# ####### Server is listening #######
# 2. Server received: Hi
# Type some text to send => Hello
# 1. Server sent : Hello
# ####### Server is listening #######

# server.py
import socket
HOST = socket.gethostname() 
PORT = 31000 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print("\nWaiting for incoming connections...\n")

s_name, addr = s.recvfrom(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
name = input(str("Enter your name: "))
s.sendto(name.encode(), addr)
while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.sendto(message.encode(), addr)
        print("\n")
        break
    s.sendto(message.encode(), addr)
    message,addr = s.recvfrom(1024)
    message = message.decode()
    print(s_name, ":", message)