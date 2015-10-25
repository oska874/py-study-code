import Tkinter as tk
import tkFileDialog
import transmit_cli

## callback
def selectTftpFold():
	global tfoldStr
	dir = tkFileDialog.askdirectory()
	if dir != "" :
		tfoldStr.set(dir)
	else:
		tfoldStr.set(u"./")

def selectFtpFold():
	global ffoldStr
	dir = tkFileDialog.askdirectory()
	if dir != "" :
		ffoldStr.set(dir)
	else:
		ffoldStr.set(u"./")

def selectHttpFold():
	global hfoldStr
	dir = tkFileDialog.askdirectory()
	if dir != "" :
		hfoldStr.set(dir)
	else:
		hfoldStr.set(u"./")

def selectSocketFold():
	global sfoldStr
	dir = tkFileDialog.askdirectory()
	if dir != "":
		sfoldStr.set(dir)
	else:
		sfoldStr.set(u"./")

###
# tftp
def tftpdStartCall():
	global tfoldStr
	transmit_cli.my_tftpd(ip=tfipStr.get(), port=tfportStr.get(),local=tfoldStr.get())

def tftpdStopCall():
	transmit_cli.my_tftpd2()

# ftp
def ftpdStartCall():
	global ffoldStr
	transmit_cli.my_ftpd(ip=fipStr.get(), port=fportStr.get(),local=ffoldStr.get())
	print ffoldStr.get()
	
def ftpdStopCall():
	transmit_cli.my_ftpd2()

#http
def httpdStartCall():
	global hfoldStr 
	transmit_cli.my_httpd(ip=hipStr.get(), port=hportStr.get(),local=u"./")#hfoldStr.get())

def httpdStopCall():
	transmit_cli.my_httpd2()

#socket
def socketdCall():
	global sfoldStr
	transmit_cli.my_socketd(ip=sipStr.get(), port=sportStr.get(),local=sfoldStr.get())

## main ##
if __name__ == "__main__":

	root = tk.Tk()

#value of entris
	fipStr=tk.StringVar()
	fportStr=tk.StringVar()
	ffoldStr=tk.StringVar()

	tfipStr=tk.StringVar()
	tfportStr=tk.StringVar()
	tfoldStr=tk.StringVar()

	hipStr=tk.StringVar()
	hportStr=tk.StringVar()
	hfoldStr=tk.StringVar()

	sipStr=tk.StringVar()
	sportStr=tk.StringVar()
	sfoldStr=tk.StringVar()

#ftp
	ftpPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	ftpPane.pack()
	
	ftpIp = tk.Entry(ftpPane, bd =5,textvariable=fipStr)
	ftpIp.insert(0,"0.0.0.0")
	ftpPane.add(ftpIp)
	
	ftpPort = tk.Entry(ftpPane, bd =5,textvariable=fportStr)
	ftpPort.insert(0,"20")
	ftpPane.add(ftpPort)

	ftpFold = tk.Entry(ftpPane, bd =5,textvariable=ffoldStr)
	ftpFold.insert(0,"./")
	ftpPane.add(ftpFold)

	ftpBtnSel = tk.Button(text="select fold",width=10,command=selectFtpFold)
	ftpPane.add(ftpBtnSel)

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

	tftpFold = tk.Entry(tftpPane, bd =5,textvariable=tfoldStr)
	tftpFold.insert(0,"./")
	tftpPane.add(tftpFold)

	tftpBtnSel = tk.Button(text="select fold",width=10,command=selectTftpFold)
	tftpPane.add(tftpBtnSel)

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

	httpFold = tk.Entry(httpPane, bd =5,textvariable=hfoldStr)
	httpFold.insert(0,"no use")
	httpPane.add(httpFold)
	
	httpBtnSel = tk.Button(text="select fold",width=10,command=selectHttpFold)
	httpPane.add(httpBtnSel)

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

	socketFold = tk.Entry(socketPane, bd =5,textvariable=sfoldStr)
	socketFold.insert(0,"./")
	socketPane.add(socketFold)
	
	socketBtnSel = tk.Button(text="select fold",width=10,command=selectSocketFold)
	socketPane.add(socketBtnSel)

	socketBtn = tk.Button(text="socket start",width=10,command=socketdCall)
	socketPane.add(socketBtn)

	socketBtnStop = tk.Button(text="stop",width=10,command=socketdCall)
	socketPane.add(socketBtnStop)

## info
	infoPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	infoPane.pack()


	root.mainloop()