def firstElementKTime(arr, k):
    # code here

    dict = {}
    if k == 1:
        return arr[0]
    for n in arr:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n] += 1
            if dict[n] == k:
                return n
    return -1

print(firstElementKTime([2,3,1,4,2,5,3],2))