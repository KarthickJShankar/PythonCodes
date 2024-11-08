def Solution(arr):
    count = 0
    while count<3:
        for n in range(len(arr)):
            for m in range(n+1,len(arr)):
                if arr[n]>arr[m]:
                    arr[n],arr[m] = arr[m],arr[n]
        max_val = arr.pop()
        count+=1
    return max_val

print(Solution([3,2,7,4,5,8,1,6]))

