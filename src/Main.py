import time
import RobotArm

robot = RobotArm.RobotArm()

robot.init()
time.sleep(3)

#robot.handOpen()
#time.sleep(3)

robot.moveToInitialPos()
time.sleep(3)

#robot.handClose()
#time.sleep(3)

robot.moveToPos()
time.sleep(3)

robot.reset()
