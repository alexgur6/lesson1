import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x/2)
y4 = np.cos(x/2)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

ax[0, 0].plot(x, y1)
ax[0, 0].set_title('sin(x)')
ax[0, 1].plot(x, y2)
ax[0, 1].set_title('cos(x)')
ax[1, 0].plot(x, y3)
ax[1, 0].set_title('sin(x/2)')
ax[1, 1].plot(x, y4)
ax[1, 1].set_title('cos(x/2)')

for i in range(2):
    for j in range(2):
        ax[i, j].set_xlabel('x')
        ax[i, j].set_ylabel('y')

plt.tight_layout() # Размещение подписей в компактном виде

plt.show()
