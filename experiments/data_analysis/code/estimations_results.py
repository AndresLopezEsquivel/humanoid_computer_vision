import csv
import matplotlib.pyplot as plt
import numpy as np
from kalman_filter_2 import EKF
from pprint import pprint

TEST = {
    # === TEST 1 ===
    "1" : {
        "PATH": ("/home/andres/Andres/humanoid_computer_vision/experiments/data_analysis" +
"/logs/2024-02-22/test1_position_feb22.csv"),
        "N" : 25,
        "region" : {
            "min_index" : 40,
            "max_index" : 150
        },

        "y_pos" : {
            "t_lim_1" : 4,
            "t_lim_2" : 13.7,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : -0.6
            },
            "region_2" : {
                "text" : "II",
                "x" : 9,
                "y" : -1.1
            },
            "region_3" : {
                "text" : "III",
                "x" : 16.5,
                "y" : -0.6
            }
        },

        "x_pos" : {
            "t_lim_1" : 4,
            "t_lim_2" : 13.7,
            "region_1" : {
                "text" : "I",
                "x" : 1.3,
                "y" : 1.1
            },
            "region_2" : {
                "text" : "II",
                "x" : 9,
                "y" : 1.1
            },
            "region_3" : {
                "text" : "III",
                "x" : 16.5,
                "y" : 1.1
            }
        },

        "y_vel" : {
            "t_lim_1" : 4,
            "t_lim_2" : 13.7,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : 0.05
            },
            "region_2" : {
                "text" : "II",
                "x" : 9,
                "y" : 0.05
            },
            "region_3" : {
                "text" : "III",
                "x" : 16.5,
                "y" : 0.05
            }
        },

        "x_vel" : {
            "t_lim_1" : 4,
            "t_lim_2" : 13.7,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : 0.05
            },
            "region_2" : {
                "text" : "II",
                "x" : 9,
                "y" : 0.05
            },
            "region_3" : {
                "text" : "III",
                "x" : 16.5,
                "y" : 0.05
            }
        }
    },

    # === TEST 2 ===
    "2" : {
        "PATH": ("/home/andres/Andres/humanoid_computer_vision/experiments/data_analysis" +
"/logs/2024-02-22/test2_position_feb22.csv"),
        "N" : 30,
        "region" : {
            "min_index" : 60,
            "max_index" : 146
        },

        "y_pos" : {
            "t_lim_1" : 5.8,
            "t_lim_2" : 14.5,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : -0.6
            },
            "region_2" : {
                "text" : "II",
                "x" : 9,
                "y" : -1.1
            },
            "region_3" : {
                "text" : "III",
                "x" : 16.5,
                "y" : -0.6
            }
        },

        "x_pos" : {
            "t_lim_1" : 5.8,
            "t_lim_2" : 14.5,
            "region_1" : {
                "text" : "I",
                "x" : 1.5,
                "y" : 0.4
            },
            "region_2" : {
                "text" : "II",
                "x" : 8.3,
                "y" : 0.4
            },
            "region_3" : {
                "text" : "III",
                "x" : 16.2,
                "y" : 0.4
            }
        },

        "y_vel" : {
            "t_lim_1" : 5.8,
            "t_lim_2" : 14.5,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : 0.05
            },
            "region_2" : {
                "text" : "II",
                "x" : 9,
                "y" : 0.05
            },
            "region_3" : {
                "text" : "III",
                "x" : 16.5,
                "y" : 0.05
            }
        },

        "x_vel" : {
            "t_lim_1" : 5.8,
            "t_lim_2" : 14.5,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : 0.03
            },
            "region_2" : {
                "text" : "II",
                "x" : 9,
                "y" : 0.03
            },
            "region_3" : {
                "text" : "III",
                "x" : 16.5,
                "y" : 0.03
            }
        }
    },

    # === TEST 3 ===

    "3" : {
        "PATH": ("/home/andres/Andres/humanoid_computer_vision/experiments/data_analysis" +
"/logs/2024-02-22/test3_position_feb22.csv"),
        "N" : 12,
        "region" : {
            "min_index" : 19,
            "max_index" : 44
        },

        "y_pos" : {
            "t_lim_1" : 1.8,
            "t_lim_2" : 4.6,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : -0.6
            },
            "region_2" : {
                "text" : "II",
                "x" : 3,
                "y" : -0.6
            },
            "region_3" : {
                "text" : "III",
                "x" : 5.5,
                "y" : -0.6
            }
        },

        "x_pos" : {
            "t_lim_1" : 1.8,
            "t_lim_2" : 4.6,
            "region_1" : {
                "text" : "I",
                "x" : 1.3,
                "y" : 1.1
            },
            "region_2" : {
                "text" : "II",
                "x" : 2.8,
                "y" : 0.4
            },
            "region_3" : {
                "text" : "III",
                "x" : 5.5,
                "y" : 1.1
            }
        },

        "y_vel" : {
            "t_lim_1" : 1.8,
            "t_lim_2" : 4.6,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : 0.05
            },
            "region_2" : {
                "text" : "II",
                "x" : 3.2,
                "y" : 0.05
            },
            "region_3" : {
                "text" : "III",
                "x" : 5.5,
                "y" : 0.05
            }
        },

        "x_vel" : {
            "t_lim_1" : 1.8,
            "t_lim_2" : 4.6,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : 0.05
            },
            "region_2" : {
                "text" : "II",
                "x" : 3.2,
                "y" : 0.05
            },
            "region_3" : {
                "text" : "III",
                "x" : 5.5,
                "y" : 0.05
            }
        }
    },

    # === TEST 4 ===

    "4" : {
        "PATH": ("/home/andres/Andres/humanoid_computer_vision/experiments/data_analysis" +
"/logs/2024-02-22/test4_position_feb22.csv"),
        "N" : 12,
        "region" : {
            "min_index" : 14,
            "max_index" : 41
        },

        "y_pos" : {
            "t_lim_1" : 1.4,
            "t_lim_2" : 4,
            "region_1" : {
                "text" : "I",
                "x" : 0.5,
                "y" : -1.5
            },
            "region_2" : {
                "text" : "II",
                "x" : 3,
                "y" : -1.5
            },
            "region_3" : {
                "text" : "III",
                "x" : 5.3,
                "y" : -1.5
            }
        },

        "x_pos" : {
            "t_lim_1" : 1.4,
            "t_lim_2" : 4,
            "region_1" : {
                "text" : "I",
                "x" : 0.5,
                "y" : 0.85
            },
            "region_2" : {
                "text" : "II",
                "x" : 3,
                "y" : 0.85
            },
            "region_3" : {
                "text" : "III",
                "x" : 5.5,
                "y" : 0.85
            }
        },

        "y_vel" : {
            "t_lim_1" : 1.4,
            "t_lim_2" : 4,
            "region_1" : {
                "text" : "I",
                "x" : 1.15,
                "y" : 0.05
            },
            "region_2" : {
                "text" : "II",
                "x" : 3.1,
                "y" : 0.05
            },
            "region_3" : {
                "text" : "III",
                "x" : 5.4,
                "y" : 0.05
            }
        },

        "x_vel" : {
            "t_lim_1" : 1.4,
            "t_lim_2" : 4,
            "region_1" : {
                "text" : "I",
                "x" : 1.24,
                "y" : 0.05
            },
            "region_2" : {
                "text" : "II",
                "x" : 3.2,
                "y" : 0.05
            },
            "region_3" : {
                "text" : "III",
                "x" : 5.5,
                "y" : 0.05
            }
        }
    }
}

