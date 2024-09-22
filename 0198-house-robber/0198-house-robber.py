class Solution:
    def rob(self, nums: List[int]) -> int:
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
        
        