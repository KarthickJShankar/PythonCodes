class Solution:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def GCD(self):
        if self.x ==1 and self.y==1:
            return 1
        for n in range(2,min(self.x,self.y)+1):
            if self.x%n ==0 and self.y%n == 0:
                return n
    def LCM(self):
        if self.x ==1 and self.y==1:
            return 1
        for n in range(1,min(self.x,self.y)):
            if max(self.x,self.y)*n % min(self.x,self.y)==0:
                return max(self.x,self.y)*n

s = Solution(1,1)
print(s.GCD())
print(s.LCM())