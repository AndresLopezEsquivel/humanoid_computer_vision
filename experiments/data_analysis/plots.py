#!/usr/bin/env python3
import matplotlib.pyplot as plt
from pprint import pprint
import csv
import os

DATA_SOURCES_DIR = './data_sources/'

for csv_path in os.listdir('./data_sources/'):

    with open(DATA_SOURCES_DIR + csv_path, newline = '') as csv_file:

        data = [[float(row[0]),
                float(row[1]),
                float(row[2]),
                float(row[3]),
                float(row[4]),
                float(row[5]),
                float(row[6])]
                for row in csv.reader(csv_file)]

    start_time = data[0][0]

    data = [[row[0] - start_time,
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],]
            for row in data]

    time_data = [row[0] for row in data]

    x_data = [row[1] for row in data]

    y_data = [row[2] for row in data]

    kf_x_pos = [row[3] for row in data]

    kf_y_pos = [row[4] for row in data]

    kf_x_vel = [row[5] for row in data]

    kf_y_vel = [row[6] for row in data]

    y_speed = [(y_data[i] - y_data[i-1]) / (time_data[i] - time_data[i - 1])
               if i - 1 >= 0 else 0
               for i
               in range(len(y_data))]

    x_speed = [(x_data[i] - x_data[i-1]) / (time_data[i] - time_data[i - 1])
               if i - 1 >= 0 else 0
               for i
               in range(len(y_data))]
    
    # Plot y-axis position along with the ball's velocity

    fig, y_position = plt.subplots()
    
    y_position.set_title('Posición en el eje y')
    y_position.plot(time_data, y_data, label = '[m] (Sin KF)')
    y_position.plot(time_data, kf_y_pos, label = '[m] (Con KF)')
    # y_position.plot(time_data, kf_y_vel, label = '[m/s] (Con KF)')
    y_position.set_xlabel(xlabel = 'Tiempo [s]')
    y_position.legend()
    y_position.grid(True)
    plt.savefig(f"./plots/y_axis_position_{csv_path.split('.')[0]}.png")

    # Plot y-axis velocity

    fig, y_vel = plt.subplots()

    y_vel.set_title('Velocidad en el eje y')
    y_vel.plot(time_data, kf_y_vel)
    y_vel.set_ylabel(ylabel = '[m/s]')
    y_vel.set_xlabel(xlabel = 'time [s]')
    y_vel.grid(True)
    plt.savefig(f"./plots/y_axis_velocity_{csv_path.split('.')[0]}.png")

    # Plot x-axis position along with the ball's velocity

    fig, x_position = plt.subplots()
    
    x_position.set_title('Posición en el eje x')
    x_position.plot(time_data, x_data, label = '[m] (Sin KF)')
    x_position.plot(time_data, kf_x_pos, label = '[m] (Con KF)')
    # x_position.plot(time_data, kf_x_vel, label = '[m/s] (Con KF)')
    x_position.set_xlabel(xlabel = 'Tiempo [s]')
    x_position.legend()
    x_position.grid(True)
    plt.savefig(f"./plots/x_axis_position_{csv_path.split('.')[0]}.png")

    # Plot x-axis velocity

    fig, x_vel = plt.subplots()

    x_vel.set_title('Velocidad en el eje x')
    x_vel.plot(time_data, kf_x_vel)
    x_vel.set_ylabel(ylabel = '[m/s]')
    x_vel.set_xlabel(xlabel = 'time [s]')
    x_vel.grid(True)
    plt.savefig(f"./plots/x_axis_velocity_{csv_path.split('.')[0]}.png")