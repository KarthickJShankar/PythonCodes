def Solution(r):
    if r == 1:
        return 1
    new_list = []
    for n in range(2,r+1):
        count = 0
        for m in range(2,n):
            if n%m == 0:
                count+=1
        if count == 0:
            new_list.append(n)
    return new_list

print(Solution(100))

