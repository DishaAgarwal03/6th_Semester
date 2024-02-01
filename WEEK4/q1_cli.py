#client.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9991

s.sendto("Sending address".encode(),(host,port))
tm, _ = s.recvfrom(1024)
print(' Current time from Server:', tm.decode())
s.close()