def ln_approximation(x):
    result = 0
    tol = x
    n = 1
    
    while abs(tol) >= 1e-6:
        result += tol
        n += 1
        tol = (-1) ** (n - 1) * (x ** n) / n
    
    return round(result, 8)


x_value = float(input())
result = ln_approximation(x_value)
print(result)
