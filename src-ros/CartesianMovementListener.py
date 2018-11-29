#!/usr/bin/env python

import sys
sys.path.insert(0, '/home/alexandre/catkin_ws/src/ros_mitsubishi/src')

import RobotArm
robot = RobotArm.RobotArm()

import rospy
from ros_mitsubishi.msg import CartesianMessage

def callback(data):
    rospy.loginfo(" I heard %s", data)
    
    print "antes"
    print data
    robot.moveCartesianPosition(data.x, data.y, data.z, data.a, data.b, data.speed) #x, y, z, a, b, speed
    print data

def listener():
    robot.init()

    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber("cartesianMovement", CartesianMessage, callback)
    rospy.spin()

    robot.turnOff()


if __name__ == '__main__':
    listener()