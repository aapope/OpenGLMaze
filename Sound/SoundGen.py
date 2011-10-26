#!usr/bin/env python
#
#Colter Fatt
#Application Design
#
#OpenGLMaze
#Random music generator

import ImageTk, Image, random
from Extended_Wave import Wave

#Global Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
ZOMBIE_GRAY = (100,100,100)
YELLOW = (255,255,0)
BLUE = (0,0,255)


class GenerateMusic():

    def __init__(self, filename, f_out_name):
        f = Image.open(filename)
        mus = self.make_music(f)

    def make_music(self, f):
        '''Gets the color of the pixels, which determines which chord progression is added to the score'''
        #Gets the length and width of the map
        self.width = f.size[0]
        self.length = f.size[1]
        
        self.line = 0
        self.lineprev = 0
        self.notes = []
        
        #Compares the current line in the picture to the previous line and based the music off the difference
        for y in range(self.length):
            self.lineprev = self.line
            self.line = 0
            for x in range(self.width):
                color = f.getpixel((x,y))
                self.line += self.handle_pixel(color)
            self.write_progression(self.lineprev - self.line)
        self.write_part(self.notes)

    def handle_pixel(self, color):
        '''Returns a value to determine the overall value of the line'''
        
        if color == WHITE:
            return 1
        
        elif color == BLACK:
            return -1

        else:
            return 0
                
    def write_progression(self, inNum):
        '''When called adds a chord progression to the music, based on a number'''
        
        #If the input number is not within the range of -5 to 5, a random number in that frange is chosen.
        if not (inNum > -6) & (inNum < 6):
            inNum = random.randrange(-5, 5, 1)
        
        #Adds the notes if the input number is the specified number
        if inNum == 0:
            self.notes.append((.5, 'C4'))
            self.notes.append((.5, 'E4'))
            self.notes.append((.5, 'G4'))
            self.notes.append((.5, 'C5'))
                
        elif inNum == 1:
            self.notes.append((.5, 'C4'))
            self.notes.append((.5, 'Eb4'))
            self.notes.append((.5, 'G4'))
            self.notes.append((.5, 'C5'))
        
        elif inNum == 2:
            self.notes.append((.5, 'C4'))
            self.notes.append((.5, 'F4'))
            self.notes.append((.5, 'A4'))
            self.notes.append((.5, 'C5'))
                
        elif inNum == 3:
            self.notes.append((.5, 'C4'))
            self.notes.append((.5, 'E4'))
            self.notes.append((.5, 'E5'))
            self.notes.append((.5, 'C5'))
                
        elif inNum == 4:
            self.notes.append((.5, 'C5'))
            self.notes.append((.5, 'F4'))
            self.notes.append((.5, 'E4'))
            self.notes.append((.5, 'C5'))
                
        elif inNum == 5:
            self.notes.append((.5, 'C5'))
            self.notes.append((.5, 'G4'))
            self.notes.append((.5, 'B4'))
            self.notes.append((.5, 'A4'))
                
        elif inNum == -1:
            self.notes.append((.5, 'C5'))
            self.notes.append((.5, 'G4'))
            self.notes.append((.5, 'E4'))
            self.notes.append((.5, 'C4'))
                
        elif inNum == -2:
            self.notes.append((.5, 'C5'))
            self.notes.append((.5, 'A4'))
            self.notes.append((.5, 'F4'))
            self.notes.append((.5, 'C4'))
                
        elif inNum == -3:
            self.notes.append((.5, 'C5'))
            self.notes.append((.5, 'A4'))
            self.notes.append((.5, 'Eb4'))
            self.notes.append((.5, 'C4'))
        
        elif inNum == -4:
            self.notes.append((.5, 'C5'))
            self.notes.append((.5, 'G4'))
            self.notes.append((.5, 'Eb4'))
            self.notes.append((.5, 'C4'))
                
        elif inNum == -5:
            self.notes.append((.5, 'C5'))
            self.notes.append((.5, 'F4'))
            self.notes.append((.5, 'E4'))
            self.notes.append((.5, 'C4'))
        

    def write_part(self, notes):
        '''Will write to the Wave class's array the line'''
        start_time = 0
        for i in notes:
            if i[1] != '':
                s.make_sine(start_time, i[0], i[1], 1000)
            start_time += i[0]
            if len(i) > 2:
                start_time += i[2]


if __name__=="__main__":
    s = Wave()
    rb = GenerateMusic("testMaze02.bmp", "testMaze02.xml")
    s.save()