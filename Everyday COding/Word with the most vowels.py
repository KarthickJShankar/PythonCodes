def Solution(sen):
    sen = sen.split(' ')
    dict = {}
    for n in sen:
        for m in n:
            if m in ['a','e','i','o','u']:
                if n not in dict:
                    dict[n] = 1
                else:
                    dict[n] +=1

    return max(dict,key=dict.get)
print(Solution("This is an example sentence"))