#Reverse The String
def solution(st):
    return st[::-1]

print(solution('hello'))
########################################################################################################################

#Check for palindrome
def solution(st):
    return st.lower() == st[::-1].lower()

print(solution('racecar'))
########################################################################################################################

#Number of Vowels and Consonants
def solution(st):
    vowels = ['a','e','i','o','u']
    new_dict = {'vowels':0, 'Consonants':0}
    for n in st.lower():
        if n in vowels:
            new_dict['vowels'] +=1
        elif n.isalnum():
            new_dict['Consonants'] +=1
    return new_dict

print(solution('Hello World'))
########################################################################################################################

#Find the first non repeating character
def solution(st):
    new_dict = {}
    for n in st:
        new_dict[n] = new_dict.get(n,0)+1
    print(new_dict)
    for n in st:
        if new_dict[n] == 1:
            return n
    return -1
print(solution('swiss'))
########################################################################################################################

#Remove Duplicates
def solution(st):
    new_list = []
    for n in st:
        if n not in new_list:
            new_list.append(n)
    return ''.join(new_list)

print(solution('programming'))

#Reverse each word
def solution(st):
    new_list = []
    st = st.split()
    for n in st:
        new_list.append(n[::-1])
    print(new_list)
    return ' '.join(new_list)

print(solution('Python is fun'))
########################################################################################################################

#Count unique character
def solution(st):
    st = st.split()
    st = ''.join(st)
    new_list = []
    for n in st.lower():
        if n not in new_list:
            new_list.append(n)
    return len(new_list)

print(solution('programmingP'))
########################################################################################################################

#Check if string is palindrome
def solution(st):
    new_list = []
    for n in st.lower():
        if n.isalpha():
            new_list.append(n)
    st = ''.join(new_list)
    print()
    return st == st[::-1]

print(solution('A man, a plan, a canal: Panama'))
########################################################################################################################

#Find the most frequent character
from collections import Counter
def solution(st):
    new_dict = Counter(st)
    max_freq = new_dict.most_common(1)
    print(max_freq)
    if max_freq:
        return max_freq[0][0]

print(solution('banana'))
########################################################################################################################

#Remove duplicates keeping the last ocurrance
def solution(st):
    new_list = []
    for n in st:
        if n not in new_list:
            new_list.append(n)
        elif n in new_list:
            new_list.remove(n)
            new_list.append(n)
    return ''.join(new_list)
print(solution('programming'))
########################################################################################################################

#find all substrings
def solution(st):
    new_list = []
    for n in range(len(st)):
        for m in range(n+1,len(st)+1):
            new_list.append(st[n:m])
    return new_list
print(solution('abc'))
########################################################################################################################
#Longest substring without repetition
def solution(st):
    max_len = 0
    left = 0
    new_dict = {}

    for right,val in enumerate(st):
        if val in new_dict:
            left = new_dict[val]+1
        new_dict[val] = right
        max_len = max(max_len,right-left+1)
    return max_len

print(solution('abcabcbb'))
########################################################################################################################

#Anagram Check
from collections import Counter
def solution(st1,st2):
    return Counter(st1) == Counter(st2)

print(solution('listen','silent'))
########################################################################################################################

#permutions
from itertools import permutations

def solution(st):
    new_list = []
    for n in permutations(st):
        new_list.append(''.join(n))
    return new_list
print(solution('abc'))
########################################################################################################################

#longest palindromic substring
def solution(st):
    if st == st[::-1]:
        return len(st)
    new_dict = {}
    for n in range(len(st)):
        for m in range(len(st)-1,1,-1):
            if st[n:m] == st[n:m][::-1]:
                new_dict[st[n:m]] = len(st[n:m])
    return max(new_dict, key=new_dict.get), max(new_dict.values())

print(solution('babad'))
########################################################################################################################

#4. Minimum Window Substring (Sliding Window)
#Write a function to find the smallest substring in a string s that contains all the characters of a string t.

def solution(st,t):
    new_list = []
    min_list = []
    max_len = 0
    left = 0
    new_dict={}
    for right,val in enumerate(st):
        new_dict[val] = new_dict.get(val,0)+1
        if val not in new_list:
            new_list.append(val)
        if len(new_dict)>=len(t):
            if ''.join(sorted(t)) in ''.join(sorted(new_list)):
                left_side = st[left]
                new_dict[left_side] -=1
                if new_dict[left_side]==0:
                    del new_dict[left_side]
            left+=1
            max_len = max(max_len,right-left+1)
            min_list.append(max_len)
    return min(min_list)


print(solution('ADOBECODEBANC','ABC'))
########################################################################################################################
#Check if the str is a substring:
def solution(st,st1):
    # new_list = []
    # for n in range(len(st)):
    #     for m in range(n+1,len(st)+1):
    #         new_list.append(st[n:m])
    # print(new_list)
    # return st1 in new_list

    return st1 in st

print(solution('abc','ab'))

########################################################################################################################

#Reverse words in a string

