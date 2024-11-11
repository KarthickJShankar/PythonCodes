def solution(A,B,C):
    if A > B:
        # A is greater than B, compare A with C
        if A < C:
            return A  # A is the middle value
        elif B > C:
            return B  # B is the middle value
        else:
            return C  # C is the middle value
    else:
        # B is greater than A, compare B with C
        if B < C:
            return B  # B is the middle value
        elif A > C:
            return A  # A is the middle value
        else:
            return C  # C is the middle value

    return middle_val

print(solution(978,150,300))
