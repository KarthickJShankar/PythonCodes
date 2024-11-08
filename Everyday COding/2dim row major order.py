
a=[[1,2,3],[4,5,6],[7,8,9]]

def Solution(arr):
    new_arr = []
    for n in range(len(arr)):
        for m in range(len(arr[0])):
            new_arr.append(arr[n][m])

    return new_arr

print(Solution(a))

