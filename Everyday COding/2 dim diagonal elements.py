def Solution(arr1):
    new_arr_primary = []
    new_arr_secondary =[]
    for n in range(len(arr1)):
        new_arr_primary.append(arr1[n][n])
        new_arr_secondary.append(arr1[n][len(arr1)-n-1])
    return new_arr_primary,new_arr_secondary


a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(Solution(a))