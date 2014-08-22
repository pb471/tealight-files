#Imports
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

#Classdefs
class 2DArray:
  #Constructor
  def __init__(self, i_size, j_size, default_value = 0):
    self.i_size = i_size
    self.j_size = j_size
    self.Matrix = self.create_matrix(i_size, j_size, default_value)
  
  #Return an i by j matrix, all components set to default_value
  def create_matrix(self, i_size, j_size, default_value):
    Matrix = [[0 for x in xrange(j_size)] for x in xrange(i_size)]
    for i in range(0, size):
      for j in range(0, size):
        Matrix[i][j] = default_value
    return Matrix

#Main
M = 2DArray(3,3,1)