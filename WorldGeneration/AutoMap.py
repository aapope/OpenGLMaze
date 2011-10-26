	
import Image
import random

__author__ = "Zach Dwyer, Ethan Genz, and Emily Burton-Boehr"
__version__ = 1.0
__date__ = "October 25, 2011"


'''Class that generates a pseudo-random maze .bmp file'''

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HEIGHT = 1000
WIDTH = 1000

class AutoMap:

	def __init__(self):
		'''Constructor for AutoMap object'''
		self.im = Image.new("RGB", (WIDTH, HEIGHT))
		self.pixels = {}
		self.stack = []

		self.fillList()

		self.handle_pixel((1,1))

		self.fillEdges()

		self.drawMap()
		
		self.im.save("AUTOMAP.bmp")

	

	def fillList(self):
		'''Method that stores every pixel value from self.im at (x,y) as (r,g,b)'''
		for i in range(self.im.size[0]):
        	    for j in range(self.im.size[1]):
        	       color = self.im.getpixel((i, j))
		       coords = (i, j)                        
        	       self.pixels[coords] = color

	
	def handle_pixel(self, root_pix):
		'''Method that takes a starting pixel as input and generates the entire maze'''

		self.stack.append(root_pix)

		while len(self.stack) > 0:

	
			pick = random.choice(self.stack)
			if self.hasNeighbors(pick):
				unCarved = self.getUncarved(pick)
				newPick = random.choice(unCarved)
			
				self.pixels[newPick] = WHITE
				changeX , changeY = (newPick[0] - pick[0], newPick[1] - pick[1])
				
				self.pixels[(newPick[0] - changeX/2, newPick[1] - changeY/2)] = WHITE
				self.stack.append(newPick)
			
			else:
				self.stack.remove(pick)
		


	def drawMap(self):
		'''Method for putting new maze pixels on the image object'''
		for key, value in self.pixels.items():
			self.im.putpixel(key, value)




	def getUncarved(self, coords):
		'''Returns a list of unCarved neighbors for specific pixel at input coords'''
		unCarved = []
		if self.pixels[(coords[0], coords[1] + 2)] == BLACK:
			unCarved.append((coords[0], coords[1] + 2))

		if self.pixels[(coords[0] + 2, coords[1])] == BLACK:
			unCarved.append((coords[0] + 2, coords[1]))
			
		if coords[1] > 2  and self.pixels[(coords[0], coords[1] - 2)] == BLACK :
			unCarved.append((coords[0], coords[1] - 2))

		if coords[0] > 2  and self.pixels[(coords[0] - 2, coords[1])] == BLACK:
			unCarved.append((coords[0] - 2, coords[1]))
		return unCarved
		


        def hasNeighbors(self, coords):
		'''Given coords return True is pixel has unCarved neighbors. False otherwise'''
		if coords[0] < HEIGHT - 2 and coords[1] < WIDTH - 2:
			if self.pixels[(coords[0], coords[1]+2)] == BLACK:
				return True
			elif self.pixels[(coords[0] + 2, coords[1])] == BLACK:
				return True
			elif coords[1] > 2 and self.pixels[(coords[0], coords[1]-2)] == BLACK:
				return True
			elif coords[0] > 2 and self.pixels[(coords[0] - 2, coords[1])] == BLACK:
				return True
		else:
			return False
			
	
	def fillEdges(self):
		'''Closes maze edges with black pixels'''
		for i in range(HEIGHT):
			self.pixels[(i , HEIGHT - 1)] = BLACK
		for j in range(WIDTH):
			self.pixels[(WIDTH - 1, j)] = BLACK
			
if __name__ == "__main__":
	am = AutoMap()

	
