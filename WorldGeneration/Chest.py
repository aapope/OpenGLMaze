'''Stores information about a certain Chest object'''
__author__ = "Zach, Emily, Ethan"
__date__ = "24 October 2011"
from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
from WorldObject import WorldObject

class Chest(WorldObject):
    '''Stores information about an object, including its position in space and its color'''

    def __init__(self, position, points = 100, color = (255,255,0), obj_type = "chest"):
        '''
        @type  position:  3-tuple (x, y, z)
        @param position:  Specifying the object's position
        @type  color:     3-tuple (R, G, B)
        @param color:     Specifying the color values
        @type  obj_type:  String        
        @param obj_type:  This WorldObject's type
        @return:          A Chest object that inherits from WorldObject
        '''
        WorldObject.__init__(self, position, color, obj_type)                #format from ibiblio website
        #super(Block, self).__init__(self, position, color)        #format from lecture 
        self.points = 100


    def get_points(self):
        return self.points

    
