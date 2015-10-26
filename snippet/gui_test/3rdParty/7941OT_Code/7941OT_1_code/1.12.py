"""
Code illustration: 1.12
A demonstration of tkinter Variable Class
IntVar, StringVar & BooleanVar

@Tkinter GUI Application Development Hotshot
""" 



from Tkinter import *
root = Tk()

def show():
    print "You entered:"
    print "Employee Number: "+ str(en.get())
    print "Login Password: "+ pw.get()
    print "Remember Me: "+ str(rm.get())
    print '*'*30

#demo of IntVar
Label(root, text="Employee Number:").grid(row=1, column=1)
en = IntVar()
Entry(root, width=40, textvariable=en).grid(row=1, column=2, columnspan=2)
en.set("120350")


#demo of StringVar
Label(root, text="Login Password:").grid(row=2, column=1, sticky='w')
pw = StringVar() # defines the widget state as string
Entry(root,width=40, show="*",  textvariable=pw).grid(row=2, column=2, columnspan=2) 
pw.set("mysecretpassword")

Button(root,text="Login", command=show).grid(row=3, column=3)

#demo of Boolean var
rm = BooleanVar()
Checkbutton(root, text="Remember Me", variable=rm).grid(row=3, column=2)
rm.set(True)



root.mainloop()
