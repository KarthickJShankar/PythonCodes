def Solution(arr):
    for n in range(len(arr)):
        if n < len(arr)-1:
            if arr[n] > arr[n+1]:
                arr[n] = arr[n+1]
            else:
                arr[n] = -1
        else:
            arr[n] = -1
    return arr

print(Solution([4,2,5,1,3,2]))