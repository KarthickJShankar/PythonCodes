def Solution(arr1,d):
    row = 0
    col = 0
    while row<len(arr1):
        if arr1[row][col]==d:
            return (row,col)
        col+=1
        if col>=len(arr1[0]):
            col = 0
        row+=1

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
print(Solution(matrix,5))