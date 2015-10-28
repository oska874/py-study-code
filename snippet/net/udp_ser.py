import socket
import sys,os,time

#udp
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s1.bind(("localhost",8082))

while True:
	try:		
		rcv, addr = s1.recvfrom(100)
		print(rcv)
		time.sleep(3)
		s1.sendto("hello udp",addr)
	except Exception, e:
		s1.close()
		print("s1 error")
		break

s1.close()
print("ser over")