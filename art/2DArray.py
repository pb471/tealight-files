#Imports
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from random import randint

#Classdefs
class Array2D:
  #Constructor
  def __init__(self, i_size, j_size, default_value = 0):
    self.i_size = i_size
    self.j_size = j_size
    self.array= self.create_matrix(i_size, j_size, default_value)
  
  #Return an i by j matrix, all components set to default_value
  def create_matrix(self, i_size, j_size, default_value):
    array = [[0 for x in xrange(j_size)] for x in xrange(i_size)]
    for i in range(0, i_size):
      for j in range(0, j_size):
        array[i][j] = default_value
    return array
  
  #Overload indexing
  def __getitem__(self, i):
    return self.array[i][j]
  
  #Set the values of the matrix to random integers
  def randomize_components(self, lower_bound, upper_bound):
      for i in range(0, self.i_size):
        for j in range(0, self.j_size):
          self.array[i][j] = randint(lower_bound, upper_bound)
  
  #Neatly prints the matrix
  def print_matrix(self):
    for i in range(0, self.i_size):
      print self.array[i]
  

#Main
M = Array2D(4,7,1)
M.print_matrix()
M.randomize_components(0, 3)
M.print_matrix()
M[1]