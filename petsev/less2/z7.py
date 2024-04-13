import numpy as np
def min(x):
    a = 0
    b = 0
    c = 0
    for i in range(0, len(x)):
        if x[i] < x[a]:
            a = i
    for i in range(0, len(x)):
        if i == a:
            continue
        if x[i] < x[b]:
            b = i
    for i in range(0, len(x)):
        if i == a:
            continue
        if i == b:
            continue
        if x[i] < x[c]:
            c = i
    minimu = np.array([x[a],x[b],x[c]])
    return minimu

x = np.array([3, 2, 5, 4, 1, 7, 0, -2, 48])
print(min(x))