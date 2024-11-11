def Solution(arr,x):
    new_list = []
    for n in arr:
        if n <x :
            new_list.append(n)
    return len(new_list)

print(Solution([1,2,3,4,5],5))