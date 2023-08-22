import matplotlib.pyplot as plt
from pprint import pprint
import csv
import os

DATA_SOURCES_DIR = './data_sources/'

for csv_path in os.listdir('./data_sources/'):

    with open(DATA_SOURCES_DIR + csv_path, newline = '') as csv_file:

        data = [[float(row[0]),
                float(row[1]),
                float(row[2])]
                for row in csv.reader(csv_file)]

    start_time = data[0][0]

    data = [[row[0] - start_time, row[1], row[2]]
            for row in data]

    time_data = [row[0] for row in data]

    x_data = [row[1] for row in data]

    y_data = [row[2] for row in data]

    y_speed = [(y_data[i] - y_data[i-1]) / (time_data[i] - time_data[i - 1])
               if i - 1 >= 0 else 0
               for i
               in range(len(y_data))]

    x_speed = [(x_data[i] - x_data[i-1]) / (time_data[i] - time_data[i - 1])
               if i - 1 >= 0 else 0
               for i
               in range(len(y_data))]
    
    # y-axis plots

    fig, (y_position_plot, y_speed_plot) = plt.subplots(2)

    fig.suptitle('y-axis ' + csv_path)

    y_position_plot.plot(time_data, y_data)

    y_position_plot.set(xlabel = 'time [s]', ylabel = 'position [m]')

    y_speed_plot.plot(time_data, y_speed)

    y_speed_plot.set(xlabel = 'time [s]', ylabel = 'speed [m/s2]')

    plt.savefig(f"./plots/y_axis_plot_{csv_path.split('.')[0]}.png")

    # x-axis plots

    fig, (x_position_plot, x_speed_plot) = plt.subplots(2)

    fig.suptitle('x-axis ' + csv_path)

    x_position_plot.plot(time_data, x_data)

    x_position_plot.set(xlabel = 'time [s]', ylabel = 'position [m]')

    x_speed_plot.plot(time_data, x_speed)

    x_speed_plot.set(xlabel = 'time [s]', ylabel = 'speed [m/s2]')

    plt.savefig(f"./plots/x_axis_plot_{csv_path.split('.')[0]}.png")