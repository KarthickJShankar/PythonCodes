import numpy as np

#LINEAR ALGEBRA
# 2x+3y=8
# 3x+8y=9
# solve x,y?

result = np.linalg.solve([[2,3],[3,8]],[8,9])
print(result)


# 2x+3y+9z=16
# 3x+8y_2z=92
# 1x+8y+7z=62
# solve x,y,z?

result = np.linalg.solve([[2,3,9],[3,8,2],[1,8,7]],[19,92,62])
print(result)
#linalg - Linear Algebra
#-----------------------------------------------------------------------------------------
#TRIGNOMETRY
#Sin,Cos and Tan
#Numpy doesnt understand degrees
#Sin 30 degree
a = np.sin(30 * np.pi/180)
print(a)
#Sin 90 degree
b = np.sin(90 * np.pi/180)
print(b)
#Cos 30 degree
c= np.cos(90 * np.pi/180)
print(c)
#tan 30 degree
d = np.tan(90 * np.pi/180)
print(d)

#to calculate sin , cos and tan of a array
a = np.array([[1,2,3],[4,5,6]])
print(np.sin(a))