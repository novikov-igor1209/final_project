import numpy as np
import matplotlib.pyplot as plt

def trajectory(x_0, v_0):
    M = 1.989e30
    dt = 3600 * 24
    G = 6.67e-11
    r = np.zeros((N+1, 2))
    v = np.zeros((N+1, 2))
    t = np.arange(0, int(N*dt) + 1, dt)
    r[0] = [x_0, 0]
    v[0] = [0, v_0]
    r_norm = np.linalg.norm(r[0])
    a_prev = -G * M / (r_norm**3) * r[0]
    for i in range(N):
        r[i+1] = r[i] + v[i] * dt + 0.5 * a_prev * dt**2
        r_norm = np.linalg.norm(r[i+1])
        a_new = -G * M / (r_norm**3) * r[i+1]
        v[i+1] = v[i] + 0.5 * (a_prev + a_new) * dt
        a_prev = a_new
    return r

def plot_trajectory(rz, rj, title="Траектория движения планеты"):
    plt.figure(figsize=(10, 8))
    plt.plot(0, 0, 'grey', markersize=20, label='Звезда')
    plt.plot(rz[:, 0], rz[:, 1], 'blue', linewidth=2, label='Траектория Земли')
    plt.plot(rz[0, 0], rz[0, 1], 'green', markersize=6, label='Начальное положение Земли')
    plt.plot(rj[:, 0], rj[:, 1], 'black', linewidth=2, label='Траектория Юпитера')
    plt.plot(rj[0, 0], rj[0, 1], 'red', markersize=10, label='Начальное положение Юпитера')
    plt.xlabel('x координата [м]', fontsize=12)
    plt.ylabel('y координата [м]', fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
    plt.tight_layout()
    plt.show()

Mc = 1.989e30
mz = 5.972e24
mj = 1.8987e27
xz = 152e9
xj = 817e9
vz = 29290
vj = 13070
N = 365
dt = 3600 * 24
rz = trajectory(xz, vz)
rj = trajectory(xj, vj)

plot_trajectory(rz, rj, "Орбита")
plot_trajectory(rj, "Орбита")