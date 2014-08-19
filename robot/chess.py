from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here



for j in range(0,4):
  for i in range(0,50):
    move()
    if touch() == "wall":
      turn(1)
      move()
      move()
      move()
      move()
    else smell() 
      move()
    


       

