#Import stuff
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)

#Classdefs
class Lattice:
  
  #Constructor
  def __init__(self, side_length):
    self.Array = create_matrix(side_length)
    self.side_length = side_length
    self.N = side_length*side_length


#Function definitions
def create_matrix(size, default_value=0):
  Matrix = [[0 for x in xrange(size)] for x in xrange(size)]
  for i in range(0, size):
    for j in range(0, size):
      Matrix[i][j] = default_value
  return Matrix

def draw_lattice(s):
  for i in range(0, s.side_length):
    print s.side_length
    print i
    box(i+30, 30, 20, 20)
  
     
s = Lattice(9)
print s.N
draw_lattice(s)

