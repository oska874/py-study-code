"""
Code illustration: 7.10

Bar Graph

Tkinter GUI Application Development Hotshot
""" 

import Tkinter
import random

root = Tkinter.Tk()


cwidth = 250
cheight = 220
barWidth = 20


canv = Tkinter.Canvas(root, width=cwidth, height=cheight, bg= 'white')
canv.pack()

plotdata= [random.randint(0,200) for r in xrange(12)]
for x, y in enumerate(plotdata):
    x1 = x  + x * barWidth 
    y1 = cheight - y 
    x2 = x  + x * barWidth + barWidth
    y2 = cheight
    canv.create_rectangle(x1, y1, x2, y2, fill="blue")
    canv.create_text(x1+3, y1, text=str(y),anchor='sw' )




root.mainloop()