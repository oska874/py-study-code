"""
Code illustration: 1.02
Adding some widgets
Tkinter GUI Application Development Hotshot
""" 

from Tkinter import *
root = Tk() 
mylabel = Label(root,text="I am a label widget")    #(1)
mybutton = Button(root,text="I am a button")        #(2)
mylabel.pack()                                      #(3)
mybutton.pack()                                     #(4)
root.mainloop()
