#seconf largest element
def solution(arr):
    largest = second_largest = float('-inf')
    for n in arr:
        if n > largest:
            second_largest = largest
            largest = n
        elif largest > n > second_largest:
            second_largest = n
    return second_largest

print(solution([3,4,5,2,7,1,8,6]))


#string is a palindrom
def soltuion(St):
    return St.lower() == St[::-1].lower()
print(soltuion("Malayalam"))

#sentence is a palindrom
def solution(st):
    st = st.lower().split()
    st = ''.join(st)
    return st == st[::-1]
print(solution("A man a plan a canal Panama"))

#intersection:
def solution(arr1,arr2):
    new_list = []
    min_arr = min(arr1,arr2)
    print(min_arr)
    max_arr = max(arr1, arr2)
    print(max_arr)
    for n in min_arr:
        if n in max_arr:
            new_list.append(n)
    return new_list
print(solution([1, 2, 3, 4], [3, 4, 5, 6]))


#fibonacco sequence:
def solution(n):
    a = 0
    b = 1
    for n in range(n):
        print(a,end=' ')
        a,b = b,a
        b +=a
    return a
print(solution(10))

#frequency of words in a string
def solution(st):
    st = st.split()
    dict = {}
    for n in st:
        if n not in dict:
            dict[n] = 1
        else:
            dict[n]+=1
    return dict

print(solution("the quick brown fox jumps over the lazy dog the fox"))


#find Prime numbers in a range

def soluton(a):
    new_list = []
    for n in range(a):
        count = 0
        for m in range(2,n):
            if n%m == 0:
                count+=1
        if count == 0:
            new_list.append(n)
    return new_list
print(soluton(20))


#Reverse Words in a sentence:
def solution(st):
    st = st.split()
    return ' '.join(st[::-1])
print(solution("hi there everybody"))

#Rotate list
def solution(arr,k):
    if k > len(arr):
        return -1
    return arr[-k:]+arr[:-k]

print(solution([1,2,3,4,5],1))


#frequency of characters
from collections import Counter
def solution(st):
    return Counter(st)

print(solution("hello world"))


