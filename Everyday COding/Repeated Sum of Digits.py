def repeatedSumOfDigits(N):
    # code here

    while N >= 10:
        sum_val = 0
        for n in str(N):
            sum_val += int(n)
        N = sum_val
    return N

print(repeatedSumOfDigits(1234))