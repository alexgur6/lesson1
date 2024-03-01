def max_particle_speed(position, time):
    speed = []
    
    # Вычисляем скорость для каждого временного интервала
    for i in range(1, len(position)):
        delta_x = position[i] - position[i - 1]
        speed = delta_x / time
        speed.append(abs(speed))

    # Находим максимальное значение модуля скорости
    max_speed = max(speed)

    return int(max_speed)

# Пример использования:
position_input = input("Введите положение частицы через пробел: ").split()
position = [float(pos) for pos in position_input]
time = 0.01
result = max_particle_speed(position, time)
print(result)