def solution(st):
    st = st.split()
    new_list = []
    for n in st[::-1]:
        new_list.append(n)
    return ' '.join(new_list)

print(solution('Hello World'))
########################################################################################################################

#Check if strings are rotation of each other
from collections import Counter
def solution(st1,st2):
    if len(st1)!=len(st2) or Counter(st1) != Counter(st2):
        return False
    return st2 in (st1+st1)

print(solution('abcd','dabc'))

########################################################################################################################

#String complete Compression
from collections import Counter
def solution(st):
    new_dict = Counter(st)
    new_list= []
    # for n in st:
    #     if n not in new_dict:
    #         new_dict[n] = new_dict.get(n,0)+1
    #     else:
    #         new_dict[n] +=1
    for key,val in new_dict.items():
        new_list.append(key+str(val))

    return ''.join(new_list)

print(solution('aabcccccaaa'))

########################################################################################################################
#String Compression:

def solution(st):
    new_list = []
    count = 1
    for n in range(1,len(st)):
        if st[n] == st[n-1]:
            count +=1
        else:
            new_list.append(st[n-1]+str(count))
            count = 1
    new_list.append(st[-1]+str(count))
    return ''.join(new_list)
print(solution('aabccccaaa'))

########################################################################################################################
#Longest Substring with At Most K Distinct Characters

def solution(st,k):
    new_dict = {}
    left = 0
    max_len =0
    for right,val in enumerate(st):

        new_dict[val] = new_dict.get(val,0)+1

        while len(new_dict) > k:
            left_side = st[left]
            new_dict[left_side] -= 1
            if new_dict[left_side] == 0:
                del new_dict[left_side]
            left+=1
        max_len = max(max_len,right-left+1)
    return max_len

print(solution('eceba',2))
########################################################################################################################

from collections import Counter
#Find All Anagrams in a String
def solution(st,p):
    new_list = []
    for n in range(len(st)-len(p)):
        count =n+1
        while count<=n+len(p):
            count += 1
            if Counter(st[n:count]) == Counter(p):

                new_list.append(n)

    return new_list

print(solution('aba'*10,'abab'))
########################################################################################################################

# Substrings of Size K with K Distinct Characters
def solution(st,k):
    new_list = []
    for n in range(len(st)+1-k):
        new_list.append(st[n:n+k])
    return new_list

print(solution('awaglk',4))
########################################################################################################################

#Longest Repeating Character Replacement
def solution(st,k):
    max_len = 0
    left = 0
    new_dict = {}
    max_count = 0
    for right,val in enumerate(st):
        new_dict[val] = new_dict.get(val,0)+1
        max_count = max(max_count,new_dict[val])

        while (right-left+1) - max_count > k:
            new_dict[st[left]]-=1
            left+=1
        max_len = max(max_len,right-left+1)
    return max_len

print(solution('AABABBA',1))


########################################################################################################################
from collections import Counter

def min_window_substring(s, t):
    if not s or not t:
        return ""

    # Frequency of characters in t
    t_freq = Counter(t)
    required = len(t_freq)  # Number of unique characters in t that must be present in the window

    # Sliding window pointers
    left, right = 0, 0
    formed = 0  # To keep track of how many unique characters in t are matched in the window
    window_counts = {}
    min_len = float('inf')
    min_window = ""

    while right < len(s):
        # Add the current character to the window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # If the current character matches the required count in t, increase 'formed'
        if char in t_freq and window_counts[char] == t_freq[char]:
            formed += 1

        # Try to shrink the window from the left
        while left <= right and formed == required:
            # Update the minimum window if needed
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]

            # Remove the character at the left pointer from the window
            char = s[left]
            window_counts[char] -= 1
            if char in t_freq and window_counts[char] < t_freq[char]:
                formed -= 1

            left += 1  # Shrink the window

        # Expand the window by moving the right pointer
        right += 1

    return min_window

# Test the function
print(min_window_substring("ADOBACODEBANC", "ABC"))  # Output: "BANC"
########################################################################################################################

#Rotate the array by k #Clockwise
def solution(arr,k):
    return arr[-k:]+arr[:-k]

print(solution(['a', 'b', 'c', 'd', 'e'],2))
########################################################################################################################
#AntiCLockwise
def solution(arr,k):
    return arr[k:]+arr[:k]
print(solution(['a', 'b', 'c', 'd', 'e'],2))
########################################################################################################################
#Check if a string is present is another string
def solution(st1,st2):
    final_list = [[]]
    new_list = []
    if len(st2)>len(st1):
        return -1
    if st2 in st1:
        return True
    else:
        for n in st1:
            final_list += [m + [n] for m in final_list]
        for n in final_list:
            new_list.append(''.join(n))
        print(new_list)
        if st2 in new_list:
            return True
    return False


print(solution('abcd','bd'))
#**********************************************************************************************************************8
from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


    def color(self):
        return 'White'

class Dog(Animal):

    def sound(self):
        return 'Bark'

    def color(self):
        return 'Black'


