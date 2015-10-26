"""
Code illustration: 8.13
Creating Custom Mixins
Tkinter GUI Application Development Hotshot
""" 

from Tkinter import *

def frame(parent,  row, col):
    widget = Frame(parent)
    widget.grid(row= row, column=col)
    return widget

def label(parent,  row, col, text):
    widget = Label(parent, text=text)
    widget.grid(row= row, column=col,  sticky='w', padx=2)
    return widget

def button(parent, row, col, text, command):
    widget = Button(parent, text=text, command=command)
    widget.grid(row= row, column=col, sticky='e', padx=5, pady=3)
    return widget

def entry(parent,  row, col, var):
    widget = Entry(parent,textvariable= var)
    widget.grid(row= row, column=col, sticky='w', padx=5)
    return widget

def button_pressed(uname, pwd):
    print 'Username: %s' %uname
    print 'Password: %s'%pwd

if __name__ == '__main__':
    root = Tk()
    frm = frame(root, 0,0) 
    label(frm, 1,0,'Username:')
    uname= StringVar()
    entry(frm, 1,1,uname)
    label(frm, 2,0,'Password:')
    pwd= StringVar()
    entry(frm, 2,1,pwd)
    button(frm,3,1, 'login', lambda: button_pressed(uname.get(),pwd.get()) )
    root.mainloop()