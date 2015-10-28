import socket
import sys,os,time

#tcp
c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	c1.connect(("localhost",1084))
except Exception,e:
	c1.close()
	print("c1 1 1")

while True:
	try:
		rcv = c1.recv(100)
		print(rcv)
		c1.send("nice to meet you")
		time.sleep(3)
	except Exception, e:
		c1.close()
		print("c1 error")
		break

c1.close()
print("cli over")