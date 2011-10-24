'''Stores information about a certain door'''
__author__ = "Ethan, Zach, and Emily"
__date__ = "23 October 2011"

from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
from WorldObject import WorldObject

class Door(WorldObject):
    '''Stores information about a door, including its position in space and its color'''

    def __init__(self, position, color,  door_id, door_open = False, obj_type = "door",):
        '''
        @param position  Specifying the object's position
        @type  position  3-tuple (x, y, z)
        @param color     Specifying the color values
        @type  color     3-tuple (R, G, B)
        @param door_id   The door's id
        @type  door_id   Integer
        @param door_open Specifies if the door is open (unlocked) or not
        @type  door_open Boolean
        @param obj_type  This WorldObject's type
        @type  obj_type  String
        '''


        #super(Key, self).__init__(self, position, color)
        WorldObject.__init__(self, position, color, obj_type)                #format from ibiblio website
        self.id = obj_id
        self.open = obj_open

    def get_id(self):
        return self.id
        
    def is_open(self):
        return self.open

    def open(self):
        self.open = True

    def close(self):
        self.open = False