import numpy as np
from numba import njit

def read_file(filename):
    data = []
    try:
       with open(filename, 'r', encoding='utf-8') as f:
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
    except FileNotFoundError:
        print(f"Файл {filename} не найден, используются тестовые значения")
        data = [[1.989e30, 0, 0, 0, 0], [5.972e24, 152e9, 0, 0, 29290]]
    return np.array(data)



@njit
def count_boost(x1, y1, x2, y2, mass2):
    G = 6.67430e-11
    dx = x2 - x1
    dy = y2 - y1
    r_squared = dx*dx + dy*dy + 1e-10
    force = G * mass2 / r_squared
    dist = np.sqrt(r_squared)
    ax = force * dx / dist
    ay = force * dy / dist
    return ax, ay

@njit
def count_coords(x, y, vx, vy, masses, axprev, ayprev):
    dt = 3600 * 24
    n = len(x)
    ax = np.empty(n)
    ay = np.empty(n)
    for i in range(n):
        total_ax, total_ay = 0.0, 0.0
        for j in range(n):
            if i != j:
                ax_ij, ay_ij = count_boost(x[i], y[i], x[j], y[j], masses[j])
                total_ax += ax_ij
                total_ay += ay_ij
        ax[i], ay[i] = total_ax, total_ay

    for i in range(n):
        vx += 0.5 * (ax + axprev) * dt
        vy += 0.5 * (ay + ayprev) * dt

    for i in range(n):
        x += vx * dt + 0.5 * axprev * dt ** 2
        y += vy * dt + 0.5 * ayprev * dt ** 2
    
    return x, y, vx, vy, ax, ay
