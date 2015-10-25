import tftpy as tftp
import pyftpdlib as ftp
import http as http
import re


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
def my_tftpd(ip=0,port=0):
	#print("start tftp"+ip+":"+port)
	if valid_port(port) == 0 and valid_ip(ip) == 0:
		print("start tftpd : "+ip+":"+port)

		return 0
	else:
		return -1

def my_ftpd(ip=0,port=0):
	#print("start ftp"+ip+":"+port)
	if valid_port(port) == 0 and valid_ip(ip) == 0:
		print("start ftpd : "+ip+":"+port)
		return 0
	else:
		return -1
def my_httpd(ip=0,port=0):
	#print("start http"+ip+":"+port)
	if valid_port(port) == 0 and valid_ip(ip) == 0:
		print("start httpd : "+ip+":"+port)
		return 0
	else:
		return -1
def my_socketd(ip=0,port=0):
	#print("start socket"+ip+":"+port)
	if valid_port(port) == 0 and valid_ip(ip) == 0:
		print("start socketd : "+ip+":"+port)
		return 0
	else:
		return -1

