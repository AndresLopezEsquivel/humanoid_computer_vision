#!/usr/bin/env python3  
import rospy
import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
import tf2_geometry_msgs
# added 21-jun-2023
import csv
import time
# added 21-sep-2023
import numpy as np
from kalman_filter import EKF

# http://wiki.ros.org/tf2/Tutorials/Writing%20a%20tf2%20listener%20%28Python%29
# https://answers.ros.org/question/335584/how-to-transpose-and-rotate-frames-and-get-new-coordinates/

def write_pose_and_time(x_pose, y_pose, file_path):

    with open(file_path, 'a', newline = '') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow([time.time(), x_pose, y_pose])

if __name__ == '__main__':
    
    rospy.init_node('ball_pose')
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('left_foot_plane_link', 'new_camera_optical', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            # rate.sleep()
            continue

        p_new_camera = tf2_geometry_msgs.tf2_geometry_msgs.PoseStamped()
        p_new_camera.header.frame_id = 'new_camera_optical'
        p_new_camera.pose.position.x = 0.5
        
        p_left_foot_plane  = tf2_geometry_msgs.do_transform_pose(p_new_camera, trans)

        try:
            trans2 = tfBuffer.lookup_transform('left_foot_plane_link', 'camera_optical', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            # rate.sleep()
            continue

        # print('p_new_camera to left_foot_plane: ', p_left_foot_plane.pose.position.x, p_left_foot_plane.pose.position.y, p_left_foot_plane.pose.position.z)
        # print('origin of camera_optical to left_foot_plane: ', trans2.transform.translation.x, trans2.transform.translation.y, trans2.transform.translation.z)

        Qx = float(p_left_foot_plane.pose.position.x)
        Qy = float(p_left_foot_plane.pose.position.y)
        Qz = float(p_left_foot_plane.pose.position.z)

        Px =  float(trans2.transform.translation.x)
        Py =  float(trans2.transform.translation.y)
        Pz =  float(trans2.transform.translation.z)

        # print(Px, Py, Pz)
        
        PQ = [Px - Qx, Py - Qy, Pz - Qz]
        """
        k = (-1 * Pz)/PQ[2]

        ball_x = Px + k * PQ[0]
        ball_y = Py + k * PQ[1]
        ball_z = 0
        print('=' * 10)
        print('without kalman filter: ',ball_x,ball_y,ball_z)
        """
        
        # ball radius
        r = 0.08 / 2
        k = (r - Pz) / PQ[2]
        ball_x = Px + k * PQ[0]
        ball_y = Py + k * PQ[1]
        ball_z = r

        ball_x = round(ball_x, 2)
        ball_y = round(ball_y, 2)
        ball_z = round(ball_z, 2)
        
        
        # Applying Kalman Filter and considering constant velocity

        Q = np.identity(4) * 0.1
        R = np.identity(2) * 0.01
        kf = EKF(0.1, Q, R)
        kf_pos_x, kf_pos_y, _, _ = kf.estimate(Z = [ball_x, ball_y])
        print(10 * '===')
        print('without kalman filter: ', 'x: ', ball_x, 'y: ', ball_y, 'z: ', ball_z)
        print('with kalman filter:', kf_pos_x, kf_pos_y)
        print(10 * '===')

        # write_pose_and_time(ball_x, ball_y, './ball_pose_data_2023-07-04-184552.csv')

