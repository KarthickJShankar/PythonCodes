import numpy as np
#if a^b = c   ->   b = log base(a) c
#e = 2.7  ->  e = 1+1/1! +1/2! +1/3!.........+1/n!


# 5^b=20
# what is b?
b = np.log(20)/np.log(5)
# print(b)

# what is the value of e^5
# print(np.exp(5))

#what is the value of pi
# print(np.pi)

a = np.array([[1,2,3,4],[5,6,7,8]])
# print(a)
b = np.concat((a,a))
# print(b)

# print(np.empty((2,2)))

print(a.T)

arr1 = np.array([[1], [2], [3]])  # Shape: (3, 1)
arr2 = np.array([[10, 20, 30]])   # Shape: (1, 3)

result = arr1 + arr2
print(result)


a = [[1,2,3],[4,5,6]]
b = [1,2,4]
print(np.array(a)+np.array(b))

import copy
a = [[1,2,3,4]]
b = copy.copy(a)
b[0][0] = 10
print(b,a)
a = [1,2,3,4]
c = copy.deepcopy(a)
c[0] = 99
print(c,a)
