import Tkinter as tk
import tftpy as tftp
import pyftpdlib as ftp
import http as http

import transmit_cli

def tftpdStartCall():
	transmit_cli.my_tftpd(ip=tfipStr.get(), port=tfportStr.get())

def tftpdStopCall():
	transmit_cli.my_tftpd2()

def ftpdStartCall():
	#print("start ftp"+fipStr.get()+":"+fportStr.get())
	transmit_cli.my_ftpd(ip=fipStr.get(), port=fportStr.get())

def ftpdStopCall():
	#print("start ftp"+fipStr.get()+":"+fportStr.get())
	transmit_cli.my_ftpd2()

def httpdStartCall():
	transmit_cli.my_httpd(ip=hipStr.get(), port=hportStr.get())

def httpdStopCall():
	transmit_cli.my_httpd2()

def socketdCall():
	#print("start socket"+sipStr.get()+":"+sportStr.get())
	transmit_cli.my_socketd(ip=sipStr.get(), port=sportStr.get())

if __name__ == "__main__":
	root = tk.Tk()

	fipStr=tk.StringVar()
	fportStr=tk.StringVar()
	tfipStr=tk.StringVar()
	tfportStr=tk.StringVar()
	hipStr=tk.StringVar()
	hportStr=tk.StringVar()
	sipStr=tk.StringVar()
	sportStr=tk.StringVar()

#ftp
	ftpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	ftpPane.pack()
	
	ftpIp = tk.Entry(ftpPane, bd =5,textvariable=fipStr)
	ftpIp.insert(0,"0.0.0.0")
	ftpPane.add(ftpIp)
	
	ftpPort = tk.Entry(ftpPane, bd =5,textvariable=fportStr)
	ftpPort.insert(0,"20")
	ftpPane.add(ftpPort)

	ftpBtnStart = tk.Button(text="ftp start",width=10,command=ftpdStartCall)
	ftpPane.add(ftpBtnStart)

	ftpBtnStop = tk.Button(text="stop",width=10,command=ftpdStopCall)
	ftpPane.add(ftpBtnStop)

#tftp
	tftpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	tftpPane.pack()

	tftpIp = tk.Entry(tftpPane, bd =5,textvariable=tfipStr)
	tftpIp.insert(0,"0.0.0.0")
	tftpPane.add(tftpIp)

	tftpPort = tk.Entry(tftpPane, bd =5,textvariable=tfportStr)
	tftpPort.insert(0,"69")
	tftpPane.add(tftpPort)

	tftpBtnStart = tk.Button(text="tftp start",width=10,command=tftpdStartCall)
	tftpPane.add(tftpBtnStart)

	tftpBtnStop = tk.Button(text="stop",width=10,command=tftpdStopCall)
	tftpPane.add(tftpBtnStop)
#http
	httpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	httpPane.pack()

	httpIp = tk.Entry(httpPane, bd =5,textvariable=hipStr)
	httpIp.insert(0,"0.0.0.0")
	httpPane.add(httpIp)

	httpPort = tk.Entry(httpPane, bd =5,textvariable=hportStr)
	httpPort.insert(0,"80")
	httpPane.add(httpPort)

	httpBtn = tk.Button(text="http start",width=10,command=httpdStartCall)
	httpPane.add(httpBtn)

	httpBtnStop = tk.Button(text="stop",width=10,command=httpdStopCall)
	httpPane.add(httpBtnStop)
	
#socket
	socketPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	socketPane.pack()

	socketIp = tk.Entry(socketPane, bd =5,textvariable=sipStr)
	socketIp.insert(0,"0.0.0.0")
	socketPane.add(socketIp)

	socketPort = tk.Entry(socketPane, bd =5,textvariable=sportStr)
	socketPort.insert(0,"1080")
	socketPane.add(socketPort)

	socketBtn = tk.Button(text="socket start",width=10,command=socketdCall)
	socketPane.add(socketBtn)

	socketBtnStop = tk.Button(text="stop",width=10,command=socketdCall)
	socketPane.add(socketBtnStop)

	root.mainloop()