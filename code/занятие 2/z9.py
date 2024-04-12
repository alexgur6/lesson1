import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 1/4 * np.sin(0.5 * x**2 - y) - np.exp(-((x-5)**2 + (y-2)**2))

x = np.linspace(2, 8, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure()
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(label='f(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции f(x, y)')
# Определение минимума функции с точностью до десятых
min_x, min_y = np.unravel_index(np.argmin(Z), Z.shape)
min_val = np.min(Z)
min_x_val = x[min_x]
min_y_val = y[min_y]

plt.scatter(min_x_val, min_y_val, color='red')
plt.show()
