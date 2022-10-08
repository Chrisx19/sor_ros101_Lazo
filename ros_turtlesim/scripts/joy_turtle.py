#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def joy_callback(msg_joy):
    vel = Twist()
    
    vel.linear.x = 4 * msg_joy.axes[1]
    vel.angular.z = 4 * msg_joy.axes[3]
    vel_pub.publish(vel)
    
rospy.init_node('joy_turtle')
joy_sub = rospy.Subscriber("/joy", Joy, joy_callback)
vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)
rospy.spin()
