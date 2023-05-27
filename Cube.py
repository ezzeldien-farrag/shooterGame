import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

rotation_angle = 0  

def draw_cube():
    global rotation_angle 

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity()  

    glRotatef(rotation_angle, 1, 1, 1)  

    glBegin(GL_QUADS) 
    
    
    glColor3f(0.0, 0.0, 0.5)  
    glVertex3f(1.0, 1.0, 1.0)  
    glColor3f(0.0, 0.0, 1.0)  
    glVertex3f(-1.0, 1.0, 1.0)  
    glColor3f(0.0, 0.0, 1.0)  
    glVertex3f(-1.0, -1.0, 1.0) 
    glColor3f(0.0, 0.0, 0.5) 
    glVertex3f(1.0, -1.0, 1.0) 
    

    glColor3f(0.0, 0.0, 0.5)  
    glVertex3f(1.0, 1.0, -1.0)
    glColor3f(0.0, 0.0, 1.0) 
    glVertex3f(-1.0, 1.0, -1.0)
    glColor3f(0.0, 0.0, 1.0)  
    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(0.0, 0.0, 0.5)  
    glVertex3f(1.0, -1.0, -1.0)
    
    glColor3f(0.0, 0.0, 0.5) 
    glVertex3f(-1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 1.0) 
    glVertex3f(-1.0, 1.0, -1.0)
    glColor3f(0.0, 0.0, 1.0)  
    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(0.0, 0.0, 0.5) 
    glVertex3f(-1.0, -1.0, 1.0)
    
    glColor3f(0.0, 0.0, 0.5) 
    glVertex3f(1.0, 1.0, -1.0)
    glColor3f(0.0, 0.0, 1.0)  
    glVertex3f(1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 1.0)  
    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(0.0, 0.0, 0.5) 
    glVertex3f(1.0, -1.0, -1.0)
    

    glColor3f(0.0, 0.0, 0.5)
    glVertex3f(1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.8) 
    glVertex3f(-1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.8) 
    glVertex3f(-1.0, 1.0, -1.0)
    glColor3f(0.0, 0.0, 0.5) 
    glVertex3f(1.0, 1.0, -1.0)
    
    glColor3f(0.0, 0.0, 0.5)
    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(0.0, 0.0, 0.8)
    glVertex3f(-1.0, -1.0, 1.0)
    glColor3f(0.0, 0.0, 0.8)
    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(0.0, 0.0, 0.5)
    glVertex3f(1.0, -1.0, -1.0)

    glEnd()
    
    glutSwapBuffers()

def update_rotation_angle():
    global rotation_angle
    rotation_angle += 1 
    if rotation_angle > 360:
        rotation_angle = 0
    time.sleep(0.01)
    glutPostRedisplay() 

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) 
    glutInitWindowSize(500, 500) 
    glutCreateWindow(b"Cube")  
    
    glutDisplayFunc(draw_cube) 
    glutIdleFunc(update_rotation_angle)

    glEnable(GL_DEPTH_TEST)  
    glMatrixMode(GL_PROJECTION) 
    gluPerspective(45, 1, 0.1, 50.0) 
    
    glTranslatef(0.0, 0.0, -5.0) 

    glutMainLoop()

if __name__ == "__main__":
    main()
