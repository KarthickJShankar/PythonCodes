def areIsomorphic(s1, s2):
    if len(set(s1)) != len(set(s2)) or len(s1)!=len(s2):
        return False

    x = set(s1)
    m = 0
    for n in x:

        x = s2.replace(s2[m],n)
        print(x)
        m+=1

    if s1 == x:
        return True
    else:
        return False

print(areIsomorphic('rir','vev'))
