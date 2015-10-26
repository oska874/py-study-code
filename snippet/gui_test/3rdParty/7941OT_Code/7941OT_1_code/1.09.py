"""
Code illustration: 1.09
A demonstration of common pack() options

@Tkinter GUI Application Development Hotshot
""" 
from Tkinter import *
root = Tk()
# Absolute positioning
Button(root, text="Absolute Placement").place(x=20, y=10)
# Relative positioning
Button(root, text="Relative").place(relx=0.8, rely=0.2, relwidth=0.5, width=10, anchor = NE)
root.mainloop()
