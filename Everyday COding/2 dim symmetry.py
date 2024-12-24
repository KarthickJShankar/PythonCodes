def Solution(arr):
    # if len(arr) != len(arr[0]):
    #     return False
    # for n in range(len(arr)):
    #     for m in range(len(arr[0])):
    #         if arr[n][m] != arr[m][n]:
    #             return False
    # return True
    fina_list = []
    for n in zip(*arr):
        fina_list.append(list(n))
    print(fina_list)
    if a == fina_list:
        return True
    return False

a = [
    [1, 3, 2],
    [2, 4, 5],
    [3, 5, 6]
]
print(Solution(a))

