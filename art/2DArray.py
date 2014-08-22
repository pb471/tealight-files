#Imports
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

#Classdefs
class 2DArray:
  def __init__(self, i_size, j_size, default_value = 0):
    self.i_size = i_size
    self.j_size = j_size
    self.Matrix = self.create_matrix(i_size, j_size, default_value)
  
  def create_matrix(self, i_size, j_size, default_value):
    
    