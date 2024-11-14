def solution(a,b):
    # return: expected length of the intersection array.

    # code here
    x = min(a, b)
    count = 0
    for n in x:
        if n in max(a, b):
            count += 1
    return count

a = [89, 24, 75, 11, 23]
b = [89, 2, 75,3]
print(solution(a,b))