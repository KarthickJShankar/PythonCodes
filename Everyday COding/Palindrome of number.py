def Solution(n):
    n = list(str(n))
    new_n = n[::-1]
    if int(''.join(n)) == int(''.join(new_n)):
        return "Yes"
    else:
        return "No"

print(Solution(555))