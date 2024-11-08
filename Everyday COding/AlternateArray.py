def Solution(arr):
    new_list = []
    for n in range(len(arr)):
        if n%2 ==0:
            new_list.append(arr[n])
    return new_list


print(Solution([1,2,3,4,5,6]))
