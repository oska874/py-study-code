#!/usr/bin/env python
"""
Code illustration: 3.01
Drum Program Editor Code
Creating OOP Based GUI structure


@Tkinter GUI Application Development Hotshot
""" 

from Tkinter import *

class DrumMachine():

    def app(self):
        self.root = Tk()
        self.root.title('Drum Beast')
        self.root.mainloop()


# ==============================================
if __name__ == '__main__':
    
    dm = DrumMachine()
    dm.app()
