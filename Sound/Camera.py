from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from XMLParser import *
import Image
from Block import Block
import sys
from Snowman import Snowman
from GameSounds import GameSounds

name = 'Example'
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400


__author__ = "Zach Dwyer and Trisha Andrews"
__date__ = "October 20, 2011"
__version__ = 1.1

class Camera:

	def __init__(self):
		'''Constructor to initialize Camera postion'''
		self.transX = -8
		self.transY = 0
		self.transZ = 14
		self.rotX = 0
		self.rotY = 0
		self.rotZ = 0
		
		self.BLOCK_SIZE = 0.5
		
		parser = XMLParser("Blockworld.xml")
		self.soundboard = GameSounds()
        
		self.soundboard.loadSound("crashsound.wav")
		self.soundboard.loadMusic("outfile.wav")
		self.blocks = parser.getBlocks()

	def printBlocks(self):
		'''Prints the block'''
		for block in self.blocks:
			print block

	def main(self):
		'''Method to initialize OpenGL window'''
                glutInit(sys.argv)
    		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    		glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    		glutCreateWindow(name)

	        glutKeyboardFunc(self.keyPressed)

		glEnable(GL_TEXTURE_2D)
		glMatrixMode(GL_PROJECTION)
		gluPerspective(45, 1 , .15, 100 )
		glMatrixMode(GL_MODELVIEW)

		
    		light_diffuse = (.8, .8, .8, 1)
    		light_position = (.5, 1, -.5, 1)
    		glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    		glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    		light_ambient = (.35, .35, .35, 1)
    		light_position = (0, 0, 3, 0)
    		glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
    		glLightfv(GL_LIGHT1, GL_POSITION, light_position)

		glEnable(GL_DEPTH_TEST)    		
		glEnable(GL_LIGHTING)
    		glEnable(GL_LIGHT0)
    		glEnable(GL_LIGHT1)

		self.loadTextures()
		self.soundboard.playMusic()
		
    		glutDisplayFunc(self.display)
    		glutMainLoop()

	def keyPressed(self, key, x, y):
		'''Method for handing keyPress events'''
		print "Pressed key: ", key
		if key == 'a':
			self.transX += -.1
			self.soundboard.playSound()
		if key == 'd':
			self.transX += .1
		if key == 'q':
			self.transY += -.1
		if key == 'e':
			self.transY += .1
		if key == 's':
			self.transZ += .1
		if key == 'w':
			self.transZ += -.1
		if key == 'i': #j
			self.rotX += -3
		if key == 'k': #l
			self.rotX += 3
		if key == 'l':#k
			self.rotY += 3
		if key == 'j':#i
			self.rotY += -3
		if key == 'o':
			self.rotZ += -3
		if key == 'u':
			self.rotZ += 3
    		self.display()

	def loadTextures(self):
		'''Loads a texture for the floor'''
		image = Image.open("WhiteCobblestone.jpg")
	
		ix = image.size[0]
		iy = image.size[1]
		image = image.tostring("raw", "RGBX", 0, -1)
	
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)


	def display(self, x=0, y=0):
		'''Method for displaying snowmen on OpenGL window'''
    		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    		glLoadIdentity()
	
		
	#	glTranslate(self.transX, self.transY, self.transZ)
		glRotate(self.rotX, 1 , 0 , 0)
		glRotate(self.rotY, 0 , 1, 0)
		glRotate(self.rotZ, 0 , 0 , 1)

		gluLookAt(self.transX, self.transY, self.transZ, self.transX , self.transY , self.transZ -3 , 0 , 1, 0)
	#	gluLookAt(self.transX, self.transY, self.transZ, self.rotX, self.rotY, self.rotZ -3, 0 , 1 , 0)
		
	       #	glColor(.5, 0.0, .7)
		glBegin(GL_QUADS)
		
		glTexCoord2f(0.0, 0.0); glVertex3f(-16.0, -.5, -16.0)
		glTexCoord2f(1.0, 0.0); glVertex3f(16.0, -.5, -16.0)
		glTexCoord2f(1.0, 1.0); glVertex3f(16.0, -.5, 16.0)
		glTexCoord2f(0.0, 1.0); glVertex3f(-16.0, -.5, 16.0)
		
		glEnd()
		
		glTranslate(-8, 0, 8)

    		sm = Snowman()
		sm.createSnowman(.5)

		glTranslate(2, -1.25, 0)

		for block in self.blocks:
			
			glMaterial(GL_FRONT, GL_AMBIENT, (block.getR(),block.getG(), block.getB()));

			glTranslate(block.getX(), block.getY(), block.getZ())

			glutSolidCube(self.BLOCK_SIZE)
		
    		glFlush()
        
		


if __name__ == '__main__': 
	
	cam = Camera()
	cam.main()
	glDisable(GL_TEXTURE_2D);







