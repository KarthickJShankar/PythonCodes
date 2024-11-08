def Solution(arr1,d):
    for n in range(len(arr1)):
        for m in range(len(arr1[0])):
            if d == arr1[n][m]:
                return (n,m)

    return -1

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
print(Solution(matrix,5))