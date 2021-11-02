#!/usr/bin/env python2.7

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from ti_mmwave_rospkg.msg import RadarScan
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion


class CommandToJointStateX:
    def __init__(self):
        self.joint_name = "base_to_pipe_x"
        self.joint_state = JointState()
        self.joint_state.name.append(self.joint_name)
        self.joint_state.position.append(0.0)
        self.joint_state.velocity.append(0.0)
        self.joint_pub = rospy.Publisher("joint_states", JointState, queue_size=1)
        self.command_sub = rospy.Subscriber("/imu_iphone", Imu, self.command_callback, queue_size=1)



    def command_callback(self, msg):
        orientation_list = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
        self.joint_state.position[0] = roll
        self.joint_state.header.stamp = rospy.Time.now()
        self.joint_pub.publish(self.joint_state)

class CommandToJointStateY:
    def __init__(self):
        self.joint_name = "base_to_pipe_y"
        self.joint_state = JointState()
        self.joint_state.name.append(self.joint_name)
        self.joint_state.position.append(0.0)
        self.joint_state.velocity.append(0.0)
        self.joint_pub = rospy.Publisher("joint_states", JointState, queue_size=1)
        self.command_sub = rospy.Subscriber("/imu_iphone", Imu,
                                            self.command_callback, queue_size=1)

    def command_callback(self, msg):
        orientation_list = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
        self.joint_state.position[0] = pitch
        self.joint_state.header.stamp = rospy.Time.now()
        self.joint_pub.publish(self.joint_state)

if __name__ == '__main__':
    rospy.init_node('command_to_joint_state')
    command_to_joint_stateX = CommandToJointStateX()
    command_to_joint_stateY = CommandToJointStateY()
    rospy.spin()



