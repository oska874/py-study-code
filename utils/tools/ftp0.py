# -*- coding:utf-8 -*-

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
 
 
def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()
    # Define a new user having full r/w permissions
    authorizer.add_user('test', 'test','./', perm='elradfmwM')
    # Define a read-only anonymous user
    authorizer.add_anonymous('./')
 
    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer
 
    # Define a customized banner (string returned when client connects)
    handler.banner = "Welcome to Jayvic's FTP."
 
    # Instantiate FTP server class and listen on 127.0.0.1:21
    address = ('127.0.0.1', 21)
    server = FTPServer(address, handler)
 
    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5
 
    # start ftp server
    server.serve_forever()
 
 
if __name__ == '__main__':
    main()