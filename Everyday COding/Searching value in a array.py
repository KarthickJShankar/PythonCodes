def Solution(k: int, arr: list) -> int:
    if k not in arr:
        return -1
    else:
        return arr.index(k) + 1

print(Solution(3,[1,2,3,4,5],))