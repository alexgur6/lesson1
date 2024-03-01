def volume(a, b, c=None):
    if c is None:
        return a * b
    else:
        return a * b * c

vvod = input().split()
a = float(vvod[0])
b = float(vvod[1])

# Проверка количества введенных аргументов
if len(vvod) == 3:
    c = float(vvod[2])
else:
    c = None

# Вызов функции и вывод результата
result = volume(a, b, c)
if c is None:
    print(result)
else:
    print(result)
