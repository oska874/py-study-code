import socket
 
response = 'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 11\r\n\r\nHello World'
 
server = socket.socket()
server.bind(('0.0.0.0', 9527))
server.listen(1024)
 
while True:
    client, clientaddr = server.accept()  # blocking
    print(client)
    print(clientaddr)
    request = client.recv(1024)  # blocking
    client.send(response)  # maybe blocking
    client.close()

