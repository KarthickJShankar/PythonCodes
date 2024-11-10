import math
def Solution(v):
    result1 = 5*v*v+4
    result2 = 5*v*v-4
    if int(math.sqrt(result1))**2 == result1 or int(math.sqrt(result2))**2 == result2:
        return True
    else:
        return False

print(Solution(2))
