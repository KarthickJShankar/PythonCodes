def Solution(arr, k):
    # if k not in arr:
    #     return -1
    # arr.sort()
    # middle_val = int(len(arr)/2)
    # if arr[middle_val] == k:
    #     return middle_val
    # elif arr[middle_val]< k:
    #     for n in range(middle_val+1,len(arr)):
    #         if arr[n] == k:
    #             return n
    # else:
    #     for n in range(middle_val,-1,-1):
    #         if arr[n] == k:
    #             return n
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid+1
        elif arr[mid] > k:
            right = mid-1
    return  -1



print(Solution([1,2,3,4,5],4))