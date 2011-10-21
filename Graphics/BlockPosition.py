'''Stores information about the block's position in space'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"

class BlockPosition:
    '''Stores information about the block's position in space'''

    def __init__(self, position):
        '''Sets the initial block position with a three-tuple: x, y, z. Float precision'''
        self.X, self.Y, self.Z = position
        self.X = float(self.X)
        self.Y = float(self.Y)
        self.Z = float(self.Z)

    def set(self, position):
        '''Sets the block position with a three-tuple: x, y, z. Float precision'''
        self.X, self.Y, self.Z = position
        self.X = float(self.X)
        self.Y = float(self.Y)
        self.Z = float(self.Z)

    def get(self):
        '''Returns a three-tuple of floats: x, y, z'''
        return (self.X, self.Y, self.Z)

    def __str__(self):
        '''Returns x  y z'''
        return str(self.X)+' '+str(self.Y)+' '+str(self.Z)
