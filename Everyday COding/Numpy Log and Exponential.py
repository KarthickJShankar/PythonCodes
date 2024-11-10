import numpy as np
#if a^b = c   ->   b = log base(a) c
#e = 2.7  ->  e = 1+1/1! +1/2! +1/3!.........+1/n!


# 5^b=20
# what is b?
b = np.log(20)/np.log(5)
print(b)

# what is the value of e^5
print(np.exp(5))

#what is the value of pi
print(np.pi)

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
b = np.concat((a,a))
print(b)