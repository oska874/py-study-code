"""
Code illustration: 8.01
Tkinter Trace Variable Demo

Tkinter GUI Application Development Hotshot
""" 

from Tkinter import *
root = Tk()
myvar = StringVar()
def trace_when_myvar_written(var,indx,mode):
    print "Traced variable %s"%myvar.get()
    #print 'mode: %s'%mode

myvar.trace_variable("w", trace_when_myvar_written)

Label(root, textvariable=myvar).pack(padx=5, pady=5)
Entry(root, textvariable=myvar).pack(padx=5, pady=5)


root.mainloop()