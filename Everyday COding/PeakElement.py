def Solution(val):
    for n in range(len(val)):
        if n!=0 and n!=len(val)-1:
            if val[n] > val[n+1] and val[n] > val[n-1]:
                return True
        elif n==0:
            if val[n] > val[n + 1] and val[n] > val[-1]:
                return True
        elif n==len(val)-1:
            if val[n] > val[n - 1] and val[n] > val[0]:
                return True
    return False

print(Solution([1,2,3]))

