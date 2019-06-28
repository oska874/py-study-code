# -*- coding: UTF-8 -*-
#button

import tkinter as tk
import tkMessageBox

def helloCallback():
	tkMessageBox.showinfo( "Hello Python", "Hello World")

root = tk.Tk()				#top windows

btn = tk.Button(root,text="hello",command=helloCallback)
btn.pack()

btn1 = tk.Button(root,text="exit",command=quit)
btn1.pack()
root.mainloop()				#start application