#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from ti_mmwave_rospkg.msg import RadarScan


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s')
    print(data)

def listener():

    rospy.init_node('listener', anonymous=True)
    
    rospy.Subscriber('/ti_mmwave/radar_scan', RadarScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
