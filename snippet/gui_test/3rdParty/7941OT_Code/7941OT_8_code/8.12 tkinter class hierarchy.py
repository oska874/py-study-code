"""
Code illustration: 8.12
Tkinter Class Hierarchy Inspect
Tkinter GUI Application Development Hotshot
""" 
import Tkinter
import inspect

print 'Class Hierarchy for Frame Widget'
for i, classname in enumerate(inspect.getmro(Tkinter.Frame)):
    print '%s: %s'%(i, classname)
    
print 'Class Hierarchy for Toplevel'
for i, classname in enumerate(inspect.getmro(Tkinter.Toplevel)):
    print '%s: %s'%(i, classname)

print 'Class Hierarchy for Tk'
for i, classname in enumerate(inspect.getmro(Tkinter.Tk)):
    print '%s: %s'%(i, classname)