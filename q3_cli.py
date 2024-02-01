import socket
HOST = socket.gethostname() 
PORT = 31001
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