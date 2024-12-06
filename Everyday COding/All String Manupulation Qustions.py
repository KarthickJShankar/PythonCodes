# def reverse_vowels(st):
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
#     st = list(st)
#     new_list = []
#     new_vowel = []
#     for i,n in enumerate(st):
#         if n in vowels:
#             new_list.append(i)
#             new_vowel.append((n))
#     # print(new_vowel,new_list)
#     new_vowel = new_vowel[::-1]
#     count = 0
#     for m in new_list:
#         st[m] = new_vowel[count]
#         count +=1
#     print(''.join(st))
#
# reverse_vowels("Hello!") # "Holle!"
# reverse_vowels("Tomatoes") # "Temotaos"
# reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
# reverse_vowels("aeiou") # "uoiea"
# reverse_vowels("why try, shy fly?") # "why try, shy fly?"

#

#Rearrange Character by Frequency
# def solution(st):
#     my_dict = {}
#     new_list = []
#     for n in st:
#         if n not in my_dict:
#             my_dict[n]= 1
#         else:
#             my_dict[n]+=1
#     sorted_dict = dict(sorted(my_dict.items(), key=lambda items:items[1], reverse=True))
#     print(sorted_dict)
#     for key,val in sorted_dict.items():
#         new_list.append(key*val)
#     return ''.join(new_list)
#
#
# print(solution('programming'))


#Avoid Consecutive Repeats
# def solution(st):
#     new_dict = {}
#     start = 0
#     max_len =  0
#     for idx,val in enumerate(st):
#         if val in new_dict and new_dict[val] >=start:
#             start = new_dict[val]+1
#         new_dict[val] = idx
#         max_len = max(max_len,idx-start+1)
#     return max_len
#
# print(solution('abcacbab'))

#Avoid Character Repeats
# from collections import  Counter
# def solution(st):
#     new_dict = Counter(st)
#
#     new_dict = sorted(new_dict.items(),key=lambda items:items[1],reverse=True)
#     print(new_dict)
#     max_key_len = new_dict[0][1]
#     print(max_key_len)
#     if max_key_len > (len(st)+1)//2:
#         return ''
#     result = ['']*len(st)
#     idx = 0
#     for char, count  in new_dict:
#         for _ in range(count):
#             result[idx] = char
#             idx+=2
#         if idx > len(st):
#             idx = 1
#     return ''.join(result)
#
# print(solution('aaabb'))


# def solution(st):
#     new_dict = {}
#     start = 0
#     max_len = 0
#     for idx,val in enumerate(st):
#         if val in new_dict and new_dict[val] >= start:
#             start = new_dict[val]+1
#         new_dict[val] = idx
#
#         max_len = max(max_len,idx-start+1)
#     return max_len
#
# print(solution('ababcbb'))
#
# def solution(arr):
#     final_list = [[]]
#     for n in arr:
#         final_list += [m +[n] for m in final_list]
#     return final_list
# print(solution([1,2,3]))
#
# def solution(arr):
#
#     final_list = [[]]
#     for n in range(len(arr)):
#         new_list = []
#         for m in range(n+1, len(arr)+1):
#             new_list.append(arr[n:m])
#         final_list.append(new_list)
#     return final_list
#
# print(solution([1,2,3]))


# def solution(st):
#     vowels = ['a','e','i','o','u']
#     vowel_list = []
#     consonents = []
#     for n in st:
#         if n in vowels:
#             vowel_list.append(n)
#         else:
#             consonents.append(n)
#     return ''.join(vowel_list+consonents)
#
# print(solution('hello'))


# def solution(st):
#     new_list = []
#     for idx,val in enumerate(st):
#
#         if val in new_list:
#             if val == new_list[-1]:
#                 new_list.pop()
#         else:
#             new_list.append(val)
#     return ''.join(new_list)
#
#
# print(solution('azxxzy'))

# def solution(st):
#     result = []
#     st = st.split()
#     for n in st:
#         result.append(n[::-1])
#     return ' '.join(result)
#
# print(solution('Hello World  Python'))
# a = [3,1,2,4]

# from collections import Counter
# def solution(st):
#     result = Counter(st)
#     print(result)
#     new_list = []
#     for idx, val in result.items():
#         new_list.append(idx)
#         new_list.append(str(val))
#     return ''.join(new_list)
#
# print(solution('aaAAbb'))

#To check which has the least frequency
# from collections import Counter
# def solution(st):
#     result = Counter(st)
#     new_list = []
#     result = sorted(result.items(), key=lambda x:x[1], reverse=False)
#     for idx,val in result:
#         new_list.append(idx)
#     return ''.join(new_list)
#
# print(solution('aabbccdde'))
#
# #To check which occurs more odd times and even times
#
# from collections import Counter
#
# def solution(st):
#     result = Counter(st)
#     odd_dict = {}
#     even_dict = {}
#     for idx,val in result.items():
#         if result[idx] %2 == 0:
#             even_dict[idx] = result[idx]
#         else:
#             odd_dict[idx] = result[idx]
#     new_list = []
#     for idx,val in odd_dict.items():
#         new_list.append(idx)
#     for idx,val in even_dict.items():
#         new_list.append(idx)
#     return ''.join(new_list)
#
# print(solution('aabccddee'))

