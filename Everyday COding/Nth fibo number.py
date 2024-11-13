
def Solution(n,):
    a = 0
    b = 1
    count = 0
    for m in range(n-1):
        a,b = b,a
        b +=a
    return b
print(Solution(10))



