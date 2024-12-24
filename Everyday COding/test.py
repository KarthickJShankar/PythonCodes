# import itertools
# def func():
#     for n in itertools.count(10):
#         print(n)
#         if n%23 == 0:
#             return True
# print(func())

#Max and Min
# def solution(arr):
#     left = float("inf")
#     right = 0
#     for n in arr:
#         if n > right:
#             right = n
#         if n < left:
#             left = n
#     return [left,right]

#Third Highest
# def Solution(arr):
#     right = third_largest = float("-inf")
#     second_right = float("-inf")
#     for n in arr[1:]:
#         if n > right:
#             third_largest = second_right
#             second_right = right
#             right = n
#
#         if n > second_right and n != right:
#             third_largest = second_right
#             second_right = n
#         if n > third_largest and n!=second_right and n!=right:
#             third_largest = n
#
#     return third_largest
# print(Solution([5,2,8,6,7,3,9,1,3]))


#Third_Lowest
# def Solution(arr):
#     lowest = second_lowest = third_lowest = float("inf")
#     for n in arr:
#         if n < lowest:
#             third_lowest = second_lowest
#             second_lowest = lowest
#             lowest = n
#         elif n < second_lowest and n!=lowest:
#             third_lowest = second_lowest
#             second_lowest = n
#         elif n < third_lowest and n!=second_lowest and n!=lowest:
#             third_lowest = n
#     return third_lowest
# print(Solution([5,2,8,6,7,3,9,1,3]))

#decorator
# def decorator(func):
#     def wrapper(*args):
#         val = func(*args)
#         return val*2
#     return wrapper
#
# @decorator
# def calculate(*arg):
#     result = 1
#     for n in arg:
#         result*=n
#     print(result)
#     return result
#
# print(calculate(2,3,4,5))


#generator

# def generator(arr):
#     for n in arr:
#         yield n
#
# g = generator([1,2,3,4])
# for n in g:
#     print(n*2)



#accessmodifiers
# class Access:
#     def __init__(self,b):
#         self.a = 0
#         self.b = b
#     # def __calculate_a(self):
#     #     return self.a*5
#     def _calculate_b(self):
#         return self.b*10
#
#     def get_a(self):
#         return self.a*5
#     def set_a(self,a):
#         self.a = a
# class C(Access):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c = c
#
#     def calculate_c(self):
#         return self.a*self.b/self.c
#
#
# a = Access(10)
# # c = C(5,10,20)
# # d = c.calculate_c()
# # e = c._calculate_b()
# a.set_a(20)
# print(a.get_a())
# # print(e)
# # print(c.calculate_c())


# #Thirdsmallest
# def Soltuion(arr):
#     largest = sec_largest = third_largest = float("inf")
#     for n in arr:
#         if n < largest:
#             third_largest = sec_largest
#             sec_largest = largest
#             largest = n
#         elif largest <n < sec_largest:
#             third_largest = sec_largest
#             sec_largest = n
#         elif sec_largest < n < third_largest:
#             third_largest = n
#     return third_largest
#
# print(Soltuion([4,2,7,5,9,6,1]))


#transpose
import numpy as np
# def solution(a):
#
#     final_result = []
#     for n in range(len(a[0])):
#         result = []
#         for m in range(len(a)):
#             result.append(a[m][n])
#         final_result.append(result)
#     return final_result
#
#
# a = [[1, 2, 3], [4, 5, 6]]
# print(solution(a))

# def solution(a):
    # final_result = []
    # for n in range(len(a[0])):
    #     result = []
    #     for m in range(len(a)-1,-1,-1):
    #         result.append(a[m][n])
    #     final_result.append(result)
    # return final_result
#     a = np.array(a)
#     b = a.transpose()
#     print(b)
#     c = np.flip(b, axis=1)
#     print(c)
#
# a = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# print(solution(a))

# def solution(a):
#     a = np.array(a)
#     # result = []
#     # for n in range(len(a)):
#     #     result.append(max(a[n]))
#     # return result
#     return np.max(a,axis=1)
#
# a =[[1, 2, 3],
#  [7, 5, 1],
#  [4, 8, 6]]
# print(solution(a))

# def solution(a,k):
#     # for n in range(len(a[0])):
#     #     for m in range(len(a)):
#     #         if a[n][m] == k:
#     #             return (n,m)
#     # return -1
#     l = k in a
#     return l
#
# a = [1, 3, 5]
#  # [7, 9, 11],
#  # [13, 15, 17]]
# print(solution(a,3))

# def solution(a):
#     result = a[0]
#     for k in range(1,len(a)):
#         result.extend(a[k])
#     return result

