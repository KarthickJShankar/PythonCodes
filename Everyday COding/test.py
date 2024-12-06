# import itertools
# def func():
#     for n in itertools.count(10):
#         print(n)
#         if n%23 == 0:
#             return True
# print(func())

#Max and Min
# def solution(arr):
#     left = float("inf")
#     right = 0
#     for n in arr:
#         if n > right:
#             right = n
#         if n < left:
#             left = n
#     return [left,right]

#Third Highest
# def Solution(arr):
#     right = third_largest = float("-inf")
#     second_right = float("-inf")
#     for n in arr[1:]:
#         if n > right:
#             third_largest = second_right
#             second_right = right
#             right = n
#
#         if n > second_right and n != right:
#             third_largest = second_right
#             second_right = n
#         if n > third_largest and n!=second_right and n!=right:
#             third_largest = n
#
#     return third_largest
# print(Solution([5,2,8,6,7,3,9,1,3]))


#Third_Lowest
# def Solution(arr):
#     lowest = second_lowest = third_lowest = float("inf")
#     for n in arr:
#         if n < lowest:
#             third_lowest = second_lowest
#             second_lowest = lowest
#             lowest = n
#         elif n < second_lowest and n!=lowest:
#             third_lowest = second_lowest
#             second_lowest = n
#         elif n < third_lowest and n!=second_lowest and n!=lowest:
#             third_lowest = n
#     return third_lowest
# print(Solution([5,2,8,6,7,3,9,1,3]))

#decorator
# def decorator(func):
#     def wrapper(*args):
#         val = func(*args)
#         return val*2
#     return wrapper
#
# @decorator
# def calculate(*arg):
#     result = 1
#     for n in arg:
#         result*=n
#     print(result)
#     return result
#
# print(calculate(2,3,4,5))


#generator

# def generator(arr):
#     for n in arr:
#         yield n
#
# g = generator([1,2,3,4])
# for n in g:
#     print(n*2)



#accessmodifiers
# class Access:
#     def __init__(self,b):
#         self.a = 0
#         self.b = b
#     # def __calculate_a(self):
#     #     return self.a*5
#     def _calculate_b(self):
#         return self.b*10
#
#     def get_a(self):
#         return self.a*5
#     def set_a(self,a):
#         self.a = a
# class C(Access):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c = c
#
#     def calculate_c(self):
#         return self.a*self.b/self.c
#
#
# a = Access(10)
# # c = C(5,10,20)
# # d = c.calculate_c()
# # e = c._calculate_b()
# a.set_a(20)
# print(a.get_a())
# # print(e)
# # print(c.calculate_c())


# #Thirdsmallest
# def Soltuion(arr):
#     largest = sec_largest = third_largest = float("inf")
#     for n in arr:
#         if n < largest:
#             third_largest = sec_largest
#             sec_largest = largest
#             largest = n
#         elif largest <n < sec_largest:
#             third_largest = sec_largest
#             sec_largest = n
#         elif sec_largest < n < third_largest:
#             third_largest = n
#     return third_largest
#
# print(Soltuion([4,2,7,5,9,6,1]))


#transpose
import numpy as np
# def solution(a):
#
#     final_result = []
#     for n in range(len(a[0])):
#         result = []
#         for m in range(len(a)):
#             result.append(a[m][n])
#         final_result.append(result)
#     return final_result
#
#
# a = [[1, 2, 3], [4, 5, 6]]
# print(solution(a))

# def solution(a):
    # final_result = []
    # for n in range(len(a[0])):
    #     result = []
    #     for m in range(len(a)-1,-1,-1):
    #         result.append(a[m][n])
    #     final_result.append(result)
    # return final_result
#     a = np.array(a)
#     b = a.transpose()
#     print(b)
#     c = np.flip(b, axis=1)
#     print(c)
#
# a = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# print(solution(a))

# def solution(a):
#     a = np.array(a)
#     # result = []
#     # for n in range(len(a)):
#     #     result.append(max(a[n]))
#     # return result
#     return np.max(a,axis=1)
#
# a =[[1, 2, 3],
#  [7, 5, 1],
#  [4, 8, 6]]
# print(solution(a))

# def solution(a,k):
#     # for n in range(len(a[0])):
#     #     for m in range(len(a)):
#     #         if a[n][m] == k:
#     #             return (n,m)
#     # return -1
#     l = k in a
#     return l
#
# a = [1, 3, 5]
#  # [7, 9, 11],
#  # [13, 15, 17]]
# print(solution(a,3))

# def solution(a):
#     result = a[0]
#     for k in range(1,len(a)):
#         result.extend(a[k])
#     return result

# def solution(a,e):
#     dict = {}
#     for n in range(len(a[0])):
#         for m in range(len(a)):
#             if a[n][m] not in dict:
#                 dict[a[n][m]] = 1
#             else:
#                 dict[a[n][m]] +=1
#     return max(dict, key=dict.get)
#
#
#
# a = [[6, 2, 3],
#  [4, 1, 6],
#  [7, 8, 6]]
# print(solution(a,1))

# def  solution(a1,a2):
#     a1 = np.array(a1)
#     a2 = np.array(a2)
#     if a1.shape == a2.shape:
#         for n in range(len(a1)):
#             if np.array_equal(a1,a2):
#                 return True
#             else:
#                 return False
#     else:
#         return -1
#
# a1 = [[1, 2],
#  [3, 4]]
# a2 = [[1, 2],
#  [3, 4]]
# print(solution(a1,a2))


# def solution(a):
    # sum = 0
    # for n in range(len(a)):
    #     for m in range(len(a[0])):
    #         sum +=a[n][m]
    # return sum
    # a = np.array(a)
    # return np.sum(a)

# def solution(a):
#     # a = np.array(a)
#     # return np.argmax(np.sum(a,axis=1))
#     result = []
#     dict = {}
#     for n in range(len(a)):
#         sum =0
#         for m in range(len(a[0])):
#             sum +=a[n][m]
#             dict[n] = sum
#         result.append(sum)
#     max_index = result.index(max(result))
#     return max_index,max(result)


# def solution(a):
#     primary = []
#     secondary = []
#     for n in range(len(a)):
#         primary.append(a[n][n])
#     for n in range(len(a)-1,-1,-1):
#         secondary.append(a[abs(n-2)][n])
#
#     return primary,secondary
#
#
# a = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# print(solution(a))


#lambda
# a=[1,2,3,4,5]
# b = list(map(lambda x:x*10,filter(lambda x:x>=2 and x%2==0,a)))
# print(b)
# b = 10
# d = 30
# c = lambda x,y:b+d
# print(c(b,d))

# def solution(a,b,n,m):
#     # code here
#     a = sorted(list(set(a)))
#     b = sorted(list(set(b)))
#     new_list = []
#     # max_len = max(a, b)
#     # min_len = min(a, b)
#     for n in a:
#         if n not in b:
#             new_list.append(n)
#     return new_list
#
# a = [9,5,-6,-5,-2,-7,4]
# b = [-5,7,-1,-6,1,-3,-6,3]
# c = 7
# d = 8
# print(solution(a,b,c,d))

import re
a = 'shankarthick93@gmail.com'

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern,a):
    print(True)
else:
    print(False)


import re

b = 'Karthickshankar'
c = r'^[a-zA-Z0-9]+t{1}[a-zA-Z0-9]+$'

if re.match(c,b):
    print(True)
else:
    print(False)
