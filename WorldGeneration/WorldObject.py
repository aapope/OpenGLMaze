'''Stores information about a certain object'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"
from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
import math

class WorldObject:
    '''Stores information about an object, including its position in space and its color'''

    def __init__(self, position, color, obj_type = "generic"):
        '''Initializes an object's color and position. Takes two 3-tuples (xyz and rgb)'''
        
        #self.position = ObjectPosition((float(position[0]),
        #float(position[1]), float(position[2])))
        self.x = float(position[0])
        self.y = float(position[1])
        self.z = float(position[2])
        self.r = float(color[0])
        self.g = float(color[1])
        self.b = float(color[2])
        self.dist = 0
        self.type = obj_type
        self.width = 1.1
        
    def get_pos(self):
        '''Returns a three-tuple: x, y, z
        '''
        return (self.x, self.y, self.z)

    def set_pos(self, position):
        '''Sets the position with a three-tuple: x, y, z
        @type  position: 3-tuple
        @param position: The new position
        '''
        self.x = float(position[0])
        self.y = float(position[1])
        self.z = float(position[2])

    def get_color(self):
        '''Returns a three-tuple: r, g, b
        @return: A 3-tuple of the r,g,b values
        '''
        return (self.r, self.g, self.b)

    def set_color(self, color):
        '''Sets the color with a three-tuple: r, g, b
        @type  color: 3-tuple
        @param color: The color in 3-tuple form (r, g, b)
        '''
        self.r = float(color[0])
        self.g = float(color[1])
        self.b = float(color[2])
        
    def __str__(self):
        '''Returns x y z r g b
        @return: String representation as x,y,z,r,g,b
        '''
        return ' '.join([self.x, self.y, self.z,
                         self.r, self.g, self.b])

    def get_type(self):
        return self.type

    def get_dist(self, x, y, z):
        self.dist = math.sqrt((self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2)
        return self.dist

    def width(self):
        return self.width
