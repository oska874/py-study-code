"""
Code illustration: 8.04

Demonstration of percent substitutions in data validation
Tkinter GUI Application Development Hotshot
""" 

import Tkinter as tk

class PSubDemo():
    def __init__(self):
        self.root = tk.Tk()
        tk.Label(text='Type Something Below').pack()
        vcmd = (self.root.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        tk.Entry(self.root, validate="all", validatecommand=vcmd).pack()
        self.root.mainloop()

    def validate(self, d, i, P, s, S, v, V, W):
        print "Following Data is received for running our validaition checks:"
        print "d:'%s'" % d
        print "i:'%s'" % i
        print "P:'%s'" % P
        print "s:'%s'" % s
        print "S:'%s'" % S
        print "v:'%s'" % v
        print "V:'%s'" % V
        print "W:'%s'" % W
        # returning true for now
        # in actual validation you return true if data is valid else return false
        return True

app = PSubDemo()