PRUEBA = "4"
PATH = TEST[PRUEBA]["PATH"]

dt = 0.1
Q = np.identity(4) * 0.001
R = np.identity(2) * 0.005 # 0.04
kf_apriori = EKF(dt, Q, R)
kf_aposteriori = EKF(dt, Q, R)

N = TEST[PRUEBA]["N"] # Número de muestras

t = []
x_pos_meas = []
y_pos_meas = []
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

selected_y_pos_meas = y_pos_meas[TEST[PRUEBA]["region"]["min_index"]:TEST[PRUEBA]["region"]["max_index"]]
selected_y_vel_aposteriori = y_vel_aposteriori[TEST[PRUEBA]["region"]["min_index"]:TEST[PRUEBA]["region"]["max_index"]]
selected_t = t[TEST[PRUEBA]["region"]["min_index"]:TEST[PRUEBA]["region"]["max_index"]]
selected_t0 = selected_t[0]
selected_t = [t - selected_t0 for t in selected_t]
i = 0

while i <= N:
    kf_apriori.predict()
    kf_data = kf_apriori.update(Z = [0, selected_y_pos_meas[i]])
    y_pos_apriori.append(kf_data[1][0])
    y_vel_apriori.append(kf_data[3][0])
    i += 1

while i < len(selected_y_pos_meas):
    kf_data = kf_apriori.predict()
    y_pos_apriori.append(kf_data[1][0])
    y_vel_apriori.append(kf_data[3][0])
    kf_apriori.x = kf_data
    i += 1

