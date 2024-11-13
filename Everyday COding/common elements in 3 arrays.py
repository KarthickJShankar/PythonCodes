def Solution(arr1,arr2,arr3):
    new_list = []
    for n in arr1:
        if n in arr2 and n in arr3:
            new_list.append(n)
    x = sorted(list(set(new_list)))
    return x

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(Solution(arr1,arr2, arr3))

