import pyglet
from pyglet.gl import *

import random

CONTEXTS = ['Work', 'Home', 'Phone']
FOLDERS = ['Project A', 'Project B', 'Project C']
PRIORITIES = [ 1, 2, 3 ]

LABEL_OFFSET = 0
TASK_SCALE = 2
TASK_IMAGE = 'assets/task.png'

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
    self.position = [random.randrange(0,window.width,1), random.randrange(0,window.height,1)]

    self.image = pyglet.resource.image( image_name )
    self.image.scale = TASK_SCALE
    center_anchor(self.image)
  
    label_text = self.title + '\n' + self.context + '\n' + self.folder + '\n' + str(self.priority) 
  
    self.label = pyglet.text.Label( label_text,
				   font_name= 'Sans Serif',
				   font_size= 8,
				   x = self.position[0] + self.image.width // 2 + LABEL_OFFSET, 
				   y = self.position[1],
				   anchor_x = 'left', anchor_y = 'center',
				   width = 100,
				   multiline = True)
  

  def draw(self):
    #self.position[0] += 1
    #self.position[1] += 1
    self.image.blit( self.position[0], self.position[1] )
    self.label.x = self.position[0] + self.image.width // 2 + LABEL_OFFSET
    self.label.y = self.position[1]
    self.label.draw()
				  

@window.event
def on_draw():
    window.clear()
    #task.draw()
    for theTask in tasks:
      theTask.draw()

# Setup transparency
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

CONTEXTS = ['Work', 'Home', 'Phone']
FOLDERS = ['Project A', 'Project B', 'Project C']
PRIORITIES = [ 1, 2, 3 ]

# Create tasks
task = Task('assets/task.png',
	    'Do something',
	    CONTEXTS[ random.randrange(len(CONTEXTS) - 1) ],
	    FOLDERS[ random.randrange(len(FOLDERS) - 1) ],
	    PRIORITIES[ random.randrange(len(PRIORITIES) - 1)])

tasks = []
count = 0
while ( count < 30 ):
  tasks.append( Task( TASK_IMAGE,
		      'Do something',
		      CONTEXTS[ random.randrange(len(CONTEXTS) - 1) ],
		      FOLDERS[ random.randrange(len(FOLDERS) - 1) ],
		      PRIORITIES[ random.randrange(len(PRIORITIES))] ))
  count += 1

pyglet.app.run()
