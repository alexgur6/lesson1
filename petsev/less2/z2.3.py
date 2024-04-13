import numpy as np
import matplotlib.pyplot as plt

num_points = 150
r = np.random.uniform(0, 2, num_points)
theta = np.radians(np.random.uniform(0, 360, num_points))

plt.figure(figsize=(6, 6))
plt.axes(projection='polar')

sizes = 400 * r**2


plt.scatter(theta, r,
            s=sizes,
            c=theta,
            cmap='hsv',
            alpha=0.8)

plt.show()
