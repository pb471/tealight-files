from tealight.logo import move, turn


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size / 4
  for i in range(0, edges):
    move(size)
    #square(decoration)
    circle(decoration)
    turn(angle)

def circle(side):
  N = 100
  angle = 360.0/N
  for i in range(0, N):
    move(side)
    turn(angle)
    
turn(-90)
waterwheel(12,100)
