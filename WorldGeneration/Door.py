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
        @type  position  3-tuple (x, y, z)
        @param position  Specifying the object's position
        @type  color     3-tuple (R, G, B)
        @param color     Specifying the color values
        @type  door_id   Integer
        @param door_id   The door's id
        @type  door_open Boolean
        @param door_open Specifies if the door is open (unlocked) or not
        @type  obj_type  String
        @param obj_type  This WorldObject's type
        '''
        #super(Key, self).__init__(self, position, color)
        WorldObject.__init__(self, position, color, obj_type)                #format from ibiblio website
        self.id = door_id
        self.open = door_open
        self.width = 2

    def get_id(self):
        return self.id
        
    def is_open(self):
        return self.open

    def open(self):
        self.open = True

    def close(self):
        self.open = False
