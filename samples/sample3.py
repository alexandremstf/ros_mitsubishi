#!/usr/bin/env python
import os
path = os.getcwd() + '/catkin_ws/src/ros_mitsubishi/src'

import sys
sys.path.insert(0, path)

import rospy
from ros_mitsubishi.msg import CartesianMessage
from ros_mitsubishi.msg import JointMessage

def talker():
	pub = rospy.Publisher('jointMovement', JointMessage, queue_size=1000)
	rospy.init_node('sample3', anonymous=True)

	joint = JointMessage(0.000, 0.000, 0.000, 0.000, 0.000, 100.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(0.000, 0.000, 60.000, 0.000, 0.000, 100.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(0.000, 90.000, 0.000, 0.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(0.000, 90.000, -90.000, 0.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(0.000, 90.000, -90.000, 90.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(0.000, 90.000, -90.000, -90.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(0.000, 90.000, -90.000, 45.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(-150.000, 90.000, -90.000, 45.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(-150.000, 45.000, -90.000, 45.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	joint = JointMessage(0.000, 0.000, 0.000, 0.000, 0.000, 30.0) #j1, j2, j3, j5, j6, speed
	pub.publish(joint)
	

if __name__ == '__main__':
    talker()
