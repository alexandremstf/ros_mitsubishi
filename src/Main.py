import time
import RobotArm
import Communication

robot = RobotArm.RobotArm()

robot.init()
time.sleep(2)

robot.moveJointPosition('(0.000, 0.000, 0.000, 0.000, 0.000, 0.000)', '80.0')
time.sleep(5)
robot.moveCartesianPosition('(250.000, 0.000, 450.000, 0.000, 180.000, 0.000)(6,0)', '200.0')
time.sleep(5)

print robot.readJointPosition()
print robot.readCartesianPosition()

robot.reset()

#QoKJ1;0.00;J2;21.19;J3;72.78;J4;****;J5;86.03;J6;0.00;;****,****;50;0.00;00000000
#QoKX;250.00;Y;0.00;Z;450.00;A;0.00;B;180.00;;6,0;50;0.00;00000000
