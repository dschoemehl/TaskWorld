import pyglet
from pyglet.gl import *

window = pyglet.window.Window()

# Setup transparency
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

image = pyglet.resource.image( 'assets/task.png' )

@window.event
def on_draw():
    window.clear()
    image.blit( 50, 50 )

pyglet.app.run()
