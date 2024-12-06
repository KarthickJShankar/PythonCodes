def Solution(arr1,arr2):
    new_list = []
    if sorted(arr1) == sorted(arr2):
        return list(set(arr1))
    min_list = min(arr1,arr2)
    max_list = max(arr1,arr2)
    for n in min_list:
        if n in max_list:
            new_list.append(n)
    return list(set(new_list))

print(Solution([1, 2, 4, 3, 4],[1,2,3,4,4]))