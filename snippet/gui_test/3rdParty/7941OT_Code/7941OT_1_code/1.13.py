"""
Code illustration: 1.13
A demonstration of:
1)some important top-level methods
2)tkinter styling

@Tkinter GUI Application Development Hotshot
""" 

from Tkinter import *
root = Tk()

#demo of some important top-level methods
root.geometry('142x280+150+200') #specify top-level window size and position
root.title("Style Demo") #specifying title of the program
root.wm_iconbitmap('brush1.ico')#changing the default icon
#root.overrideredirect(1) # remove the top-level border - uncomment this line to see the difference
root.configure(background='#4D4D4D')#top level styling

# connecting to the external styling optionDB.txt
root.option_readfile('optionDB.txt')


#widget specific styling
mytext = Text(root, background='#101010', foreground="#D6D6D6", borderwidth=18, relief='sunken',width=16, height=5 )
mytext.insert(END, "Style is knowing \nwho you are, what \nyou want to say, \nand not giving a \ndamn.")
mytext.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

# all the below widgets derive their styling from optionDB.txt file

Button(root, text='*' ).grid(row=1, column=1)
Button(root, text='^' ).grid(row=1, column=2)
Button(root, text='#' ).grid(row=1, column=3)
Button(root, text='<' ).grid(row=2, column=1)
Button(root, text='OK', cursor='target').grid(row=2, column=2)#changing cursor style
Button(root, text='>').grid(row=2, column=3)
Button(root, text='+' ).grid(row=3, column=1)
Button(root, text='v', font='Verdana 8').grid(row=3, column=2)
Button(root, text='-' ).grid(row=3, column=3)
for i in range(0,10,1):
  Button(root, text=str(i) ).grid( column=3 if i%3==0  else (1 if i%3==1 else 2), row= 4 if i<=3  else (5 if i<=6 else 6))

#styling with built-in bitmap images
mybitmaps = ['info','error', 'hourglass',  'questhead','question', 'warning']
for i in mybitmaps:
  Button(root, bitmap=i,  width=20, height=20).grid(row=(mybitmaps.index(i)+1), column=4, sticky='nw')


root.mainloop()
