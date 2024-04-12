import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import minimize
def gauss(z, sigma, x0, y0):
 x, y = z
 return np.exp(-((x-x0)**2 + (y-y0)**2) / sigma**2)
neg_gauss = lambda z, sigma, x0, y0: -gauss(z, sigma, x0, y0)
x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)
Z = gauss((X, Y), 100, 0, 0)
def mixed(z, *args):
 return np.sum(neg_gauss(z, *params) for params in args)
Z = mixed((X, Y), (10, -5, -12), (7, 5, 5), (9, -5, 10))
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
contours = ax.contour(X, Y, Z, 16, colors="black", linewidths=2,
linestyles='-.')
ax.clabel(contours, inline=True, fontsize=16)
contours = ax.contourf(X, Y, Z, 200, cmap=plt.cm.jet)
plt.show()