def Solution(arr):
    for n in range(len(arr)):
        if sum(arr[:n]) == sum(arr[n + 1:]):
            return n+1
    return -1

print(Solution([5,3,5,9,3,5,5]))