# -*- coding: UTF-8 -*-
#canvas

import Tkinter as tk

root=tk.Tk()				#top windows
canvas1 = tk.Canvas()		#canvas instance

img = tk.PhotoImage(file="C:/Users/zl/Desktop/a4.gif")
i2 = canvas1.create_image(0,100,image=img)

canvas1.pack()				#put canvas into windows, layout as "pack"
root.mainloop()				#start application