from scipy.optimize import minimize

def f(xy, a, b):
    x, y = xy
    return (x + y)**2 - 2*x*(y + a) - 2*y*b + a + b
a = 0
b = 0
# Начальное предположение для x и y (вблизи точки (0, 0))
xy0 = [0, 0]

# Функция для минимизации
minimized_function = lambda xy: f(xy, a, b)

# Поиск минимума с использованием функции minimize
result = minimize(minimized_function, xy0)

# Вывод результатов
x_min, y_min = result.x
print("Координаты (x, y) локального минимума: ({:.1f}, {:.1f})".format(x_min, y_min))
