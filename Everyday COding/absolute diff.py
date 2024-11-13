def Solution(arr,X):
    for n in range(len(arr)):
        for m in range(n+1,len(arr)):
            if arr[n]-arr[m] == X:
                return True
    return -1

print(Solution([2,5,3,4,3,3,2],8))