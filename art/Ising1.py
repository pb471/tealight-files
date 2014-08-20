#Import stuff
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from random import random

#################
#Classdefs
class Lattice:
  def __init__(self, side_length, magnetisation):
    self.Array = create_Ising_matrix(side_length, magnetisation)
    self.side_length = side_length
    self.N = side_length*side_length
    
  def Magnetisation(self):
    M = 0
    for i in range(0, self.side_length):
      for j in range(0, self.side_length):
        M = M + self.Array[i][j]
    M = float(M)/self.N
    return M
  
class Params:
  def __init__(self, L, M0, J, T, B, colour1, colour2):
    self.L = L
    self.M0 = M0
    self.J = J
    self.T = T
    self.B = B
    self.UpColour = colour1
    self.DownColour = colour2
        

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
  global P
  initial_offset = [30,30]
  square_size = [40,40]
  for i in range(0, s.side_length):
    for j in range(0, s.side_length):
      if(s.Array[i][j] == 1):
        color(P.UpColour)
      else:
        color(P.DownColour)
      box(i*square_size[0] + initial_offset[0], 
          j*square_size[1] +  initial_offset[1], 
          square_size[0]-1, 
          square_size[0]-1)
      
#Neatly print magnetisation
def print_magnetisation(s):
  color("black")
  t = "Magnetisation: %.2f " % s.Magnetisation()
  text(600,600, t)

#Neatly print parameters
def print_params(P):
  color("black")
  t = ["a", "b", "c"]
  t[0] = str(P.J)
  t[1] = str(P.T)
  t[2] = str(P.B)
  to_print = "J = " + t[1] + "\n T = " + t[2]
  text(600,100, t)
  
  
#Test frame event
def handle_keydown(a):
  global P
  clear_screen()
  s = Lattice(P.L, P.M0)
  print_magnetisation(s)
  print_params(P)
  draw_lattice(s)

  
#####################
#Main
P = Params(9, #Side length
           0.5, #Fraction spin-up
           1, #J
           1, #T
           0, #Field
           "green", #spin-up colour
           "brown") #spin-down colour
S = Lattice(P.L, P.M0)
print_magnetisation(S)
draw_lattice(S)

