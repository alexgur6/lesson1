import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)
def func(x, y):
 return np.power(x, 4) - np.power(y, 4)
Z = func(X, Y)
fig, ax = plt.subplots(1, 1, figsize=(8, 8), subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z / Z.max(), cmap=plt.cm.ocean_r)
ax.view_init(30, 60) #Угол просмотра
