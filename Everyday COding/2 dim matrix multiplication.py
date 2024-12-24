import numpy as np
def Solution(arr1,arr2):
   result = np.matmul(arr1,arr2)
   return result

a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6],
    [7, 8]
]
print(Solution(a,b))