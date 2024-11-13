from itertools import permutations

def Solutions(arr):
    count = 0
    for n in permutations(arr):
        count+=1
        print(n)
    return count

print(Solutions([5,3,2,4,1]))