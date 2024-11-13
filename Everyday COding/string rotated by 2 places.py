def solution(s1,s2):
    clockwise = s1[-2:]+s1[:-2]
    counter_clockwise = s1[2:]+s1[:2]
    if clockwise == s2 or counter_clockwise == s2:
        return True
    return False

print(solution('daxjheq','eqdaxjh'))


