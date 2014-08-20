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
    
  def Magnetisation(self):
    M = 0
    for i in range(0, self.side_length):
      for j in range(0, self.side_length):
        M = M + self.Array[i][j]
    M = float(M)/s.N
    return M
        

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

#Wipe screen
def clear_screen():
  color("white")
  box(0,0,screen_width,screen_height)

#Draw the array of a lattice object
def draw_lattice(s):
  initial_offset = [30,30]
  square_size = [40,40]
  for i in range(0, s.side_length):
    for j in range(0, s.side_length):
      if(s.Array[i][j] == 1):
        color("red")
      else:
        color("blue")
      box(i*square_size[0] + initial_offset[0], 
          j*square_size[1] +  initial_offset[1], 
          square_size[0]-1, 
          square_size[0]-1)
      
#Neatly print magnetisation
def print_magnetisation(s):
  MagValue = s.Magnetisation() * 1
  z = "Magnetisation: %.2f " % MagValue
  text(600,600, z)
  
#Test frame event
def handle_keydown(a):
  clear_screen()
  s = Lattice(12, 0.5)
  print_magnetisation(s)
  draw_lattice(s)

  
#####################
#Main

s = Lattice(12, 0.5)
print_magnetisation(s)
draw_lattice(s)

