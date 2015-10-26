"""
Code illustration: 7.04

Demo of Network Programming With Socket Module

Tkinter GUI Application Development Hotshot
""" 
 
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
print 'Socket Created'
host = 'www.google.com';
port = 80;
try:
    ip = socket.gethostbyname( host )
 
except socket.gaierror:
    print 'Could not resolve Hostname'
    sys.exit()
 
#Connect to remote server
s.connect((ip , port))
print 'Socket Connected to ' + host + ' on ip ' + ip
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
 
print 'Message send successfully'
#Now receive data
received_message = s.recv(4098)
print received_message 