def Solution(arr):
    for n in range(len(arr)-1):
        for m in range(n+1,len(arr)):
            if arr[n] > arr[m]:
                arr[n],arr[m] = arr[m],arr[n]
    return arr

print(Solution([5,2,8,6,3,7,9,1,3]))

