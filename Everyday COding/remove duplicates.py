def Solution(arr):
    new_list = []
    for n in arr:
        if n not in new_list:
            new_list.append(n)
    return new_list

print(Solution(['11','19', '84', '84']))