x0 = float(input("Введите x координату точки P: "))
y0 = float(input("Введите y координату точки P: "))

# Проверяем попадание точки в кольцо
if ((x0-1)**2 + (y0)**2 < 2**2) and ((x0-1)**2 + (y0)**2 > 1**2):
    in_circle = "yes"
else:
    in_circle = "no"

# Проверяем попадание точки в прямоугольник
if abs(x0-4) < 2 and abs(y0-2) < 3:
    in_rectangle = "yes"
else:
    in_rectangle = "no"

# Проверяем варианты попадания точки
if in_circle == "yes" and in_rectangle == "no":
    print("yes no")
elif in_circle == "no" and in_rectangle == "yes":
    print("no yes")
elif in_circle == "yes" and in_rectangle == "yes":
    print("yes yes")
else:
    print("no no")

x0, y0 = map(float, input().split())