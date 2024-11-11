import math
def Solution(arr):
    if len(arr)<1:
        return None
    elif len(arr)==1:
        return arr
    else:
        min_val = float("inf")
        max_val = float("-inf")

        for n in arr:
            if n < min_val:
                min_val = n

            if n > max_val:
                max_val = n
        print(max_val,min_val)

a = [-1,-2,-3,-4,-5]
Solution(a)
