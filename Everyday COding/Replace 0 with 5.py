def Solution(n):
    new_str = str(n)
    x = new_str.replace('0', '5')
    return int(''.join(x))

print(Solution(1005))
