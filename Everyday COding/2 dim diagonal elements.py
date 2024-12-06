# def Solution(arr1):
#     new_arr_primary = []
#     new_arr_secondary =[]
#     for n in range(len(arr1)):
#         new_arr_primary.append(arr1[n][n])
#         new_arr_secondary.append(arr1[n][len(arr1)-n-1])
#     return new_arr_primary,new_arr_secondary

def solution(arr):
    result = []
    while arr:
        result += arr.pop(0)
        if arr and arr[0]:
            for row in arr:
                result.append(row.pop())
        if arr and arr[0]:
            result += arr.pop()[::-1]
        if arr and arr[0]:
            for row in arr[::-1]:
                result.append(row.pop(0))
    return result

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(solution(a))