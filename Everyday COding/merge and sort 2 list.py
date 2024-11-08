def Solution(arr1,arr2):
    # new_list = arr1+arr2
    # new_list.sort()
    # return new_list
    i =0
    j=0
    new_list  = []
    while i < len(arr1) and j <len(arr2):
        new_list.append(arr1[i])
        i+=1
        new_list.append(arr2[j])
        j+=1
    while i < len(arr1):
        new_list.append(arr1[i])
        i +=1
    while j < len(arr2):
        new_list.append(arr2[j])
        j+=1
    return new_list



list1 = [1, 3]
list2 = [2, 4, 6, 8]
print(Solution(list1,list2))