# Y - position

_, y_pos = plt.subplots()

t_lim_1 = TEST[PRUEBA]["y_pos"]["t_lim_1"]
t_lim_2 = TEST[PRUEBA]["y_pos"]["t_lim_2"]

y_pos.plot(t, y_pos_meas, label = 'Mediciones')
y_pos.plot(t, y_pos_aposteriori, label = 'Estimaciones a posteriori')
y_pos.axvline(x = t_lim_1, linestyle = '--', linewidth = 1, color = 'k')
y_pos.axvline(x = t_lim_2, linestyle = '--', linewidth = 1, color = 'k')
y_pos.set_xlabel(xlabel = '[s]')
y_pos.set_ylabel(ylabel = '[m]')
y_pos.set_title(f"Posición en el eje y (prueba {PRUEBA})")

y_pos.text(x = TEST[PRUEBA]["y_pos"]["region_1"]["x"],
y = TEST[PRUEBA]["y_pos"]["region_1"]["y"],
s = TEST[PRUEBA]["y_pos"]["region_1"]["text"],
fontsize = 20)

y_pos.text(x = TEST[PRUEBA]["y_pos"]["region_2"]["x"],
y = TEST[PRUEBA]["y_pos"]["region_2"]["y"],
s = TEST[PRUEBA]["y_pos"]["region_2"]["text"],
fontsize = 20)

y_pos.text(x = TEST[PRUEBA]["y_pos"]["region_3"]["x"],
y = TEST[PRUEBA]["y_pos"]["region_3"]["y"],
s = TEST[PRUEBA]["y_pos"]["region_3"]["text"],
fontsize = 20)

y_pos.legend()
y_pos.grid(True)

# X - position

_, x_pos = plt.subplots()

t_lim_1 = TEST[PRUEBA]["x_pos"]["t_lim_1"]
t_lim_2 = TEST[PRUEBA]["x_pos"]["t_lim_2"]

x_pos.plot(t, x_pos_meas, label = 'Mediciones')
x_pos.plot(t, x_pos_aposteriori, label = 'Estimaciones a posteriori')
x_pos.axvline(x = t_lim_1, linestyle = '--', linewidth = 1, color = 'k')
x_pos.axvline(x = t_lim_2, linestyle = '--', linewidth = 1, color = 'k')
x_pos.set_xlabel(xlabel = '[s]')
x_pos.set_ylabel(ylabel = '[m]')
x_pos.set_title(f"Posición en el eje x (prueba {PRUEBA})")

x_pos.text(x = TEST[PRUEBA]["x_pos"]["region_1"]["x"],
y = TEST[PRUEBA]["x_pos"]["region_1"]["y"],
s = TEST[PRUEBA]["x_pos"]["region_1"]["text"],
fontsize = 20)

x_pos.text(x = TEST[PRUEBA]["x_pos"]["region_2"]["x"],
y = TEST[PRUEBA]["x_pos"]["region_2"]["y"],
s = TEST[PRUEBA]["x_pos"]["region_2"]["text"],
fontsize = 20)

x_pos.text(x = TEST[PRUEBA]["x_pos"]["region_3"]["x"],
y = TEST[PRUEBA]["x_pos"]["region_3"]["y"],
s = TEST[PRUEBA]["x_pos"]["region_3"]["text"],
fontsize = 20)

x_pos.legend()
x_pos.grid(True)

# Y - velocity

_, y_vel = plt.subplots()

t_lim_1 = TEST[PRUEBA]["y_vel"]["t_lim_1"]
t_lim_2 = TEST[PRUEBA]["y_vel"]["t_lim_2"]

