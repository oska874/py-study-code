import socket

print("create socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("done")

print("looking up for port number...")
port = socket.getservbyname('http','tcp')
print("done")

print("connect to baidu.com")
s.connect(("www.baidu.com",port))
print("done");

print("connect from ",s.getsockname())
print("connect to ",s.getpeername())
