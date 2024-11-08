def Solution(arr):
    for n in range(len(arr)):
        for m in range(n+1,len(arr)):
            if arr[n]>arr[m]:
                arr[n],arr[m] = arr[m],arr[n]
    return arr


print(Solution([2,1,4,5,6,3]))