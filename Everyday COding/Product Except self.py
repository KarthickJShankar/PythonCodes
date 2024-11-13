def Solution(arr):
    new_list = []
    for n in range(len(arr)):
        temp = 1
        for m in range(len(arr)):
            if m==n:
                continue
            else:
                temp *= arr[m]
        new_list.append(temp)
    return new_list
print(Solution([10, 3, 5, 6, 2]))