y_vel.plot(t, y_vel_aposteriori, label = 'Estimaciones a posteriori')
y_vel.axvline(x = t_lim_1, linestyle = '--', linewidth = 1, color = 'k')
y_vel.axvline(x = t_lim_2, linestyle = '--', linewidth = 1, color = 'k')
y_vel.set_xlabel(xlabel = '[s]')
y_vel.set_ylabel(ylabel = '[m/s]')
y_vel.set_title(f"Velocidad en el eje y (prueba {PRUEBA})")

y_vel.text(x = TEST[PRUEBA]["y_vel"]["region_1"]["x"],
y = TEST[PRUEBA]["y_vel"]["region_1"]["y"],
s = TEST[PRUEBA]["y_vel"]["region_1"]["text"],
fontsize = 20)

y_vel.text(x = TEST[PRUEBA]["y_vel"]["region_2"]["x"],
y = TEST[PRUEBA]["y_vel"]["region_2"]["y"],
s = TEST[PRUEBA]["y_vel"]["region_2"]["text"],
fontsize = 20)

y_vel.text(x = TEST[PRUEBA]["y_vel"]["region_3"]["x"],
y = TEST[PRUEBA]["y_vel"]["region_3"]["y"],
s = TEST[PRUEBA]["y_vel"]["region_3"]["text"],
fontsize = 20)

y_vel.legend()
y_vel.grid(True)

# X - velocity

_, x_vel = plt.subplots()

t_lim_1 = TEST[PRUEBA]["x_vel"]["t_lim_1"]
t_lim_2 = TEST[PRUEBA]["x_vel"]["t_lim_2"]

x_vel.plot(t, x_vel_aposteriori, label = 'Estimaciones a posteriori')
x_vel.axvline(x = t_lim_1, linestyle = '--', linewidth = 1, color = 'k')
x_vel.axvline(x = t_lim_2, linestyle = '--', linewidth = 1, color = 'k')
x_vel.set_xlabel(xlabel = '[s]')
x_vel.set_ylabel(ylabel = '[m/s]')
x_vel.set_title(f"Velocidad en el eje x (prueba {PRUEBA})")

x_vel.text(x = TEST[PRUEBA]["x_vel"]["region_1"]["x"],
y = TEST[PRUEBA]["x_vel"]["region_1"]["y"],
s = TEST[PRUEBA]["x_vel"]["region_1"]["text"],
fontsize = 20)

x_vel.text(x = TEST[PRUEBA]["x_vel"]["region_2"]["x"],
y = TEST[PRUEBA]["x_vel"]["region_2"]["y"],
s = TEST[PRUEBA]["x_vel"]["region_2"]["text"],
fontsize = 20)

x_vel.text(x = TEST[PRUEBA]["x_vel"]["region_3"]["x"],
y = TEST[PRUEBA]["x_vel"]["region_3"]["y"],
s = TEST[PRUEBA]["x_vel"]["region_3"]["text"],
fontsize = 20)

x_vel.legend()
x_vel.grid(True)

# Y - position prediction

_, y_pos_pred = plt.subplots()

y_pos_pred.plot(selected_t, selected_y_pos_meas, label = 'Mediciones')
y_pos_pred.plot(selected_t, y_pos_apriori, label = 'Estimaciones a priori')
y_pos_pred.plot(selected_t,
                selected_y_pos_meas[:TEST[PRUEBA]["N"]] + [None] * (len(selected_y_pos_meas) - TEST[PRUEBA]["N"]),
                'ro', label = 'Mediciones consideradas', markersize = 2)
y_pos_pred.set_xlabel(xlabel = '[s]')
y_pos_pred.set_ylabel(ylabel = '[m]')
y_pos_pred.set_title(f"Predicción de posición en el eje y (prueba {PRUEBA})")

y_pos_pred.legend()
y_pos_pred.grid(True)

# Y - vel prediction

_, y_vel_pred = plt.subplots()

y_vel_pred.plot(selected_t, selected_y_vel_aposteriori, label = 'Estimaciones a posteriori')
y_vel_pred.plot(selected_t, y_vel_apriori, label = 'Estimaciones a priori')
y_vel_pred.set_xlabel(xlabel = '[s]')
y_vel_pred.set_ylabel(ylabel = '[m/s]')
y_vel_pred.set_title(f"Predicción de velocidad en el eje y (prueba {PRUEBA})")

y_vel_pred.legend()
y_vel_pred.grid(True)

plt.show()
