#!/usr/bin/env python3
import rospy
import time
import math
from geometry_msgs.msg import Twist             #velocity package for command velocity


rospy.init_node('event2')
publisher = rospy.Publisher('/cmd_vel_AV', Twist, queue_size=1)

msg = Twist()   #constructor

# while not rospy.is_shutdown():
    # Move forward          When sending value, it has to be continues so that robot dont stop
start_time = time.time()
while ( (time.time() - start_time) < 5):   #one second to go forward
    msg.linear.x = 63          #m/s
    msg.angular.z = 0.0         #rad/sec
    publisher.publish(msg)
    time.sleep(0.1)             #before stopping, it will have that wait delay
msg.linear.x = 0.0              #This is the stop, so it goes for 1 second then stop
publisher.publish(msg)

    # Turn
# start_time = time.time()
# while (time.time() - start_time) < 1:   #one second to turn
#     msg.linear.x = 0.0                      #m/s
#     msg.angular.z = -1*math.pi/2.0         #rad/sec  pi/2 on unit circle
#     publisher.publish(msg)
#     time.sleep(0.1)
# msg.angular.z = 0.0                         #This is the stop, so it turns for 1 second then stop      
# publisher.publish(msg)
