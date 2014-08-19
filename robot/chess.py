from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here



for j in range(0,2):
  for i in range(0,40):
    move()
    if touch() == "wall":
      turn(1)
      move()
      move()
      move()
      move()
      turn(1)
    
turn(3)
move()
move()
move()
move()
turn(3)
    


       

