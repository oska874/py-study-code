from Tkinter import *

fred = Button()
fred.pack()

def turnRed( event):
    event.widget["activeforeground"] = "red"
    print("1111")

fred.bind("<Enter>", turnRed)

fred.mainloop()

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()


# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(10000, 4000)
# start the program
myapp.mainloop()