import numpy as np
import matplotlib.pyplot as plt

def read_file():
    filename = "parameters.txt"
    data = []
    try:
       with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 4:
                        m = float(parts[0])
                        x0 = float(parts[1])
                        y0 = float(parts[2])
                        vx = float(parts[3])
                        vy = float(parts[3])
                        data.append((m, x0, y0, vx, vy))
    except FileNotFoundError:
        print(f"Файл {filename} не найден, используются тестовые значения")
        data = [[1.989e30 0 0 0 0], [5.972e24 152e9 0 0 29290]]
    return data


def count_coords(x, y, vx, vy, a, r):
    dt = 3600 * 24
    ax = a * r[0]
    ay = a * r[1]
    vx_next = vx + ax * dt
    vy_next = vy + ay * dt
    x_next = x + vx * dt
    y_next = y + vy * dt
    return x_next, y_next, vx_next, vy_next


def count_boost(x1, y1, x2, y2 M, m):

    return