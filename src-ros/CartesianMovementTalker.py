#!/usr/bin/env python

import rospy
from ros_mitsubishi.msg import CartesianMessage

def talker():
    pub = rospy.Publisher('cartesianMovement', CartesianMessage, queue_size=10)
    
    rospy.init_node('talker', anonymous=True)
    
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        message = CartesianMessage()

        message.x = 10
        message.y = 20
        message.z = 30
        message.a = 40
        message.b = 50

        rospy.loginfo(message)
        
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#rostopic pub /cartesianMovement ros_mitsubishi/CartesianMessage "{x: 10.0, y: 20.0, z: 30.0, a: 20.0, b: 10.0}" -r 2