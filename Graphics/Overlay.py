"""Overlay drawing functions for the Heads Up Display."""
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_overlay(camera):
    """Draw the HUD."""

    _setup()

    glTranslate(50, 50, 0)
    glRotate(-camera.rot_Y, 0, 0, 1)
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex2f(0, -10)
    glVertex2f(10, -15)
    glVertex2f(0, 20)
    glVertex2f(-10, -15)
    glEnd()

    _teardown()

def draw_menu():
    """Draw the in-game menu."""
    _setup()
    _teardown()

def _setup():
    glDisable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, 700.0, 0, 700.0, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()    
    
def _teardown():
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def handle_click(x, y):
    """Handle mouse click on menu elements."""
    pass
