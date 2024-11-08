def Solution(arr):
    new_arr = []
    for n in arr:
        if n not in new_arr:
            new_arr.append(n)
    return new_arr

arr = [1, 2, 3, 2, 4, 3, 5, 1]
print(Solution(arr))