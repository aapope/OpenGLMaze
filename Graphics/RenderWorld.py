'''Contains a class that renders the maze itself.'''

__author__ = "Emily and Andrew"
__date__ = "21 October 2011"

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Player import Camera
from WorldGeneration import Block
from WorldGeneration import Key
from WorldGeneration import Door
from WorldGeneration import LoadWorld
from Sound import GameSounds
from time import time
import Image
import math
import Overlay
from Obj2 import Model

class RenderWorld:
    '''This is the class that renders maze.
    Camera angles are handled by Camera.py.
    '''
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 700
    MAP_SIZE =100

    def __init__(self, file_name):
        '''Sets up camera, modes, lighting, sounds, and objects.'''
        self.set_up_graphics()
        self.makeLights()
        self.objects, self.player_loc = LoadWorld.load(file_name)
        self.camera = Camera(self.player_loc[0],0,self.player_loc[1])

        glClearColor(.529,.8078,.980,0)

        glutIdleFunc(self.display)
        glutDisplayFunc(self.display)

        glutIgnoreKeyRepeat(GLUT_KEY_REPEAT_OFF)
        glutKeyboardFunc(self.keyPressed)
        glutKeyboardUpFunc(self.keyUp)

        glutSetCursor(GLUT_CURSOR_NONE)
        glutPassiveMotionFunc(self.mouseMove)

        self.floor_texture = Image.open("Graphics/checkerboard.bmp")
        self.ix, self.iy = self.floor_texture.size
        self.floor = self.floor_texture.tostring("raw", "RGBX", 0, -1)
        
        self.door = Model('Graphics/basicdoor.obj','door')
        self.key = Model('Graphics/Key.obj', 'key')
        self.zombie = Model('Graphics/zombie.obj', 'zombie')#try zombie5.obj for fun sometime
        self.chest = Model('Graphics/treasure.obj', 'chest')
        self.soundboard = GameSounds()
        self.footSound = self.soundboard.toSound("Sound/footsteps.wav")
        self.collisionSound = self.soundboard.toSound("Sound/crashsound.wav")
        self.pickSound = self.soundboard.toSound("Sound/picksound.wav")
        self.zomSound = self.soundboard.toSound("Sound/zombie.wav")
        self.fanSound = self.soundboard.toSound("Sound/fanfare.wav")
        self.soundboard.loadMusic("Sound/music.wav")
        self.soundboard.playMusic()

        self.zomstart = time()

        glutMainLoop()

    def set_up_graphics(self):
        '''Sets up OpenGL to provide double buffering, RGB coloring,
        depth testing, the correct window size, perspective
        rendering/fulcrum clipping, and a title.'''
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        glutCreateWindow('Mazeworld!')

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45,1,.15,100)
        glMatrixMode(GL_MODELVIEW)

        glEnable(GL_DEPTH_TEST)

    def makeLights(self):
        '''Sets up the light sources and their positions. We have an
        ambient light and two sets of specular/diffuse lights.'''
        self.diffuse_pos1 = (50,5,0,1)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (.5, .5, .5, 1))
        glLightfv(GL_LIGHT0, GL_POSITION, self.diffuse_pos1)

        glLightfv(GL_LIGHT1, GL_AMBIENT, (.2, .2, .2, 1))
        glLightfv(GL_LIGHT1, GL_POSITION, (0, 0, 1, 0))

        glLightfv(GL_LIGHT2, GL_SPECULAR, (.8, .8, .8, 1))
        glLightfv(GL_LIGHT2, GL_POSITION, self.diffuse_pos1)

        self.diffuse_pos2 = (0,1,0,1)
        glLightfv(GL_LIGHT3, GL_DIFFUSE, (.5, .5, .5, 1))
        glLightfv(GL_LIGHT3, GL_POSITION, self.diffuse_pos2)
        glLightfv(GL_LIGHT4, GL_SPECULAR, (.8, .8, .8, 1))
        glLightfv(GL_LIGHT4, GL_POSITION, self.diffuse_pos2)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
        glEnable(GL_LIGHT2)

    def display(self, x=0, y=0):
        '''Called for every refresh; redraws the floor and objects
        based on the camera angle. Calls collision detection, handles
        the appropriate objects for keys, doors, etc.'''
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        self.camera.move(self.objects)
        self.camera.check_collisions(self.objects)
        self.camera.renderCamera()
        self.renderLightSource()
        self.makeFloor()

        # Transparent objects!
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Thou shalt not enable sort_by_dist.

        for obj in self.objects:
            color = obj.get_color()
            pos = obj.get_pos()
            obj_type = obj.get_type()

            glPushMatrix()

            # Set the objects shininess, ambient, diffuse, and
            # specular reflections. The objects are slightly
            # transparent. <- (nick: Why?)
            glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 75)
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [color[0], color[1], color[2], .5])
            glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [.4, .4, .4, 1])
            glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [.9, .9, .9, .8])

            glTranslate(pos[0], pos[1], pos[2])

            if obj_type == 'block':
                glutSolidCube(2)

            elif obj_type == 'key' or obj_type == 'chest':
                if not obj.get_has():
                    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 75)
                    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [color[0], color[1], color[2], .5])
                    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [.4, .4, .4, .7])
                    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [.9, .9, .9, .6])
                    self.makeobj(obj.get_type())

            elif obj_type == 'zombie':
                glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 75)
                glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [color[0], color[1], color[2], .5])
                glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [.4, .4, .4, .7])
                glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [.9, .9, .9, .6])
                zomX, zomY, zomZ = pos # We already grabbed pos.
                self.makeobj(obj.get_type())

            elif obj_type == 'chest':
                glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 75)
                glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [color[0], color[1], color[2], .5])
                glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [.4, .4, .4, .7])
                glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [.9, .9, .9, .6])
                self.makeobj(obj.get_type())

            elif obj_type == 'door':
                if obj.get_key().get_has():
                    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [color[0], color[1], color[2], .2])
                    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [.4, .4, .4, .2])
                    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [.9, .9, .9, .2])
                else:
                    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 75)
                    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [color[0], color[1], color[2], .5])
                    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [.4, .4, .4, .7])
                    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [.9, .9, .9, .6])
                glRotate(obj.get_rotation(), 0, 1, 0)
                self.makeobj(obj.get_type())

            else:
                glutSolidSphere(2, 40, 40)

            glPopMatrix()

        glDisable(GL_BLEND)

        Overlay.draw_overlay(self.camera,
                             self.soundboard.paused)

        
        if self.camera.key_timeout > 0:
            Overlay.draw_text("Got a key!")
            self.camera.key_timeout -= 1
        if self.camera.dead_timeout > 0:
            Overlay.draw_text("A zombie killed you!")
            self.camera.dead_timeout -= 1
        if self.camera.treasure_timeout > 0:
            Overlay.draw_text("Got treasure!")
            self.camera.treasure_timeout -= 1
            
        glutSwapBuffers()

    def mouseMove(self, x, y):
        '''Called when the mouse is moved.'''
        factor = 1
        padding = 50
        tmp_x = (self.camera.mouse_x - x)/factor
        tmp_y = (self.camera.mouse_y - y)/factor
        self.camera.rotate(0, tmp_x, 0)
        if x <= 0 + padding or x >= self.WINDOW_WIDTH - padding:
            x = self.WINDOW_WIDTH/2
            glutWarpPointer(x, y)
        if y <= 0 + padding or y >= self.WINDOW_HEIGHT - padding:
            y = self.WINDOW_HEIGHT / 2
            glutWarpPointer(x, y)
        self.camera.mouse_x = x
        self.camera.mouse_y = y
        
    def keyPressed(self, key, x, y):
        '''Called when a key is pressed.'''
        if key.lower() in self.camera.keys:
            self.camera.keys[key.lower()] = True
        if glutGetModifiers() == GLUT_ACTIVE_SHIFT:
            self.camera.keys["shift"] = True
        if key == 'j':
            self.camera.rotate(0,3,0)
        elif key == 'l':
            self.camera.rotate(0,-3,0)
        elif key == 'i':
            self.camera.rotate(3,0,0)
        elif key == 'k':
            self.camera.rotate(-3,0,0)
        elif key == ' ':
            self.camera.height(.1)
        elif key == 'c':
            self.camera.height(-.1)
        elif key == 'm':
            if self.soundboard.paused:
                self.soundboard.unpauseMusic()
            else:
                self.soundboard.pauseMusic()
        elif key == 'x':
            exit(0)

    def keyUp(self, key, x, y):
        '''Called when a key is released.'''
        # Speed things up by not checking if the key is in the map
        self.camera.keys[key.lower()] = False
        if not glutGetModifiers() == GLUT_ACTIVE_SHIFT:
            self.camera.keys["shift"] = False

    def renderLightSource(self):
        '''Resets the light sources to the right position.'''
        glLightfv(GL_LIGHT0, GL_POSITION, self.diffuse_pos1)
        glLightfv(GL_LIGHT2, GL_POSITION, self.diffuse_pos2)
        glLightfv(GL_LIGHT3, GL_POSITION, self.diffuse_pos2)
        glLightfv(GL_LIGHT4, GL_POSITION, self.diffuse_pos2)

    def makeFloor(self):
        '''Makes a floor of the correct size and places an self.floor_texture
        (texture) on it.'''
        glEnable(GL_TEXTURE_2D)

        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, self.ix, self.iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.floor)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex(-self.MAP_SIZE,-.5,-self.MAP_SIZE)
        glTexCoord2f(1.0, 0.0)
        glVertex(self.MAP_SIZE,-.5,-self.MAP_SIZE)
        glTexCoord2f(1.0, 1.0)
        glVertex(self.MAP_SIZE,-.5,self.MAP_SIZE)
        glTexCoord2f(0.0, 1.0)
        glVertex(-self.MAP_SIZE,-.5,self.MAP_SIZE)
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def makeobj(self, kind):
        '''Makes the desired object from the loaded obj file.'''

        if kind == 'key':
            self.key.rawDraw()
        elif kind == 'door':
            self.door.rawDraw()
        elif kind == 'zombie':
            self.zombie.rawDraw()
        elif kind == 'chest':
            self.chest.rawDraw()



    def get_visible(self, lst):
        '''Only draws the objects sitting in front of the camera.
        Everything behind it is left undrawn.'''
        to_use = []
        for item in lst:
            c = item.dist
            x,z = self.camera.project_move_other()
            b = self.camera.get_camera_distance(x, 0, z)
            a = item.get_dist(x, 0, z)
            angle = 0
            try:
                num = ((b**2)+(c**2)-(a**2))/(2*b*c)
                angle = math.acos(num)/math.pi*180
            except:
                pass
            if angle > 90:
                to_use.append(item)
        return to_use
