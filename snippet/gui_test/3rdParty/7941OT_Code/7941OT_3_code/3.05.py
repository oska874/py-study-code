#!/usr/bin/env python
"""
Code illustration: 3.05
Playing Sound Files with pymedia module

@Tkinter GUI Application Development Hotshot
""" 

from Tkinter import *
import tkFileDialog
import tkMessageBox
import os

#modules for playing sounds
import time
import wave
import pymedia.audio.sound as sound



#constants
MAX_DRUM_NUM = 5

class DrumMachine():
    
    
    def __init__(self):
        self.widget_drum_name = []
        self.widget_drum_file_name = [0]*MAX_DRUM_NUM
        self.current_drum_no = 0
        

    def play(self):
          for i in range(len(self.button[0])):
                for item in self.button:
                    try:
                        if item[i].cget('bg') == 'green':
                            if not self.widget_drum_file_name[self.button.index(item)]:continue
                            sound_filename = self.widget_drum_file_name[self.button.index(item)]
                            self.play_sound(sound_filename)
                    except:continue
                time.sleep(3/4.0)#corresponds to 80 beats per minute (80 BPM)(60/80)

    def play_sound(self, sound_filename):
        try:
            self.s = wave.open(sound_filename, 'rb')
            sample_rate = self.s.getframerate()
            channels = self.s.getnchannels()
            frmt = sound.AFMT_S16_LE
            self.snd= sound.Output(sample_rate, channels, frmt)
            s = self.s.readframes(300000)
            self.snd.play(s)
        except:
            pass






    def drum_load(self, drum_no):
        def callback(): 
            self.current_drum_no = drum_no
            try:
                file_name = tkFileDialog.askopenfilename(defaultextension=".wav",filetypes=[("Wave Files","*.wav"),("OGG Files","*.ogg")])
                if not file_name: return
                try:
                    del self.widget_drum_file_name[drum_no]
                except:pass
                self.widget_drum_file_name.insert(drum_no, file_name)
                drum_name = os.path.basename(file_name)
                self.widget_drum_name[drum_no].delete(0, END)
                self.widget_drum_name[drum_no].insert(0, drum_name)
            except:
                tkMessageBox.showerror('Invalid', "Error loading drum samples")
            
        return callback


    def button_clicked(self,i,j,bpu):
            def callback():                 
                btn = self.button[i][j]
                color = 'grey55' if (j/bpu)%2 else 'khaki'
                new_color = 'green' if btn.cget('bg') != 'green' else color
                btn.config(bg=new_color)
            return callback  

    def create_play_bar(self):
        playbar_frame = Frame(self.root, height=15)
        ln = MAX_DRUM_NUM+10
        playbar_frame.grid(row=ln, columnspan=13,sticky=W+E,padx=15, pady=10)
        button = Button( playbar_frame, text ='Play', command= self.play)
        button.grid(row= ln, column=1, padx=1)
        button = Button( playbar_frame, text ='Stop')
        button.grid(row= ln, column=3,padx=1)
        loop = BooleanVar()
        loopbutton = Checkbutton(playbar_frame, text='Loop', variable=loop)
        loopbutton.grid(row=ln, column=16,padx=1)
       
        
    def create_left_pad(self):
        '''creating actual pattern editor pad'''
        left_frame = Frame(self.root)
        left_frame.grid(row=10, column=0, columnspan=6,sticky=W+E+N+S)
        tbicon = PhotoImage(file='images/openfile.gif')
        for i in range(0, MAX_DRUM_NUM):
            button = Button(left_frame, image=tbicon, command= self.drum_load(i))
            button.image = tbicon
            button.grid(row=i, column=0,  padx=5,pady=2)
            self.drum_entry = Entry(left_frame)
            self.drum_entry.grid(row=i, column=4, padx=7,pady=2)
            self.widget_drum_name.append(self.drum_entry)
            

    def create_right_pad(self):
        bpu = self.bpu.get()
        units = self.units.get()
        c = bpu * units
        right_frame = Frame(self.root)
        right_frame.grid(row=10, column=6,sticky=W+E+N+S, padx=15, pady=2)
        self.button = [[0 for x in range(c)] for x in range(MAX_DRUM_NUM)]
        for i in range(MAX_DRUM_NUM):
            for j in range(c):
                color = 'grey55' if (j/bpu)%2 else 'khaki'
                self.button[i][j] = Button(right_frame,  bg=color, width=1, command=self.button_clicked(i,j,bpu))
                self.button[i][j].grid(row=i, column=j)

    def create_top_bar(self):
        '''creating top buttons'''
        topbar_frame = Frame(self.root)
        topbar_frame.config(height=25)
        topbar_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5)

        Label(topbar_frame, text='Units:').grid(row=0, column=4)
        self.units = IntVar()
        self.units.set(4)
        self.units_widget = Spinbox(topbar_frame, from_=1, to=8, width=5, textvariable=self.units,command= self.create_right_pad)
        self.units_widget.grid(row=0, column=5)
        
 
        Label(topbar_frame, text='BPUs:').grid(row=0, column=6)
        self.bpu = IntVar()
        self.bpu.set(4)
        self.bpu_widget = Spinbox(topbar_frame, from_=1, to=10, width=5, textvariable=self.bpu, command= self.create_right_pad)
        self.bpu_widget.grid(row=0, column=7)

        self.create_right_pad()
        
        
    def app(self):
        self.root = Tk()
        self.root.title('Drum Beast')
        self.create_top_bar()
        self.create_left_pad()
        
        self.create_play_bar()
        self.root.mainloop()
        
# ======================================================================
if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()
