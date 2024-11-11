def Solution(num):
    num = list(str(num))
    new_num = ''.join(num[::-1])
    return int(new_num)

print(Solution(200))