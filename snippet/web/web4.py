import Queue
import socket
import threading
 
response = 'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 11\r\n\r\nHello World'
 
server = socket.socket()
server.bind(('0.0.0.0', 9526))
server.listen(1024)
 
def handler(queue):
    while True:
        client  = queue.get()
        request = client.recv(1024)
        client.send(response)
        client.close()
 
queue = Queue.Queue()
processors = 8
for i in range(0, processors):
    thread = threading.Thread(target=handler, args=(queue,))
    thread.daemon = True
    thread.start()
 
while True:
    client, clientaddr = server.accept()
    queue.put(client)

