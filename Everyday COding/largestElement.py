def Solution(arr):
    # return max(arr)
    temp = arr[0]
    for n in arr[1:]:
        if temp < n:
            temp = n
    return temp


print(Solution([1,2,3,4,77,6,7]))