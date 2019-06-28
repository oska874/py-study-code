"""
Code illustration: 2.06
A demonstration of tkFileDialog

@tkinter GUI Application Development Hotshot
""" 


from tkinter import *
import tkinter.filedialog


root = Tk()

def askopenfile():
    tkinter.filedialog.askopenfile(mode='r')
    

def askopenfilename():
    tkinter.filedialog.askopenfilename()

def asksaveasFile():
    tkinter.filedialog.asksaveasfile()


def asksaveasfilename():
    tkinter.filedialog.asksaveasfilename()

def askDirectory():
    tkinter.filedialog.askdirectory()

fr1 = Frame(root)
fr2 = Frame(root)
opt = {'fill': BOTH, 'side':LEFT, 'padx': 2, 'pady': 3}
Label(text="Demo of tkFileDialog").pack()
Button(fr1, text='open_file', command=askopenfile).pack(opt)
Button(fr1, text='open_filename', command=askopenfilename).pack(opt)
Button(fr1, text='save_asfile', command=asksaveasFile).pack(opt)
Button(fr2, text='save_asfilename', command=asksaveasfilename).pack(opt)
Button(fr2, text='directory', command=askDirectory).pack(opt)


fr1.pack()
fr2.pack()


root.mainloop()

