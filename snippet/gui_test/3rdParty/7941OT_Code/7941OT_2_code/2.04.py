"""
Code illustration: 2.04

Indexing and tagging demonstrated
Implementation of:
1. select_all
2. on_find


@Tkinter GUI Application Development Hotshot
""" 
from Tkinter import *
import tkFileDialog
root = Tk()
root.geometry('350x350')

#########################################################################
#demo of indexing and tagging features of text widget

def select_all():
        textPad.tag_add('sel', '1.0', 'end')
        

def on_find():
        t2 = Toplevel(root)
        t2.title('Find')
        t2.geometry('262x65+200+250')
        t2.transient(root)
        Label(t2, text="Find All:").grid(row=0, column=0, sticky='e')
        v=StringVar()
        e = Entry(t2, width=25, textvariable=v)
        e.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        e.focus_set()
        c=IntVar()
        Checkbutton(t2, text='Ignore Case', variable=c).grid(row=1, column=1, sticky='e', padx=2, pady=2)
        Button(t2, text="Find All", underline=0,  command=lambda: search_for(v.get(),c.get(), textPad, t2,e)).grid(row=0, column=2, sticky='e'+'w', padx=2, pady=2)
        def close_search():
                textPad.tag_remove('match', '1.0', END)
                t2.destroy()
        t2.protocol('WM_DELETE_WINDOW', close_search)#override close button

def search_for(needle,cssnstv, textPad, t2,e) :
        textPad.tag_remove('match', '1.0', END)
        count =0
        if needle:
                pos = '1.0'
                while True:
                    pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END)
                    if not pos: break
                    lastpos = '%s+%dc' % (pos, len(needle))
                    textPad.tag_add('match', pos, lastpos)
                    count += 1
                    pos = lastpos
                textPad.tag_config('match', foreground='red', background='yellow')
        e.focus_set()
        t2.title('%d matches found' %count)
        



########################################################################
#Levaraging built in text widget functionalities

def undo():
    textPad.event_generate("<<Undo>>")
    
def redo():
    textPad.event_generate("<<Redo>>")
    
    
def cut():
    textPad.event_generate("<<Cut>>")
    
def copy():
    textPad.event_generate("<<Copy>>")
    
def paste():
    textPad.event_generate("<<Paste>>")
    


######################################################################

#defining icons for compund menu demonstration
newicon = PhotoImage(file='icons/new_file.gif')
openicon = PhotoImage(file='icons/open_file.gif')
saveicon = PhotoImage(file='icons/Save.gif')
cuticon = PhotoImage(file='icons/Cut.gif')
copyicon = PhotoImage(file='icons/Copy.gif')
pasteicon = PhotoImage(file='icons/Paste.gif')
undoicon = PhotoImage(file='icons/Undo.gif')
redoicon = PhotoImage(file='icons/Redo.gif')
menubar = Menu(root)

# File menu,for open,save,save as and quit       
filemenu = Menu(menubar, tearoff=0 ) 
filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT, image=newicon, underline=0  )
filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT, image=openicon, underline =0)
filemenu.add_command(label="Save", accelerator='Ctrl+S',compound=LEFT, image=saveicon,underline=0)
filemenu.add_command(label="Save as",accelerator='Shift+Ctrl+S')
filemenu.add_separator()        
filemenu.add_command(label="Exit", accelerator='Alt+F4') 
menubar.add_cascade(label="File", menu=filemenu)  


#Edit menu - Undo, Redo, Cut, Copy and Paste 
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo",compound=LEFT,  image=undoicon, accelerator='Ctrl+Z', command=undo)
editmenu.add_command(label="Redo",compound=LEFT,  image=redoicon, accelerator='Ctrl+Y', command=redo)
editmenu.add_separator() 
editmenu.add_command(label="Cut", compound=LEFT, image=cuticon, accelerator='Ctrl+X', command=cut)
editmenu.add_command(label="Copy", compound=LEFT, image=copyicon,  accelerator='Ctrl+C', command=copy)
editmenu.add_command(label="Paste",compound=LEFT, image=pasteicon, accelerator='Ctrl+V', command = paste)
editmenu.add_separator()
editmenu.add_command(label="Find",underline= 0, accelerator='Ctrl+F', command=on_find)
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=7, accelerator='Ctrl+A', command=select_all)
menubar.add_cascade(label="Edit", menu=editmenu)


#View menu - 
viewmenu = Menu(menubar, tearoff=0)
showln = IntVar()
showln.set(1)
viewmenu.add_checkbutton(label="Show Line Number", variable=showln)
showinbar = IntVar()
showinbar.set(1)
viewmenu.add_checkbutton(label="Show Info Bar at Bottom", variable=showinbar)
hltln = IntVar()
viewmenu.add_checkbutton(label="Highlight Current Line", onvalue=1, offvalue=0, variable=hltln)
themesmenu = Menu(menubar, tearoff=0)
viewmenu.add_cascade(label="Themes", menu=themesmenu)


#we define a color scheme dictionary containg name and color code as key value pair
clrschms = {
'1. Default White': 'FFFFFF',
'2. Greygarious Grey':'D1D4D1',
'3. Lovely Lavender':'E1E1FF' , 
'4. Aquamarine': 'D1E7E0',
'5. Bold Beige': 'FFF0E1',
'6. Cobalt Blue':'333AA',
'7. Olive Green': '5B8340',
}
themechoice= StringVar()
themechoice.set('1. Default White')
for k in sorted(clrschms):
    themesmenu.add_radiobutton(label=k, variable=themechoice)
menubar.add_cascade(label="View", menu=viewmenu)

# About menu - Aboutus, Help
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About")
aboutmenu.add_command(label="Help")
menubar.add_cascade(label="About",  menu=aboutmenu)

# Returning defined setting for widget
root.config(menu=menubar)


#
# Adding top label to hold and left labels
# we have colored it for now to differentiate it from the main window
#

shortcutbar = Frame(root,  height=25, bg='light sea green')
shortcutbar.pack(expand=NO, fill=X)
lnlabel = Label(root,  width=2,  bg = 'antique white')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)


#
# Adding Text Widget & ScrollBar widget
#

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll=Scrollbar(textPad)
textPad.configure(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT,fill=Y)



root.mainloop()
