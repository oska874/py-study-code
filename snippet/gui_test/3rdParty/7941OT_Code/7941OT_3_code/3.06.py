#!/usr/bin/env python
"""
Code illustration: 3.06
Demo of widget.config()

@Tkinter GUI Application Development Hotshot
""" 
from Tkinter import *
root = Tk()
widget = Button(root, text="#", bg='green')
widget.pack()

# prints out a dictionary of all config items for that widget
print widget.config() 

#prints out the dictionary key value pair for the 'bg' option of the said widget
print widget.config('bg')


root.mainloop()
 
