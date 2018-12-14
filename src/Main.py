#!/usr/bin/env python

import time
import RobotArm
import Communication
import StringHandler

robot = RobotArm.RobotArm()

robot.init()

#U
#robot.moveCartesianPosition(215.000, -180.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(215.000, -180.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(215.000, -130.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(215.000, -130.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(215.000, -130.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed

#E
robot.moveCartesianPosition(215.000, -80.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -30.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -30.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -30.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed

#M
robot.moveCartesianPosition(215.000, 20.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 20.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 45.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 70.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 70.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed

stringHandler = StringHandler.StringHandler()
print stringHandler.getJointPositionByString(robot.readJointPosition())
print stringHandler.getCartesianPositionByString(robot.readCartesianPosition())

robot.turnOff()