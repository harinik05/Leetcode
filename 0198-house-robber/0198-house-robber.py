class Solution:
    def __init__(self):
        self.memo = []
    
    #Memoization method:
    def memoize(self, i, nums):
        #1. Base Case if i == 0
        if i==0:
            return nums[0]
        elif i==1:
            return max(self.memoize(0,nums), nums[1])
        
        #2. If i not in memo
        if self.memo[i] == -1:
            self.memo[i] = max(self.memoize(i-1, nums), self.memoize(i-2, nums) + nums[i])
        
        #3. Return the answer
        return self.memo[i]
            
    def rob(self, nums:List[int]) -> int:
        self.memo = [-1] *len(nums)
        #1. Memoize
        return self.memoize(len(nums)-1, nums)
        
    def rob_DP(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #a. Create the DP array 
        DP = [0] * len(nums)
        
        #b. Initialize the first two variables 
        DP[0] = nums[0]
        DP[1] = max(DP[0], nums[1])
        
        #c. Loop through the whole thing 
        for i in range(2, len(nums)):
            #a. Find the totalSum 
            totalSum = max(DP[i-2] + nums[i], DP[i-1])
            
            #b. Put in the Dp array 
            DP[i] = totalSum 
        
        return DP[-1]
        
        