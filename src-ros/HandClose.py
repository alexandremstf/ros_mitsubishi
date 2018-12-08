#!/usr/bin/env python
import os
path = os.getcwd() + '/src/ros_mitsubishi/src'

import sys
sys.path.insert(0, path)

import RobotArm
robot = RobotArm.RobotArm()

import rospy

def listener():
    robot.init()

    rospy.init_node('talker', anonymous=False)
    robot.handClose()

    robot.turnOff()

if __name__ == '__main__':
    listener()
