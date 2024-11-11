def gcd(a: int, b: int) -> int:
    # code here
    for n in range(a, -1, -1):
        if b % n == 0 and a%n==0:
            return n

    return -1

print(gcd(15,16))