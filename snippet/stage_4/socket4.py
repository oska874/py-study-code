import socket
import sys,os,time

#udp

c1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	try:
		c1.sendto("see you udp",("127.0.0.1",8082))
		rcv = c1.recv(100)
		print(rcv)
		time.sleep(3)		
	except Exception, e:
		c1.close()
		print("s1 error")
		break

c1.close()
print("ser over")