# do this to disable firewall b/w these machines
# 210905412_disha@networklab:~/Desktop/210905412_labs/WEEK4$ sudo ufw allow 31621/udp
# 210905412_disha@networklab:~/Desktop/210905412_labs/WEEK4$ sudo ufw allow to 172.16.59.36
# 210905412_disha@networklab:~/Desktop/210905412_labs/WEEK4$ sudo ufw allow from 172.16.59.36

import socket
HOST = '172.16.59.36'
PORT = 31621
addr = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
name = input(str("\nEnter your name: ")) 
s.sendto(name.encode(), addr)
s_name, _ = s.recvfrom(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")
while True:
    message, _ = s.recvfrom(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.sendto(message.encode(), addr)
        print("\n")
        break
    s.sendto(message.encode(), addr)