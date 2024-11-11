def solution(A, B):
    # code here
    new_str1 = set(A)
    new_str2 = set(B)
    new_list = []
    for n in list(new_str1):
        if n in new_str2:
            new_str2.remove(n)
            new_str1.remove(n)
    new_list.extend(new_str1)
    for n in new_str2:
        new_list.append(n)
    if len(new_list) == 0:
        return -1
    new_list.sort()
    final = ''.join(new_list)
    return final

print(solution('geeksforgeeks','geeksquiz'))
