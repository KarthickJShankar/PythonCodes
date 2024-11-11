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