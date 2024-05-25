# Ref: https://www.youtube.com/watch?v=LCK1qdp_HhQ
# https://github.com/amengede/getIntoGameDev/blob/main/pyopengl%202024/1%20-%20hello%20window/main.py
# Packages: pip install pygame PyOpenGL PyOpenGL_accelerate glfw

import glfw
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

vp_size_changed = False
def fb_resize_callback(window, w, h):
    global vp_size_changed
    vp_size_changed = True

class App3D:
    def __init__(self):

        # initialize pygame and get a clock 
        glfw.init()
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_PROFILE, GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
        # glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)

        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "LearnOpenGL_Py", None, None)
        glfw.make_context_current(self.window)
        glfw.set_window_size_callback(self.window, fb_resize_callback)

        # self.clock = pg.time.Clock()  # Will be used to control frame rate

        # Initialize OpenGL
        glClearColor(0.1, 0.2, 0.2, 1) # R, G, B and alpha
        pass

    def mainLoop(self):
        global vp_size_changed

        while not glfw.window_should_close(self.window):
            #check events
            glfw.poll_events()
            if glfw.get_key(self.window, GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
                break

            if vp_size_changed == True:
                vp_size_changed = False
                w, h = glfw.get_framebuffer_size(self.window)
                glViewport(0, 0, w, h)
                print("new viewport size:", w, h)

            #refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)

            ## refesh screen - Main Render Loop
            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)

            # Timing
            # self.clock.tick(60)  # set FPS to 60

        return

    def quit(self):
        # Clean up appand resources 
        glfw.destroy_window(self.window)
        glfw.terminate()
        return
    
if __name__ == "__main__":
    myApp = App3D()
    myApp.mainLoop()
    myApp.quit()