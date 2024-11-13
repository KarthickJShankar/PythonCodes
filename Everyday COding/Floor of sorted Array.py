def Solution(arr,k):
    left = 0
    right = len(arr)-1

    floor_value = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > k:
            right = mid-1

        elif arr[mid] == k:
            return arr[mid]
        elif arr[mid] < k:
            floor_value = arr[mid]
            left = mid + 1
    return floor_value

arr  = [1, 2, 8, 10, 11, 12, 19]
k = 0
print(Solution(arr,k))

