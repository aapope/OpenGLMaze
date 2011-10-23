'''Stores the color attributes for a block'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"
class ObjectColor:
    '''Stores the color attributes for a block'''

    def __init__(self, rgb):
        '''Sets the initial rgb values with a three-tuple: r, g, b. All floats'''
        self.r = float(rgb[0])
        self.g = float(rgb[1])
        self.b = float(rgb[2])
        
    def set(self, rgb):
        '''Set the rgb values with a three-tuple: r, g, b. Float precision'''
        self.r = float(rgb[0])
        self.g = float(rgb[1])
        self.b = float(rgb[2])

    def get(self):
        '''Returns a three-tuple: r, g, b. Float precision'''
        return (self.r, self.g, self.b)
    
    def __str__(self):
        '''Returns r g b'''
        return str(self.r)+' '+str(self.g)+' '+str(self.b)
