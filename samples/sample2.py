#!/usr/bin/env python
import os
path = os.getcwd() + '/catkin_ws/src/ros_mitsubishi/src'

import sys
sys.path.insert(0, path)

import rospy
from ros_mitsubishi.msg import CartesianMessage
from ros_mitsubishi.msg import JointMessage

def talker():
	pub = rospy.Publisher('cartesianMovement', CartesianMessage, queue_size=1000)
	rospy.init_node('sample2', anonymous=True)
	
	cartesian = CartesianMessage(250.000, 0.000, 450.000, 0.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(250.000, 0.000, 300.000, 0.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(380.000, 0.000, 300.000, 0.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(300.000, 30.000, 350.000, 0.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(300.000, 30.000, 350.000, 0.000, 90.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(450.000, 0.000, 350.000, 0.000, 90.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(450.000, 0.000, 350.000, 180.000, 90.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(250.000, 0.000, 450.000, 0.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)

if __name__ == '__main__':
    talker()
