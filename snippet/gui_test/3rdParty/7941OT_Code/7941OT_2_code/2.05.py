"""
Code illustration: 2.05
A demonstration of different types of top-level window

@Tkinter GUI Application Development Hotshot
""" 


from Tkinter import *
root = Tk()

#top level window
root.title('Toplevel Window')
root.geometry('300x300')
Label(root, text='I am the Main Toplevel window\n All other windows here are my children').pack()


#child of top-level
c = Toplevel(root)
Label(c, text='I am a child of root\n If i loose focus, I may hide below the top level, \n I am destroyed, if root is destroyed').pack()
c.geometry('400x100+300+300')


#transient window
t = Toplevel(root)
Label(t, text='I am a transient window of root\n I always stay on top of my parent\n I get hidden if my parent window is minimized').pack()
t.transient(root)


#no window decoration
nw = Toplevel(root, bg='black')
Label(nw, text='I am a top-level with no window manager\n I cannot be resized or moved', bg='black', fg='white').pack()
nw.overrideredirect(1)
nw.geometry('250x100+700+500')


root.mainloop()
