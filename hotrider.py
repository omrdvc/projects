from js import robot

while robot.is_ok():
    if robot.front() == robot.center() + 1 :
        robot.move_forward() 
    elif robot.right() == robot.center() + 1 :
           robot.turn_right()
    elif robot.left() == robot.center() + 1 :
           robot.turn_left()
       