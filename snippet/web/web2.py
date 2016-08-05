# -*- encoding:utf8 -*-

import socket
import signal
import multiprocessing
 
response = 'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 11\r\n\r\nHello World'
 
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 9527))
server.listen(1024)
 
def handler(client):
    request = client.recv(1024)
    client.send(response)
    client.close()
 
#多进程里的子进程执行完后并不会死掉，而是变成僵尸进程，等待主进程挂掉后才会死掉，下面这条语句可以解决这个问题。
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
 
while True:
    client, addr = server.accept()
    process = multiprocessing.Process(target=handler, args=(client,))
    process.start()

