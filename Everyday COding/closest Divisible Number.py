import itertools

def Solution(N,M):
    quotient = N // M
    first_inside_divisible = quotient*M
    first_outside_divisible = (quotient+1)*M
    if abs(N-first_inside_divisible) < abs(N-first_outside_divisible):
        return first_inside_divisible
    elif abs(N-first_inside_divisible) > abs(N-first_outside_divisible):
        return first_outside_divisible
    else:
        return max(first_inside_divisible,first_outside_divisible)




print(Solution(-15,6))