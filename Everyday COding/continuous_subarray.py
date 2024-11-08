def subArraySum(arr, target):
    if len(arr) > 1:
        for n in range(len(arr)):
            temp = arr[n]
            if temp == target:
                return [arr.index(temp) + 1, arr.index(temp) + 1]
            for m in range(n + 1, len(arr)):
                temp += arr[m]
                if temp == target:
                    return [n + 1, m + 1]
    else:
        return [1, 1] if arr[0] == target else -1
    return -1

print(subArraySum([26,3,28,7],52))