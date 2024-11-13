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



