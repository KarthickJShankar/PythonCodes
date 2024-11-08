def Solution(sen):
    dict = {}
    sen = sen.split(' ')
    for n in sen:
        new_val = len(n)
        dict[n] = new_val
    return max(dict,key=dict.get)

print(Solution("The quick brown fox jumped over the lazy dog"))
