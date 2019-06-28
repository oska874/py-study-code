"""
Code illustration: 1.02
Adding some widgets
tkinter GUI Application Development Hotshot
""" 

from tkinter import *
root = Tk() 
mylabel = Label(root,text="I am a label widget")    #(1)
mybutton = Button(root,text="I am a button")        #(2)
mylabel.pack()                                      #(3)
mybutton.pack()                                     #(4)
root.mainloop()
