import numpy as np
import matplotlib.pyplot as plt

# Определение параметров R и r
R = 3
r = 1

# Создание массивов для переменных theta и phi
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)

# Создание сетки для переменных theta и phi
Theta, Phi = np.meshgrid(theta, phi)

# Вычисление координат x, y, z
x = (R + r * np.cos(Phi)) * np.cos(Theta)
y = (R + r * np.cos(Phi)) * np.sin(Theta)
z = r * np.sin(Phi)

# Построение поверхности
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Установка равного масштаба осей
ax.set_box_aspect([np.ptp(x), np.ptp(y), np.ptp(z)])

plt.show()
