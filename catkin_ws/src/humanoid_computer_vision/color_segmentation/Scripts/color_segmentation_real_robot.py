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
from experiments.srv import example, exampleResponse, exampleRequest

CAMERA_MATRIX = np.array([[531.16719459, 0,686.90394518], [0, 532.5711697, 364.00099154], [0, 0, 1]], dtype=np.float32)

DIST = np.array([[-0.31429497,  0.09157624, -0.00064995,  0.00094649, -0.01083083]], dtype=np.float32)

def get_color_segmentation(bgr_image, hsv_lower_limit, hsv_upper_limit):

    img_hsv = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    img_bin = cv2.inRange(img_hsv, hsv_lower_limit, hsv_upper_limit)

    # Erode and then dilate

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

    img_without_noise = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)

    return img_without_noise    

def get_centroid_px_from_binary_img(binary_img):

    nonzero_elements = cv2.findNonZero(binary_img)

    centroid = cv2.mean(nonzero_elements)

    x = int(centroid[0])

    y = int(centroid[1])

    return (x,y)

def get_undistorted_image(distorted_image, camera_matrix, distortion_coef):

    """
    h,  w = distorted_image.shape[:2]

    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix,
                                                      distortion_coef,
                                                      (w,h),
                                                      1,
                                                      (w,h))

    dst = cv2.undistort(distorted_image,
                        camera_matrix,
                        distortion_coef,
                        None,
                        newcameramtx)
    """
    # x, y, w, h = roi

    # dst = dst[y:y+h, x:x+w]

    dst = cv2.undistort(distorted_image, camera_matrix, distortion_coef, None)

    return dst

def get_undistorted_point_px(distorted_point, camera_matrix, distortion_coef):

    fx = camera_matrix[0][0]
    fy = camera_matrix[1][1]
    cx = camera_matrix[0][2]
    cy = camera_matrix[1][2]

    centroid = np.array([distorted_point[0],
                         distorted_point[1]],
                         dtype = np.float32)
    
    undistorted_point = cv2.undistortPoints(centroid,
                                            camera_matrix,
                                            distortion_coef)
    
    x = int(undistorted_point[0][0][0] * fx + cx)

    y = int(undistorted_point[0][0][1] * fy + cy)

    return (x, y)

def get_undistorted_px_by_service(distorted_point):

  serv_name = 'experimental_service'
  rospy.wait_for_service(serv_name)
  try:
    undistort_px = rospy.ServiceProxy(name = serv_name,
                                      service_class = example)

    req = exampleRequest()
    req.x_dist = distorted_point[0]
    req.y_dist = distorted_point[1]
    res = undistort_px(req)    
    print('x_dist: ', res.x_undis)
    print('y_dist: ', res.y_undis)

    return (int(res.x_undis), int(res.y_undis))

  except rospy.ServiceException as e:
    print("Service call failed: ", e)

def get_roll_pitch_yaw(centroid_x,
                       centroid_y,
                       img_x_center,
                       img_y_center,
                       width_resolution,
                       height_resolution,
                       hfov_rad,
                       vfov_rad):
  # https://themetalmuncher.github.io/fov-calc/

  # hfov = 150 degrees, vfov = 130 degrees

  k_hfov = hfov_rad / width_resolution

  k_vfov = vfov_rad / height_resolution

  return [0, # roll
          (centroid_y - img_y_center) * k_vfov, # pitch
          (img_x_center - centroid_x) * k_hfov] # yaw

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

def camera_callback():

    rospy.init_node('color_segmentation')

    rate = rospy.Rate(10)

    cap = cv2.VideoCapture(0)

    while not rospy.is_shutdown():

      _, frame = cap.read()

      distorted_image = frame

      # Getting color segmentation

      hsv_lower_limit = np.array([40, 100, 50])

      hsv_upper_limit = np.array([80, 255, 255])

      binary_image = get_color_segmentation(bgr_image = distorted_image,
                                          hsv_lower_limit = hsv_lower_limit,
                                          hsv_upper_limit = hsv_upper_limit)
    
      distorted_centroid = get_centroid_px_from_binary_img(binary_img = binary_image)

      x_distorted, y_distorted = distorted_centroid
      
      # Getting undistorted image

      undistorted_img = get_undistorted_image(distorted_image = distorted_image,
                                              camera_matrix = CAMERA_MATRIX,
                                              distortion_coef = DIST)
      """
      undistorted_centroid = get_undistorted_point_px(distorted_point = distorted_centroid,
                                                      camera_matrix = CAMERA_MATRIX,
                                                      distortion_coef = DIST)
      """ 
      
      undistorted_centroid = get_undistorted_px_by_service(distorted_point = distorted_centroid)
      
      x_undistorted, y_undistorted = undistorted_centroid
    
      undistorted_img = cv2.circle(undistorted_img,
                                  (undistorted_centroid[0],
                                  undistorted_centroid[1]),
                                  radius = 5,
                                  color = (0, 0, 255),
                                  thickness = -1)
      
      # == TF ==
      # hfov_rad = 2.9671 (170), vfov_rad = 2.8449 (163)
      # hfov_rad = 2.6180 (150), vfov_rad = 2.2689 (130)
      # hfov_rad = 2.4435 (140), vfov_rad = 2.0071 (140)
      """
      roll, pitch, yaw = get_roll_pitch_yaw(centroid_x = x_undistorted,
                                            centroid_y = y_undistorted,
                                            width_resolution = 1280,
                                            height_resolution = 894,
                                            hfov_rad = 2.6180, 
                                            vfov_rad = 2.2689)
      """

      angles = get_roll_pitch_yaw(centroid_x = x_undistorted,
                                  centroid_y = y_undistorted,
                                  img_x_center = 640,
                                  img_y_center = 870/2, # 870/2
                                  width_resolution = 1280,
                                  height_resolution = 870, # 870
                                  hfov_rad = 2.6180,
                                  vfov_rad = 2.2689)
      
      roll, pitch, yaw = angles

      q = get_quaternion_from_euler(roll = roll,
                                    pitch = pitch,
                                    yaw = yaw)

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

      # == INFO TO PRINT ==
    
      print('distorted_centroid: ',
            distorted_centroid,
            ' undistorted_centroid: ',
            undistorted_centroid,
            'angles RPY: ',
            angles)
    
      cv2.imshow('binary_image', binary_image)

      cv2.imshow('distorted_image', distorted_image)

      cv2.imshow('undistorted_image', undistorted_img)

      rate.sleep()

      if cv2.waitKey(1) & 0xFF == ord('q'):

         break

      if rospy.is_shutdown():

         cap.release()   

      cv2.waitKey(1)
      


if __name__ == '__main__':

    node_name = 'color_segmentation'

    topic_name = '/cv_camera/image_raw'

    try:
    
      camera_callback()

    except rospy.ROSInterruptException:
       
       pass

    # rospy.Subscriber(name = topic_name, data_class = Image, callback = camera_callback)

    # rospy.spin()