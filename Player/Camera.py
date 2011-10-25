'''Stores and changes the camera position'''
__author__ = "Emily and Andrew"
__date__ = "20 October 2011"
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Sound import GameSounds
#from Graphics import RenderWorld
import math

class Camera:
    '''Stores and changes the camera position'''

    SPEED = .5
    ROTATE = 1
    WIDTH = 1

    def __init__(self, x=0, y=0, z=0):
        '''Initializes everything to 0'''
        self.pos_X = x
        self.pos_Y = y
        self.pos_Z = z
        self.start_pos=(x,y,z)
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
        self.points = 0
        self.dead_timeout = 0
        self.key_timeout = 0
        self.treasure_timeout = 0
        self.soundboard = GameSounds()
        
        self.footSound = self.soundboard.toSound("Sound/footsteps.wav")
        self.footSound.set_volume(1.0)
        self.collisionSound = self.soundboard.toSound("Sound/crashsound.wav")
        self.collisionSound.set_volume(1.5)
        self.pickSound = self.soundboard.toSound("Sound/picksound.wav")
        self.treasureSound = self.soundboard.toSound("Sound/cash.wav")
        self.zomSound = self.soundboard.toSound("Sound/zombie.mp3")
        
    def renderCamera(self):
        '''Translates and rotates the camera to the correct position'''
        glRotatef(-self.rot_X , 1.0, 0.0, 0.0)
        glRotatef(-self.rot_Y , 0.0, 1.0, 0.0)
        glRotatef(-self.rot_Z , 0.0, 0.0, 1.0)
        glTranslatef(-self.pos_X, -self.pos_Y, -self.pos_Z)

    def move(self, objects):
        self.check_collisions(objects)
        if self.keys['a']:
            x, z = self.strafe(-self.SPEED)
            self.pos_Z += z
            self.pos_X += x
            self.footSound.play()
        if self.keys['d']:
            x, z = self.strafe(self.SPEED)
            self.pos_Z += z
            self.pos_X += x
            self.footSound.play()
        if self.keys['w']:
            x, z = self.walk(-self.SPEED)
            self.pos_Z += z
            self.pos_X += x
            self.footSound.play()
        if self.keys['s']:
            x, z = self.walk(self.SPEED)
            self.pos_Z += z
            self.pos_X += x
            self.footSound.play()
        
    def rotate(self, x, y, z):
        '''Rotates by x, y, and z'''
        self.rot_X += x
        self.rot_Y += y
        self.rot_Z += z

    def strafe(self, amt):
        '''Strafes left or right, bassed on the angle'''
        tmp_Z = math.cos(self.rot_X*math.pi/180)*math.sin(-self.rot_Y*math.pi/180)*amt
        tmp_X = math.cos(self.rot_X*math.pi/180)*math.cos(self.rot_Y*math.pi/180)*amt
        return (tmp_X, tmp_Z)
        #Use to allow for change in height based on angle
        #self.pos_Y += math.cos(self.rot_X*math.pi/180)*math.sin(-self.rot_Z*math.pi/180)*amt

    def walk(self, amt):
        '''Walks forward and back based on the angle you're facing'''
        tmp_Z = math.cos(self.rot_X*math.pi/180)*math.cos(self.rot_Y*math.pi/180)*amt
        tmp_X = math.cos(self.rot_X*math.pi/180)*math.sin(self.rot_Y*math.pi/180)*amt
        return (tmp_X, tmp_Z)
        #Use to allow for change in height based on angle
        #self.pos_Y += math.cos(self.rot_Z*math.pi/180)*math.sin(-self.rot_X*math.pi/180)*amt

    def height(self, amt):
        '''Goes up or down. Always along the y axis'''
        self.pos_Y += amt

    def check_collisions(self, objects):
        '''Checks for objects within aware distance and performs a hit test upon them'''
        for obj in objects:
            x2, y2, z2 = obj.get_pos()
            tmp_x, tmp_y, tmp_z = self.project_move()
            if obj.get_dist(self.pos_X, self.pos_Y, self.pos_Z) < self.aware:
                self.hitTest(obj, tmp_x, tmp_y, tmp_z)
            else:
                if obj.get_type()=='zombie':
                    if obj.get_dist(self.pos_X, self.pos_Y, self.pos_Z) < 5.5:
                        self.zomSound.play()

    def project_move(self):
        tmp_X = self.pos_X
        tmp_Y = self.pos_Y
        tmp_Z = self.pos_Z
        if self.keys['a']:
            x, z = self.strafe(-self.SPEED)
            tmp_Z += z
            tmp_X += x
        if self.keys['d']:
            x, z = self.strafe(self.SPEED)
            tmp_Z += z
            tmp_X += x
        if self.keys['w']:
            x, z = self.walk(-self.SPEED)
            tmp_Z += z
            tmp_X += x
        if self.keys['s']:
            x, z = self.walk(self.SPEED)
            tmp_Z += z
            tmp_X += x
        return (tmp_X, tmp_Y, tmp_Z)

    def hitTest(self, obj, x, y, z):
        w = obj.width
        for i in range(1,5):
            x2, z2 = self.get_sides(i)
            x += x2
            z += z2
            tmp_x, tmp_y, tmp_z = obj.get_pos()
            if x < tmp_x + w/2 and x > tmp_x - w/2 and z < tmp_z + w/2 and z > tmp_z - w/2:
                if obj.get_type()=='zombie':
                    # If a zombie is encountered, you are transported back to the start
                    self.pos_X=self.start_pos[0]
                    self.pos_Y=self.start_pos[1]
                    self.pos_Z=self.start_pos[2]
                    self.dead_timeout = 50
                elif obj.get_type()=='key':
                    if not obj.get_has(): 
                        obj.get_key()
                        self.key_timeout = 50
                        self.pickSound.play()
                        obj.get_door().open()
                elif obj.get_type()=='door':
                    if not obj.is_open():
                        self.reverse_move()
                        self.collisionSound.play()
                elif obj.get_type()=='chest':
                    if not obj.get_has():
                        obj.get_chest()
                        self.treasure_timeout = 50
                        self.points += obj.get_points()
                        self.treasureSound.play()
                else:
                    self.reverse_move()
                    self.collisionSound.play()
                        
    def get_sides(self, side):
        '''Returns points of given side of bounding box'''
        tmp_X = 0
        tmp_Z = 0
        
        if side == 1:
            tmp_Z = math.cos(self.rot_X*math.pi/180)*math.cos(self.rot_Y*math.pi/180)*(-self.WIDTH/2)
            tmp_X = math.cos(self.rot_X*math.pi/180)*math.sin(self.rot_Y*math.pi/180)*(-self.WIDTH/2)
        if side == 2:
            tmp_Z = math.cos(self.rot_X*math.pi/180)*math.sin(-self.rot_Y*math.pi/180)*(self.WIDTH/2)
            tmp_X = math.cos(self.rot_X*math.pi/180)*math.cos(self.rot_Y*math.pi/180)*(self.WIDTH/2)
        if side == 3:
            tmp_Z = math.cos(self.rot_X*math.pi/180)*math.cos(self.rot_Y*math.pi/180)*(-self.WIDTH/2)
            tmp_X = math.cos(self.rot_X*math.pi/180)*math.sin(self.rot_Y*math.pi/180)*(-self.WIDTH/2)
        if side == 4:
            tmp_Z = math.cos(self.rot_X*math.pi/180)*math.sin(-self.rot_Y*math.pi/180)*(self.WIDTH/2)
            tmp_X = math.cos(self.rot_X*math.pi/180)*math.cos(self.rot_Y*math.pi/180)*(self.WIDTH/2)

        return (tmp_X, tmp_Z)
        #Use to allow for change in height based on angle
        #self.pos_Y += math.cos(self.rot_X*math.pi/180)*math.sin(-self.rot_Z*math.pi/180)*amt

    def reverse_move(self):
        if self.keys['a']:
            x, z = self.strafe(self.SPEED)
            self.pos_Z += z
            self.pos_X += x
        if self.keys['d']:
            x, z = self.strafe(-self.SPEED)
            self.pos_Z += z
            self.pos_X += x
        if self.keys['w']:
            x, z = self.walk(self.SPEED)
            self.pos_Z += z
            self.pos_X += x
        if self.keys['s']:
            x, z = self.walk(-self.SPEED)
            self.pos_Z += z
            self.pos_X += x
    
    def project_move_other(self):
        tmp_X = self.pos_X
        tmp_Y = self.pos_Y
        tmp_Z = self.pos_Z
        x, z = self.walk(self.SPEED)
        tmp_Z += z
        tmp_X += x
        return (tmp_X, tmp_Z)

    def get_camera_distance(self, x2, y2, z2):
        '''Returns the distance from given point'''
        tmp_x = (self.pos_X - x2)**2
        tmp_y = (self.pos_Y - y2)**2
        tmp_z = (self.pos_Z - z2)**2
        return math.sqrt(tmp_x+tmp_y+tmp_z)
