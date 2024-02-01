# 3. Write a TCP/UDP peer to peer chat system between two different machines.

# do this to disable firewall b/w these machines
# 210905412_disha@networklab:~/Desktop/210905412_labs/WEEK4$ sudo ufw allow 31621/udp
# 210905412_disha@networklab:~/Desktop/210905412_labs/WEEK4$ sudo ufw allow to 172.16.59.36
# 210905412_disha@networklab:~/Desktop/210905412_labs/WEEK4$ sudo ufw allow from 172.16.59.36

import socket
HOST = '172.16.59.36'
PORT = 31621
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