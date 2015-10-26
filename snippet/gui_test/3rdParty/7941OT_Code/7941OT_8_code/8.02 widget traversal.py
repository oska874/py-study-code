"""
Code illustration: 8.02

Widget Traversal
Tkinter GUI Application Development Hotshot
""" 
from Tkinter import *

class TraversalDemo:
    def __init__(self, root):
        
        topframe = Frame(root, takefocus=1, highlightthickness=2, highlightcolor='red')
        en = Entry(topframe, width=25)
        en.grid(row=0, column=4,sticky=W)
        en.insert(END, 'Tabs jumps to next widget')
        topframe.pack(fill=X, expand=1)
        topframe.focus_force() 
        
        buttonframe = Frame(root, highlightthickness=2,  highlightcolor='red')
        for button, clm in (('A',1), ('B',2), ('C',3), ('D',4)):
            Button(buttonframe, text=button, highlightthickness=2).grid(padx=10, pady=6, row=0, column=clm, sticky=NSEW)
        buttonframe.pack(fill=X, expand=1)
        
        radioframe = Frame(root, takefocus=1, highlightthickness=2,  highlightcolor='red')
        v= IntVar()
        for i in range(4):
            Radiobutton(radioframe, text=i, variable=v, value=i).grid(padx=10, pady=6, row=1, column=i, sticky=NSEW)
        radioframe.pack(fill=X, expand=1)
        
        textframe = Frame(root, takefocus=1, highlightthickness=2,  highlightcolor='red')
        text = Text(textframe, width=25, height=4)
        text.insert(END, 'Tabs does not jump to the next widget.Use Cntrl + Tab to traverse')
        text.grid(row=0, column=1, columnspan=3)
        textframe.pack(fill=X, expand=1)        
        
        scaleframe = Frame(root, takefocus=0)
        Scale(scaleframe, from_=0.0, to=100.0, label='use left/right key', orient=HORIZONTAL, takefocus=1, highlightthickness=2,  highlightcolor='red').pack()
        scaleframe.pack(fill=X, expand=1) 
        
   
        

root = Tk()
app = TraversalDemo(root)
root.mainloop()
