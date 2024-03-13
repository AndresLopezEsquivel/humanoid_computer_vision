import csv
import matplotlib.pyplot as plt
import numpy as np
from kalman_filter_2 import EKF
from pprint import pprint

PATH = ("/home/andres/Andres/humanoid_computer_vision/experiments/data_analysis" +
"/logs/2024-02-22/test1_position_feb22.csv")

PRUEBA = 1

dt = 0.1
Q = np.identity(4) * 0.001
R = np.identity(2) * 0.03 # 0.04
kf_apriori = EKF(dt, Q, R)
kf_aposteriori = EKF(dt, Q, R)

N = 20 # Número

t = []
x_pos_meas = []
y_pos_meas = []
x_pos_apriori = []
y_pos_apriori = []
x_pos_aposteriori = []
y_pos_aposteriori = []
x_vel_aposteriori = []
y_vel_apriori = []
y_vel_aposteriori = []

with open(PATH, newline = '') as csv_file:
    for row in csv.reader(csv_file):
        t.append(float(row[0]))
        x_pos_meas.append(float(row[1]))
        y_pos_meas.append(float(row[2]))

i = 0
while i < len(x_pos_meas):
    kf_aposteriori.predict()
    kf_data = kf_aposteriori.update(Z = [x_pos_meas[i], y_pos_meas[i]])
    x_pos_aposteriori.append(kf_data[0][0])
    y_pos_aposteriori.append(kf_data[1][0])
    x_vel_aposteriori.append(kf_data[2][0])
    y_vel_aposteriori.append(kf_data[3][0])
    i += 1

# Y - position

_, y_pos = plt.subplots()

t_lim_1 = 4
t_lim_2 = 13.7

y_pos.plot(t, y_pos_meas, label = 'Mediciones')
y_pos.plot(t, y_pos_aposteriori, label = 'Estimaciones a posteriori')
y_pos.axvline(x = t_lim_1, linestyle = '--', linewidth = 1, color = 'k')
y_pos.axvline(x = t_lim_2, linestyle = '--', linewidth = 1, color = 'k')
y_pos.set_xlabel(xlabel = '[s]')
y_pos.set_ylabel(ylabel = '[m]')
y_pos.set_title(f"Posición en el eje y (prueba {PRUEBA})")

y_pos.text(x = 1.24,
y = -0.6,
s = "I",
fontsize = 20)

y_pos.text(x = 9,
y = -1.1,
s = "II",
fontsize = 20)

y_pos.text(x = 16.5,
y = -0.6,
s = "III",
fontsize = 20)

y_pos.legend()
y_pos.grid(True)

# X - position

_, x_pos = plt.subplots()

t_lim_1 = 4
t_lim_2 = 13.7

x_pos.plot(t, x_pos_meas, label = 'Mediciones')
x_pos.plot(t, x_pos_aposteriori, label = 'Estimaciones a posteriori')
x_pos.axvline(x = t_lim_1, linestyle = '--', linewidth = 1, color = 'k')
x_pos.axvline(x = t_lim_2, linestyle = '--', linewidth = 1, color = 'k')
x_pos.set_xlabel(xlabel = '[s]')
x_pos.set_ylabel(ylabel = '[m]')
x_pos.set_title(f"Posición en el eje x (prueba {PRUEBA})")

x_pos.text(x = 1.3,
y = 1.1,
s = "I",
fontsize = 20)

x_pos.text(x = 9,
y = 1.1,
s = "II",
fontsize = 20)

x_pos.text(x = 16.5,
y = 1.1,
s = "III",
fontsize = 20)

x_pos.legend()
x_pos.grid(True)

# Y - velocity

_, y_vel = plt.subplots()

t_lim_1 = 4
t_lim_2 = 13.7

y_vel.plot(t, y_vel_aposteriori, label = 'Estimaciones a posteriori')
y_vel.axvline(x = t_lim_1, linestyle = '--', linewidth = 1, color = 'k')
y_vel.axvline(x = t_lim_2, linestyle = '--', linewidth = 1, color = 'k')
y_vel.set_xlabel(xlabel = '[s]')
y_vel.set_ylabel(ylabel = '[m/s]')
y_vel.set_title(f"Velocidad en el eje y (prueba {PRUEBA})")

y_vel.text(x = 1.24,
y = -0.6,
s = "I",
fontsize = 20)

y_vel.text(x = 9,
y = -1.1,
s = "II",
fontsize = 20)

y_vel.text(x = 16.5,
y = -0.6,
s = "III",
fontsize = 20)

y_vel.legend()
y_vel.grid(True)

plt.show()
