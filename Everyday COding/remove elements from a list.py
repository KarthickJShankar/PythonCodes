def Solution(arr,e):
    for n in arr:
        if n == e:
            arr.remove(e)

    return arr

arr = [1, 2, 3, 4, 2, 5, 2, 6]
print(Solution(arr,2))