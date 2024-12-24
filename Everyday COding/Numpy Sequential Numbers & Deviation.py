import numpy as np
import random
#Equal distribution
a = [[1,2,3,4],[5,6,7,8]]
a = np.array(a)
b = [[10,11,12,13],[15,16,17,18]]
b = np.array(b)
#linspace means linear space
a = np.linspace(1,20,10)
print(a)

b = np.random.randint(1,20)
print(b)
print(random.randrange(10,100,5))
c = np.arange(1,10,0.7)
print(c)

#Zeros
d = np.zeros(8,int)
print(d)
#Ones
e = np.ones(8,int)

#Standard Deviation
f = np.std(a)
print(f)

#Mean
g = np.mean(a)
print(g)

#Median
h = np.median(a)
print(h)