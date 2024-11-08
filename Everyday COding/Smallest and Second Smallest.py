def Solution(arr):
    arr.sort()
    a = list(set(arr))
    if len(a)>1:
        return [a[0],a[1]]
    else:
        return -1


print(Solution([1,3,4,2]))


def minAnd2ndMin(arr):
    if len(arr) < 2:
        return -1

        # Initialize minimum and second minimum as infinity
    min1, min2 = float('inf'), float('inf')

    for num in arr:
        if num < min1:
            min2 = min1
            min1 = num
        elif min1 < num < min2:
            min2 = num

    # If second minimum hasn't changed, it means there's no distinct second minimum
    return [min1, min2] if min2 != float('inf') else -1


print(minAnd2ndMin([4, 1, 3, 2]))
