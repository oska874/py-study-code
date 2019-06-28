"""
Code illustration: 7.05

Fetching web content with urllib -  demo

tkinter GUI Application Development Hotshot
""" 


import urllib.request, urllib.parse, urllib.error
data =  urllib.request.urlopen('http://www.packtpub.com')
print(data.read())
data.close()
