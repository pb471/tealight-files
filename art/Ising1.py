#Import stuff
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from random import random
from random import randint
from math import exp

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
  
  #Runs the Metropolis algorithm on the spin lattice
  def MetropolisAlg(self):
    global P
    #Create pair of randoms
    x = randint(0,self.side_length - 1)
    y = randint(0, self.side_length - 1)
    
    #Get the spin at that site and the 4 nearest neighbours
    spin = [0, 0, 0, 0, 0]
    spin = self.GetSpins(x, y)
    
    #Get energy, try a spin flip, get new energy
    energy_before = self.GetEnergy(spin)
    spin[0] = -spin[0]
    energy_after = self.GetEnergy(spin)
    
    #Test against Boltzmann
    energy_change = energy_after - energy_before
    r = random()
    boltzmann_value = exp(-(energy_change)/P.T)
    if r < boltzmann_value:
      self.Array[x][y] = -self.Array[x][y]
      
    draw_lattice(self)
    
    #co_ords = [x, y]
    #print co_ords
    #print S
    #print self.Array
  
  #Returns a vector of 5 spins: a spin and its nearest neighbours
  def GetSpins(self, x, y):
    spin = [0, 0, 0, 0, 0]
    spin[0] = self.Array[x][y]
    spin[1] = self.GetSpinCyclicBC(x+1,y)
    spin[2] = self.GetSpinCyclicBC(x-1,y)
    spin[3] = self.GetSpinCyclicBC(x,y+1)
    spin[4] = self.GetSpinCyclicBC(x,y-1)
    return spin
  
  #Returns a single spin, enforcing cyclic BCs
  def GetSpinCyclicBC(self, x, y):
  
    if x == self.side_length:
      x = 0
    elif x < 0:
      x = (self.side_length - 1)
      
    if y == self.side_length:
      y = 0
    elif y < 0:
      y = (self.side_length - 1)
    
    spin_out = self.Array[x][y]
    
    #to_print = [x, y]
    #print to_print
    
    return spin_out
  
  def GetEnergy(self, spin):
    global P
    #Sum over nearest neighbours
    spin_sum = sum(spin) - spin[0]
    
    #Get energy
    energy = P.J * spin[0] * spin_sum
    return energy
     
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
      #Draw boxes
      box(i*square_size[0] + initial_offset[0], 
          j*square_size[1] +  initial_offset[1], 
          square_size[0]-1, 
          square_size[0]-1)
      
      #Print co-ords and spin
      #color("black")
      #t = str(i) + str(j) + str(s.Array[i][j])
      #text(i*square_size[0] + initial_offset[0], 
          #j*square_size[1] +  initial_offset[1],
          #t)
      
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
  to_print = "J = " + t[0] + " T = " + t[1] + " B = " + t[2]
  text(600,100, to_print)
  
  
#Test frame event
def handle_keydown(a):
  global P
  clear_screen()
  print_magnetisation(s)
  print_params(P)
  draw_lattice(s)
  s.MetropolisAlg()

  
#####################
#Main
P = Params(8, #Side length
           0.5, #Fraction spin-up
           -1, #J
           1, #T
           0, #Field
           "green", #spin-up colour
           "brown") #spin-down colour
s = Lattice(P.L, P.M0)
