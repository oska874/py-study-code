"""
Code illustration: 8.08
tkfont Demo
tkinter GUI Application Development Hotshot
""" 

from tkinter import Tk, Label, Pack
import tkinter.font
root=Tk()
label = Label(root, text="Humpty Dumpty was pushed")
label.pack()
currentfont = tkinter.font.Font(font=label['font'])
print('Actual :' + str(currentfont.actual()))
print('Family : ' + currentfont.cget("family"))
print('Weight : ' + currentfont.cget("weight"))
print('Text width of Dumpty : %d' %currentfont.measure("Dumpty"))
print('Metrics:' + str(currentfont.metrics()))
currentfont.config(size=14)
label.config (font=currentfont)
print('New Actual :' + str(currentfont.actual()))
root.mainloop()