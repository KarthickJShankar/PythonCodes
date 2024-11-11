def Solution(arr):
    dict = {}
    for n in arr:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n]+=1
    count = max(dict.values())
    new_val = [char for char,val in dict.items() if val == count]
    return min(new_val)

print(Solution("aaaaa"))


