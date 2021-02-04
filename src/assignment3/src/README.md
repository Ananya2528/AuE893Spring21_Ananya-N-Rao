1. circle.py has the source code to command the turtlebot3 to go in a circular path in gazebo environment.


2. square.py has the source code to command the turtlebot3 to go in a square path in gazebo environment

' enter the command roslaunch assignment3 move.launch code:=circle ' to run the circle.py file

' enter the command roslaunch assignment3 move.launch code:=circle ' to run the square.py file

As soon as this file is executed gazebo environment is launched automatically with turtlebot spawned in the empty_world model and the bot will start moving in circular or 2x2 square path respectively.

As the square.py traces a 2x2 openloop square i.e., with no controller, the bot traces a square-like path as the accumulated errors aren't accounted for.



