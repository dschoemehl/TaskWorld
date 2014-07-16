import pyglet
from pyglet.gl import *

window = pyglet.window.Window()

# Helper functions
def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

# Task Class
class Task():
  def __init__(self, image_name, title, context, folder, priority):
    self.title = image_name
    self.title = title
    self.context = context
    self.folder = folder
    self.priority = priority
    self.position = [50,50]

    self.image = pyglet.resource.image( image_name )
    center_anchor(self.image)
  
    label_text = self.title + ', ' + self.context + ', ' + self.folder + ', ' + self.priority 
  
    self.label = pyglet.text.Label( label_text,
				   font_name= 'Sans Serif',
				   font_size= 12,
				   x = self.position[0] + self.image.width // 2, 
				   y = self.position[1],
				   anchor_x = 'left', anchor_y = 'center' )
  

  def draw(self):
    self.position[0] += 1
    self.position[1] += 1
    self.image.blit( self.position[0], self.position[1] )
    self.label.x = self.position[0] + self.image.width // 2
    self.label.y = self.position[1]
    self.label.draw()
				  

@window.event
def on_draw():
    window.clear()
    task.draw()

# Setup transparency
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Create tasks
task = Task('assets/task.png',
	    'Do something',
	    'Work',
	    'Project',
	    '1')

pyglet.app.run()
