'''Stores information about a certain key'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"

from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
from WorldObject import WorldObject

class Key(WorldObject):
    '''Stores information about an object, including its position in space and its color'''

    def __init__(self, position, color, obj_type = "key"):
        '''Initializes the key's color and position. Takes two 3-tuples (xyz and rgb)'''
        #super(Key, self).__init__(self, position, color)
        WorldObject.__init__(self, position, color, obj_type)                #format from ibiblio website
        self.type = "key"
        
