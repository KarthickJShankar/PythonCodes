def Solution(arr):
    if len(arr)<1:
        return [[]]
    final_list =[]
    for n in range(len(arr)):
        for m in range(n+1,len(arr)+1):
            final_list.append(arr[n:m])
    return final_list


print(Solution([1,2,3]))
