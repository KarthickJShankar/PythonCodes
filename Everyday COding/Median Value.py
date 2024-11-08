import math
def find_median( v):
    v.sort()
    v_len = len(v)
    if v_len%2 ==1:
        return v[math.floor(v_len/2)]
    else:
        new_val = v[math.ceil(v_len/2)-1] + v[math.ceil(v_len/2)]
        return math.floor(new_val/2)

print(find_median([1,3,2,5]))