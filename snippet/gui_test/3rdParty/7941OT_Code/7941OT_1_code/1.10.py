"""
Code illustration: 1.10
A demonstration of event binding with the bind() method

@tkinter GUI Application Development Hotshot
""" 
from tkinter import *

root = Tk()
Label(root, text='Click at different \n locations in the frame below').pack()
def callback(event): ##(2)
    print((dir(event)))##(3) Inspecting the instance event
    print(("you clicked at", event.x, event.y)) ##(4)
    

myframe = Frame(root, bg='khaki', width=130, height=80)
myframe.bind("<Button-1>", callback)##(1)
myframe.pack()

root.mainloop()
