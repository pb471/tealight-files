#Import stuff
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

#Classdefs

#Function definitions
def create_matrix(i_max, j_max, DefaultValue=0):
  Matrix = [[0 for x in xrange(i_max)] for x in xrange(j_max)]
  for i in range(0, i_max):
    for j in range(0, j_max):
      Matrix[i][j] = DefaultValue
     
Mat1 = create_matrix(4,4)
print Mat1[1][1]

