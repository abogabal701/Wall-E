from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from numpy import *

def draw():
    glClearColor(.72, .72, .72, 1)
    ###########FACE###########
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor(.10, .10, .10)
    glVertex2d(.2, 0.2)
    glVertex2d(0.2, 0)
    glVertex2d(-0.2, 0)
    glVertex2d(-0.2, 0.2)
    glEnd()
    ######قرن#########
    glBegin(GL_POLYGON)
    glColor(.10, .20, .20)
    glVertex2d(0.2, 0.3)
    glVertex2d(0.2, 0.2)
    glVertex2d(.1, 0.2)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(.10, .20, .20)
    glVertex2d(-0.2, 0.3)
    glVertex2d(-0.2, 0.2)
    glVertex2d(-.1, 0.2)
    glEnd()
    #############eye1#######
    glBegin(GL_POLYGON)
    glColor(1, 1, 0)
    glVertex2d(.12, .14)
    glVertex2d(0.12, 0.09)
    glVertex2d(0.08, 0.09)
    glVertex2d(0.08, 0.14)
    glEnd()
#########eye2############################
    glBegin(GL_POLYGON)
    glColor(1, 1, 0)
    glVertex2d(-.08, .14)
    glVertex2d(-.08, 0.09)
    glVertex2d(-0.12, 0.09)
    glVertex2d(-0.12, 0.14)
    glEnd()
############nose##############
    glBegin(GL_POLYGON)
    glColor(1, 1,0)
    glVertex2d(0,.11)
    glVertex2d(.05,.08)
    glVertex2d(-.05, 0.08)
    glEnd()
    ############mouse#############
    glBegin(GL_POLYGON)
    glColor(1, 1,0)
    glVertex2d(.03, .01)
    glVertex2d(-.07, .03)
    glVertex2d(-.05, 0.06)
    glEnd()
    #############الوسط#############
    glBegin(GL_POLYGON)
    glColor(1, 1, 0)
    glVertex2d(.2, -.3)
    glVertex2d(.2, -0.4)
    glVertex2d(-.2, -0.4)
    glVertex2d(-0.2,-0.3)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1, 0, 0)
    glVertex2d(.05, -.33)
    glVertex2d(.05, -0.37)
    glVertex2d(-.05, -0.33)
    glVertex2d(-0.05, -0.37)
    glEnd()
###########body#######
    glBegin(GL_POLYGON)
    glColor(.10, .10, .10)
    glVertex2d(.1, 0)
    glVertex2d(0.2, -.3)
    glVertex2d(-0.2, -.3)
    glVertex2d(-0.1, 0)
    glEnd()
    ######الرجلين##############
    glBegin(GL_POLYGON)
    glColor(.10, .10, .10)
    glVertex2d(.2, -0.4)
    glVertex2d(0.2, -.6)
    glVertex2d(0.05, -.6)
    glVertex2d(0.05, -0.4)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(.10, .10, .10)
    glVertex2d(-0.05, -0.4)
    glVertex2d(-0.05, -.6)
    glVertex2d(-0.2, -.6)
    glVertex2d(-0.2, -0.4)
    glEnd()
    ######## القدم#################
    glBegin(GL_POLYGON)
    glColor(.10, .20, .20)
    glVertex2d(.2, -0.6)
    glVertex2d(0.2, -.65)
    glVertex2d(0.05, -.65)
    glVertex2d(0.05, -0.6)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(.10, .20, .20)
    glVertex2d(-.05, -.6)
    glVertex2d(-0.05, -.65)
    glVertex2d(-0.2, -.65)
    glVertex2d(-0.2, -.6)
    glEnd()
########## Wings##############
    glBegin(GL_POLYGON)
    glColor(.10, .20, .20)
    glVertex2d(.1, 0)
    glVertex2d(0.3, -0.1)
    glVertex2d(0.4, -.4)
    glVertex2d(0.3, -.3)
    glVertex2d(0.2, -0.4)
    glVertex2d(0.1, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(.10, .20, .20)
    glVertex2d(-.1, 0)
    glVertex2d(-0.3, -0.1)
    glVertex2d(-0.4, -.4)
    glVertex2d(-0.3, -.3)
    glVertex2d(-0.2, -0.4)
    glVertex2d(-0.1, 0)
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Robot")
glutInitWindowSize(100, 100)
glutDisplayFunc(draw)
glutMainLoop()