import matplotlib.pyplot as plt
import math
import numpy
points = numpy.random.randint(0, 100, (3000, 2))
edges = numpy.random.randint(0, 3000, (6000, 2))
x = points[:,0].flatten()
y = math.sin(2*x) * math.exp((x+2)/10)**2


plt.plot(x, y)
plt.show()
plt.figure(figsize=(8,3))
plt.grid(lw=0.5, ls='--')
plt.plot(x,y, lw = 4.0, #толщина линии
 color='red' #выбор одного из "вшитых" цветов, которые можно подзывать по имени
 #color =(0.1, 0.9, 0.5, 0.95) #Задание цвета в формате rgba
 #color='#fc03d7' #задание цвета в формате hex
)
plt.plot(x,y, lw = 5.0, color='black', zorder=0)