# def solution(a,e):
#     dict = {}
#     for n in range(len(a[0])):
#         for m in range(len(a)):
#             if a[n][m] not in dict:
#                 dict[a[n][m]] = 1
#             else:
#                 dict[a[n][m]] +=1
#     return max(dict, key=dict.get)
#
#
#
# a = [[6, 2, 3],
#  [4, 1, 6],
#  [7, 8, 6]]
# print(solution(a,1))

# def  solution(a1,a2):
#     a1 = np.array(a1)
#     a2 = np.array(a2)
#     if a1.shape == a2.shape:
#         for n in range(len(a1)):
#             if np.array_equal(a1,a2):
#                 return True
#             else:
#                 return False
#     else:
#         return -1
#
# a1 = [[1, 2],
#  [3, 4]]
# a2 = [[1, 2],
#  [3, 4]]
# print(solution(a1,a2))


# def solution(a):
    # sum = 0
    # for n in range(len(a)):
    #     for m in range(len(a[0])):
    #         sum +=a[n][m]
    # return sum
    # a = np.array(a)
    # return np.sum(a)

# def solution(a):
#     # a = np.array(a)
#     # return np.argmax(np.sum(a,axis=1))
#     result = []
#     dict = {}
#     for n in range(len(a)):
#         sum =0
#         for m in range(len(a[0])):
#             sum +=a[n][m]
#             dict[n] = sum
#         result.append(sum)
#     max_index = result.index(max(result))
#     return max_index,max(result)


# def solution(a):
#     primary = []
#     secondary = []
#     for n in range(len(a)):
#         primary.append(a[n][n])
#     for n in range(len(a)-1,-1,-1):
#         secondary.append(a[abs(n-2)][n])
#
#     return primary,secondary
#
#
# a = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# print(solution(a))


#lambda
# a=[1,2,3,4,5]
# b = list(map(lambda x:x*10,filter(lambda x:x>=2 and x%2==0,a)))
# print(b)
# b = 10
# d = 30
# c = lambda x,y:b+d
# print(c(b,d))

# def solution(a,b,n,m):
#     # code here
#     a = sorted(list(set(a)))
#     b = sorted(list(set(b)))
#     new_list = []
#     # max_len = max(a, b)
#     # min_len = min(a, b)
#     for n in a:
#         if n not in b:
#             new_list.append(n)
#     return new_list
#
# a = [9,5,-6,-5,-2,-7,4]
# b = [-5,7,-1,-6,1,-3,-6,3]
# c = 7
# d = 8
# print(solution(a,b,c,d))

# import re
# a = 'shankarthick93@gmail.com'
#
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# if re.match(pattern,a):
#     print(True)
# else:
#     print(False)
#
#
# import re
#
# b = 'Karthickshankar'
# c = r'^[a-zA-Z0-9]+t{1}[a-zA-Z0-9]+$'
#
# if re.match(c,b):
#     print(True)
# else:
#     print(False)

# a = 'abcdef'
# b = 'bcd'
# if b in a:
#     print(1)
# else:
#     print(2)
# from collections import Counter
# a = 'tan'
# b='ant'
# print(Counter(a), Counter(b))
# if Counter(a) == Counter(b):
#     print(1)
# else:
#     print(2)

# def solution(arr,d):
#     return arr[d:]+arr[:d]
#
# print(solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20],3))
# def lenOfLongestSubarr(arr, k):
#     # code here
#     new_list = []
#     sum_list = []
#     temp = 0
#     for n in range(len(arr)):
#         for m in range(n + 1, len(arr)+1):
#             new_list.append(arr[n:m])
#     print(new_list)
#     for i in new_list:
#         sum_list.append(sum(i))
#     for idx, j in enumerate(sum_list):
#
#         if j == 0:
#             temp = max(temp, len(new_list[idx]))
#     return temp
#
#
# a = [15, -2, 2, -8, 1, 7, 10, 23]
# k = 3
# print(lenOfLongestSubarr(a,k))

# a = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
#
#
# def rowWithMax1s(arr):
#     # code here
#     new_dict = {}
#     for idx, val in enumerate(arr):
#         temp = 0
#         for n in val:
#             if n == 1:
#                 temp += 1
#         new_dict[idx] = temp
#     return max(new_dict.items(), key=lambda x:x[1])[0]
#
# print(rowWithMax1s(a))

# def findTriplets(arr):
#     # code here
#     final_list = [[]]
#     for n in arr:
#         final_list += [m + [n] for m in final_list]
#     final_list.pop(0)
#     print(final_list)
#     for m in final_list:
#         if len(m) == 3:
#             if sum(m) == 0:
#                 return True
#     return False
#
# a = [44, 33, 18, -22, -37, -13, -35, 37, -13]
# print(findTriplets(a))


