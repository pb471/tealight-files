#Import stuff
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

#Classdefs

#Function definitions
def create_matrix(size, default_value=0):
  Matrix = [[0 for x in xrange(size)] for x in xrange(size)]
  for i in range(0, size):
    for j in range(0, size):
      Matrix[i][j] = default_value
  return Matrix
     
Mat1 = create_matrix(3,-2.1)
print Mat1[2][0]

