'''This is the class that renders blocks (and the floor that they sit on). Camera angles are handled by another class'''
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
import Image
from Obj2 import Model

# TODO: Choosing only the ones you can see to actually render. 
#       Speed up the rendering process so the game runs more smoothly
#       Nicer ground? Reflections? Shadows?
class RenderWorld:
    '''This is the class that renders blocks (and the floor that they sit on). Camera angles are handled by another class'''
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400
    
    def __init__(self, file_name):
        '''Sets everything up: camera, modes, lighting, and the list of blocks'''        
        self.camera = Camera()
        self.set_up_graphics()
        self.makeLights()
        self.objects = LoadWorld.load(file_name)
        stuff = ''
        stuff = [stuff + 'yes' for obj in self.objects
         if obj.get_type() == 'door']
        print stuff
        glClearColor(.529,.8078,.980,0)
        glutIdleFunc(self.display)
        glutDisplayFunc(self.display)
        glutIgnoreKeyRepeat(GLUT_KEY_REPEAT_OFF)
        glutKeyboardFunc(self.keyPressed)
        glutKeyboardUpFunc(self.keyUp)
        glutSetCursor(GLUT_CURSOR_NONE)
        glutPassiveMotionFunc(self.mouseMove)
        self.door = Model('Graphics/basicdoor.obj','door')
        self.key = Model('Graphics/Key.obj', 'key')
        self.soundboard = GameSounds()
        self.soundboard.loadMusic("Sound/outfile.wav")
        self.soundboard.playMusic()
        glutMainLoop()

    def set_up_graphics(self):
        '''Sets up the gl modes that are necessary'''
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        glutCreateWindow('Mazeworld!')
        
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45,1,.15,100)
        glMatrixMode(GL_MODELVIEW)
        
        glEnable(GL_DEPTH_TEST)

    def makeLights(self):
        '''Sets up the light sources and their positions. We have an ambient light and two sets of specular/diffuse lights'''
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
        '''Called for every refresh; redraws the floor and objects and based on the camera angle'''
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.camera.move()
        self.camera.check_collisions(self.objects)
        self.camera.renderCamera()        
        self.renderLightSource()        
        self.makeFloor()
        #Transparent objects!
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.sort_by_dist()

        for obj in self.objects[:]:
            color = obj.get_color()
            pos = obj.get_pos()
            glPushMatrix()
            #Set the objects shininess, ambient, diffuse, and specular reflections. The objects are slightly transparent.
            glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 75)
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0,0,0,1])#[color[0], color[1], color[2], 1])
            glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [.4, .4, .4, 1])
            glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [.9, .9, .9, .7])
            glTranslate(pos[0],pos[1],pos[2])
            if obj.get_type() == 'block':
                glutSolidCube(2)
            elif obj.get_type() == 'key':
#                glutSolidCube(2)
                self.makeobj(obj.get_type())
            elif obj.get_type() == 'door':
                #glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [.7, .7, .7, 1])
                #glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [.9, .9, .9, .7])
                self.makeobj(obj.get_type())
            else:
                glutSolidSphere(2, 40, 40)
            glPopMatrix()
        glDisable(GL_BLEND)

        glFlush()

    def mouseMove(self, x, y):
        '''Called when the move is moved'''
        factor = 1
        padding = 10
        tmp_x = (self.camera.mouse_x - x)/factor
        tmp_y = (self.camera.mouse_y - y)/factor
        self.camera.rotate(tmp_y, tmp_x, 0)
        if x <= 0+padding or x >= self.WINDOW_WIDTH-padding:
            x = self.WINDOW_WIDTH/2
            glutWarpPointer(x, y)
        if y <= 0+padding or y >= self.WINDOW_HEIGHT-padding:
            y = self.WINDOW_HEIGHT/2
            glutWarpPointer(x, y)
        self.camera.mouse_x = x
        self.camera.mouse_y = y

    def keyPressed(self, key, x, y):
        '''Called when a key is pressed'''
        if key.lower() in self.camera.keys:
            self.camera.keys[key] = True
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
        elif key == 'x':
            exit(0)

    def keyUp(self, key, x, y):
        '''Called when a key is released'''
        if key.lower() in self.camera.keys:
            self.camera.keys[key] = False
    
    def renderLightSource(self):
        '''Resets the light sources to the right position'''
        glLightfv(GL_LIGHT0, GL_POSITION, self.diffuse_pos1)
        glLightfv(GL_LIGHT2, GL_POSITION, self.diffuse_pos2)
        glLightfv(GL_LIGHT3, GL_POSITION, self.diffuse_pos2)
        glLightfv(GL_LIGHT4, GL_POSITION, self.diffuse_pos2)
        
    def makeFloor(self):
        '''Makes a floor of size size and places an image (texture) on it'''
        glEnable(GL_TEXTURE_2D)
        size = 50
        image = Image.open("Graphics/checkerboard.bmp")
	
        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)

        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0) ; glVertex(-size,-.5,-size)
        glTexCoord2f(1.0, 0.0) ; glVertex(size,-.5,-size)
        glTexCoord2f(1.0, 1.0) ; glVertex(size,-.5,size)
        glTexCoord2f(0.0, 1.0) ; glVertex(-size,-.5,size)
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def makeobj(self, kind):
        if kind == 'key':
#            print 'key'
            self.key.rawDraw()
        elif kind == 'door':
#            print 'door'
            self.door.rawDraw()

    def sort_by_dist(self):
        for obj in self.objects:
            obj.get_dist(self.camera.pos_X, self.camera.pos_Y, self.camera.pos_Z)
        self.objects = sorted(self.objects, key=lambda obj: obj.dist, reverse=True)

if __name__ == '__main__':
    RENDER = RenderWorld('OpenGLMaze/WorldGeneration/keys.xml')