# def solution(arr):
#     for n in range(len(arr)):
#         left = n+1
#         right = left+1
#         is_True =True
#         while is_True:
#             if n == len(arr)-1:
#                 if arr[n] + arr[0] + arr[1] == 0:
#                     return True
#                 return False
#             elif n == len(arr)-2:
#                 if arr[n] + arr[-1] + arr[0] == 0:
#                     return True
#                 else:
#                     is_True = False
#             else:
#                 if arr[n]+arr[left]+arr[right] == 0:
#                     return True
#                 else:
#                     is_True = False
#     return False
# print(solution([-26, 22 ,-35, 0, -20, -11, 0, -47, -36, 4]))


# def solution(st,k):
#     left = 0
#     new_dict = {}
#     max_freq = 0
#     max_count = 0
#     for right,val in enumerate(st):
#         new_dict[val] = new_dict.get(val,0)+1
#         max_count = max(max_count,new_dict[val])
#         while (right-left+1)-max_count > k:
#             new_dict[st[left]] -=1
#             left+=1
#         max_freq = max(max_freq,right-left+1)
#     return max_freq
#
# print(solution('bbabaab',1))
#
# def solution(st):
#     a = len(st)
#     new_list = []
#     for m in range(len(st)-2):
#         while a > m + 2:
#             if st[m:a] == st[m:a][::-1]:
#                 new_list.append(''.join(st[m:a]))
#             else:
#                 a -= 1
#         a = len(st)


#
# print(solution('msgygo'))
#
#
# def spirallyTraverse(self, mat):
#     # code here
#     new_list = []
#     while mat:
#         new_list += mat.pop(0)
#         if mat and mat[0]:
#             for m in mat:
#                 new_list.append(m.pop())
#         if mat and mat[0]:
#             new_list += mat[-1].pop()
#         if mat and mat[0]:
#             for m in mat:
#                 new_list.append(m.pop(0))
#     return new_list

# def rearrange(arr):
#     ##Your code here
#     count = 1
#     new_list = []
#     half_val = int(len(arr) * 0.5)
#     while count <= half_val:
#         new_list.extend([arr[-count],arr[count-1]])
#         count += 1
#     if len(arr)%2 == 0:
#         return new_list
#     else:
#         new_list.append(arr[half_val])
#         return new_list
#
# print(rearrange([890, 289, 483, 519, 550, 447, 946, 957, 92, 783]))

# Kedane's theorem

# def solution(arr):
#     new_list= []
#     sum_list = []
#     result = 0
#     for n in range(len(arr)):
#         for m in range(n+1,len(arr)+1):
#             new_list.append(arr[n:m])
#     print(new_list)
#     for val in new_list:
#         sum_list.append(sum(val))
#     print(sum_list)
#
#     max_val = max(sum_list)
#     for idx,val in enumerate(sum_list):
#         if val == max_val:
#             result = max(result, len(new_list[idx]))
#     return result
# def solution(arr):
#     current_sum = 0
#     max_sum = arr[0]
#     for n in arr:
#         if current_sum<0:
#             current_sum = 0
#         current_sum +=n
#         max_sum = max(max_sum,current_sum)
#     return max_sum
#
# print(solution([2, 3, -8, 7, -1, 2, 3]))

# def twoRepeated(arr):
#     # Your code here
#     new_dict = {}
#     new_list = []
#     for num in arr:
#         if str(num) not in new_dict:
#             new_dict[str(num)] = 1
#         else:
#             new_list.append(num)
#     return new_list
# print(twoRepeated([1,2,2,1]))

# def solution(st):
#     left =0
#     new_dict = {}
#     max_count = 0
#     for right,val in enumerate(st):
#         if val in new_dict and new_dict[val]>=left:
#             left = new_dict[val]+1
#         new_dict[val] = right
#         max_count = max(max_count,right-left +1)
#     return max_count
# print(solution('abcbcabbc'))

# def solution(st1,st2):
#     new_dict1 = {}
#     new_dict2 = {}
#     for char1,char2 in zip(st1,st2):
#         if char1 in new_dict1:
#             if new_dict1[char1] != char2:
#                 return False
#         else:
#             new_dict1[char1] == char2
#
#         if char2 in new_dict2:
#             if new_dict2[char2] !=char1:
#                 return False
#         else:
#             new_dict2[char2] = char1
#     return True

# def solution(arr):
#     current_sum = 0
#     max_sum = arr[0]
#     for n in arr:
#         if current_sum<0:
#             current_sum = 0
#         current_sum+=n
#         max_sum = max(max_sum,current_sum)
#     return max_sum
#
# print(solution([1,-2,7,-3,1,4,-8,1]))
#
# def smallestSubWithSum(x, arr):
#     # Your code goes here
#     current_sum = 0
#     count = 0
#     for n in arr:
#         if current_sum <= 0:
#             current_sum = 0
#             count = 0
#         current_sum += n
#         count += 1
#
#         if current_sum >= x:
#             return count
#
# print(smallestSubWithSum(1,[0,1,3,5]))

