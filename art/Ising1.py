#Import stuff
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from random import random

#################
#Classdefs
class Lattice:
  
  #Constructor
  def __init__(self, side_length, magnetisation):
    self.Array = create_Ising_matrix(side_length, magnetisation)
    self.side_length = side_length
    self.N = side_length*side_length

################
#Function definitions

#Create a square matrix
def create_Ising_matrix(size, magnetisation):
  Matrix = [[0 for x in xrange(size)] for x in xrange(size)]
  for i in range(0, size):
    for j in range(0, size):
      q = random()
      if(q < magnetisation):
        Matrix[i][j] = 1
      else:
        Matrix[i][j] = -1
  return Matrix

#Draw the array of a lattice object
def draw_lattice(s):
  InitialOffset = [30,30]
  SquareSize = [40,40]
  for i in range(0, s.side_length):
    for j in range(0, s.side_length):
      if(s.Array[i][j] == 1):
        color("red")
      else:
        color("blue")
      box(i*SquareSize[0] + InitialOffset[0], 
          j*SquareSize[1] +  InitialOffset[1], 
          SquareSize[0]-1, 
          SquareSize[0]-1)
  
#####################
#Main

s = Lattice(9, 0.5)
draw_lattice(s)

