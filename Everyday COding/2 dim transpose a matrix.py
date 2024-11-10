def Solution(arr):
    final_list = []
    for n in range(len(arr[0])):
        new_list = []
        for m in range(len(arr)):
            new_list.append(arr[m][n])
        final_list.append(new_list)
    return final_list

import numpy
a = numpy.array([
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
])
print(a.transpose())
a = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
print(Solution(a))