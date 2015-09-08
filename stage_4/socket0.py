import socket

print(socket.getaddrinfo("example.org", 80, 0, 0, socket.IPPROTO_TCP))

print(socket.getfqdn())

print(socket.gethostbyname("ezio-HP-ENVY-15-Notebook-PC"))

print(socket.gethostbyname_ex("ezio-HP-ENVY-15-Notebook-PC"))

print(socket.gethostbyaddr("127.0.0.1"))

print(socket.getprotobyname("udplite"))

s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(s1)
