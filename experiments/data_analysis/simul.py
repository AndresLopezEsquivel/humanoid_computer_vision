from kalman_filter_2 import EKF
from random import gauss
import matplotlib.pyplot as plt
import numpy as np

sigma = 0.02 # standard deviation
dt = 0.1 # sampling time

Q = np.identity(4) * 0.001
R = np.identity(2) * 0.002
kf = EKF(dt, Q, R)

k = 0.02
samples = 80

real_y = [k * i for i in range(samples)]
noised_y = [round(gauss(k * i, sigma),3) for i in range(samples)]
kf_y = []
kf_vel_y = []
y_pre = []
vy_pre = []
t = [i * dt for i in range(samples)]

i = 0

while i < len(noised_y):
    kf.predict()
    kf_data = kf.update(Z = [0, noised_y[i]])
    kf_y.append(kf_data[1][0])
    kf_vel_y.append(kf_data[3][0])
    i += 1

kf = EKF(dt, Q, R)

i = 0
N = 30 # Number of samples

while i < N:
    kf.predict()
    kf_data = kf.update(Z = [0, noised_y[i]])
    y_pre.append(kf_data[1][0])
    vy_pre.append(kf_data[3][0])
    i += 1

while i < len(noised_y):
    kf_data = kf.predict()
    y_pre.append(kf_data[1][0])
    vy_pre.append(kf_data[3][0])
    kf.x = kf_data
    i += 1

_, y_mes = plt.subplots()

y_mes.plot(t, real_y, label = 'Posición real')
y_mes.plot(t, noised_y, label = 'Posición medida')
# y.plot(t, kf_y, label = '[m] (Posición estimada)')
y_mes.set_xlabel(xlabel = '[s]')
y_mes.set_ylabel(ylabel = '[m]')
y_mes.set_title('Medición de posición')
y_mes.legend()
y_mes.grid(True)

_, y_est = plt.subplots()

y_est.plot(t, real_y, label = 'Posición real')
y_est.plot(t, kf_y, label = 'Posición estimada')
y_est.set_xlabel(xlabel = '[s]')
y_est.set_ylabel(ylabel = '[m]')
y_est.set_title('Estimación de posición')
y_est.legend()
y_est.grid(True)

_, vy_est = plt.subplots()

vy_est.plot(t, kf_vel_y)
vy_est.set_xlabel(xlabel = '[s]')
vy_est.set_ylabel(ylabel = '[m/s]')
vy_est.set_title('Estimación de velocidad')
vy_est.grid(True)

_, y_pred = plt.subplots()

y_pred.plot(t, real_y, label = 'Posición real')
y_pred.plot(t, y_pre, label = 'Predicción de posición')
y_pred.plot(t, noised_y[:N] + [None] * (samples - N), 'ro', label = 'Mediciones muestreadas', markersize = 2)
y_pred.set_xlabel(xlabel = '[s]')
y_pred.set_ylabel(ylabel = '[m]')
y_pred.set_title('Predicción de posición')
y_pred.legend()
y_pred.grid(True)

_, vy_pred = plt.subplots()

vy_pred.plot(t, kf_vel_y, label = 'Velocidad estimada')
vy_pred.plot(t, vy_pre, label = 'Predicción de velocidad')
vy_pred.set_xlabel(xlabel = '[s]')
vy_pred.set_ylabel(ylabel = '[m/s]')
vy_pred.set_title('Predicción de velocidad')
vy_pred.legend()
vy_pred.grid(True)

plt.show()
