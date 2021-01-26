#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI= 3.1415926535897

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")

    ang_vel = float(input ("Input your angular velocity:"))
    speed = float(input("Input your speed:"))
    rot = float(input("Input number of rotations:"))
    distance = 2.0*PI*rot*(speed/ang_vel)
    isAnti_Clockwise = int(input("Anti_Clockwise? (0 or 1) : ")) #True=1 or False=0

    #Checking if the movement is Anti_Clockwise or Clockwise
    if(isAnti_Clockwise):
        vel_msg.angular.z = abs(ang_vel)
    else:
        vel_msg.angular.z = -abs(ang_vel)
    #Since we are moving just in x-axis
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    #vel_msg.angular.z = ang_vel

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance <= distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
