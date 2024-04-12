def volume(a, b, c=None):
    if c is None:
        # Если передано два аргумента, вычисляем площадь прямоугольника
        return a * b
    else:
        # Если переданы три аргумента, вычисляем объем параллелепипеда
        return a * b * c


print(volume(2, 3))     # Вывод: 6 
print(volume(2, 3, 4))  # Вывод: 24 
