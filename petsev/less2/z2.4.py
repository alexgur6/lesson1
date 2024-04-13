import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(-5, 5, 40)

y = np.sin(x) + np.tan(2 * (x - 2))

yerr = np.array(random.sample(range(-100, 101), 40)) / 100  # значения от -1 до 1

plt.figure(figsize=(10, 5))
plt.errorbar(x, y, yerr=yerr, ecolor='forestgreen', capsize=10, elinewidth=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y(x) с погрешностями')
plt.grid(True)
plt.show()
