from tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

left1 = Label(m1,text="l1")
m1.add(left1)

m2 = PanedWindow(m1, orient=HORIZONTAL)#VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

mid0 = Label(m2,text="middle pane")
m2.add(mid0)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

mainloop()