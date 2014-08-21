#Import stuff
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from random import random
from random import randint
from math import exp
from tealight.utils import sleep

#################
#Classdefs
class Lattice:
  def __init__(self, side_length, magnetisation):
    global P
    self.Array = create_Ising_matrix(side_length, magnetisation)
    self.side_length = side_length
    self.N = side_length*side_length
    self.spins_changed = 0
    self.render_spins_changed = create_matrix(P.MetSteps, 3)
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
    
    #co_ords = [x, y]
    #print co_ords
    #print S
    #print self.Array
    
  #Runs the Metropolis algorithm on the spin lattice
  #and renders graphics
  def MetropolisAlg2(self):
    global P
    #Create pair of randoms
    x = randint(0,self.side_length - 1)
    y = randint(0, self.side_length - 1)
    
    #Get the spin at that site and the 4 nearest neighbours
    spin = [0, 0, 0, 0, 0]
    spin = self.GetSpins(x, y)
    old_spin = spin[0]
    
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
    
    #Update spin render array
    if old_spin != self.Array[x][y]:
      self.render_spins_changed[self.spins_changed][0] = x
      self.render_spins_changed[self.spins_changed][1] = y
      self.render_spins_changed[self.spins_changed][2] = self.Array[x][y]
      self.spins_changed = self.spins_changed + 1
    
    #If required number of steps reached, render spins
    if self.spins_changed == P.MetSteps:
      draw_spins(self.render_spins_changed, P.MetSteps)
      self.spins_changed = 0
      self.render_spins_changed = create_matrix(P.MetSteps, 3)
  
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
    
    #Add magnetic field energy
    mag_energy = sum(spin) * P.B
    energy = energy - mag_energy
    return energy
     
class Params:
  def __init__(self, L, M0, J, T, B, MetSteps, SleepTime,
               colour1, colour2):
    self.L = L
    self.M0 = M0
    self.J = J
    self.T = T
    self.B = B
    self.MetSteps = MetSteps
    self.SleepTime = SleepTime
    self.UpColour = colour1
    self.DownColour = colour2
    
class Graph:
  def __init__(self, x, y, x_width, y_width, 
               px_max, py_max, point_size, colour):
    self.x = x
    self.y = y
    self.x_width = x_width
    self.y_width = y_width
    self.px_max = px_max
    self.py_max = py_max
    self.point_size = point_size
    self.colour = colour
    
  def Clear(self):
    color("black")
    box(self.x, self.y, self.x_width, self.y_width)
  
  #def AddPoint(self, px, py):
    #circle
    
        

################
#Function definitions

#Create a square Ising matrix
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

#Create a general matrix
def create_matrix(i_size, j_size):
  Matrix = [[0 for x in xrange(j_size)] for x in xrange(i_size)]
  for i in range(0, i_size):
    for j in range(0, j_size):
      Matrix[i][j] = 0
  return Matrix

#Wipe screen
def clear_values():
  color("white")
  box(690,30,200,150)

#Draw the array of a lattice object
def draw_lattice(s):
  global P
  initial_offset = [30,30]
  square_size = [500/s.side_length,500/s.side_length]
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
def draw_spins(render_spin_changed, N):
  global P
  initial_offset = [30,30]
  square_size = [500/s.side_length,500/s.side_length]
  for i in range(0, N):
    if(render_spin_changed[i][2] == 1):
      color(P.UpColour)
    else:
      color(P.DownColour)
    #Draw boxes
    box(render_spin_changed[i][0]*square_size[0] + initial_offset[0], 
          render_spin_changed[i][1]*square_size[1] +  initial_offset[1], 
          square_size[0]-1, 
          square_size[0]-1)
      
#Neatly print magnetisation
def print_magnetisation(s):
  color("black")
  t = "%.2f" % s.Magnetisation()
  text(690,50, t)

#Neatly print parameters
def print_params(P):
  color("black")
  t = ["a", "b", "c"]
  t[0] = str(P.J)
  t[1] = str(P.T)
  t[2] = str(P.B)
  
  for i in range(0,3):
    text(690, 50 + (i+1) * 20, t[i])
    
def draw_letters():
  color("black")
  r = ["M:", "J:", "T:", "B:"]
  for i in range(0,4):
    text(660, 50 + i * 20, r[i])
    
#Convert rgba vector to string
def coltostr(col):
  string_out = "rgba("
  for i in range(0,4):
    string_out = string_out + str(col[i]) + ","
  print string_out
  
  
  
  
#Handle keypresses
def handle_keydown(key):
  keys[key] = 1
    
def handle_keyup(key):
  keys[key] = 0
  
def handle_frame():
  global P
  #sleep(P.SleepTime)
  clear_values()
  if keys["q"] == 1:
    P.T = P.T + 0.05
  if keys["a"] == 1:
    P.T = P.T - 0.05
  if keys["w"] == 1:
    P.B = P.B + 0.05
  if keys["s"] == 1:
    P.B = P.B - 0.05
  
  for i in range(0,P.MetSteps):
    s.MetropolisAlg2()
  print_params(P)
  print_magnetisation(s)
  
  #G.AddPoint(P.T, s.Magnetisation() )
  
  
#####################
#Main
Colour1 = [255, 0, 0, 1]
Colour2 = [255, 0, 0, 1]

ColourString1 = coltostr(Colour1)



P = Params(20, #Side length
           1, #Fraction spin-up
           -1, #J
           2, #T
           0, #Field
           5, #Metropolis steps per key press
           1, #Sleep time
           "blue", #spin-up colour
           "green") #spin-down colour
s = Lattice(P.L, P.M0)
G = Graph(30, 540, #graph location
          320, 320, #graph size
          10, 1, #max px and py values
          5, #Point size
          "red") #colour
G.Clear()
print_magnetisation(s)
print_params(P)
draw_lattice(s)
draw_letters()
keys = {"q" : 0, "a" : 0, "w" : 0, "s" : 0}
