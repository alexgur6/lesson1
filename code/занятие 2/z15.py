import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings

mpl.style.use('seaborn-white')
warnings.filterwarnings('ignore')


# Шаг по оси x
dx = 0.001
x = np.arange(-10, 10, dx)

# Определение функции
f0 = lambda x: (x - 0.5)**2

# Визуализация функции
plt.plot(x, f0(x))
plt.show()

# Минимизация функции
from scipy.optimize import minimize
result = minimize(f0, x0=1)

# Вывод результатов минимизации
print(result)
