def Solution(num):
    s = list(str(num))
    new_list=[]
    for n in s:
        if num%int(n) == 0:
            new_list.append(n)
    return ''.join(new_list)

print(Solution(39))
