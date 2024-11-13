def Solution(arr):
    for n in range(0,len(arr)-1,2):
        arr[n],arr[n+1] = arr[n+1],arr[n]
    return arr
print(Solution([1,2,3,4,5]))

