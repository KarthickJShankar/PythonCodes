def Solution(n: int, m: int) -> str:
    # code here
    if n < m:
        return "Lesser"
    elif n > m:
        return "Greater"
    else:
        return "Equal"
print(Solution(4,8))