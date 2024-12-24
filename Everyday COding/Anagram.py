def Solution(s1,s2):
    if len(s1) != len(s2):
        return False
    s1 = list(s1)
    s2 = list(s2)
    # s1.sort()
    # s2.sort()
    # if s1==s2:
    #     return True
    # return False
    for n in s1:
        if n in s2:
            s2.remove(n)
    if len(s2) == 0:
        return True
    return False

print(Solution("geeks","eegsk"))


from collections import defaultdict
def solution(arr):
    final_result = defaultdict(list)
    for m in arr:
        sorted_m = ''.join(sorted(m))
        final_result[sorted_m].append(m)
    return final_result.values()

print(["listen", "silent", "enlist", "hello", "world", "cat", "act", "tac", "dog", "god"])