#longest palindrome substring
#def solution(st):
#     max_len = 0
#     for n in range(len(st)):
#         for m in range(len(st),n,-1):
#             if st[n:m] == st[n:m][::-1]:
#                 max_len = max(max_len,len(st[n:m]))
#     return max_len
# print(solution('abacbaaab'))

#
# from collections import Counter
# def solution(st):
#     result = Counter(st)
#     new_list = []
#     for idx,val in result.items():
#         new_list.append(idx)
#     return ''.join(new_list)
#
# print(solution('programming'))

# def solution(st):
#     new_list = []
#     for n in range(len(st)):
#         if n ==0:
#             new_list.append(st[n])
#         else:
#
#             if st[n] == new_list[-1]:
#                 pass
#             else:
#                 new_list.append(st[n])
#     return ''.join(new_list)
# print(solution('programming'))


# from collections import Counter
# def solution(st,k):
#     result= Counter(st)
#     if len(result) == k:
#         return st
#     elif len(result) < k:
#         return -1
#     else:
#         new_dict = {}
#
#         max_len = 0
#         new_list = []
#         for m in range(len(st)):
#             for n in range(m,len(st)):
#                 if len(new_dict)<=k:
#                     if st[n] not in new_dict:
#                         new_dict[st[n]] = 1
#                         new_list.append(st[n])
#                     else:
#                         new_dict[st[n]] +=1
#                         new_list.append(st[n])
#
#             max_len = max(max_len,len(new_list))
#
#         return max_len
#
# print(solution('aabacbebebe',3))




# def solution(st,k):
#     max_len = 0
#     left = 0
#     new_dict = {}
#     for right,val in enumerate(st):
#         new_dict[val] = right
#         if len(new_dict) > k:
#             left = new_dict.get(st[left],0)
#             first_key = next(iter(new_dict))
#             new_dict.pop(first_key)
#             left +=1
#         max_len = max(max_len,right-left+1)
#     return max_len
#
# print(solution('aabccaebd',3))



# def solution(st):
#     max_val = 0
#     left = 0
#     new_dict = {}
#     for right,val in enumerate(st):
#         new_dict[val] = right
#         if len(new_dict) > 2:
#             left = min(new_dict.values())
#             remove_index = st[left]
#             new_dict.pop(remove_index)
#             left +=1
#         max_val = max(max_val,right-left+1)
#     return max_val
#
# print(solution('eceba'))


# def solution(num):
#     new_list = []
#     for n in range(num):
#         if n<10:
#             new_list.append(str(n)+str(n))
#         else:
#             new_list.append(str(n)[::-1])
#     return new_list
# print(solution(110))


# def solution(st,k):
#     max_len = 0
#     new_dict = {}
#     left = 0
#
#     for right, val in enumerate(st):
#         new_dict[val] = right
#         if len(new_dict) > k:
#             result = st[left]
#             new_dict.pop(result)
#             left = min(new_dict.values())
#         max_len = max(max_len,right-left+1)
#     return max_len
# print(solution('aabacbebebe',3))




def solution(st,k):
    max_len = 0
    left = 0
    new_dict = {}
    for right,val in enumerate(st):
        if len(new_dict)<=1:
            new_dict[val] = new_dict.get(val,0)+1
        count = 0
        final = next(iter(new_dict))
        if val != final:
            if count<k:
                new_dict[final] = new_dict.get(final,0)+1
                count+=1
        max_len = max(max_len,right-left+1)
        if count== k:
            left = new_dict[final]
    return max_len

print(solution('AABABB',1))


#
# def solution(st):
#     max_len = 0
#     left = 0
#     new_dict = {}
#
#     for right,val in enumerate(st):
#         if val in new_dict:
#             left = new_dict[val] + 1
#
#         new_dict[val] = right
#
#         max_len = max(max_len, right-left+1)
#     return max_len
# print(solution('abcabcbb'))




# def solution(st):
#     max_len = 0
#     left = 0
#     new_dict = {}
#
#     for right,val in enumerate(st):
#         if val in new_dict:
#             left_char = new_dict[val]
#             new_dict[val] -=1
#             if new_dict[val] == 0:
#                 del new_dict[val]
#             left+=1
#         new_dict[val] = new_dict.get(st[right],0)+1
#         max_len = max(max_len,right-left+1)
#     return max_len
#
# print(solution('abcabcbb'))
########################################################################################################################







