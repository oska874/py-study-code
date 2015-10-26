"""
Code illustration: 5.01

Creating GUI to Load and play a song

Tkinter GUI Application Development Hotshot
""" 



from Tkinter  import *
import tkFileDialog

import player

class GUI:
    
    currentTrack = ''

    def __init__(self, player):
        self.player = player
        player.parent = self
        self.root = Tk() 
        self.create_button_frame()
        self.create_bottom_frame()
        self.root.mainloop()
    
    
    def create_button_frame(self):
        buttonframe = Frame(self.root)
        
        self.playicon = PhotoImage(file='../icons/play.gif')
        self.stopicon = PhotoImage(file='../icons/stop.gif')
        self.playbtn=Button(buttonframe, text ='play', image=self.playicon, borderwidth=0, padx=0, command=self.toggle_play_pause)
        self.playbtn.image = self.playicon
        self.playbtn.grid(row=3, column=3)
        
        buttonframe.grid(row=1, pady=4, padx=5)
        
    
    def create_bottom_frame(self):
        bottomframe = Frame(self.root)
        
        add_fileicon = PhotoImage(file='../icons/add_file.gif')
        add_filebtn=Button(bottomframe,image=add_fileicon,borderwidth=0,padx=0, text='Add File', command=self.add_file)
        add_filebtn.image = add_fileicon
        add_filebtn.grid(row=2, column=1)
        bottomframe.grid(row=2, sticky='w',padx=5)
        
     
  
    def toggle_play_pause(self):
        if self.playbtn['text'] =='play':
            self.playbtn.config(text='stop', image=self.stopicon)
            self.player.start_play_thread()
        elif self.playbtn['text'] =='stop':
            self.playbtn.config(text ='play', image=self.playicon)
            self.player.pause()
  
    
    def add_file(self):
        tfile = tkFileDialog.askopenfilename(filetypes=[('All supported', '.mp3 .wav .ogg'), ('All files', '*.*')])
        self.currentTrack = tfile

 

         
if __name__ == '__main__':
    playerobj = player.Player()
    app = GUI(playerobj)