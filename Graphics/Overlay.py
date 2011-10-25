"""Overlay drawing functions for the Heads Up Display."""
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_overlay():
    """Draw the HUD."""

    print "Drawing HUD."
    _setup()
    glColor4f(1.0, 0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(0, 50)
    glVertex2f(100, 50)
    glVertex2f(100, 100)
    glVertex2f(0, 100)
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
