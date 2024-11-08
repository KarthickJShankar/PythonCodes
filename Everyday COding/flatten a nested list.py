def Solution(arr):
    new_list = []
    for n in arr:
        if isinstance(n,int):
            new_list.append(n)
        else:
            new_list.extend(Solution(n))
    return new_list
    # new_list = []
    # for n in arr:
    #     if isinstance(n,int):
    #         new_list.append(n)
    #     else:
    #         for m in n:
    #             if isinstance(m,int):
    #                 new_list.append(m)
    #             else:
    #                 for k in m:
    #                     new_list.append(k)
    # return new_list

nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(Solution(nested_list))