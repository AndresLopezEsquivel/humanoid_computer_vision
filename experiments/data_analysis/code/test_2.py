from kalman_filter_2 import EKF
from random import gauss
import matplotlib.pyplot as plt
import numpy as np
import csv

sigma = 0.04 # Standard deviation

dt = 1/10
# k = 0.02, samples = 76
k = 0.02
samples = 80
y = [k * i for i in range(samples)]
t = [i * dt for i in range(samples)]


kf_y = []
kf_vel_y = []

Q = np.identity(4) * 0.1
R = np.identity(2) * 0.01
kf = EKF(dt, Q, R)

i = 0
N = 20 # Number of samples

while i < N:
    kf.predict()
    kf_data = kf.update(Z = [0, y[i]])
    kf_y.append(kf_data[1][0])
    kf_vel_y.append(kf_data[3][0])
    i += 1

while i < len(y):
    kf_data = kf.predict()
    kf_y.append(kf_data[1][0])
    kf_vel_y.append(kf_data[3][0])
    kf.x = kf_data
    i += 1

# for y_pos in y:

#     kf_data = kf.estimate(Z = [0, y_pos])
#     kf_y.append(kf_data[1][0])
#     kf_vel_y.append(kf_data[3][0])

"""
with open('/home/andreslopez/data/test8.csv', newline = '') as csv_file:
    data = [[float(row[0]),
             float(row[1]),
             float(row[2])]
             for row in csv.reader(csv_file)]

start_time = data[0][0]

data = [[row[0] - start_time,
         row[1],
         row[2]]
         for row in data]

t = [row[0] for row in data]
y = [row[2] for row in data]

for y_pos in y:
    kf_data = kf.estimate(Z = [0, y_pos])
    kf_y.append(kf_data[1][0])
    kf_vel_y.append(kf_data[3][0])
"""

fig, y_position = plt.subplots()

y_position.plot(t, y[:N] + [None] * (samples - N), 'ro', label = '[m] (Mediciones muestreadas)', markersize = 4)
y_position.plot(t, y, label = '[m] (Mediciones)')
y_position.plot(t, kf_y, label = '[m] (Con KF)')
y_position.plot(t, kf_vel_y, label = '[m/s] (Con KF)')
y_position.set_xlabel(xlabel = 'Tiempo [s]')
y_position.legend()
y_position.grid(True)

plt.show()
