from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 50
y = 50
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.1

color("pink")
text(50,50,"Rachel")

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("green")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("purple")
  
  spot(x,y,8)
  
  