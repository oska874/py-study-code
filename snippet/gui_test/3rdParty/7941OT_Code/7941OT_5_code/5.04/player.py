"""
Code illustration: 5.04

NEW METHODS ADDED HERE:
-------------------------
song_len() - to calculate the total length of the song 
current_time() - to calculate the current duration of play 

METHODS MODIFIED:
-----------------------
start_play_thread - added a call to song_len to get the song length

@Tkinter GUI Application Development Hotshot
""" 


import pyglet
from threading import Thread
import time

FWDREWNDTIME = 20

class Player():
    parent = None
    metadata ={} #mp3 artist title year genre in dictionary form.
    song_length = 0 #in seconds
    paused = False
    stopped = False
    current_time = 0
    vol = 0.0
    
    def play_media(self) :
        try:
            self.myplayer= pyglet.media.Player()
            self.source = pyglet.media.load(self.parent.currentTrack)
            self.myplayer.queue(self.source)
            self.myplayer.play()
            pyglet.app.run()
        except:
            pass
            
    def current_time(self):
        try:             
            current_time = self.myplayer.time
        except:
            current_time = 0
        return current_time

    def song_len(self):
        try:             
            self.song_length = self.source.duration
        except:
            self.song_length = 0
        return self.song_length
        
                
    def start_play_thread(self):
        player_thread = Thread(target=self.play_media)
        player_thread.start()
        time.sleep(1)
        self.song_len()
        

        


    def fast_fwd(self): 
        try:             
            current_time = self.myplayer.time
            self.myplayer.seek(current_time+FWDREWNDTIME)
        except:pass
        
    def rewind(self): 
        try:             
            current_time = self.myplayer.time
            self.myplayer.seek(current_time-FWDREWNDTIME)
        except:pass

            

        
    def unpause(self):
        try:
            self.myplayer.play()
            self.paused = False
        except:pass
    
    def pause(self):
        try:
            self.myplayer.pause()
            self.paused = True
        except: pass
        
    def set_vol(self, vol):
        try:
            self.myplayer.volume = vol
        except:pass

    def mute(self):
        try:
            self.myplayer.volume = 0.0
            self.parent.volscale.set(0.0)
            #self.parent.root.update()
        except:pass
    
    def unmute(self):
        self.set_vol(self.vol)
        self.parent.volscale.set(0.3)
    

    
        
if __name__ == '__main__':
    print 'a pyglet player class implementation'