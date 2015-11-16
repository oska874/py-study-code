#-*- codiing:utf-8 -*-
'''
Created on 2012-1-6
The echo server example from the socket section can be extanded to watche for more than
one connection at a time by using select() .The new version starts out by creating a nonblocking
TCP/IP socket and configuring it to listen on an address
@author: xiaojay
'''

'''
select can do many sockets in one time, include recvive/send/exception
'''

import select
import socket
import Queue
 
#create a socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(False)
#set option reused
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR  , 1)
 
server_address= ('192.168.1.102',10001)
server.bind(server_address)
server.listen(10)
 
#sockets from which we except to read
inputs = [server]
 
#sockets from which we expect to write
outputs = []
 
#Outgoing message queues (socket:Queue)
message_queues = {}
 
#A optional parameter for select is TIMEOUT
timeout = 2000000
 

poObj = select.poll()
poObj.register(server, select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)#select.POLLIN|select.POLLOUT|select.POLLERR)

fds = ""
eves = ""
while inputs:
    print("waiting for next event")
#    readable , writable , exceptional = select.select(inputs, outputs, inputs, timeout)
    xx = poObj.poll(timeout)
    if len(xx) == 2:
        fds=xx(0)
        eves=xx(1)
        print(fds,eves)
    else:
        print("no")
    
    if fds != None:
        if eves &(select.POLLPRI| select.POLLIN):
            print("in")
        elif eves == select.POLLOUT:
            print("out")
        elif eves == select.POLLERR:
            print("err")

    # When timeout reached , select return three empty lists
    if not (fds or eves ) :
        print("Time out ! ")
        break;

