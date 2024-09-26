class Solution:
    def __init__(self):
        #1. Initialize variables 
        self.MEMO = []
    
    def memoization(self, i):
        #a. Define some base cases
        if i == 0 or i == 1:
            return 1
        if self.MEMO[i] == "*":
            self.MEMO[i] = self.memoization(i-1) + self.memoization(i-2)
        return self.MEMO[i]
    #1. Top Down approach (Memoization Approach)
    def climbStairs(self, n: int) -> int:
        #a. Define some common rules for memoization 
        self.MEMO = ["*"]*(n+1)
        
        #b. make the recursive call 
        return self.memoization(n)