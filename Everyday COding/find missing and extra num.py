#missing number
# def Solution(arr):
#     len_arr = len(arr)+1
#     total = int((len_arr * (len_arr + 1)) / 2)
#     print(total)
#     arr_total = sum(arr)
#     print(arr_total)
#     return total - arr_total
#
# print(Solution([1,2,4]))

#extra number
# def Solution(arr):
#     dict = {}
#     for n in arr:
#         if n not in dict:
#             dict[n] = 1
#         else:
#             dict[n] += 1
#     return max(dict,key=dict.get)
#
# print(Solution([1,2,3,3,4]))

#missing and Extra number

def Solution(arr):
    length = len(arr)
    total = int(length*(length+1)/2)
    print(total)
    actual_total = sum(arr)
    difference = total-actual_total
    dict = {}
    for n in arr:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n] += 1
    extra_val = max(dict,key=dict.get)
    return [extra_val, extra_val+difference]
print(Solution([1,2,3,3,5]))

# 5 = 15
# now = 14
# diff
# extra 3