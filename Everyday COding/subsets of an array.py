def Solution(arr):
    if len(arr)<1:
        return [[]]
    result = [[]]
    for num in arr:
        new_list = []
        for subset in result:
            new_list.append(subset+[num])
        result.extend(new_list)
    unique_subset = []
    for m in result:
        if m not in unique_subset:
            unique_subset.append(m)
    return unique_subset

nums = [1, 2, 2]
print(Solution(nums))