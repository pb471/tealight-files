#Import stuff
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from random import random

#################
#Classdefs
class Lattice:
  
  #Constructor
  def __init__(self, side_length):
    self.Array = create_matrix(side_length)
    self.side_length = side_length
    self.N = side_length*side_length

################
#Function definitions

#Create a square matrix
def create_matrix(size, default_value=0):
  Matrix = [[0 for x in xrange(size)] for x in xrange(size)]
  random.seed()
  for i in range(0, size):
    for j in range(0, size):
      Matrix[i][j] = default_value
  return Matrix

#Draw the array of a lattice object
def draw_lattice(s):
  InitialOffset = [30,30]
  SquareSize = [40,40]
  for i in range(0, s.side_length):
    for j in range(0, s.side_length):
      box(i*SquareSize[0] + InitialOffset[0], 
          j*SquareSize[1] +  InitialOffset[1], 
          SquareSize[0]-1, 
          SquareSize[0]-1)
  
#####################
#Main

s = Lattice(9)
draw_lattice(s)

