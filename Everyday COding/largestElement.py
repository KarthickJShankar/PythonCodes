def Solution(arr):
    # return max(arr)
    Temp = arr[0]
    for n in arr[1:]:
        if Temp < n:
            Temp = n
    return Temp


print(Solution([1,2,3,4,77,6,7]))