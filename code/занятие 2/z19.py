from scipy.optimize import minimize
import numpy as np

def f(x):
    return x**2 * (x - 4)**2 * np.exp(-x**2)

x0 = float(input("Введите начальное предположение x0: "))  #начальное предположение
dx = 0.001
x = np.arange(-4, 4, dx)

# Определение функции для минимизации
def negative_f(x):
    return -f(x)

# Поиск минимума с использованием функции minimize
result = minimize(negative_f, x0=x0)

# Вывод результатов
print("Координата x локального максимума: {:.2f}".format(result.x[0]))
