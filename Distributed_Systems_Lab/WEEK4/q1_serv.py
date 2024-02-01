# 1. Write a UDP time server to display the current time and day.

import socket
import time
# create a socket object
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9991
# bind to the port
sock.bind((host, port))
while True:
    print ("Waiting for client...")
    data,addr = sock.recvfrom(1024)
    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    sock.sendto(currentTime.encode('ascii'), addr)
    