def Solution(arr1,arr2):
    final_arr = []
    for n in range(len(arr1)):
        new_arr = []
        for m in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[n][k]*arr2[k][m]
            new_arr.append(temp)

        final_arr.append(new_arr)
    return final_arr

a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6],
    [7, 8]
]
print(Solution(a,b))