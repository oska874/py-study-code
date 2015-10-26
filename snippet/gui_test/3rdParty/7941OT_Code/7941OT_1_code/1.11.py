"""
Code illustration: 1.11
A demonstration of all Widget Binding

@Tkinter GUI Application Development Hotshot
""" 
from Tkinter import *

def show_event_details(event):     
	event_name = {"2": "KeyPress", "4": "ButtonPress", "6": "Motion", "9":"FocusIn"}
	print '='*50
	print "EventName=" + event_name[str(event.type)]
	print "EventKeySymbol=" + str(event.keysym)
	print "EventType=" + str(event.type)
	print "EventWidgetId=" + str(event.widget)
	print "EventCoordinate (x,y)=(" + str(event.x)+","+str(event.y)+")"
	print "Time:", str(event.time)

root = Tk()

myb = Button(root, text="Button Bound to: \n Keyboard Enter & Mouse Click") #create button
myb.pack(pady=5,padx=4)
myb.focus_force()         	
myb.bind("<Button-1>", show_event_details)  #bind button to mouse click
myb.bind("<Return>", show_event_details)#bind button to Enter Key 


Label(text="Entry is Bound to Mouseclick \n, FocusIn and Keypress Event").pack()
mye = Entry(root) #creating entry widget
mye.pack()


#binding entry widget to mouse click and focus in
mye.bind("<Button-1>", show_event_details) # left mouse click
mye.bind("<Button-2>", show_event_details) # right mouse click
mye.bind("<FocusIn>", show_event_details)

#binding entry widget alphabets and numbers from keyboard 
alphanum = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
for i in alphanum:
    mye.bind("<KeyPress-%s>"%i, show_event_details)

#binding entry widget to keysym
keysyms = ['Alt_L', 'Alt_R','BackSpace', 'Cancel', 'Caps_Lock','Control_L',
           'Control_R','Delete', 'Down', 'End', 'Escape', 'Execute','F1',
           'F2', 'Home', 'Insert', 'Left','Linefeed','KP_0','KP_1','KP_2',
           'KP_3','KP_4','KP_5','KP_6','KP_7','KP_8','KP_9','KP_Add',
           'KP_Decimal','KP_Divide']
for i in keysyms:
    mye.bind("<KeyPress-%s>"%i, show_event_details)


#binding Canvas widget to Motion Event
Label(text="Canvas Bound to Motion Event\n(Hover over the area \nto see motion event )").pack()		
myc = Canvas(root, background='white',width=100, height=30)
myc.pack()
myc.bind('<Motion>', show_event_details)
  

Label(text="Entry Widget Bound to \n<Any KeyPress>").pack()
mye = Entry(root) #creating entry widget
mye.pack(pady=7)
#binding entry widget to mouse click and focus in
mye.bind("<Any KeyPress>", show_event_details) # right mouse click


root.mainloop()
