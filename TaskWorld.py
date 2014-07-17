import pyglet
from pyglet.gl import *

import random

CONTEXTS = ['Work', 'Home', 'Phone']
FOLDERS = ['Project A', 'Project B', 'Project C']
PRIORITIES = [ 1, 2, 3 ]

LABEL_OFFSET = 0
TASK_SCALE = 2
TASK_IMAGE = 'assets/task.png'
CONTEXT_IMAGE = 'assets/context.png'

window = pyglet.window.Window(resizable = True)

# Helper functions
def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

# Task Class
class Task():
  def __init__(self, image_name, title, context, folder, priority):

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

# Context Class
class Context():
	def __init__(self, image_name, title):

		self.title = title

		self.image = pyglet.resource.image( image_name )
		center_anchor(self.image)
		
		self.position = [random.randrange(window.width - 100), random.randrange(window.height - 100 )]

		self.label = pyglet.text.Label( self.title,
				   font_name= 'Sans Serif',
				   font_size= 12,
				   x = self.position[0] + self.image.width // 2 + LABEL_OFFSET, 
				   y = self.position[1],
				   anchor_x = 'center', anchor_y = 'center')
	
	def draw(self):
		self.image.blit( self.position[0], self.position[1] )
		self.label.x = self.position[0]
		self.label.y = self.position[1]
		self.label.draw()




@window.event
def on_draw():
  window.clear()

  for theTask in tasks:
      theTask.draw()

  for theContext in contexts:
      theContext.draw()



# Setup transparency
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

CONTEXT_LABELS = ['Work', 'Home', 'Phone']
FOLDER_LABELS = ['Project A', 'Project B', 'Project C']
PRIORITIY_LABELS = [ 1, 2, 3 ]

# Create tasks
task = Task('assets/task.png',
	    'Do something',
	    CONTEXT_LABELS[ random.randrange(len(CONTEXT_LABELS) - 1) ],
	    FOLDER_LABELS[ random.randrange(len(FOLDER_LABELS) - 1) ],
	    PRIORITIY_LABELS[ random.randrange(len(PRIORITIY_LABELS) - 1)])

tasks = []
count = 0
while ( count < 15 ):
  tasks.append( Task( TASK_IMAGE,
		      'Do something',
		      CONTEXT_LABELS[ random.randrange(len(CONTEXT_LABELS) - 1) ],
		      FOLDER_LABELS[ random.randrange(len(FOLDER_LABELS) - 1) ],
		      PRIORITIY_LABELS[ random.randrange(len(PRIORITIY_LABELS))] ))
  count += 1

contexts = []
for theContext in range(len(CONTEXT_LABELS)):
	contexts.append( Context( CONTEXT_IMAGE, CONTEXT_LABELS[theContext] ) )


pyglet.app.run()
