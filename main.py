from functions import read_file, count_coords
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


if __name__=='main':
    data = read_file("data.txt")
    masses = data[:, 0]
    x = data[:, 1]
    y = data[:, 2]
    vx = data[:, 3]
    vy = data[:, 4]
    axprev = np.zeros_like(x)
    ayprev = np.zeros_like(y)
    fig, ax = plt.subplots(figsize=(15, 15))
    n = len(x)
    points = []
    points.append(ax.plot([], [], 'o', markersize=6)[0])
    for _ in range(1, n):
        points.append(ax.plot([], [], 'o', markersize=4)[0])
    lim = 1.1*max(x)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')

    def init():
        for point in points:
            point.set_data([], [])
        return points

    def update(frame):
        global x, y, vx, vy, masses, axprev, ayprev
        x, y, vx, vy, axprev, ayprev = count_coords(x, y, vx, vy, masses, axprev, ayprev)
        for i, point in enumerate(points):
            point.set_xdata([x[i]])
            point.set_ydata([y[i]])
        return points
    anim = FuncAnimation(fig, update, init_func=init, frames=30, interval=100, blit=True)
    plt.tight_layout()
    plt.show()