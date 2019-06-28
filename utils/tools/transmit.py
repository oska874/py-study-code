# -*- coding:utf-8 -*-
import tkinter as tk
import tkFileDialog
import transmit_cli

## callback
def selectTftpFold():
	global tfoldStr
	global infoTxtStr
	dir = tkFileDialog.askdirectory()
	if dir != "" :
		tfoldStr.set(dir)
		infoTxtStr.set(dir)
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
	if tfoldStr.get() != "":
		transmit_cli.my_tftpd(ip=tfipStr.get(), port=tfportStr.get(),local=tfoldStr.get())

def tftpdStopCall():
	transmit_cli.my_tftpd2()

# ftp
def ftpdStartCall():
	global ffoldStr
	if ffoldStr.get() != "":
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
def socketdStartCall():
	global sfoldStr
	transmit_cli.my_socketd(ip=sipStr.get(), port=sportStr.get(),local=sfoldStr.get())

def socketdStopCall():
	global sfoldStr
	transmit_cli.my_socketd2()

## client func
def selectSocketFold2():
	global sfoldStr2
	dir = tkFileDialog.askopenfilename()
	if dir != "":
		sfoldStr2.set(dir)
		infoTxtStr.set(dir)
	else:
		sfoldStr2.set(u"./")

def selectTftpFold2():
	global tfoldStr2
	global infoTxtStr
	dir = tkFileDialog.askopenfilename()
	if dir != "" :
		tfoldStr2.set(dir)
		infoTxtStr.set(dir)
	else:
		tfoldStr2.set(u"./")

def socketdStartCall2():
	global sfoldStr2
	transmit_cli.my_socketcli(ip=sipStr2.get(), port=sportStr2.get(),local=sfoldStr2.get())

def tftpdStartCall2():
	global tfoldStr2
	transmit_cli.my_tftpcliup(ip=tfipStr2.get(), port=tfportStr2.get(),local=tfoldStr2.get())

def tftpdStartCall3():
	global tfoldStr2
	transmit_cli.my_tftpclidown(ip=tfipStr2.get(), port=tfportStr2.get(),local=tfoldStr2.get())

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

	infoTxtStr=tk.StringVar()

## server
	divid0 = tk.PanedWindow(orient=tk.HORIZONTAL)
	divid0.add(tk.Label(width=100,justify='left',text="Server Part"))
	divid0.pack()

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

	ftpBtnSel = tk.Button(text="select fold",width=15,command=selectFtpFold)
	ftpPane.add(ftpBtnSel)

	ftpBtnStart = tk.Button(text="ftp start",width=15,command=ftpdStartCall)
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

	tftpBtnSel = tk.Button(text="select fold",width=15,command=selectTftpFold)
	tftpPane.add(tftpBtnSel)

	tftpBtnStart = tk.Button(text="tftp start",width=15,command=tftpdStartCall)
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

	# httpFold = tk.Entry(httpPane, bd =5,textvariable=hfoldStr)
	# httpFold.insert(0,"no use")
	# httpPane.add(httpFold)
	
	# httpBtnSel = tk.Button(text="select fold",width=10,command=selectHttpFold)
	# httpPane.add(httpBtnSel)

	httpBtn = tk.Button(text="http start",width=15,command=httpdStartCall)
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
	socketPort.insert(0,"1083")
	socketPane.add(socketPort)

	socketFold = tk.Entry(socketPane, bd =5,textvariable=sfoldStr)
	socketFold.insert(0,"./")
	socketPane.add(socketFold)
	
	socketBtnSel = tk.Button(text="select fold",width=15, command=selectSocketFold)
	socketPane.add(socketBtnSel)

	socketBtn = tk.Button(text="socket start",width=15,command=socketdStartCall)
	socketPane.add(socketBtn)

	socketBtnStop = tk.Button(text="stop",width=10,command=socketdStopCall)
	socketPane.add(socketBtnStop)

## client
	sipStr2=tk.StringVar()
	sportStr2=tk.StringVar()
	sfoldStr2=tk.StringVar()

	tfipStr2=tk.StringVar()
	tfportStr2=tk.StringVar()
	tfoldStr2=tk.StringVar()

	divid1 = tk.PanedWindow(orient=tk.HORIZONTAL)
	divid1.add(tk.Label(width=100,justify='left',text="Client Part"))
	divid1.pack()
#socket client
	socketPane2 = tk.PanedWindow(orient=tk.HORIZONTAL)
	socketPane2.pack()

	socketIp2 = tk.Entry(socketPane2, bd =5,textvariable=sipStr2)
	socketIp2.insert(0,"127.0.0.1")
	socketPane2.add(socketIp2)

	socketPort2 = tk.Entry(socketPane2, bd =5,textvariable=sportStr2)
	socketPort2.insert(0,"1083")
	socketPane2.add(socketPort2)

	socketFold2 = tk.Entry(socketPane2, bd =5,textvariable=sfoldStr2)
	socketFold2.insert(0,"./")
	socketPane2.add(socketFold2)
	
	socketBtnSel2 = tk.Button(text="select file",width=15,command=selectSocketFold2)
	socketPane2.add(socketBtnSel2)

	socketBtn2 = tk.Button(text="socket send",width=15,command=socketdStartCall2)
	socketPane2.add(socketBtn2)

#tftp client
	tftpPane2 = tk.PanedWindow(orient=tk.HORIZONTAL)
	tftpPane2.pack()

	tftpIp2 = tk.Entry(tftpPane2, bd =5,textvariable=tfipStr2)
	tftpIp2.insert(0,"127.0.0.1")
	tftpPane2.add(tftpIp2)

	tftpPort2 = tk.Entry(tftpPane2, bd =5,textvariable=tfportStr2)
	tftpPort2.insert(0,"69")
	tftpPane2.add(tftpPort2)

	tftpFold2 = tk.Entry(tftpPane2, bd =5,textvariable=tfoldStr2)
	tftpFold2.insert(0,"")
	tftpPane2.add(tftpFold2)

	tftpBtnSel2 = tk.Button(text="select file",width=15,command=selectTftpFold2)
	tftpPane2.add(tftpBtnSel2)

	tftpBtnStart2 = tk.Button(text="upload",width=15,command=tftpdStartCall2)
	tftpPane2.add(tftpBtnStart2)

	tftpBtnStart3 = tk.Button(text="download",width=10,command=tftpdStartCall3)
	tftpPane2.add(tftpBtnStart3)

## info
	infoPane = tk.PanedWindow(orient=tk.HORIZONTAL)
	infoPane.pack()

	infoText = tk.Label(width=100,justify='left',textvariable=infoTxtStr)
	infoPane.add(infoText)

	root.mainloop()