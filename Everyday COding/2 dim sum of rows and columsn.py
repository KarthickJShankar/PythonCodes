def Solution(arr):

    row_arr = []
    col_arr =[]
    for n in range(len(arr)):
        row_sum = 0
        column_sum = 0
        for m in range(len(arr[0])):
            row_sum +=arr[n][m]
            column_sum += arr[m][n]
        row_arr.append(row_sum)
        col_arr.append(column_sum)
    return row_arr,col_arr

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

print(Solution(a))
