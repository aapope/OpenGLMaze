'''Stores information about a certain object'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"
from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
import math

class WorldObject:
    '''Stores information about a block, including its position in space and its color'''

    def __init__(self, position, color, obj_type = "generic"):
        '''Initializes the block's color and position. Takes two 3-tuples (xyz and rgb)'''
        self.position = ObjectPosition(position)
        self.color = ObjectColor(color)
        self.dist = 0
        self.type = obj_type
        self.width = 1
        
    def get_pos(self):
        '''Returns a three-tuple: x, y, z
        '''
        return self.position.get()

    def set_pos(self, position):
        '''Sets the position with a three-tuple: x, y, z
        @type  position: 3-tuple
        @param position: The new position
        '''
        self.position.set(position)

    def get_color(self):
        '''Returns a three-tuple: r, g, b
        @return: A 3-tuple of the r,g,b values
        '''
        return self.color.get()

    def set_color(self, color):
        '''Sets the color with a three-tuple: r, g, b
        @type  color: 3-tuple
        @param color: The color in 3-tuple form (r, g, b)
        '''
        self.color.set(color)
        
    def __str__(self):
        '''Returns x y z r g b
        @return: String representation as x,y,z,r,g,b
        '''
        return str(self.position)+' '+str(self.color)

    def get_type(self):
        return self.type

    def get_dist(self, x, y, z):
        coords = self.position.get()
        self.dist = math.sqrt((coords[0]-x)**2 + (coords[1]-y)**2 + (coords[2]-z)**2)
        return self.dist

    def width(self):
        return self.width
