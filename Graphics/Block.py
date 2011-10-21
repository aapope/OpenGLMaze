'''Stores information about a certain block'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"
from BlockPosition import BlockPosition
from BlockColor import BlockColor

class Block:
    '''Stores information about a block, including its position in space and its color'''

    def __init__(self, position, color):
        '''Initializes the block's color and position. Takes two 3-tuples (xyz and rgb)'''
        self.position = BlockPosition(position)
        self.color = BlockColor(color)
        
    def get_pos(self):
        '''Returns a three-tuple: x, y, z'''
        return self.position.get()

    def set_pos(self, position):
        '''Sets the position with a three-tuple: x, y, z'''
        self.position.set(position)

    def get_color(self):
        '''Returns a three-tuple: r, g, b'''
        return self.color.get()

    def set_color(self, color):
        '''Sets the color with a three-tuple: r, g, b'''
        self.color.set(color)
        
    def __str__(self):
        '''Returns x y z r g b'''
        return str(self.position)+' '+str(self.color)
