#!/usr/bin/env python

import time
import RobotArm
import Communication
import StringHandler

robot = RobotArm.RobotArm()

robot.init()
time.sleep(2)

robot.moveJointPosition(0.000, 0.000, 0.000, 0.000, 0.000, 80.0) #j1, j2, j3, j4, j5, speed

robot.moveCartesianPosition(250.000, 0.000, 450.000, 0.000, 180.000, 200.0) #x, y, z, a, b, speed

stringHandler = StringHandler.StringHandler()

print stringHandler.getCartesianPositionByString(robot.readCartesianPosition())
print stringHandler.getJointPositionByString(robot.readJointPosition())

robot.reset()

