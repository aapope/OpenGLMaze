'''Stores information about a certain block'''
__author__ = "Ethan, Zach, Emily"
__date__ = "21 October 2011"
from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
from WorldObject import WorldObject

class Zombie(WorldObject):
    '''Stores information about a zombie'''

    def __init__(self, position, color = (100,100,100), obj_type = "zombie"):
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


    


    
