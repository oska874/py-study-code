"""
Code illustration: 2.01
Text Editor Code
Step 1: Adding top-level
Step 2: Add menubuttons

@Tkinter GUI Application Development Hotshot
""" 
from Tkinter import *
#
#Step 1: Create a top-level window
#
root = Tk()


#
# Step 2  Adding Menu Bar 
#

menubar = Menu(root) # frame that holds the menu buttons


# Create File menu   
filemenu = Menu(menubar, tearoff=0 )
# all file menu choices will be placed here
menubar.add_cascade(label="File", menu=filemenu) 


# Create Edit menu
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)


# Create View menu 
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)

# Create About menu
aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)

# Displaying menu on top of root.
root.config(menu=menubar)




root.mainloop() # main loop of top-level
