import numpy as np
import cv2
import matplotlib.pyplot as plt
import csv

CAMERA_MATRIX = np.array([[531.16719459, 0,686.90394518], [0, 532.5711697, 364.00099154], [0, 0, 1]], dtype=np.float32)

DIST = np.array([[-0.31429497,  0.09157624, -0.00064995,  0.00094649, -0.01083083]], dtype=np.float32)

def write_row_to_csv(row, file_path):

    with open(file_path, 'a', newline = '') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(row)

def get_undistorted_point_px(distorted_point, camera_matrix, distortion_coef, P = None):

    fx = camera_matrix[0][0]
    fy = camera_matrix[1][1]
    cx = camera_matrix[0][2]
    cy = camera_matrix[1][2]

    centroid = np.array([distorted_point[0],
                         distorted_point[1]],
                         dtype = np.float32)
    
    undistorted_point = cv2.undistortPoints(centroid,
                                            camera_matrix,
                                            distortion_coef,
                                            P = None)
    
    x = int(undistorted_point[0][0][0] * fx + cx)

    y = int(undistorted_point[0][0][1] * fy + cy)

    return (x, y)

# == 1 ==

x_data = []

y_data = []

dist_coef = None

for i in range(0, 720):

    x, y = get_undistorted_point_px((1280,i), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

for i in range(1280,-1,-1):

    x, y = get_undistorted_point_px((i,720), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

for i in range(720,-1,-1):

    x, y = get_undistorted_point_px((0,i), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

for i in range(0,1281):

    x, y = get_undistorted_point_px((i,0), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

plt.plot(x_data, y_data)

# == 2 ==

x_data = []

y_data = []

dist_coef = DIST

for i in range(0, 720):

    x, y = get_undistorted_point_px((640,i), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

plt.plot(x_data, y_data)

# == 3 ==

x_data = []

y_data = []

dist_coef = DIST

for i in range(0, 1281):

    x, y = get_undistorted_point_px((i,360), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

plt.plot(x_data, y_data)

# == 4 ==

x_data = []

y_data = []

dist_coef = DIST

for i in range(0, 720):

    x, y = get_undistorted_point_px((1280,i), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

for i in range(1280,-1,-1):

    x, y = get_undistorted_point_px((i,720), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

for i in range(720,-1,-1):

    x, y = get_undistorted_point_px((0,i), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)

for i in range(0,1281):

    x, y = get_undistorted_point_px((i,0), CAMERA_MATRIX, dist_coef)

    x_data.append(x)

    y_data.append(y)     

plt.plot(x_data, y_data)

plt.show()