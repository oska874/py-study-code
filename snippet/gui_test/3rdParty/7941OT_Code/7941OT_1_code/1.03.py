"""
Code illustration: 01.03
A demonstration of all core tkinter widgets

@Tkinter GUI Application Development Hotshot
""" 

from Tkinter import *


root = Tk()
root.title('I am a Top Level Widget, parent to other widgets')
#create a frame widget for placing menu
mymenubar = Frame(root, relief = 'raised', bd=2)
mymenubar.pack(fill = X)

# Create  Menu Widget 1 and Sub Menu 1
mymenubutton = Menubutton(mymenubar, text = 'Menu Button Widget 1', )
mymenubutton.pack(side = LEFT)
#menu widget
mymenu = Menu(mymenubutton, tearoff=0)
mymenubutton['menu'] = mymenu
mymenu.add('command', label = 'Menu Widget 1') #Add Sub Menu 1


# Create  Menu2 and Submenu2
mb2 = Menubutton(mymenubar, text = 'Menu 2', )
mb2.pack(side = LEFT)
menudd = Menu(mb2, tearoff=0)
mb2['menu'] = menudd
menudd.add('command', label = 'Sub Menu 2') # Add Sub Menu 2

#
#
# myframe1  and its contents
#


# creating a frame (myframe1) 
myframe1 = Frame(root, bd=2, relief=SUNKEN)
myframe1.pack(side=LEFT)

# add label to to myframe1
Label(myframe1, text='I am a Label widget').pack()

#add entry widget to myframe1
tv = StringVar() #discussed later
Entry(myframe1, textvariable=tv).pack()
tv.set('I am an entry widget')

#add button widget to myframe1
Button(myframe1, text='Button widget').pack()

#add check button widget to myframe1
Checkbutton(myframe1, text='CheckButton Widget').pack()

#add radio buttons to myframe1
Radiobutton(myframe1, text='Radio Button  Un', value=1).pack()
Radiobutton(myframe1, text='Radio Button  Dos',value=2).pack()
Radiobutton(myframe1, text='Radio Button  Tres', value=3).pack()


#OptionMenu Widget
Label(myframe1, text='Example of OptionMenu Widget:').pack()
OptionMenu(myframe1,'' , "Option A", "Option B", "Option C").pack()


#adding bitmap image
Label(myframe1, text='Image Fun with Bitmap Class:').pack()
bitmap = BitmapImage(file="gir.xbm")
mylabel = Label(myframe1,image=bitmap)
mylabel.image = bitmap # keep a reference!
mylabel.pack()


#
#
# frame2 and widgets it contains.
#
#



#create another frame(myframe2) to hold a list box, Spinbox Widget,Scale Widget, :
myframe2 = Frame(root, bd=2, relief=GROOVE)
myframe2.pack(side=RIGHT)

#add Photimage Class Widget to myframe2
Label(myframe2, text='Image displayed with \nPhotoImage class widget:').pack()
photo = PhotoImage(file='dance.gif')
label = Label(myframe2, image=photo)
label.image = photo # keep a reference!
label.pack()

#add listbox widget to myframe2
Label(myframe2, text='Below is an example of listbox widget:').pack()
listbox = Listbox(myframe2, height=4)
for line in ['Listbox Choice 1','Choice 2','Choice 3','Choice 4']:
    listbox.insert(END, line)
listbox.pack()


#spinbox widget
Label(myframe2, text='Below is an example of spinbox widget:').pack()
Spinbox(myframe2, values=(1, 2, 4, 8,10)).pack()

#scale widget
Scale(myframe2, from_=0.0, to=100.0, label='Scale widget', orient=HORIZONTAL).pack()


#LabelFrame
lf = LabelFrame(myframe2, text="Labelframe Widget", padx=10, pady=10)
lf.pack(padx=10, pady=10)
Entry(lf).pack()

#message widget
Message(myframe2, text='I am a Message widget').pack()


#
#
# Frame 3
#
#

myframe3 = Frame(root, bd=2, relief=SUNKEN)


#text widget and associated Scrollbar widget
mytext=Text(myframe3, height=10, width =40)
fhandle = open('textcontent.txt')
lines = fhandle.read()
fhandle.close()
mytext.insert(END, lines)
mytext.pack(side=LEFT, fill=X, padx=5)

#add scrollbar widget to the text widget
sb = Scrollbar(myframe3, orient=VERTICAL, command=mytext.yview)
sb.pack()
mytext.configure(yscrollcommand=sb.set)
myframe3.pack()


#
#
# Frame 4
#
#
#create another frame(myframe4)
myframe4 = Frame(root).pack()

c = Canvas(myframe4, bg='white', width=340, height=80)
c.pack()
c.create_oval(20,15,60,60, fill='red')
c.create_oval(40,15,60,60, fill='grey')
c.create_text(130, 38, text='I am a Canvas Widget', font=('arial', 8, 'bold'))


#
#
# A paned window widget
#
#

Label(root, text='Below is an example of Paned window widget:').pack()
Label(root, text='Notice you can adjust the size of each pane by dragging it').pack()
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=2)
left = Text(m1, height=6, width =15)
m1.add(left)
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
top = Text(m2, height=3, width =3)
m2.add(top)
bottom = Text(m2, height=3, width =3)
m2.add(bottom)

    



root.mainloop()
