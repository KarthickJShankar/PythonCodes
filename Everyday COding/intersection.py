def Solution(arr1,arr2):
    new_list = []
    for n in arr1:
        if n in arr2:
            new_list.append(n)
    return list(set(new_list))

print(Solution([1, 2, 3, 4, 4],[3, 4, 5, 6, 7]))