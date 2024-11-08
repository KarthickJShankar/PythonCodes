def Solution(n: int, m: int) -> str:
    # code here
    if n < m:
        return "lesser"
    elif n > m:
        return "greater"
    else:
        return "equal"
print(Solution(4,8))