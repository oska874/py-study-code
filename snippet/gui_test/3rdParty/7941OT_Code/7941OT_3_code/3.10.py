#!/usr/bin/env python
"""
Code illustration: 3.10.py
1. tkinter versus ttk Themed Widgets
2. new widgets introduced in ttk

@Tkinter GUI Application Development Hotshot
""" 

from Tkinter import *
import ttk


root= Tk()

style = ttk.Style()
print(style.theme_names())
#style.theme_use('clam') 

root.title('Tkinter Versus ttk Themed Widgets')

ttk.Separator(root,orient=VERTICAL).grid(row=0, rowspan=8, column=1,sticky="wns")

Label(root, text= 'Tkinter    Versus').grid(row=0, columnspan=2, sticky='ew')
ttk.Label(root, text='ttk').grid(row=0, column=1)


Button(root, text='tk Button').grid(row=1, column=0)
ttk.Button(root, text='ttk Button').grid(row=1, column=1)


Checkbutton(root, text='tk CheckButton').grid(row=2, column=0)
ttk.Checkbutton(root, text='ttk CheckButton').grid(row=2, column=1)

Entry(root).grid(row=3, column=0)
ttk.Entry(root).grid(row=3, column=1)


PanedWindow(root).grid(row=4, column=0)
ttk.PanedWindow(root).grid(row=4, column=1)

Radiobutton(root, text='tk Radio').grid(row=5, column=0)
ttk.Radiobutton(root, text='ttk Radio').grid(row=5, column=1)


Scale(root,orient=HORIZONTAL).grid(row=6, column=0)
ttk.Scale(root).grid(row=6, column=1)

ttk.Separator(root,orient=HORIZONTAL).grid(row=7, columnspan=2,sticky="ew")
ttk.Label(root, text='NEW WIDGETS INTRODUCED IN ttk').grid(row=8, columnspan=2)
ttk.Separator(root,orient=HORIZONTAL).grid(row=9, columnspan=2,sticky="ew")

ttk.Combobox(root).grid(row=11, column=0)


n = ttk.Notebook(root)
n.grid(row=12, column=1)
f1 = ttk.Frame(n); # you can embed other widgets into these frames
f2 = ttk.Frame(n); 
n.add(f1, text='Tab One')
n.add(f2, text='Tab Two')

ttk.Progressbar(root, length = 140,value=65).grid(row=13, column=0)

ttk.Sizegrip(root).grid(row=14, column=1)# small triangular thing that can be gripped to resize the window

mytree = ttk.Treeview(root, height=2, columns=2)
mytree.grid(row=14, columnspan=2)
mytree.heading('#0', text='Column A', anchor=W)
mytree.heading(2, text='Column B', anchor=W)
mytree.column(2, stretch=0, width=70)


root.mainloop()
