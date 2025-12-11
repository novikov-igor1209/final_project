import numpy as np

num_stars = 5000
masses = np.random.uniform(10e33, 1e35, size=num_stars)

angles = np.random.uniform(0, 2*np.pi, size=num_stars)
radii = np.random.uniform(100e9, 100000e9, size=num_stars)
x0 = radii * np.cos(angles)
y0 = radii * np.sin(angles)

vx0 = np.random.uniform(0, 5000, size=num_stars)
vy0 = np.random.uniform(0, 5000, size=num_stars)

stars_data = []
for i in range(num_stars):
    star = [
        masses[i],
        x0[i],
        y0[i],
        vx0[i],
        vy0[i]
    ]
    stars_data.append(star)
stars_array = np.array(stars_data)

np.savetxt('data.txt', stars_array)