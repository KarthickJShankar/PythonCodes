def pushZerosToEnd(arr):
    # code here
    new_list = []
    # new_list_without_zero =[]
    # for n in range(len(arr)):
    #     if arr[n] == 0:
    #         new_list.append(arr[n])
    #     else:
    #         new_list_without_zero.append(arr[n])
    #
    # new_list_without_zero.extend(new_list)
    # return new_list_without_zero
    for n in arr:
        if n == 0:
            new_list.append(n)
            arr.remove(n)
    arr.extend(new_list)
    return arr

print(pushZerosToEnd([1,2,0,4,3,0,5,0]))