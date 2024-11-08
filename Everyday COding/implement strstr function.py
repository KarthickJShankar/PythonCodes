def strstr(s,x):
    x_len = len(x)
    for n in range(len(s)):
        if s[n] == x[0]:
            if s[n:n + len(x)] == x:
                return n
    return -1

print(strstr('GeeksForGeeks','Fr'))
