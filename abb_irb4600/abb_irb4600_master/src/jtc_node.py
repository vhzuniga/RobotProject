#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys

def perform_trajectory():
    rospy.init_node('abb_irb4600_trajectory_publisher')

    controller_name = '/arm_controller/command'
    trajectory_publisher = rospy.Publisher(controller_name, JointTrajectory, queue_size=10)

    argv = sys.argv[1:]

    abb_joints = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']

    if len(argv) != 6:
        rospy.logerr("Please provide 6 joint positions as arguments")
        return

    goal_positions = [float(arg) for arg in argv]

    rospy.loginfo("Goal Position set, let's go!")
    rospy.sleep(1)

    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = abb_joints

    point = JointTrajectoryPoint()
    point.positions = goal_positions
    point.velocities = [0.0] * 6
    point.accelerations = [0.0] * 6
    point.time_from_start = rospy.Duration(3)

    trajectory_msg.points.append(point)

    rospy.sleep(1)
    trajectory_publisher.publish(trajectory_msg)

if __name__ == '__main__':
    try:
        perform_trajectory()
    except rospy.ROSInterruptException:
        pass