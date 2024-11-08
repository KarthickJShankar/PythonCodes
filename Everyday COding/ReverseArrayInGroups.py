def Solution(arr,k):
    if k >= len(arr):
        return arr[::-1]
    else:
        return arr[k-1::-1]+arr[-1:k-1:-1]

print(Solution([1,2,3,4,5],3))