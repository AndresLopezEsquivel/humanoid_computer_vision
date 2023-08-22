import numpy as np
import cv2
import matplotlib.pyplot as plt

DIM = (953, 720)

K = np.array(
    [
        [407.0259762535615, 0.0, 488.89663712932474],
        [0.0, 409.25366832487896, 388.1998354574297],
        [0.0, 0.0, 1.0],
    ]
)

D = np.array(
    [
        [-0.04485892302426824],
        [0.0787884305594057],
        [-0.08374236678783106],
        [0.027626067632899026],
    ]
)

CAMERA_MATRIX = np.array([[531.16719459, 0,686.90394518], [0, 532.5711697, 364.00099154], [0, 0, 1]], dtype=np.float32)

DIST = np.array([[-0.31429497,  0.09157624, -0.00064995,  0.00094649, -0.01083083]], dtype=np.float32)

newcameramtx = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(
    K, D, DIM, None, balance=1)

x_data = []

y_data = []

for i in range(0, 720):

    point = np.array([[[1280, i]]]).astype(np.float32)

    # undst_point = cv2.fisheye.undistortPoints(point, K, D, None, newcameramtx)

    undst_point = cv2.undistortPoints(point, CAMERA_MATRIX, None)

    x = undst_point[0][0][0]

    y = undst_point[0][0][1]

    x_data.append(x)

    y_data.append(y)
"""
for i in range(0, 954):

    point = np.array([[[i, 0]]]).astype(np.float32)

    undst_point = cv2.fisheye.undistortPoints(point, K, D, None, newcameramtx)

    x = undst_point[0][0][0]

    y = undst_point[0][0][1]

    x_data.append(x)

    y_data.append(y)

for i in range(0, 721):

    point = np.array([[[953, i]]]).astype(np.float32)

    undst_point = cv2.fisheye.undistortPoints(point, K, D, None, newcameramtx)

    x = undst_point[0][0][0]

    y = undst_point[0][0][1]

    x_data.append(x)

    y_data.append(y)

for i in range(0, 954):

    point = np.array([[[i, 720]]]).astype(np.float32)

    undst_point = cv2.fisheye.undistortPoints(point, K, D, None, newcameramtx)

    x = undst_point[0][0][0]

    y = undst_point[0][0][1]

    x_data.append(x)

    y_data.append(y)
"""

plt.plot(x_data, y_data)

plt.show()