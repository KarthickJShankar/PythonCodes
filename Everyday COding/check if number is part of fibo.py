import math

def Solution(n):
    return int(math.sqrt(n))**2 == n
def is_fibo(n):
    return Solution(5*n*n+4) or Solution(5*n*n-4)

number = 14
print(is_fibo(13))