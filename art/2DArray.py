#Imports
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from random import randint
from random import random

#Classdefs
class Array2D:
  #Constructor
  def __init__(self, i_size, j_size, default_value=0):
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
  
  #Gets the maximum value of the array
  def max(self):
    max_value = max(self.array)
    max_value = max(max_value)
    return max_value
  
  #Gets the minimum value of the array
  def min(self):
    max_value = min(self.array)
    max_value = min(max_value)
    return max_value
  
  #Draws the array on-screen as squares; colour indicates value
  #M.draw([30 30], [100 100])
  def draw(self, position = [30, 30], width = [200,200]):
    for i in range(0, self.i_size):
      for j in range(0, self.j_size):
        rgb_value = 255 * self.array[i][j]/self.max()
        print rgb_value
        color("red")
        box(position[0] + j * width[0]/self.j_size,
            position[1] + i * width[1]/self.i_size,
            width[0]/self.j_size - 1,
            width[1]/self.i_size - 1)
    
  
  

#Main
M = Array2D(2,2)
M.components_random()
M.print_array()
a = M.min()
print a
M.draw([90, 90], [100, 100])