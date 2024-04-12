import numpy as np
import matplotlib.pyplot as plt

#функция для вычисления f(t) = sin(v * cos(2πt))
def f(t, v):
    return np.sin(v * np.cos(2 * np.pi * t))

#создание временной оси t от 0 до 1 с шагом dt
dt = 0.01
t = np.arange(0, 1, dt)


v = float(input())

#вычисление f(t) для заданного v
ft = f(t, v)

#вычисление преобразования Фурье для f(t)
f_fft = np.fft.fft(ft)

#вычисление частот для каждого элемента в преобразовании Фурье
freq = np.fft.fftfreq(len(t), dt)

max_freq_index = np.argmax(np.abs(f_fft))

#выводим соответствующую частоту (которая соответствует неотрицательной частоте)
max_freq = np.abs(freq[max_freq_index])
print(max_freq)
