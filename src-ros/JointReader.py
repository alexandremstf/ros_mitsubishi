#!/usr/bin/env python
import os
path = os.getcwd() + '/src/ros_mitsubishi/src'

import sys
sys.path.insert(0, path)

import RobotArm
robot = RobotArm.RobotArm()

import StringHandler
stringHandler = StringHandler.StringHandler()

import rospy
from ros_mitsubishi.msg import JointMessage

def listener():
    robot.init()

    rospy.init_node('talker', anonymous=False)
    print stringHandler.getJointPositionByString(robot.readJointPosition())
    rospy.spin()

    robot.turnOff()

if __name__ == '__main__':
    listener()
