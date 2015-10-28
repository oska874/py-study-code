import socket
import sys,os,time

#tcp
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.bind(("localhost",1082))

s1.listen(2)

con,addr = s1.accept()
while True:
	try:
		print("11")
		con.send("hello world")
		rcv = con.recv(100)
		print(rcv)
		time.sleep(3)
	except Exception, e:
		con.close()
		print("s1 error")
		break

con.close()
print("ser over")