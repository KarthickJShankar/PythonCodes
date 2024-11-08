def Solution(st):
    st = ''.join(st.split(' ')).lower()
    print(st)
    print(st[::-1])
    return True if st==st[::-1] else False

s = "A man a plan a canal Panama"
print(Solution(s))





# import re
# s = "A man a plan a canal Panama"
# b = re.findall(r'\S',s)
# print(''.join(b))
# print(s[::-1])
# if s == s[::-1]:
#     print(True)
# else:
#     print(False)