import numpy as np
import math
def closest(A, v, r):
    k = 0
    for j in range(0, l):
        if j == v:
            continue
        x = A[j, 0]
        y = A[j, 1]
        z = A[j, 2]
        rost = math.sqrt((x-A[v, 0])**2 + (y-A[v, 1])**2 + (z-A[v, 2])**2)
        if rost < r:
            k += 1
    return(k)



A = np.array(
 [
 [1.0, 0.0, 2.0],
 [-1.0, 0.5, 2.0],
 [-2.0, 1.5, 0.0],
 [2.5, -1.2, -0.5],
 [1.5, 0.2, -0.2]
 ]
)
l = len(A)
r = 2.5
v = 1
print(closest(A, v, r))