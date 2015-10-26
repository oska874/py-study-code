"""
Code illustration: 8.05
validate='key' demo
Tkinter GUI Application Development Hotshot
""" 

import Tkinter as tk

class keyValidationDemo():
    def __init__(self):
        root = tk.Tk()
        tk.Label(root, text='Enter your name').pack()
        vcmd = (root.register(self.validate_data), '%S')
        invcmd = (root.register(self.invalid_name), '%S')
        tk.Entry(root, validate="key", validatecommand=vcmd, invalidcommand=invcmd).pack(pady=5, padx=5)
        self.errmsg = tk.Label(root, text= '', fg='red')
        self.errmsg.pack()
        root.mainloop()

    def validate_data(self, S):
        print "S='%s'" % S
        self.errmsg.config(text='')
        return (S.isalpha() or S ==' ')
        
    def invalid_name(self, S):
        self.errmsg.config(text='Invalid character %s \n name can only have alphabets'%S)
        

app= keyValidationDemo()