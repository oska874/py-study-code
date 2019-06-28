"""Example showing use of a callback shim"""
import tkinter

def doButton(buttonName):
	"""My desired callback. I'll need a callback shim
	because Button command callbacks receive no arguments.
	"""
	print buttonName, "pressed"

class SimpleCallback:
	"""Create a callback shim. Based on code by Scott David Daniels
	(which also handles keyword arguments).
	"""
	def __init__(self, callback, *firstArgs):
		self.__callback = callback
		self.__firstArgs = firstArgs

	def __call__(self, *args):
		return self.__callback (*(self.__firstArgs + args))

root = tkinter.Tk()

buttonNames = ("Button 1", "Button 2", "Button 3")
for name in buttonNames:
	callback = SimpleCallback(doButton, name)
	
tkinter.Button(root, text=name, command=callback).pack()

root.mainloop()