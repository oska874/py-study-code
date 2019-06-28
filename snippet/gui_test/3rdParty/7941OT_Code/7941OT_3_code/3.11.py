#!/usr/bin/env python
"""
Code illustration: 3.11.py
tttk widgets styling and theming explained


@tkinter GUI Application Development Hotshot
""" 

from tkinter import *
import tkinter.ttk
root= Tk()
x = tkinter.ttk.Style()
x.configure('.', font='Arial 14', foreground='brown', background='yellow')
x.configure('danger.TButton', font='Times 12',foreground='red', padding=1)

tkinter.ttk.Label(root, text='global style').pack()
tkinter.ttk.Button(root, text='custom style', style='danger.TButton').pack()

# Different  styling for different widget states
x.map("s.TButton",foreground=[('pressed', 'red'), ('active', 'blue')])
tkinter.ttk.Button(text="state style", style="s.TButton").pack()

# Overriding current theme styles for the combo box
curr_theme = x.theme_use()
x.theme_settings(curr_theme, { "TEntry": { "configure":  {"padding": 2}, "map": {"foreground": [("focus", "red")]}  }})

print(x.theme_names())
print(x.theme_use())

tkinter.ttk.Entry().pack()
root.mainloop()
