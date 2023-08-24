import cv2
import glob
import numpy as np

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

def get_undistorted_centroid_px(distorted_centroid, camera_matrix, distortion_coef):

    fx = camera_matrix[0][0]
    fy = camera_matrix[1][1]
    cx = camera_matrix[0][2]
    cy = camera_matrix[1][2]

    centroid = np.array([distorted_centroid[0],
                         distorted_centroid[1]],
                         dtype = np.float32)
    
    undistorted_point = cv2.undistortPoints(centroid,
                                            camera_matrix,
                                            distortion_coef)
    
    x = int(undistorted_point[0][0][0] * fx + cx)

    y = int(undistorted_point[0][0][1] * fy + cy)

    return (x, y)

camera_matrix = np.array([[531.16719459, 0,686.90394518],
                          [0, 532.5711697, 364.00099154],
                          [0, 0, 1]],
                          dtype = np.float32)

dist = np.array([[-0.31429497,  0.09157624, -0.00064995,  0.00094649, -0.01083083]],
                dtype=np.float32)

cap = cv2.VideoCapture(2)

while True:

    _, frame = cap.read()

    distorted_image = frame

        
    # Getting color segmentation

    hsv_lower_limit = np.array([40, 100, 50])

    hsv_upper_limit = np.array([80, 255, 255])

    binary_image = get_color_segmentation(bgr_image = distorted_image,
                                          hsv_lower_limit = hsv_lower_limit,
                                          hsv_upper_limit = hsv_upper_limit)
    
    distorted_centroid = get_centroid_px_from_binary_img(binary_img = binary_image)

    distorted_image = cv2.circle(distorted_image,
                                 distorted_centroid,
                                 radius = 5,
                                 color = (0, 0, 255),
                                 thickness = -1)

    """
    binary_image = cv2.circle(binary_image,
                              (distorted_centroid[0],
                               distorted_centroid[1]),
                               radius = 2,
                               color=(0, 0, 255),
                               thickness=-1)
    """
    # Drawing centroid to distorted image
    """
    bgr_image = cv2.circle(distorted_image,
                           (distorted_centroid[0],
                            distorted_centroid[1]),
                            radius = 5,
                            color=(0, 0, 255),
                            thickness=-1)
    """
    # Getting undistorted image

    undistorted_img = get_undistorted_image(distorted_image = distorted_image,
                                            camera_matrix = camera_matrix,
                                            distortion_coef = dist)
    
    undistorted_centroid = get_undistorted_centroid_px(distorted_centroid = distorted_centroid,
                                                       camera_matrix = camera_matrix,
                                                       distortion_coef = dist)
    
    
    undistorted_img = cv2.circle(undistorted_img,
                                 (undistorted_centroid[0],
                                  undistorted_centroid[1]),
                                  radius = 5,
                                  color = (0, 0, 255),
                                  thickness = -1)
    
    print(distorted_centroid, undistorted_centroid)
    
    cv2.imshow('binary_image', binary_image)

    cv2.imshow('distorted_image', distorted_image)

    cv2.imshow('undistorted_image', undistorted_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

         break