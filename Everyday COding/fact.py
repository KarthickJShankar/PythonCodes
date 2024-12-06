def solution(n):
    if n <=0:
        return -1
    a = 0
    b = 1
    count = 0
    while count<n-1:
        count+=1
        a,b=b,a
        b+=a
    return b

print(solution(10))