import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(y, t):
    u, f = y
    dydt = [2 * u - f, u]
    return dydt

# Временные шаги
t = np.linspace(0, 5, 100)

# Начальные условия
y0 = [1, 1]

# Решение системы
res = odeint(func, y0 = [1,1], t = t)


# Отображение решения f и сравнение с экспонентой
plt.plot(t, res[:, 1])
plt.plot(t[::50], np.exp(t[::50]), 'o')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Решение дифференциального уравнения второго порядка')
plt.grid(True)
plt.show()