#!/usr/bin/env python3

import cv2
import numpy as np
import rospy
import tf2_ros
import geometry_msgs.msg
import math
import tf2_msgs.msg
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def get_roll_pitch_yaw(centroid_x, centroid_y, img_x_center, img_y_center):

    horizontal_dif = abs(img_x_center - centroid_x)

    vertical_dif = abs(img_y_center - centroid_y)

    yaw_sign = -1 if centroid_x > img_x_center else 1

    pitch_sign = +1 if centroid_y > img_y_center else -1

    yaw = yaw_sign * horizontal_dif * (1.3963/640)

    pitch = pitch_sign * vertical_dif * (1.1345/480)

    return [0, pitch, yaw]

def get_quaternion_from_euler(roll, pitch, yaw):
  # https://computergraphics.stackexchange.com/questions/8195/how-to-convert-euler-angles-to-quaternions-and-get-the-same-euler-angles-back-fr
  """
  Convert an Euler angle to a quaternion.
   
  Input
    :param roll: The roll (rotation around x-axis) angle in radians.
    :param pitch: The pitch (rotation around y-axis) angle in radians.
    :param yaw: The yaw (rotation around z-axis) angle in radians.
 
  Output
    :return qx, qy, qz, qw: The orientation in quaternion [x,y,z,w] format
  """
  qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
  qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
  qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
  qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
 
  return [qx, qy, qz, qw]

def camera_callback(data):

    bridge = CvBridge()

    # 480 x 640

    frame = bridge.imgmsg_to_cv2(data)

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit = np.array([85, 50, 50])

    upper_limit = np.array([120, 255, 255])

    img_bin = cv2.inRange(img_hsv, lower_limit, upper_limit)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
	
    # Erode and then dilate

    img_without_noise = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)
	
    # Find nonzero elements
	
    nonzero_elements = cv2.findNonZero(img_without_noise)
	
    # Find centroid
	
    centroid = cv2.mean(nonzero_elements)

    distorted_centroid = np.array([[centroid[0],centroid[1]]],dtype=np.float32)

    x = int(distorted_centroid[0][0])

    y = int(distorted_centroid[0][1])

    img_bin = cv2.circle(img_bin, (x,y), radius=2, color=(0, 0, 255), thickness=-1)

    # print(x,y)

    cv2.imshow('Camera', frame)

    cv2.imshow('hsv', img_hsv)

    cv2.imshow('bin', img_bin)    

    # == TF ==

    roll, pitch, yaw = get_roll_pitch_yaw(centroid_x = x, centroid_y = y, img_x_center = 320, img_y_center = 240)

    q = get_quaternion_from_euler(roll = roll, pitch = pitch, yaw = yaw)

    print('roll, pitch, yaw', roll, pitch, yaw)

    print('qx, qy, qz, qw', q)

    # print(frame.shape)

    pub_tf = rospy.Publisher("/tf", tf2_msgs.msg.TFMessage, queue_size=1)

    # rospy.sleep(0.1)

    t = geometry_msgs.msg.TransformStamped()
    t.header.frame_id = "camera_optical"
    t.header.stamp = rospy.Time.now()
    t.child_frame_id = "new_camera_optical"
    t.transform.translation.x = 0.0
    t.transform.translation.y = 0.0
    t.transform.translation.z = 0.0

    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    tfm = tf2_msgs.msg.TFMessage([t])
    pub_tf.publish(tfm)

    cv2.waitKey(1)



if __name__ == '__main__':

    node_name = 'color_segmentation'

    topic_name = '/hardware/camera/image'

    rospy.init_node(node_name)

    rospy.Subscriber(name = topic_name, data_class = Image, callback = camera_callback)

    rospy.spin()