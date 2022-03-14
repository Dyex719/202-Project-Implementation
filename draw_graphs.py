# read and parse timew.txt and plot the time taken to solve the puzzle
from matplotlib import pyplot as plt
import numpy as np

with open('time.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]
    lines = [x.split(' ') for x in lines]
    lines.sort(key=lambda x: int(x[0].split(".")[0].split("_")[1]))
    # x = [x[0].split(".")[0].split("_")[1] for x in lines]
    # y = [float(x[2]) for x in lines]


    x = [int(x[0].split(".")[0].split("_")[1]) for x in lines]
    y = np.log([float(x[2]) for x in lines])

    n_n_2 = (np.square(np.array(x)))*np.log(np.array(x))
    # plt.plot(x, y)
    plt.plot(x, n_n_2)
    plt.xticks([3,4,5])

    plt.title('Variation of time with increase in size of the board', fontsize=14)
    plt.xlabel('Board Size', fontsize=14)
    plt.ylabel('Log Time Taken (in microseconds)', fontsize=14)
    # plt.grid(True)
    # plt save
    # plot a n^2 graph on the same graph



    plt.savefig('time.png')