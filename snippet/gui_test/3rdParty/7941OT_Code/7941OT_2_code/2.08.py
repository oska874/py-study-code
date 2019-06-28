"""
Code illustration: 2.08
A demonstration of tkMessageBox

@tkinter GUI Application Development Hotshot
""" 


from tkinter import *
import tkinter.messagebox

root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)
opt = {'fill': BOTH, 'side':LEFT, 'padx': 2, 'pady': 3}


#Demo of tkMessageBox
Label(fr1, text="Demo of tkMessageBox").pack()
def warn():
    tkinter.messagebox.showwarning("Beware", "Don't be silly")

def info():
    tkinter.messagebox.showinfo("FYI", "This is FYI")

def error():
    tkinter.messagebox.showerror("Err..", "its leaking.")

def question():
    tkinter.messagebox.askquestion("?", "Can you read this ?")
def okcancel():
    tkinter.messagebox.askokcancel("OK", "Quit Postponing ?")
def yesno():
    tkinter.messagebox.askyesno("Yes or No", "Are you incapable of saying yes?")
def retrycancel():
    tkinter.messagebox.askretrycancel("Retry", "Load Failed")


Button(fr1, text='warning', command=warn).pack(opt)
Button(fr1, text='info', command=info).pack(opt)
Button(fr1, text='error', command=error).pack(opt)
Button(fr1, text='question', command=question).pack(opt)
Button(fr2, text='okcancel', command=okcancel).pack(opt)
Button(fr2, text='yesno', command=yesno).pack(opt)
Button(fr2, text='retrycancel', command=retrycancel).pack(opt)


fr1.pack()
fr2.pack()

root.mainloop()

