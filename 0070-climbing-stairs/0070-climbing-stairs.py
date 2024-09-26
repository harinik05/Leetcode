class Solution:
    def __init__(self):
        #1. Initialize variables 
        self.MEMO = []
        self.DP = []
    
    #1. Climb Stairs Function
    def climbStairs(self, n: int) -> int:
        # DP array
        self.DP = ["*"] * (n+1)
        
        #base case
        self.DP[0] = 0
        self.DP[1] = 1
        if n>=2:
            self.DP[2] = 2
        
        for i in range(3, n+1):
            self.DP[i] = self.DP[i-1] + self.DP[i-2]
        
        return self.DP[n]
        
    def memoization(self, i):
        #a. Define some base cases
        if i == 0 or i == 1:
            return 1
        if self.MEMO[i] == "*":
            self.MEMO[i] = self.memoization(i-1) + self.memoization(i-2)
        return self.MEMO[i]
    #1. Top Down approach (Memoization Approach)
    def climbStairs_MEMO(self, n: int) -> int:
        #a. Define some common rules for memoization 
        self.MEMO = ["*"]*(n+1)
        
        #b. make the recursive call 
        return self.memoization(n)