# a = Animal()
# c = Dog()
# print(c.color())
# print(c.sound())
#***************************************************************************************************


class Dog:
    color = 'White'
    def __init__(self,sound,color):
        self.sound = sound
        self.color = color

    def sound_normal(self):
        return self.sound

    @classmethod
    def cls_color(cls):
        return cls.color

    @staticmethod
    def st_calculate(a,b):
        return a+b

# d = Dog('Meow','Black')
# print(d.color)
# print(d.st_calculate(10,20))
# print(d.sound_normal())

#**********************************************************************************************


def solution(*args,**kwargs):
    for n in args:
        print(n,end=" ")
    for m,n in kwargs.items():
        print(m+':'+n)

# print(solution(1,2,3,4,Dog='bark',Cat='Meow'))

#**********************************************************************************************


class Animal:
    def __init__(self,sound,color):
        self.sound = sound
        self.color = color

    def sound_met(self):
        return self.sound

    def colo_met(self):
        return self.color

class Dog(Animal):
    def __init__(self,sound,color,breed):
        super().__init__(sound,color)
        self.breed = breed

    def sound_met(self):
        return self.sound

    def colo_met(self):
        return self.color

    def breed_met(self):
        return self.breed

# a = Animal('Meow','White')
# print(a.colo_met())
# print(a.sound_met())
# d = Dog('Woof','Black','lab')
# print(d.colo_met())
# print(d.sound_met())
# print(d.breed_met())

#**********************************************************************************************


class Animal:
    def __init__(self,sound,color):
        self._sound = sound
        self.color = color

    def get_species(self):
        return self.__species

    def set_species(self,species):
        self.__species = species
    def _sound_met(self):
        return self._sound

    def __colo_met(self):
        return self.color

    def get_color(self):
        return self.__colo_met()
class Dog(Animal):
    def __init__(self,sound,color,breed):
        super().__init__(sound,color)
        self.breed = breed

    def sound_meth(self):
        return self._sound_met()

    def colo_met(self):
        return self.color

    def breed_met(self):
        return self.breed

a = Animal('Meow','White')
# print(a.set_species('GOlden'))
# print(a.get_species())
# print(a.get_color())
# print(a._sound_met())
# d = Dog('Woof','Black','lab')
# print(d.colo_met())
# print(d.sound_meth())
# print(d.breed_met())

#****************************************************************************************

def decorator(func):
    def wrapper(*args):
        result = func(*args)
        return result*0.5
    return wrapper

@decorator
def calculate(*args):
    result = 0
    for n in args:
        result+=n
    return result

# print(calculate(1,2,3,4,5,6))

#****************************************************************************************

def generator(arr):
    for n in arr:
        yield n
a = [1,2,3,4,5]
g = generator(a)
# for m in g:
    # print(m,end=" ")
#*****************************************************************************************


b = lambda x:x*2
a = [1,2,3,4,5,6]
# print(b(a))

c = list(map(lambda x:x*2,a))
# print(c)

d = list(filter(lambda x: x%2==0,a))
# print(d)


#****************************************************************************************

def solution(arr):
    for n in arr:
        match n:
            case 1:
                print('One')
            case 2:
                print('Two')
    return -1

# print(solution([3,4]))

#*******************************************************************************************

# a = [1,2,3,4]
# b = [5,6,7,8]
# for m in zip(a,b):
#     print(m)

#*****************************************************************************************

#REGEX
import re

def solution(email):
    pattern = r'^[a-zA-Z1-9_+.]+@[a-z]+\.[a-z]+$'
    result = re.match(pattern,email)
    if pattern:
        return 1
    else:
        return 2
# print(solution('karthick93@gmail.com'))

#****************************************************************************************

def solution1(st):
    pattern = r'\d{2}-\d{2}-\d{4}'
    result = re.findall(pattern,st)
    return result

# print(solution1('The event is on 25-12-2023 and 01-01-2024.'))

#******************************************************************************************

def phonenumber(pno):
    pattern = r'\d{3}-\d{3}-\d{4}'
    pattern1 = r'\(\d{3}\) \d{3}-\d{4}$'
    result = re.findall(pattern,pno)+re.findall(pattern1,pno)
    return result
# print(phonenumber('(123) 456-7890'))
# print(phonenumber('123-456-7890'))

#******************************************************************************************

def capital_letter(st):
    pattern = r'[A-Z][a-z]+'
    result = re.findall(pattern,st)
    return result

# def capital_letter(st):
#     pattern = r'\b\w*[A-Z]\w*\b'
#     result = re.findall(pattern, st)
#     return result
print(capital_letter('This is a Sample sentence with Some capitalized Words.'))

#******************************************************************************************

def extract_email(st):
    pattern = r'[a-zA-Z0-9+._/]+@[a-zA-Z]+\.[a-zA-Z]+'
    result = re.findall(pattern,st)
    return result
# print(extract_email('Please contact support@example.com or admin@company.com for more information.'))


#******************************************************************************************
