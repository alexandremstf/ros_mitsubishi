import time
import RobotArm

robot = RobotArm.RobotArm()

robot.init()
time.sleep(2)

robot.moveToInitialPos()
time.sleep(5)

robot.moveToPos()
time.sleep(10)

robot.reset()
