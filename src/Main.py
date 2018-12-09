#!/usr/bin/env python

import time
import RobotArm
import Communication
import StringHandler

robot = RobotArm.RobotArm()

robot.init()

#U
robot.moveCartesianPosition(215.000, -180.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -180.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -130.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -130.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -130.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
#F
robot.moveCartesianPosition(215.000, -80.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -55.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -30.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -80.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, -30.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
#O
robot.moveCartesianPosition(215.000, 20.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 20.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 70.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 70.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 20.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 70.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
#P
robot.moveCartesianPosition(215.000, 120.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 120.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 170.000, 325.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 170.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 120.000, 350.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed
robot.moveCartesianPosition(215.000, 120.000, 300.000, 90.000, 180.000, 100.0) #x, y, z, a, b, speed


#Espaço de trabalho
#robot.moveJointPosition(0.000, 0.000, 0.000, 0.000, 0.000, 100.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(0.000, 0.000, 60.000, 0.000, 0.000, 100.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(0.000, 90.000, 0.000, 0.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(0.000, 90.000, -90.000, 0.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(0.000, 90.000, -90.000, 90.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(0.000, 90.000, -90.000, -90.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(0.000, 90.000, -90.000, 45.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(-150.000, 90.000, -90.000, 45.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(-150.000, 45.000, -90.000, 45.000, 0.000, 50.0) #j1, j2, j3, j5, j6, speed
#robot.moveJointPosition(0.000, 0.000, 0.000, 0.000, 0.000, 30.0) #j1, j2, j3, j5, j6, speed

#robot.moveCartesianPosition(200.000, 180.000, 450.000, 180.000, 180.000, 50.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(200.000, 180.000, 300.000, 180.000, 180.000, 50.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(200.000, 0.000, 450.000, 180.000, 180.000, 50.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(200.000, 0.000, 450.000, 0.000, 180.000, 100.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(200.000, 0.000, 350.000, 0.000, 180.000, 100.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(250.000, 0.000, 450.000, 0.000, 90.000, 20.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(250.000, 0.000, 450.000, -90.000, 90.000, 20.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(250.000, 0.000, 450.000, 0.000, 180.000, 20.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(200.000, 30.000, 450.000, 0.000, 180.000, 20.0) #x, y, z, a, b, speed
#robot.moveCartesianPosition(250.000, 0.000, 450.000, 0.000, 180.000, 20.0) #x, y, z, a, b, speed


stringHandler = StringHandler.StringHandler()
print stringHandler.getJointPositionByString(robot.readJointPosition())
print stringHandler.getCartesianPositionByString(robot.readCartesianPosition())

robot.turnOff()