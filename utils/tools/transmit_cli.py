# -*- coding:utf-8 -*-
import tftpy as tftp
import re
import multiprocessing as mp
import threading
import time

## ftp
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.filesystems import AbstractedFS
## http
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

##socket
import socket

## global var ##
tftpdOn = 0 
tftpSer = 0
tftpProcess = 0

ftpdOn = 0
ftpSer = 0
ftpProcess = 0

httpdOn = 0
httpSer = 0
httpProcess = 0

socketdOn = 0
socketdProcess = 0
socketSer = 0
conSer = 0
SOC_S = True

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

def start_transd(type1,ip,port,local):
	global tftpSer
	global ftpSer
	global httpSer
	global socketSer
	global conSer
	global SOC_S
	print(type1,ip,port,local)
	if type1 == "tftp":
		tftpSer = tftp.TftpServer(local)
		tftpSer.listen(ip,int(port))
	elif type1 == "ftp":
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
	    ftpSer = FTPServer(address, handler)
	 
	    # set a limit for connections
	    ftpSer.max_cons = 128 
	    ftpSer.max_cons_per_ip = 2
	 
	    absfs = AbstractedFS(unicode(local),handler)
	    #absfs.cwd = u"/bbb/ss/"
	    # start ftp server
	    ftpSer.serve_forever()
	elif type1 == "http":
		HandlerClass = SimpleHTTPRequestHandler
		ServerClass  = BaseHTTPServer.HTTPServer
		Protocol     = "HTTP/1.0"
		server_address = (ip,int(port))
		HandlerClass.protocol_version = Protocol
		httpSer = ServerClass(server_address, HandlerClass)
		sa = httpSer.socket.getsockname()
		print "Serving HTTP on", sa[0], "port", sa[1], "..."
		httpSer.serve_forever()
	elif type1 == "socket":
		#tcp
		socketSer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		bi = socketSer.bind((ip,int(port)))
		socketSer.listen(2)
		conSer,addr = socketSer.accept()
		while SOC_S == True:
			try:
				conSer.send("hi")
				rcv = conSer.recv(10240)
				print(rcv)
				#time.sleep(3)
			except Exception, e:
				conSer.close()
				print("s1 error")
				break
		print("socket close")
		conSer.close()

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
		#stop_proc("tftpS")
		tftpSer.stop()
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
	global ftpSer
	if ftpdOn == 2:
		ftpdOn = 0
		#stop_proc("ftpS")
		ftpSer.close_all()
	return 0

## http set ##
def my_httpd(ip=0,port=0,local="./"):
	global httpdOn
	global httpProcess
	global processAll

	if httpdOn == 0:
		httpdOn = 2
		if valid_port(port) == 0 and valid_ip(ip) == 0:
			httpProcess = threading.Thread( target=start_transd,name='httpS',args=("http",ip,port,local))
			httpProcess.start()
			processAll['httpS']=httpProcess
			return 0
		else:
			return -1

def my_httpd2():
	global httpdOn
	global httpSer
	if httpdOn == 2:
		httpdOn = 0
		httpSer.server_close()
	return 0

## socket set ##
def my_socketd(ip=0,port=0,local="./"):
	global socketdProcess
	global socketdOn
	global SOC_S
	if socketdOn == 0:
		socketdOn = 2
		if valid_port(port) == 0 and valid_ip(ip) == 0:
			print("start socketd : "+ip+":"+port)
			SOC_S = True
			socketdProcess = threading.Thread( target=start_transd,name='socketS',args=("socket",ip,port,local))
			socketdProcess.start()
			processAll["socketS"]=socketdProcess
			return 0
		else:
			return -1

def my_socketd2():
	global conSer
	global socketdOn
	global SOC_S
	if socketdOn == 2:
		socketdOn = 0
		SOC_S = False

##client

def send_data(types,ip,port,local):
	if types == "socket":
		#tcp
		print(ip,port,local)
		lens = 1024
		c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			c1.connect((ip,int(port)))
		except Exception,e:
			c1.close()
			print("c1 ",e)

		try:
			f = open(local,'r')
		except Exception,e:
			c1.close()
			print("open file fail: ",e)

		for x in f:
			try:
				rcv = c1.recv(100)
				c1.send(x) ## must change the send amount
			except Exception, e:
				f.close()
				c1.close()
				print("c1 error,",e)
				break

		f.close()
		c1.close()
		print("send finish")	

	elif types == "tftpdown":
		#tftp download
		try:
			print(local)
			down1 = tftp.TftpClient(ip,int(port))
			down1.download(str(local),"temp_down")
		except Exception, e:
			print(e)

	elif types == "tftpup":
		#tftp upload
		try:			
			up1 = tftp.TftpClient(ip,int(port))
			up1.upload("temp_up",str(local))
		except Exception,e:
			print(e)


def my_socketcli(ip=0,port=0,local="./"):
	if valid_port(port) == 0 and valid_ip(ip) == 0:
		#first step:just send string to server,next step read file and send to server
		socketSendThread=threading.Thread(target=send_data,args=("socket",ip,port,local))
		socketSendThread.start()

def my_tftpcliup(ip=0,port=0,local="./"):
	if valid_port(port) == 0 and valid_ip(ip) == 0:
		#first step:just send string to server,next step read file and send to server
		tftpSendThread=threading.Thread(target=send_data,args=("tftpup",ip,port,local))
		tftpSendThread.start()
	pass

def my_tftpclidown(ip=0,port=0,local="./"):
	if valid_port(port) == 0 and valid_ip(ip) == 0:
		#first step:just send string to server,next step read file and send to server
		tftpSendThread=threading.Thread(target=send_data,args=("tftpdown",ip,port,local))
		tftpSendThread.start()
	pass