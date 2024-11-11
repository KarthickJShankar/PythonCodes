def Solution(s: str) -> int:
    # code here
    if int(s) == 0:
        return -1
    new_list = list(s)
    for n in range(len(new_list)-1,-1,-1):
        if new_list[n] == '1':
            return n

print(Solution('0001'))