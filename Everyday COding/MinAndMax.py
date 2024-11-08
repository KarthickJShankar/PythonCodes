def Solution(arr):
    #return [min(arr),max(arr)]
    # arr.sort()
    # return [arr[0],arr[-1]]
    min = arr[0]
    max = arr[0]
    for n in arr:
        if max < n:
            max = n
        if min > n:
            min = n
    return [min,max]


print(Solution([3, 1, 4, 1, 5, 9, -2, 6]))