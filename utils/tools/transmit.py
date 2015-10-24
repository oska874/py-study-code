import Tkinter as tk
import tftpy as tftp
import pyftpdlib as ftp
import http as http


import transmit_cli as trans

if __name__ == "__main__":
	root = tk.Tk()

#ftp
	ftpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	ftpPane.pack()

	ftpIp = tk.Entry(ftpPane, bd =5)
	ftpIp.insert(0,"input IP")
	ftpPane.add(ftpIp)

	ftpPort = tk.Entry(ftpPane, bd =5)
	ftpPort.insert(0,"input PORT")
	ftpPane.add(ftpPort)

	ftpBtn = tk.Button(text="ftp start",width=10,command=trans.my_ftpd)
	ftpPane.add(ftpBtn)

#tftp
	tftpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	tftpPane.pack()

	tftpIp = tk.Entry(tftpPane, bd =5)
	tftpIp.insert(0,"input IP")
	tftpPane.add(tftpIp)

	tftpPort = tk.Entry(tftpPane, bd =5)
	tftpPort.insert(0,"input PORT")
	tftpPane.add(tftpPort)

	tftpBtn = tk.Button(text="tftp start",width=10,command=trans.my_tftpd)
	tftpPane.add(tftpBtn)

#http
	httpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	httpPane.pack()

	httpIp = tk.Entry(httpPane, bd =5)
	httpIp.insert(0,"input IP")
	httpPane.add(httpIp)

	httpPort = tk.Entry(httpPane, bd =5)
	httpPort.insert(0,"input PORT")
	httpPane.add(httpPort)

	httpBtn = tk.Button(text="http start",width=10,command=trans.my_httpd)
	httpPane.add(httpBtn)

#socket
	socketPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	socketPane.pack()

	socketIp = tk.Entry(socketPane, bd =5)
	socketIp.insert(0,"input IP")
	socketPane.add(socketIp)

	socketPort = tk.Entry(socketPane, bd =5)
	socketPort.insert(0,"input PORT")
	socketPane.add(socketPort)

	socketBtn = tk.Button(text="socket start",width=10,command=trans.my_socketd)
	socketPane.add(socketBtn)

	root.mainloop()