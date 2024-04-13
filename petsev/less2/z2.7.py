import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
 return 1/4*np.sin(1/2*x^2-y)-np.exp(-(x-5)^2+(y-2)^2)
x = np.linspace(2, 8, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)
Z = func(X, Y) #Матрица z
fig, ax = plt.subplots(1, 1, figsize=(8, 8), subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z / Z.max(), cmap=plt.cm.ocean_r)
ax.view_init(30, 60) #Угол просмотра

#Переделать полностью