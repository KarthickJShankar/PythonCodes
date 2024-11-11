def solution(S):
    # new_list = []
    # new_st = list(st)
    # temp = 0
    # for n in range(temp,len(new_st)):
    #     for m in range(n+1,len(new_st)):
    #         if new_st[n] != new_st[m]:
    #             new_list.append(new_st[n])
    #             temp = m
    #             break
    # return ''.join(new_list)
    new_st = list(S)
    new_list = []
    if len(new_st) == 0:
        return S
    for n in range(len(new_st)):
        if n == 0:
            new_list.append(new_st[n])
        elif new_st[n] != new_st[n - 1]:
            new_list.append(new_st[n])
    return ''.join(new_list)


print(solution('aaaababa'))