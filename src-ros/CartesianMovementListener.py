#!/usr/bin/env python
import os
path = os.getcwd() + '/src/ros_mitsubishi/src'

import sys
sys.path.insert(0, path)

import RobotArm
robot = RobotArm.RobotArm()

import rospy
from ros_mitsubishi.msg import CartesianMessage

def callback(data):
	rospy.loginfo(" I heard %s", data)
	
	robot.moveCartesianPosition(data.x, data.y, data.z, data.a, data.b, data.speed) #x, y, z, a, b, speed
	print data

def listener():
    robot.init()

    rospy.init_node('listenerCartesian', anonymous=False)
    rospy.Subscriber("cartesianMovement", CartesianMessage, callback, queue_size=1000)
    rospy.spin()

    robot.turnOff()


if __name__ == '__main__':
    listener()
