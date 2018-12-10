#!/usr/bin/env python
import os
path = os.getcwd() + '/src/ros_mitsubishi/src'

import sys
sys.path.insert(0, path)

import rospy
from ros_mitsubishi.msg import CartesianMessage

def talker():
	pub = rospy.Publisher('cartesianMovement', CartesianMessage, queue_size=1000)
	rospy.init_node('sample1', anonymous=True)

	cartesian = CartesianMessage(215.000, -180.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -180.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -130.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -130.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -130.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -80.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -80.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -55.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -80.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -80.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -30.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -80.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -80.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, -30.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 20.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 20.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 70.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 70.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 20.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 70.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 120.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 120.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 170.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 170.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 120.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	cartesian = CartesianMessage(215.000, 120.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
	pub.publish(cartesian)
	

if __name__ == '__main__':
    talker()
