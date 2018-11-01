#!/usr/bin/env python

import rospy
from ros_mitsubishi.msg import CartesianMessage

def callback(data):
    rospy.loginfo(" I heard %s", data)
    
def listener():

    rospy.init_node('listener', anonymous=False)

    rospy.Subscriber("cartesianMovement", CartesianMessage, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()