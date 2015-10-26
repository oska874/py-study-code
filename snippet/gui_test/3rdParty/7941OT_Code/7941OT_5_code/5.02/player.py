"""
Code illustration: 5.02

No changes here in this iteration

@Tkinter GUI Application Development Hotshot
""" 



import pyglet
from threading import Thread
import time


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
            
       
    def start_play_thread(self):
        self.pause()
        player_thread = Thread(target=self.play_media)
        player_thread.start()
        
        
    def pause(self):
        try:
            self.myplayer.pause()
        except: pass
        
   
    
        
if __name__ == '__main__':
    print 'pyglet player class implementation'