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
scatters = [ax.plot([], [], 'o')[0] for _ in range(len(x))]
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

def init():
    for scatter in scatters:
        scatter.set_data([], [])
    return scatters

def update(frame):
    global x, y, vx, vy, masses
    axes_acc = []
    for i in range(len(x)):
        total_ax = 0
        total_ay = 0
        for j in range(len(x)):
            if i != j:
                ax, ay = count_boost(x[i], y[i], x[j], y[j], masses[j])
                total_ax += ax
                total_ay += ay
        axes_acc.append([total_ax, total_ay])
    for i in range(len(x)):
        a = axes_acc[i]
        x[i], y[i], vx[i], vy[i] = count_coords(x[i], y[i], vx[i], vy[i], ax, ay)
    for i, scatter in enumerate(scatters):
        scatter.set_data(x[i], y[i])
    return scatters
anim = FuncAnimation(fig, update, init_func=init, frames=1000, interval=20, blit=True)
plt.show()