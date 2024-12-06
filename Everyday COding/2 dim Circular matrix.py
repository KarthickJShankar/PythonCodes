# def Solution(arr):
#     result = []
#     while arr:
#         # Append the first row
#         result += arr.pop(0)
#         print(result)
#
#         # Append the last element of each remaining row
#         if arr and arr[0]:
#             for row in arr:
#                 result.append(row.pop())
#         print(result)
#         # Append the last row in reverse order
#         if arr:
#             result += arr.pop()[::-1]
#         print(result)
#         # Append the first element of each remaining row in reverse order
#         if arr and arr[0]:
#             for row in arr[::-1]:
#                 result.append(row.pop(0))
#
#         return result
# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# b= [[00,'01,02'],
#     [10,11,12],
#     [20,21,22]]
# print(Solution(a))

import numpy as np
def solution(arr):
    result = []
    while arr:
        result += arr.pop(0)
        if arr and arr[0]:
            for row in arr:
                result.append(row.pop())
        if arr and arr[0]:
            result+=arr.pop()[::-1]
        if arr and arr[0]:
            for row in arr[::-1]:
                result.append(row.pop(0))
    return result


a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(solution(a))

