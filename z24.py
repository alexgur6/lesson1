import math
def trapez(func, a, b, N):
    h = (b - a) / N
    result = 0.5 * (func(a) + func(b))

    for i in range(1, N):
        result += func(a + i * h)

    result *= h
    return round(result, 8)


def function(x):
    return math.sin(x)  

a = float(5)       
b = float(7)       
N = int(100)         

integral = trapez(function, a, b, N)
print(integral)
