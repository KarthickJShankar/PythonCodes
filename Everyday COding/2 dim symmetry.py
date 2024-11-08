def Solution(arr):
    if len(arr) != len(arr[0]):
        return False
    for n in range(len(arr)):
        for m in range(len(arr[0])):
            if arr[n][m] != arr[m][n]:
                return False
    return True


a = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
print(Solution(a))

