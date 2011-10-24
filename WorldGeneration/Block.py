'''Stores information about a certain block'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"
from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
from WorldObject import WorldObject

class Block(WorldObject):
    '''Stores information about an object, including its position in space and its color'''

    def __init__(self, position, color, obj_type = "block"):
        '''
        @type  position:  3-tuple (x, y, z)
        @param position:  Specifying the object's position
        @type  color:     3-tuple (R, G, B)
        @param color:     Specifying the color values
        @type  obj_type:  String        
        @param obj_type:  This WorldObject's type
        @return: Block
        '''
        WorldObject.__init__(self, position, color, obj_type)                #format from ibiblio website
        #super(Block, self).__init__(self, position, color)        #format from lecture 
        self.width = 1.5
    
