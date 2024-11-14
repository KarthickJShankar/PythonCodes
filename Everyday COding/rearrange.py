def solution(arr):
    new_list_positive = []
    new_list_negative = []
    new_list = []
    m = 0
    for n in arr:
        if n >=0:
            new_list_positive.append(n)
        else:
            new_list_negative.append(n)
    min_val = min(len(new_list_negative),len(new_list_positive))
    max_val = max(len(new_list_negative),len(new_list_positive))
    for n in range(min_val):
        new_list.append(new_list_positive[n])
        new_list.append(new_list_negative[n])
    if min_val == max_val:
        return new_list
    else:
        if len(new_list_positive) > min_val:
            new_list.extend(new_list_positive[min_val:])
        elif len(new_list_negative) > min_val:
            new_list.extend(new_list_negative[min_val:])
    return new_list
print(solution([35,-43,29,32,29,-37,46,39,-3,-43,-19,32,43,
27,28,11,43,-21,-35,-25,-2,36,-13,-6,2,-45,
-37,-4,-37,35,-46,5,-13,10,41,-34,-30,28,-47,
-9,26,21,-44,17,16,-5,39,14,-35,24,-9,12,-15,
31,-32,32,47,16,-30]))