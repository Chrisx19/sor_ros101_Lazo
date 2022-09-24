#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64      #This is a message that is able to handle number

rospy.init_node("Cylinder_input")
radius_pub = rospy.Publisher("/radius", Float64, queue_size=10)	#This becomes the topic
height_pub = rospy.Publisher("/height", Float64, queue_size=10)	#Becomes the topic *ROS topic list*

radius = float(input("Enter Radius: "))				#Entering input on pub radius
height = float(input("Enter Height: "))				#Entering input on Pub Height

while not rospy.is_shutdown():
	radius_pub.publish(radius)				#Publishing the radius val with topic list
	height_pub.publish(height)                              #Publishing the height val with topic list
	rospy.sleep(0.1)


