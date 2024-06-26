# Ref: https://www.youtube.com/watch?v=LCK1qdp_HhQ
# https://github.com/amengede/getIntoGameDev/tree/main/pyopengl%202024
# Packages: pip install pygame PyOpenGL PyOpenGL_accelerate

import pygame as pg
from OpenGL.GL import *

class App:
    def __init__(self):

        # initialize pygame and get a clock 
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode((800, 600), pg.OPENGL| pg.DOUBLEBUF)
        self.clock = pg.time.Clock()  # Will be used to control frame rate

        # Initialize OpenGL
        glClearColor(0.1, 0.2, 0.2, 1) # R, G, B and alpha
        self.mainLoop()
        pass

    def mainLoop(self):
        running = True
        while (running):
            # checkevents
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return

            ## refesh screen - Main Render Loop
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            # Timing
            self.clock.tick(60)  # set FPS to 60

        self.quit()
        return

    def quit(self):
        pg.quit()
        return
    
if __name__ == "__main__":
    myApp = App()