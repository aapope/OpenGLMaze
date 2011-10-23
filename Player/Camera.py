'''Stores and changes the camera position'''
__author__ = "Emily and Andrew"
__date__ = "20 October 2011"
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

class Camera:
    '''Stores and changes the camera position'''

    SPEED = .2

    def __init__(self):
        '''Initializes everything to 0'''
        self.pos_X = 0
        self.pos_Y = 0
        self.pos_Z = 0
        self.rot_X = 0
        self.rot_Y = 0
        self.rot_Z = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.keys = {}
        self.keys["w"] = False
        self.keys["a"] = False
        self.keys["s"] = False
        self.keys["d"] = False
        self.aware = 5
        
    def renderCamera(self):
        '''Translates and rotates the camera to the correct position'''
        glRotatef(-self.rot_X , 1.0, 0.0, 0.0)
        glRotatef(-self.rot_Y , 0.0, 1.0, 0.0)
        glRotatef(-self.rot_Z , 0.0, 0.0, 1.0)
        glTranslatef(-self.pos_X, -self.pos_Y, -self.pos_Z)

    def move(self):
        if self.keys['a']:
            self.strafe(-self.SPEED)
        if self.keys['d']:
            self.strafe(self.SPEED)
        if self.keys['w']:
            self.walk(-self.SPEED)
        if self.keys['s']:
            self.walk(self.SPEED)
        
    def rotate(self, x, y, z):
        '''Rotates by x, y, and z'''
        self.rot_X += x
        self.rot_Y += y
        self.rot_Z += z

    def strafe(self, amt):
        '''Strafes left or right, bassed on the angle'''
        self.pos_Z += math.cos(self.rot_X*math.pi/180)*math.sin(-self.rot_Y*math.pi/180)*amt
        self.pos_X += math.cos(self.rot_X*math.pi/180)*math.cos(self.rot_Y*math.pi/180)*amt
        #Use to allow for change in height based on angle
        #self.pos_Y += math.cos(self.rot_X*math.pi/180)*math.sin(-self.rot_Z*math.pi/180)*amt

    def walk(self, amt):
        '''Walks forward and back based on the angle you're facing'''
        self.pos_Z += math.cos(self.rot_X*math.pi/180)*math.cos(self.rot_Y*math.pi/180)*amt
        self.pos_X += math.cos(self.rot_X*math.pi/180)*math.sin(self.rot_Y*math.pi/180)*amt
        #Use to allow for change in height based on angle
        #self.pos_Y += math.cos(self.rot_Z*math.pi/180)*math.sin(-self.rot_X*math.pi/180)*amt

    def height(self, amt):
        '''Goes up or down. Always along the y axis'''
        self.pos_Y += amt

    def check_collisions(self, objects):
        for obj in objects:
            x2, y2, z2 = obj.get_pos()
            d = self.get_distance(x2, y2, z2)
            if d < self.aware:
                self.hitTest(obj)

    def hitTest(self, obj):
        pass          
            
    def get_distance(self, x2, y2, z2):
        '''Returns the distance from given point'''
        tmp_x = (self.pos_X - x2)**2
        tmp_y = (self.pos_Y - y2)**2
        tmp_z = (self.pos_Z - z2)**2
        return math.sqrt(tmp_x+tmp_y+tmp_z)

