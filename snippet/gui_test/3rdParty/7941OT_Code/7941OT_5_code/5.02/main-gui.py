"""
Code illustration: 5.02

Adding Playlist with Listbox widget

NEW ATTRIBUTES ADDED HERE
----------------------------
alltracks = [] - to track all items in the playlist


NEW METHODS ADDED HERE:
-------------------------
list_frame()
add_dir()
del_selected()
clear_list()
identify_track_to_play()

METHODS MODIFIED:
-----------------------
__init__: added newly defined list_frame method to be intiailized within the mainloop
create_bottom_frame() - added 3 new buttons: delete file, add directory & delete all     


@Tkinter GUI Application Development Hotshot
""" 




from Tkinter  import *
import tkFileDialog
import os
import time

import player

class GUI:
    alltracks = []
    currentTrack = ''
    
    def __init__(self, player):
        self.player = player
        player.parent = self
        self.root = Tk() 
        self.create_button_frame()
        self.create_list_frame()
        self.create_bottom_frame()
        self.root.mainloop()
    
    
    def create_button_frame(self):
        buttonframe = Frame(self.root)
        self.playicon = PhotoImage(file='../icons/play.gif')
        self.stopicon = PhotoImage(file='../icons/stop.gif')
        self.playbtn=Button(buttonframe, text ='play', image=self.playicon, borderwidth=0, padx=0, command=self.toggle_play_pause)
        self.playbtn.image = self.playicon
        self.playbtn.grid(row=3, column=3)
        
        buttonframe.grid(row=3, columnspan=5, sticky='w', pady=4, padx=5)
  
    
    
    def create_list_frame(self):
        list_frame = Frame(self.root)
        self.listbox = Listbox(list_frame, activestyle='none', cursor='hand2', bg='#1C3D7D', fg='#A0B9E9', selectmode=EXTENDED, width=60, heigh=10)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.listbox.bind("<Double-Button-1>", self.identify_track_to_play)
        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        list_frame.grid(row=4, padx=5)
        
    def create_bottom_frame(self):
        bottomframe = Frame(self.root)
        
        add_fileicon = PhotoImage(file='../icons/add_file.gif')
        add_filebtn=Button(bottomframe,image=add_fileicon,borderwidth=0,padx=0, text='Add File', command=self.add_file)
        add_filebtn.image = add_fileicon
        add_filebtn.grid(row=5, column=1)

       
        del_selectedicon = PhotoImage(file='../icons/del_selected.gif')
        del_selectedbtn=Button(bottomframe,image=del_selectedicon,borderwidth=0,padx=0, text='Delete', command=self.del_selected)
        del_selectedbtn.image = del_selectedicon
        del_selectedbtn.grid(row=5, column=2 )

        
        add_diricon = PhotoImage(file='../icons/add_dir.gif')
        add_dirbtn=Button(bottomframe,image=add_diricon,borderwidth=0,padx=0, text='Add Dir', command=self.add_dir)
        add_dirbtn.image = add_diricon
        add_dirbtn.grid(row=5, column=3 )

        
        
        delallicon = PhotoImage(file='../icons/delall.gif')
        delallbtn=Button(bottomframe, image=delallicon,borderwidth=0,padx=0, text='Clear All', command=self.clear_list)
        delallbtn.image = delallicon
        delallbtn.grid(row=5, column=4 )

        
        bottomframe.grid(row=5, sticky='w',padx=5)
  
  
    def add_file(self):
        filename = tkFileDialog.askopenfilename(filetypes=[('All supported', '.mp3 .wav'), ('.mp3 files', '.mp3'), ('.wav files','.wav')])
        if filename:
            self.listbox.insert(END, filename)
            self.alltracks = list(self.listbox.get(0, END))
        
        
    def add_dir(self): 
        path = tkFileDialog.askdirectory()
        if path:
            tfileList = []
            for (dirpath, dirnames, filenames) in os.walk(path):
                for tfile in filenames:
                    if tfile.endswith(".mp3") or tfile.endswith(".wav") or tfile.endswith(".ogg"):
                        tfileList.append(dirpath+"/"+tfile)
            for item in tfileList:
                self.listbox.insert(END, item) 
            self.alltracks = list(self.listbox.get(0, END))
        
        
        
    def del_selected(self):
        while len(self.listbox.curselection())>0:
            self.listbox.delete(self.listbox.curselection()[0])
        self.alltracks = list(self.listbox.get(0, END))
        
        
  
    def clear_list(self):
        self.listbox.delete(0, END)
        self.alltracks =list(self.listbox.get(0, END))
  
    def toggle_play_pause(self):
        if self.playbtn['text'] =='play':
            self.playbtn.config(text='stop', image=self.stopicon)
            self.identify_track_to_play()
        elif self.playbtn['text'] =='stop':
            self.playbtn.config(text ='play', image=self.playicon)
            self.player.pause()
            

            
    def identify_track_to_play(self, event=None):
        try:
            indx = int(self.listbox.curselection()[0])
            if self.listbox.get(indx) == "":
                self.del_selected()
        except:
            indx = 0
        self.currentTrack  = self.listbox.get(indx)
        self.player.start_play_thread()
        
                
        
        
if __name__ == '__main__':
    playerobject = player.Player()
    app = GUI(playerobject)