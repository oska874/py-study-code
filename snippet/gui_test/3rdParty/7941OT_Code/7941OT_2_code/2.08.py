"""
Code illustration: 2.08
A demonstration of tkMessageBox

@Tkinter GUI Application Development Hotshot
""" 


from Tkinter import *
import tkMessageBox

root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)
opt = {'fill': BOTH, 'side':LEFT, 'padx': 2, 'pady': 3}


#Demo of tkMessageBox
Label(fr1, text="Demo of tkMessageBox").pack()
def warn():
    tkMessageBox.showwarning("Beware", "Don't be silly")

def info():
    tkMessageBox.showinfo("FYI", "This is FYI")

def error():
    tkMessageBox.showerror("Err..", "its leaking.")

def question():
    tkMessageBox.askquestion("?", "Can you read this ?")
def okcancel():
    tkMessageBox.askokcancel("OK", "Quit Postponing ?")
def yesno():
    tkMessageBox.askyesno("Yes or No", "Are you incapable of saying yes?")
def retrycancel():
    tkMessageBox.askretrycancel("Retry", "Load Failed")


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

