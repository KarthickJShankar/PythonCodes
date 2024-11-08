def Solution(n):
    a=1
    b=1
    new_list = []
    for n in range(n):
        new_list.append(a)
        a,b = b,a
        b +=a
    return new_list
print(Solution(5))