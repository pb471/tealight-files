import tealight.logo

print "Welcome to ShapeDraw 1.0"

def Draw(Name, Colour, Size):
  if Name == "Square":
    PolygonDraw(Colour, Size, 4)

    
def PolygonDraw(Colour, Size, Sides):
  color(Colour)
  for i in range(1, Sides):
    move(Size)
    turn( 360.0 / Sides)
    
Draw("Square", "red", 3)