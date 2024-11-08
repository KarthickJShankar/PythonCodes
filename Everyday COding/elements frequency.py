def Solution(arr):
    dict = {}
    for n in arr:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n]+=1
    return dict

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(Solution(arr))