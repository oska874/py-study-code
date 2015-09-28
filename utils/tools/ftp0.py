# -*- coding:utf-8 -*-
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.filesystems import AbstractedFS
 
 
def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()
    # Define a new user having full r/w permissions
    authorizer.add_user('user_name', 'pass_word','./', perm='elradfmwM',msg_login='welcome',msg_quit='bye')
    # Define a read-only anonymous user
    authorizer.add_anonymous('./')
 
    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.max_login_attempts = 3
    handler.permit_foreign_addresses = True
    handler.tcp_no_delay = True
 
    # Define a customized banner (string returned when client connects)
    handler.banner = "Welcome to my FTP."
 
    # Instantiate FTP server class and listen on 127.0.0.1:21
    address = ('0.0.0.0', 2121)
    server = FTPServer(address, handler)
 
    # set a limit for connections
    server.max_cons = 128 
    server.max_cons_per_ip = 2
 
    absfs = AbstractedFS(u"./",handler)
    absfs.cwd = u"/bbb/ss/"
    # start ftp server
    server.serve_forever()
 
 
if __name__ == '__main__':
    main()
