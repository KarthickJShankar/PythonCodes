import math

class Solution:
    def countSquares(self, N):
        # code here
        new_list = []
        divided_by = math.sqrt(N)
        return int(math.ceil(divided_by-1))
