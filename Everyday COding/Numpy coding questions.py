import numpy as np
a = np.array([1,4,3])
print(a)
# b = a.reshape(2,5)
# print(b)

c = a[a%2 != 0]
print(c)
d = [4,5,6]
#addition
print(a+d)
print(a-d)
print(a*d)
print(a/d)

print(np.std(a))

#matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.matmul(B,A))

arr = np.array([10, 20, 30, 40, 50, 60])
Z = arr[arr>30]
print(Z)

arr = np.array([1, 2, 2, 3, 3, 3])
arr = np.unique(arr)
print(arr)

arr = np.array([[3, 1], [2, 4]])
print(np.sort(arr,axis=0))
print(np.sort(arr,axis=1))

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
c = A+B
print(c)
f = np.zeros((8,8))
# print(f)
for n in range(8):
    for m in range(8):
        if n==0 or n==len(f[0])-1:
            f[n,m] = 1
        elif m == 0 or m==len(f[0])-1:
            f[n,m] = 1
print(f)

a = np.array([[1,2,3,4]])
b = np.array([[5,6,7,8]])
c = np.concatenate((a,b),axis=0)
print(c)

arr = np.array([1, -2, 3, -4, 5])
arr[arr > 0]=0
print(arr)