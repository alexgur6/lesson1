from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Определение функции, соответствующей дифференциальному уравнению
def func(y, t):
    return t**2

# Определение массива t
dt = 1e-3
t = np.arange(0, 1, dt)

# Решение дифференциального уравнения с начальным условием y(0) = 0
res = odeint(func, y0=0, t=t)


# Построение графиков
plt.figure(figsize=(5,4))
plt.plot(t, res)
plt.plot(t[::50], t[::50]**3/3, 'o')
plt.show()

