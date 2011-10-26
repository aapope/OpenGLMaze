__author__ = '''Colter Fatt, Trisha Andrews, and Eddie Figueroa'''
__date__ = '''October 21, 2011'''
#Application Design
#Class Project
#Game Sounds

from pygame import mixer

class GameSounds():
    '''Methods for basic sound loading and playing'''
    
    def __init__(self):
    	'''Initializes mixer, number of channels to 8, and state to not paused'''
    	mixer.init()
        mixer.set_num_channels(8)
        self.paused = False

    def loadSound(self, filename):
    	'''Load a specified sound file as a Sound object'''
        self.sounddata = mixer.Sound(filename)

    def playSound(self):
    	'''Play the loaded sound file'''
        self.sounddata.play()
                            
    def loadMusic(self, filename):
    	'''Loads the background music'''
        mixer.music.load(filename)
    
    def pauseMusic(self):
    	'''Pauses background music'''
    	mixer.music.pause()
        self.paused = True
    	
    def unpauseMusic(self):
    	'''Unpauses background music'''
    	mixer.music.unpause()
        self.paused = False

    def playMusic(self):
    	'''Plays background song in an infinite loop'''
        mixer.music.play(-1)

    def toSound(self, filename):
    	'''Creates and returns a new Sound object from a file'''
        soundname = mixer.Sound(filename)
        return soundname

    def soundChannel(self, chan_num, soundname):
    	'''Creates a Channel object for controlling playback and queue a Sound object'''
        chan = mixer.Channel(chan_num)
        chan.queue(soundname)
