import tftpy as tftp
import re
import multiprocessing as mp
import threading

## ftp
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.filesystems import AbstractedFS
## http
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


## global var ##
tftpdOn = 0 
tftpSer = 0
tftpProcess = 0

ftpdOn = 0
ftpSer = 0
ftpProcess = 0

httpdOn = 0
socketdOn = 0
processAll = {}

## comman func ##
def valid_ip(ip):
	ipRe = re.compile("([0-9]{1,3}\.){3}[0-9]{1,3}$") #basic rule,and need improvement
	if ipRe.match(ip) != None:
		#print("get ip: "+ip)
		return 0
	else:
		return -1


def valid_port(port):
	portRe = re.compile("[0-9]+$")
	if portRe.match(port) != None:
		#print("get port : "+port)
		return 0
	else:
		return -1
def stop_proc(name):
	global processAll
	processAll[name].terminate()


def start_transd(type,ip,port,local):
	global tftpSer
	if type == "tftp":
		tftpSer = tftp.TftpServer(local)
		tftpSer.listen(ip,int(port))
	elif type == "ftp":
		# Instantiate a dummy authorizer for managing 'virtual' users
	    authorizer = DummyAuthorizer()
	    # Define a new user having full r/w permissions
	    authorizer.add_user('user_name', 'pass_word','./', perm='elradfmwM',msg_login='welcome',msg_quit='bye')
	    # Define a read-only anonymous user
	    authorizer.add_anonymous(local)
	 
	    # Instantiate FTP handler class
	    handler = FTPHandler
	    handler.authorizer = authorizer
	    handler.max_login_attempts = 3
	    handler.permit_foreign_addresses = True
	    handler.tcp_no_delay = True
	 
	    # Define a customized banner (string returned when client connects)
	    handler.banner = "Welcome to my FTP."
	 
	    # Instantiate FTP server class and listen on 127.0.0.1:21
	    address = (ip, int(port))
	    server = FTPServer(address, handler)
	 
	    # set a limit for connections
	    server.max_cons = 128 
	    server.max_cons_per_ip = 2
	 
	    absfs = AbstractedFS(unicode(local),handler)
	    #absfs.cwd = u"/bbb/ss/"
	    # start ftp server
	    server.serve_forever()
	elif type == "http":
		HandlerClass = SimpleHTTPRequestHandler
		ServerClass  = BaseHTTPServer.HTTPServer
		Protocol     = "HTTP/1.0"
		server_address = (ip,int(port))
		HandlerClass.protocol_version = Protocol
		httpd = ServerClass(server_address, HandlerClass)
		sa = httpd.socket.getsockname()
		print "Serving HTTP on", sa[0], "port", sa[1], "..."
		httpd.serve_forever()

## tftp set##
def my_tftpd(ip=0,port=0,local="./"):
	global tftpdOn
	global tftpProcess
	global processAll

	if tftpdOn == 0:
		tftpdOn = 2
		if valid_port(port) == 0 and valid_ip(ip) == 0:
			#tftpProcess = mp.Process(name='tftpS', target=start_transd,args=("tftp",ip,port,local))
			#tftpProcess.start()
			tftpProcess = threading.Thread(target=start_transd,name='tftpS',args=("tftp",ip,port,local))
			tftpProcess.start()
			processAll['tftpS']=tftpProcess
			return 0
		else:
			return -1

def my_tftpd2():
	global tftpdOn
	global tftpSer
	global tftpProcess
	if tftpdOn == 2:
		tftpdOn = 0
		stop_proc("tftpS")
	return 0

## ftp set ##
def my_ftpd(ip=0,port=0,local="./"):
	global ftpdOn
	global ftpProcess
	global processAll

	if ftpdOn == 0:
		#print("111: "+local)
		#print("ip %s port %s " % (ip,port))
		ftpdOn = 2
		if valid_port(port) == 0 and valid_ip(ip) == 0:
			#ftpProcess = mp.Process(name='ftpS', target=start_transd,args=("ftp",ip,port,local))
			#ftpProcess.start()
			ftpProcess = threading.Thread(target=start_transd,name='ftpS',args=("ftp",ip,port,local))
			ftpProcess.start()
			processAll['ftpS']=ftpProcess
			return 0
		else:
			return -1

def my_ftpd2():
	global ftpdOn
	global ftpProcess
	if ftpdOn == 2:
		ftpdOn = 0
		stop_proc("ftpS")
	return 0

## http set ##
def my_httpd(ip=0,port=0,local="./"):
	global httpdOn
	global httpProcess
	global processAll

	if httpdOn == 0:
		httpdOn = 2
		if valid_port(port) == 0 and valid_ip(ip) == 0:
			#httpProcess = mp.Process(name='httpS', target=start_transd,args=("http",ip,port,local))
			httpProcess = threading.Thread( target=start_transd,name='httpS',args=("http",ip,port,local))
			httpProcess.start()
			processAll['httpS']=httpProcess
			return 0
		else:
			return -1

def my_httpd2():
	global httpdOn
	global httpProcess
	if httpdOn == 2:
		httpdOn = 0
		stop_proc("httpS")
	return 0


## socket set ##
def my_socketd(ip=0,port=0,local="./"):
	if valid_port(port) == 0 and valid_ip(ip) == 0:
		print("start socketd : "+ip+":"+port)
		return 0
	else:
		return -1

