#!/usr/bin/env python

import sys
sys.path.insert(0, '/home/alexandre/catkin_ws/src/ros_mitsubishi/src')

import RobotArm
robot = RobotArm.RobotArm()

import rospy
from ros_mitsubishi.msg import JointMessage

def callback(data):
    rospy.loginfo(" I heard %s", data)
    
    robot.init()
    robot.moveJointPosition(data.j1, data.j2, data.j3, data.j4, data.j5, data.speed) #j1, j2, j3, j4, j5, speed
    robot.reset()

    
def listener():
    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber("jointMovement", JointMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()