"""
Code illustration: 7.05

Fetching web content with urllib -  demo

Tkinter GUI Application Development Hotshot
""" 


import urllib
data =  urllib.urlopen('http://www.packtpub.com')
print data.read()
data.close()
