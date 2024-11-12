import math
def Solution(n):
    if n % 2 != 0:
        return False
    x = math.log(n,)
    print(x)
    if 2**int(x) == n:
        return True
    else:
        return False

print(Solution(8))