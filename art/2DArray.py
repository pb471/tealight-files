#Imports
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

#Classdefs
class Array2D:
  #Constructor
  def __init__(self, i_size, j_size, default_value = 0):
    self.i_size = i_size
    self.j_size = j_size
    self.Array= self.create_matrix(i_size, j_size, default_value)
  
  #Return an i by j matrix, all components set to default_value
  def create_matrix(self, i_size, j_size, default_value):
    Matrix = [[0 for x in xrange(j_size)] for x in xrange(i_size)]
    for i in range(0, i_size):
      for j in range(0, j_size):
        Matrix[i][j] = default_value
    return Matrix

#Main
M = Array2D(4,3,1)
print M.Array
print M.Array[3][1]