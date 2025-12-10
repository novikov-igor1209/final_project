import numpy as np
from concurrent.futures import ProcessPoolExecutor
from scipy.constants import G
from config import dt

def read_file(filename):
    data = []
    f = open(filename, 'r', encoding='utf-8')
    for line in f:
        if line.strip():
            parts = line.split()
            if len(parts) == 5:
                m = float(parts[0])
                x0 = float(parts[1])
                y0 = float(parts[2])
                vx = float(parts[3])
                vy = float(parts[4])
                data.append((m, x0, y0, vx, vy))
    return np.array(data)


def count_boost(x1, y1, x2, y2, mass2):
    dx = x2 - x1
    dy = y2 - y1
    dr =  + 1e-10
    r_squared = dx*dx + dy*dy + dr
    force = G * mass2 / r_squared
    dist = np.sqrt(r_squared)
    ax = force * dx / dist
    ay = force * dy / dist
    return ax, ay

def compute_acceleration(i, x, y, masses):
    total_ax, total_ay = 0.0, 0.0
    for j in range(len(x)):
        if i != j:
            ax_ij, ay_ij = count_boost(x[i], y[i], x[j], y[j], masses[j])
            total_ax += ax_ij
            total_ay += ay_ij
    return i, total_ax, total_ay

def count_coords(x, y, vx, vy, masses, axprev, ayprev):
    n = len(x)
    ax = np.empty(n)
    ay = np.empty(n)
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(compute_acceleration, i, x, y, masses) for i in range(n)]
        for future in futures:
            i, total_ax, total_ay = future.result()
            ax[i], ay[i] = total_ax, total_ay
    vx += 0.5 * (ax + axprev) * dt
    vy += 0.5 * (ay + ayprev) * dt
    x += vx * dt + 0.5 * axprev * dt ** 2
    y += vy * dt + 0.5 * ayprev * dt ** 2
    return x, y, vx, vy, ax, ay