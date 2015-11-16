#-*- coding:utf8 -*-
import socket
import select
import Queue

server_address=('0.0.0.0',10001)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(False)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(server_address)
server.listen(5)

message_queues={}
#poll时间单位是毫秒
timeout = 1000

# Create a limit for the event
READ_ONLY = ( select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
READ_WRITE = (READ_ONLY|select.POLLOUT)

# Set up the poller
poller = select.poll()
poller.register(server,READ_ONLY)
#Map file descriptors to socket objects
#server.fileno()是获得server这个socket的文件描述符，是int类型
fd_to_socket = {server.fileno():server,}

i=0
while True:
    i=i+1
    events = poller.poll(timeout)
    print(events,i)
    #fd是描述符，flag是event状态，都是int类型
    for fd ,flag in  events:
        # Retrieve the actual socket from its file descriptor
        #s为当前的socket对象
        s = fd_to_socket[fd]
        
        if flag & (select.POLLIN | select.POLLPRI) :
            print(i)
            if s is server :
                print(i)
                # A readable socket is ready to accept a connection
                connection , client_address = s.accept()
                print " Connection " , client_address
                connection.setblocking(False)
                 
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection,READ_ONLY)
                 
                #Give the connection a queue to send data
                message_queues[connection]  = Queue.Queue()
            else :
                data = s.recv(1024)
                if data:
                    print(i)
                    # A readable client socket has data
                    print "  received %s from %s " % (data, s.getpeername())
                    message_queues[s].put(data)
                    poller.modify(s,READ_WRITE)
                else :
                    print(i)
                    # Close the connection
                    print "  closing" , s.getpeername()
                    # Stop listening for input on the connection
                    poller.unregister(s)
                    s.close()
                    del message_queues[s]
        elif flag & select.POLLHUP :
            print(i)
            #A client that "hang up" , to be closed.
            print " Closing ", s.getpeername() ,"(HUP)"
            poller.unregister(s)
            s.close()
        elif flag & select.POLLOUT :
            print(i)
            #Socket is ready to send data , if there is any to send
            try:
                next_msg = message_queues[s].get_nowait()
            except Queue.Empty:
                # No messages waiting so stop checking
                print s.getpeername() , " queue empty"
                poller.modify(s,READ_ONLY)
            else :
                print " sending %s to %s" % (next_msg , s.getpeername())
                s.send(next_msg)
        elif flag & select.POLLERR:
            print(i)
            #Any events with POLLERR cause the server to close the socket
            print "  exception on" , s.getpeername()
            poller.unregister(s)
            s.close()
            del message_queues[s]
