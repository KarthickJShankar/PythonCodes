def Solution(arr):
    dict = {}
    for n in arr:
        if n not in dict:
            dict[n] = 1
        else:
            return arr.index(n)

print(Solution([7,4,0,9, 4, 8, 8, 2, 4, 5, 5, 1]))
