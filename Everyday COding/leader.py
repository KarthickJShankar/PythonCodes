def Solution(arr):
    new_arr = []
    new_arr.append(arr[-1])
    max_right = arr[-1]
    for n in range(len(arr)-2,-1,-1):
        if arr[n] > max_right:
            max_right = arr[n]
            new_arr.append(arr[n])
    new_arr.reverse()
    return new_arr

print(Solution([16, 17, 4, 3, 5, 2]))