"""
Code illustration: 8.12
tkinter Class Hierarchy Inspect
tkinter GUI Application Development Hotshot
""" 
import tkinter
import inspect

print('Class Hierarchy for Frame Widget')
for i, classname in enumerate(inspect.getmro(tkinter.Frame)):
    print('%s: %s'%(i, classname))
    
print('Class Hierarchy for Toplevel')
for i, classname in enumerate(inspect.getmro(tkinter.Toplevel)):
    print('%s: %s'%(i, classname))

print('Class Hierarchy for Tk')
for i, classname in enumerate(inspect.getmro(tkinter.Tk)):
    print('%s: %s'%(i, classname))