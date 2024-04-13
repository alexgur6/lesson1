import numpy as np
def nonzero(A):
 """
 A: <np.ndarray> - матрица
 ---------------
 Returns: x, y: <int>, <int> - найденный индекс строки и столбца, соответственно
 """
 # your code here
 for x in range(0,99):
     for y in range(0,99):
         if A[x,y] != 0:
            return x, y
A = np.zeros((100,100))
A[56,70] = 4
print(nonzero(A))