"""
Code illustration: 8.08
tkfont Demo
Tkinter GUI Application Development Hotshot
""" 

from Tkinter import Tk, Label, Pack
import tkFont
root=Tk()
label = Label(root, text="Humpty Dumpty was pushed")
label.pack()
currentfont = tkFont.Font(font=label['font'])
print 'Actual :' + str(currentfont.actual())
print 'Family : ' + currentfont.cget("family")
print 'Weight : ' + currentfont.cget("weight")
print 'Text width of Dumpty : %d' %currentfont.measure("Dumpty")
print 'Metrics:' + str(currentfont.metrics())
currentfont.config(size=14)
label.config (font=currentfont)
print 'New Actual :' + str(currentfont.actual())
root.mainloop()