#!/usr/bin/env python

import time
import RobotArm
import Communication
import StringHandler

robot = RobotArm.RobotArm()

robot.init()

robot.moveJointPosition(0.000, 0.000, 0.000, 0.000, 0.000, 80.0) #j1, j2, j3, j5, j6, speed
robot.moveJointPosition(10.000, 10.000, 10.000, 0.000, 0.000, 80.0) #j1, j2, j3, j5, j6, speed
robot.moveJointPosition(20.000, 20.000, 20.000, 0.000, 0.000, 80.0) #j1, j2, j3, j5, j6, speed
robot.moveJointPosition(30.000, 30.000, 30.000, 0.000, 0.000, 60.0) #j1, j2, j3, j5, j6, speed
robot.moveJointPosition(40.000, 40.000, 40.000, 0.000, 0.000, 60.0) #j1, j2, j3, j5, j6, speed
robot.moveJointPosition(0.000, 0.000, 0.000, 0.000, 0.000, 60.0) #j1, j2, j3, j5, j6, speed

#robot.moveCartesianPosition(250.000, 0.000, 450.000, 0.000, 180.000, 200.0) #x, y, z, a, b, speed

#stringHandler = StringHandler.StringHandler()
#print "oi"
#print stringHandler.getJointPositionByString(robot.readJointPosition())
#print stringHandler.getCartesianPositionByString(robot.readCartesianPosition())


robot.turnOff()