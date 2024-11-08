def maximizeMoney( N, K):
    # code here
    temp = 0
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return K

    elif N > 2:
        for n in range(1, N + 1, 2):
            temp += K
        return temp

print(maximizeMoney(5,10))