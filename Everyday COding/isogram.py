def isIsogram(s):
    # Your code here
    new_set = list(set(s))
    new_list = list(s)
    new_set.sort()
    new_list.sort()
    if new_list == new_set:
        print(new_list)
        print(new_set)
        return 1
    else:
        return 0

print(isIsogram("acvfderty"))
