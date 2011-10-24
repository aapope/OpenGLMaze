'''Stores information about a certain key'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"

from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
from WorldObject import WorldObject

class Key(WorldObject):
    '''Stores information about a key, including its position in space and its color'''

    def __init__(self, position, color, key_id, obj_type = "key"):
       '''
       @type  position:  3-tuple (x, y, z)
       @param position:  Specifying the object's position
       @type  color:     3-tuple (R, G, B)
       @param color:     Specifying the color values
       @type  key_id:   Integer
       @param key_id:   The key's id
       @type  obj_type:  String
       @param obj_type:  This WorldObject's type
       '''
        #super(Key, self).__init__(self, position, color)
       WorldObject.__init__(self, position, color, obj_type)                #format from ibiblio website
       self.id = key_id
        
    def get_id(self):
        return self.id
