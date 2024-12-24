def Solution(arr):
    final_matrix=[]
    #
    # for n in range(len(arr)):
    #     new_arr = []
    #     for m in range(len(arr[0])):
    #         new_arr.append(arr[m][n])
    #     final_matrix.append(new_arr)
    # return final_matrix
    for n in zip(*arr):
        final_matrix.append(list(n))
    return final_matrix

a=[[1,2,3],[4,5,6],[7,8,9]]
print(Solution(a))