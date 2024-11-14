def solution(s):
    #code here
        dict = {}
        if len(s) == 1:
            return s[0]
        if len(set(s)) == 1:
            return -1
        for n in s:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n]+=1
        for n in dict:
            if dict[n] == 1:
                return n
        return -1

print(solution('geeks'))