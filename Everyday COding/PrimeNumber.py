def Solution(x):
    if x<=1:
        return "Not a Prime Number"
    for n in range(2,x):
        if x%n == 0:
            return "Not a Prime Number"

    return "Prime Number"

print(Solution(1))