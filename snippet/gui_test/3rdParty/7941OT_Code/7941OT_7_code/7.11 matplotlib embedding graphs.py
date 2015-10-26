"""
Code illustration: 7.11

Embedding Matplotlib graph on tkinter

Tkinter GUI Application Development Hotshot
""" 

import Tkinter as Tk
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

root = Tk.Tk()

#creating the graph
f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
t = arange(-1.0,1.0,0.001)
s = t*sin(1/t)
a.plot(t,s)

# embedding matplotlib figure f on a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#creating toolbar
toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()

root.mainloop()