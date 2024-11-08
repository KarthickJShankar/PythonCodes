def Solution(arr,k):
    if k == len(arr):
        return [arr[k-1]]+arr[:k-1]
    elif k == 0:
        return arr[1:]+[arr[0]]
    elif k>0 and k<len(arr):
        arr[k-1],arr[k-2]=arr[k-2],arr[k-1]
        return arr

print(Solution([9, 8, 7, 6, 4, 2, 1, 3],4))