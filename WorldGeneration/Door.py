'''Stores information about a certain door'''
__author__ = "Ethan, Zach, and Emily"
__date__ = "23 October 2011"

from ObjectPosition import ObjectPosition
from ObjectColor import ObjectColor
from WorldObject import WorldObject

class Door(WorldObject):
    '''Stores information about a door, including its position in space and its color'''

    def __init__(self, position, color,  door_id, rotation = 0, door_open = False, obj_type = "door"):
        '''Initialize door
        @type  position:  3-tuple (x, y, z)
        @param position:  Specifying the object's position
        @type  color:     3-tuple (R, G, B)
        @param color:     Specifying the color values
        @type  door_id:   Integer
        @param door_id:   The door's id
        @type  door_open: Boolean
        @param door_open: Specifies if the door is open (unlocked) or not
        @type  obj_type:  String
        @param obj_type:  This WorldObject's type
        '''
        #super(Key, self).__init__(self, position, color)
        WorldObject.__init__(self, position, color, obj_type)                #format from ibiblio website
        self.id = door_id
        self.rotation = rotation
        self.open = door_open
        self.width = 2

    def get_id(self):
        '''
        @return: The door's ID
        '''
        return self.id
        
    def is_open(self):
        '''        
        @return: Whether or not the door is open        '''
        return self.open

    def open(self):
        ''' Set the self.open boolean to true        '''
        self.open = True

    def close(self):
        ''' Set the self.open boolean to false        '''
        self.open = False

    def get_rotation(self):
        '''
        @return: The current rotation angle of this door
        '''
        return self.rotation

    def set_rotation(self, rotation):
        '''
        '''
        self.rotation = rotation

