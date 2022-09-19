#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

volume = 0
density = 0 

volume_found = False
density_found = False

def volume_callback(data):
	global volume
	global volume_found
	volume = data.data
	volume_found = True
	
def density_callback(data):
	global density
	global density_found
	density = data.data
	density_found = True

def weight_calc():
	if density_found and volume_found:
		weight_calc = volume * density
		weight_pub.publish(weight_calc)

rospy.init_node("cylinder_weight")
rospy.Subscriber("/volume", Float64, volume_callback)
rospy.Subscriber("/density", Float64, density_callback)
weight_pub = rospy.Publisher("/weight", Float64, queue_size=10)

while not rospy.is_shutdown():
    weight_calc()
    rospy.sleep(0.1)
