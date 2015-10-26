"""
Code illustration: 1.05
Where to use pack() options

@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
root = Tk()
fr = Frame(root)

Button(fr, text='ALL IS WELL').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fr, text='BACK TO BASICS').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fr, text='CATCH ME IF U CAN').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fr, text='LEFT').pack(side=LEFT)
Button(fr, text='CENTER').pack(side=LEFT)
Button(fr, text='RIGHT').pack(side=LEFT)
fr.pack()
root.mainloop()
