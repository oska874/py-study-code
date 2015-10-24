# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root,width=20 )
bottomframe.pack( side = BOTTOM)

redbutton = Button(frame, text="Red", fg="red",width=20 )
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown",width=20 )
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue",width=20 )
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black",width=20 )
blackbutton.pack( side = BOTTOM)

root.mainloop()