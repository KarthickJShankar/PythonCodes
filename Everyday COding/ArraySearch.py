def Solution(arr,ele):
    if ele in arr:
        return arr.index(ele)
    else:
        return -1


print(Solution([1,2,3,4,5],4))