"""Overlay drawing functions for the Heads Up Display."""
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_overlay(camera, paused):
    """Draw the HUD."""

    _setup()
    glPushMatrix()
    _draw_compass(camera)
    glPopMatrix()
    _draw_speaker(paused)
    _teardown()

def _draw_compass(camera):
    glTranslate(50, 50, 0)
    glColor3f(0.75, 0.75, 0.75)
    glBegin(GL_LINES)
    glVertex2f(0, 25)
    glVertex2f(0, -25)
    glVertex2f(25, 0)
    glVertex2f(-25, 0)
    glEnd()

    glRotate(-camera.rot_Y, 0, 0, 1)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-10, -15)
    glVertex2f(0, -10)
    glVertex2f(10, -15)
    glVertex2f(0, 15)
    glEnd()

def _draw_speaker(paused):
    glTranslate(700, 0, 0)
    # Draw the right-side box
    glBegin(GL_QUADS)
    glVertex2f(-50, 50, 0)
    glVertex2f(-50, 60, 0)
    glVertex2f(-60, 60, 0)
    glVertex2f(-60, 50, 0)
    glVertex2f(-60, 50, 0)
    glEnd()
    # Draw the speaker cone
    glBegin(GL_QUADS)
    glVertex2f(-70, 40, 0)
    glVertex2f(-60, 50, 0)
    glVertex2f(-60, 60, 0)
    glVertex2f(-70, 70, 0)
    glEnd()
    # Draw the paused X through the speaker
    if paused:
        glColor3f(1.0, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(-78, 74, 0)
        glVertex2f(-80, 72, 0)
        glVertex2f(-45, 37, 0)
        glVertex2f(-43, 39, 0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(-43, 72, 0)
        glVertex2f(-46, 74, 0)
        glVertex2f(-81, 39, 0)
        glVertex2f(-79, 37, 0)
        glEnd()
    
def draw_menu():
    """Draw the in-game menu."""
    _setup()
    _teardown()

def _setup():
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, 700.0, 0, 700.0, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()    
    
def _teardown():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def handle_click(x, y):
    """Handle mouse click on menu elements."""
    pass
