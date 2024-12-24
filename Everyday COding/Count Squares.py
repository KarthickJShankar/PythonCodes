import math

class Solution:
    def countSquares(self, N):
        # code here
        new_list = []
        divided_by = math.sqrt(N)
        return round(divided_by)

s= Solution()
print(s.countSquares(22))