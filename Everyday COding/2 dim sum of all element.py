def Solution(arr):
    temp = 0
    for n in range(len(arr)):
        for m in range(len(arr[0])):
            temp +=arr[n][m]
    return temp

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(Solution(a))
