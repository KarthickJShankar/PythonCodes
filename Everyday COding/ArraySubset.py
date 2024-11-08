def Solution(arr1,arr2):
    for n in arr2:
        if n in arr1:
            arr1.remove(n)
        else:
            return "No"
    return "Yes"

print(Solution([11, 7, 1, 13, 21, 3, 7, 3],[11, 3, 55, 1, 7]))