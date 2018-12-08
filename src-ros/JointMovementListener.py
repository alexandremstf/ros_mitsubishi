#!/usr/bin/env python

import sys
sys.path.insert(0, '/home/paulo/catkin_ws/src/ros_mitsubishi/src')

import RobotArm
robot = RobotArm.RobotArm()

import rospy
from ros_mitsubishi.msg import JointMessage

def callback(data):
    rospy.loginfo(" I heard %s", data)
    
    robot.moveJointPosition(data.j1, data.j2, data.j3, data.j5, data.j6, data.speed) #j1, j2, j3, j5, j6, speed

def listener():
    robot.init()

    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber("jointMovement", JointMessage, callback)
    rospy.spin()

    robot.turnOff()

if __name__ == '__main__':
    listener()
