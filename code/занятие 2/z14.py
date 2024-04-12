from scipy.integrate import odeint
import numpy as np

def model(f, t):
    return f + t

# Заданные параметры
f0 = float(input("Введите значение f(0): "))
dt = 0.001
t = np.arange(0, 2, dt)

# Решение дифференциального уравнения
f = odeint(model, f0, t)

# Находим значение f(t = 1)
index_t_equals_1 = int(1 / dt)
f_at_t_1 = f[index_t_equals_1][0]

print("f(t = 1) =", round(f_at_t_1, 2))
