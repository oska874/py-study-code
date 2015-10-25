import Tkinter as tk
import tftpy as tftp
import pyftpdlib as ftp
import http as http

def tftpdCall():
	#print("start tftp"+tfipStr.get()+":"+tfportStr.get())
	trans.my_tftpd(ip=tfipStr.get(), port=tfportStr.get())

def ftpdCall():
	#print("start ftp"+fipStr.get()+":"+fportStr.get())
	trans.my_ftpd(ip=fipStr.get(), port=fportStr.get())

def httpdCall():
	#print("start http"+hipStr.get()+":"+hportStr.get())
	trans.my_httpd(ip=hipStr.get(), port=hportStr.get())

def socketdCall():
	#print("start socket"+sipStr.get()+":"+sportStr.get())
	trans.my_socketd(ip=sipStr.get(), port=sportStr.get())


import transmit_cli as trans

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

	ftpBtn = tk.Button(text="ftp start",width=10,command=ftpdCall,relief=tk.RAISED)
	ftpPane.add(ftpBtn)

#tftp
	tftpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	tftpPane.pack()

	tftpIp = tk.Entry(tftpPane, bd =5,textvariable=tfipStr)
	tftpIp.insert(0,"0.0.0.0")
	tftpPane.add(tftpIp)

	tftpPort = tk.Entry(tftpPane, bd =5,textvariable=tfportStr)
	tftpPort.insert(0,"69")
	tftpPane.add(tftpPort)

	tftpBtn = tk.Button(text="tftp start",width=10,command=tftpdCall)
	tftpPane.add(tftpBtn)

#http
	httpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	httpPane.pack()

	httpIp = tk.Entry(httpPane, bd =5,textvariable=hipStr)
	httpIp.insert(0,"0.0.0.0")
	httpPane.add(httpIp)

	httpPort = tk.Entry(httpPane, bd =5,textvariable=hportStr)
	httpPort.insert(0,"80")
	httpPane.add(httpPort)

	httpBtn = tk.Button(text="http start",width=10,command=httpdCall)
	httpPane.add(httpBtn)

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

	root.mainloop()