import itertools
class Solution:
    def find(self,A,B):
        A = A+1
        for n in itertools.count(A):
            if n%B ==0:
                return n



c = Solution()
print(c.find(5,3))