import numpy as np
a = [[1,2,3,4],[5,6,7,8]]
a = np.array(a)
b = [[10,11,12,13],[15,16,17,18]]
b = np.array(b)
#Addition
if a.shape == b.shape:
    print(a+b)
else:
    print("Not of the same size")
print("\n")

#Subtraction
if a.shape == b.shape:
    print(a-b)
else:
    print("Not of the same size")
print("\n")

#Element wise multiplication -- shape has to be equal
#If we multiply a,b -- suppose has a dimension (p,q) b will have to be (q,anything)
if a.shape == b.shape:
    print(a*b)
else:
    print("Not of the same size")
print("\n")

#Matrix multiplication -- Element need not be same
#Will not work - np.dot(a,b) and alos np.dot(b,a)
c = [[1,2,3,4],[5,6,7,8]]
c = np.array(a)
d = [[10,11,12,13],[15,16,17,18]]
d = np.array(b)
d = d.T
c.dot(d)

#Element Division
if a.shape == b.shape:
    print(a/b)
else:
    print("Not of the same size")
print("\n")

#Element Power
if a.shape == b.shape:
    print(a**b)
else:
    print("Not of the same size")

#Floor Division -- Quotient
if a.shape == b.shape:
    print(a//b)
else:
    print("Not of the same size")

#Mod -- Division
#Element Power
if a.shape == b.shape:
    print(a%b)
else:
    print("Not of the same size")