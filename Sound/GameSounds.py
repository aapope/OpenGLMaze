#!usr/bin/env python
#
#Colter Fatt, Trisha Andrews, and Eddie Figueroa
#Application Design
#Oct. 21, 2011
#
#Class Project
#Game Sounds

from pygame import mixer

class GameSounds():
    
    def __init__(self):
    	mixer.init()
        mixer.set_num_channels(8)

    def loadSound(self, filename):
        self.sounddata = mixer.Sound(filename)

    def playSound(self):
        self.sounddata.play()
                            
    def loadMusic(self, filename):
        mixer.music.load(filename)
    
    def pauseMusic(self):
    	mixer.music.pause()
    	
    def unpauseMusic(self):
    	mixer.music.unpause()

    def playMusic(self):
        mixer.music.play(-1)
