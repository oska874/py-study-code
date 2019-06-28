# -*- coding: UTF-8 -*-
#button

import tkinter as tk
import tkMessageBox

def helloCallback():
	tkMessageBox.showinfo( "Hello Python", "Hello World")

root = tk.Tk()				#top windows

L1 = tk.Label(root, text="User Name")
L1.pack( side = tk.LEFT)
E1 = tk.Entry(root, bd =5)
E1.pack(side = tk.RIGHT)


root.mainloop()				#start application