# def findElement(arr):
#     # code here
#     for idx, val in enumerate(arr):
#         if idx == len(arr) - 1:
#             return -1
#         left = float('-inf')
#         right = float('inf')
#         for n in arr[:idx]:
#             left = max(left, n)
#         for m in arr[idx + 1:]:
#             right = min(right, m)
#         if left < val < right:
#             return val
#     return -1
#
# print(findElement([4,2,5,7]))

# def romanToDecimal(s):
#     # code here
#     previous_val = 0
#     result = 0
#     new_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     for n in reversed(s):
#         current_val = new_dict[n]
#         if current_val < previous_val:
#             result -= current_val
#         else:
#             result += current_val
#         previous_val = current_val
#     return result
# print(romanToDecimal('XXIV'))

# a = [1,2,3,4]
# b = list(reversed(a))
# print(b)

# def swapElements(arr, n):
#     for n in range(n-2):
#         arr[n],arr[n+2] = arr[n+2],arr[n]
#     return arr
#
# print(swapElements([1,2,3,4,5],5))

from collections import Counter
# import re
# def checkPangram(s):
#     # code here
#     param = re.sub('[^a-zA-z]+','', s).lower()
#     param = ''.join(param)
#     print(param)
#     result = set(param)
#     if len(result) == 26:
#         return True
#     else:
#         return False
#
# print(checkPangram('Bawds jog, flick quartz, vex nymph'))

# def minNumber(arr):
#     # Your code here
#     arr_c = arr
#     arr_a = arr
#     low = min(arr)
#     count_c = 0
#     count_a = 0
#     for n in range(len(arr)):
#         arr1 = arr_c[-count_c:] + arr_c[:-count_c]
#         count_c += 1
#         if arr1[-1] == low:
#             return count_c-1
#         arr2 = arr_a[count_a:] + arr_a[:count_a]
#         count_a += 1
#         if arr2[-1] == low:
#             return count_a-1
# print(minNumber([3,1,5,4,2]))


# def secFrequent(arr):
#     # code here
#     arr1 = Counter(arr)
#     max_val = max(arr1, key=arr1.get)
#
#     del arr1[max_val]
#     return max(arr1, key=arr1.get)
# print(secFrequent(['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']))

# def roundToNearest(str):
#     # Complete the function
#     last_val = int(str[-1])
#     first_Val = int(str[0])
#     if last_val > 5 and last_val <= 9:
#         result = int(str) + 10 - last_val
#     else:
#         result = int(str) - int(last_val)
#     return result
#
# print(roundToNearest('2648946165654'))


a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[1,11,12],
     [13,5,15],
     [7,17,9]]

# def solution(a,b):
#     new_list= []
#     for n,m in zip(a,b):
#         print(n,m)
#         new_list.append(sum(n)+sum(m))
#     return new_list
# print(solution(a,b))

# def solution(a,b):
#     new_a = []
#     new_b = []
#     for n in a:
#         for m in n:
#             new_a.append(m)
#     for m in b:
#         for n in m:
#             new_b.append(n)
#     print(new_a)
#     print(new_b)
#     result = dict(zip(new_a,new_b))
#     return result

# def solution(a):
#     for n in zip(*a):
#         print(list(n))
# c = [1,2,3,4,5]
# d = [1,4,7,8,9]
# def solution(c,d):
#     new_list = []
#     for n,m in zip(c,d):
#         print(n,m)
#         if n==m:
#             new_list.append(n)
#     return new_list
# print(solution(c,d))


# def solution(st1,st2):
#     # new_list = []
#     # for n,m in zip(st1,st2):
#     #     new_list.append(n+m)
#     # return ''.join(new_list)
#     new_list = []
#     st1 = sorted(st1)
#     st2 = sorted(st2)
#     for n,m in zip(st1,st2):
#         if n!=m:
#             return False
#         else:
#             new_list.append(n)
#     return new_list
# print(solution('abc','abca'))

# c = [1,2,3,4,5]
# d = [1,4,7,8,9]
# def solution(a,b):
#     result = [n for n,m in zip(a,b) if n==m]
#     return result
#
# print(solution(c,d))

# a  = [(1,2,3),(4,5,6)]
# b = [(7,8,9),(10,11,12)]
# def solution(a,b):
#     new_list = []
#     for n in zip(*a,*b):
#         new_list.extend(n)
#     return new_list
#
# print(solution(a,b))