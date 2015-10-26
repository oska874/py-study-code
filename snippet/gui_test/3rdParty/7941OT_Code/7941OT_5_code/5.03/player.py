"""
Code illustration: 5.03

Adding Functionality of Next, Forward, Previous, Rewind Mute & Volume

NEW METHODS ADDED HERE:
-------------------------
fast_fwd
rewind
mute
unmute


METHODS MODIFIED:
-----------------------



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
            self.myplayer.push_handlers(on_eos=self.what_next)
            self.source = pyglet.media.load(self.parent.currentTrack)
            self.myplayer.queue(self.source)
            self.myplayer.play()
            pyglet.app.run()
        except:
            pass
            
   
    def what_next(self):
        if self.stopped:
            self.stopped = False
            return None
        if self.parent.selectedloopchoice == 1:
            # No Loop
            return None
        if self.parent.selectedloopchoice == 2:
            # Loop current
            self.parent.launch_play()
        if self.parent.selectedloopchoice == 3:
            # Loop All
            self.fetch_next_track()
            
    def fetch_next_track(self):
        try:
            next_trackindx = self.parent.alltracks.index(self.parent.currentTrack) +1
            self.parent.currentTrack = self.parent.alltracks[next_trackindx]
            self.parent.launch_play()
        except:
            print 'end of list'

                
    def start_play_thread(self):
        player_thread = Thread(target=self.play_media)
        player_thread.start()
        
    
        
        


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