def Solution(arr):
    for m in range(len(arr)):
        for n in range(len(arr)-1):
            if arr[n] > arr[n+1]:
                arr[n],arr[n+1] = arr[n+1],arr[n]
    return arr

print(Solution([3,5,4,2,1]))