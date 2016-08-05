import select
import socket
 
response = 'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 11\r\n\r\nHello World'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server_address = ('localhost', 9527)
server.bind(server_address)
server.listen(1024)
READ_ONLY = select.EPOLLIN | select.EPOLLPRI
epoll = select.epoll()
epoll.register(server, READ_ONLY)
timeout = 60
fd_to_socket = { server.fileno(): server}
while True:
    events = epoll.poll(timeout)
    for fd, flag in events:
        sock = fd_to_socket[fd]
        if flag & READ_ONLY:
            if sock is server:
                conn, client_address = sock.accept()
                conn.setblocking(False)
                fd_to_socket[conn.fileno()] = conn
                epoll.register(conn, READ_ONLY)
            else:
                request = sock.recv(1024)
                sock.send(response)
                sock.close()
                del fd_to_socket[fd]

