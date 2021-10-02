#! /usr/bin/env python

import rospy 
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import random

def my_publisher():
    # control part

    rospy.init_node('rrr_control_python_node')
    control_publisher = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)

    while not rospy.is_shutdown():
        
        msg = JointTrajectory()

        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ''
        msg.joint_names = ['joint1', 'joint2', 'joint3']

        point = JointTrajectoryPoint()
        j1 = 2 * (random.random() - 0.5)  # 0 - 1 -> -0.5 - 0.5
        j2 = 2 * (random.random() - 0.5)
        j3 = 2 * (random.random() - 0.5)

        point.positions = [j1, j2, j3]
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration(1)

        msg.points.append( point )

        control_publisher.publish( msg )
        rospy.loginfo( msg ) 


if __name__ == '__main__':

    my_publisher()


