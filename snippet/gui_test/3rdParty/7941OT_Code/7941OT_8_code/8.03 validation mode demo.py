"""
Code illustration: 8.03

Validation Modes Demo

Tkinter GUI Application Development Hotshot
""" 

import Tkinter as tk

class ValidateModeDemo():
    def __init__(self):
        self.root = tk.Tk()
        vcmd = (self.root.register(self.validate), '%V') 
        
        # validate = none mode - will not call validate method ever.
        tk.Label (text='None').pack()
        tk.Entry(self.root, validate="none", validatecommand=vcmd).pack()
        
        # validate = focus mode - will call validate method on focusin and focusout
        tk.Label (text='Focus').pack()
        tk.Entry(self.root, validate="focus", validatecommand=vcmd).pack()
        

        # validate = focusin mode - - will call validate method on focusin
        tk.Label (text='Focusin').pack()
        tk.Entry(self.root, validate="focusin", validatecommand=vcmd).pack()


        # validate = focusout mode - will call validate method on focusout
        tk.Label (text='Focus Out').pack()
        tk.Entry(self.root, validate="focusout", validatecommand=vcmd).pack()

        # validate = Key mode - will call validate method only when you type something or edit the entry
        tk.Label (text='key').pack()
        tk.Entry(self.root, validate="key", validatecommand=vcmd).pack()

        # validate = all mode - will call validate method on focus and key events
        tk.Label (text='all').pack()
        tk.Entry(self.root, validate="all", validatecommand=vcmd).pack()
        
       
        self.root.mainloop()

    def validate(self, v):
        print 'Called Just Now Via Mode %s' %v
        # this is where you will validate your data and return True or False
        #depending on wether the data is valid or not
        # for now let us just return True for all cases.
        return True
    
app = ValidateModeDemo()