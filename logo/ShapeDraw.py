from tealight.logo import (move, 
                           turn, 
                           color)

print "Welcome to ShapeDraw 1.0"

def Draw(Name, Colour, Size):
  if Name == "Square":
    PolygonDraw(Colour, Size, 4)
  elif Name == "Triangle":
    PolygonDraw(Colour, Size, 3)

    
def PolygonDraw(Colour, Size, Sides):
  color(Colour)
  for i in range(0, Sides):
    move(Size)
    turn( 360.0 / Sides)
    
Draw("Triangle", "red", 120)

Matrix = [[0 for x in xrange(5)] for x in xrange(5)] 
print Matrix[1][2]