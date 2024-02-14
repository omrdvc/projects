from js import robot
 
for i in range(0,5):
    robot.move_distance(1.0)

for i in range(0,1):
    robot.rotate_angle(-90)
    robot.move_distance(1.0)
    robot.rotate_angle(-90) 

for i in range(0,5):
    robot.move_distance(1.0)

for i in range(0,1):
    robot.rotate_angle(90)
    robot.move_distance(1.0)
    robot.rotate_angle(90)

for i in range(0,5):
    robot.move_distance(1.0)

for i in range(0,1):
    robot.rotate_angle(-90)
    robot.move_distance(1.0)
    robot.rotate_angle(-90)

for i in range(0,5):
    robot.move_distance(1.0)

for i in range(0,1):
    robot.move_distance(-2.5)
    robot.rotate_angle(-90)
    robot.move_distance(0.5)
    robot.move_distance(1.0)
    robot.move_distance(1.0)
    robot.move_distance(1.0)