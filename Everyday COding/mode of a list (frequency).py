import collections
def Solution(arr):
    # new_val = collections.Counter(arr)
    # print(max(new_val,key=new_val.get))
    dict = {}
    for n in arr:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n] +=1
    return max(dict,key=dict.get)

print(Solution([1, 3, 3, 7, 8, 8, 8, 9, 10]))
