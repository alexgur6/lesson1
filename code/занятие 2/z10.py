import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
    return np.sin(x ** 2 + y ** 2)/(x ** 2 + y ** 2)
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y) #Создание матриц из массивов
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
cmap='viridis', edgecolor='none')
ax.set_title('Поверхность')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
