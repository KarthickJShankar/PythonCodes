

def Solution(w1,w2):
    # if len(w1)!=len(w2):
    #     return False
    # else:
    #     new_list1 = sorted(list(w1.lower()))
    #     new_list2 = sorted(list(w2.lower()))
    #     if new_list1 == new_list2:
    #         return True
    # return False
    if len(w1) != len(w2):
        return False
    new1 = list(w1.lower())
    new2 = list(w2.lower())
    for n in new1:
        if n in new2:
            new2.remove(n)
    if len(new2) != 0:
        return False

    return True

print(Solution("abab", "abab"))