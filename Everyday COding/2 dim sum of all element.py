def Solution(arr):
    temp = 0
    for n in arr:
        temp+=sum(n)
    return temp
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(Solution(a))
