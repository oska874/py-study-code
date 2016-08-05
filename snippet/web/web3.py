import socket
import multiprocessing
 
response = 'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 11\r\n\r\nHello World'
 
server = socket.socket()
server.bind(('0.0.0.0', 9527))
server.listen(1024)
 
def handler():
    while True:
        client, addr = server.accept()
        request = client.recv(1024)
        client.send(response)
        client.close()
processors = 8
for i in range(0, processors):
    process = multiprocessing.Process(target=handler, args=())
    process.start()

