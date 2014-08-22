#Imports
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from random import randint
from random import random

#Classdefs
class Array2D:
  #Constructor
  def __init__(self, i_size, j_size, default_value):
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
  def __getitem__(self, index):
    return self.array[index[0]][index[1]]

  def __setitem__(self, index, value):
    self.array[index[0]][index[1]] = value
    
  #Set the values of the matrix to a constant
  def components_constant(self, value):
      for i in range(0, self.i_size):
        for j in range(0, self.j_size):
          self.array[i][j] = value
  
  #Set the values of the matrix to random integers
  def components_randint(self, lower_bound, upper_bound):
      for i in range(0, self.i_size):
        for j in range(0, self.j_size):
          self.array[i][j] = randint(lower_bound, upper_bound)
          
  #Set the values of the matrix to a random float on [0,1]
  def components_random(self):
      for i in range(0, self.i_size):
        for j in range(0, self.j_size):
          self.array[i][j] = random()
  
  #Neatly prints the array
  def print_array(self):
    for i in range(0, self.i_size):
      print self.array[i]
      
  #Sums the array
  def sum(self):
    sumvalue = 0
    for i in range(0, self.i_size):
      for j in range(0, self.j_size):
        sumvalue += self.array[i][j]
    return sumvalue
  
  def draw(self, position, width):
    
  
  

#Main
M = Array2D(4,4,0)
M.components_constant(3)
M.print_array()
p =  M[1,2]
M.components_random()
M.print_array()