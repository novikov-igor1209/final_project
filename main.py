from functions import read_file, count_coords, count_boost
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


data = read_file("parameters.txt")
masses = data[:, 0]
x = data[:, 1]
y = data[:, 2]
vx = data[:, 3]
vy = data[:, 4]

fig, ax = plt.subplots()
points = [ax.plot([], [], 'o', markersize=5)[0] for _ in range(len(x))]
ax.set_xlim(-900e9, 900e9)
ax.set_ylim(-900e9, 900e9)
ax.set_aspect('equal')

def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    global x, y, vx, vy, masses
    x, y, vx, vy = count_coords(x, y, vx, vy, masses)
    for i, point in enumerate(points):
        point.set_xdata([x[i]])
        point.set_ydata([y[i]])
    return points
anim = FuncAnimation(fig, update, init_func=init, frames=10000, interval=5, blit=True)
plt.tight_layout()
plt.show()
