class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #1. Initialize two variables (current and overall max sum)
        counterSum = 0
        overallMax = -float("inf")
        
        #2. for loop 
        for number in nums:
            counterSum += number
            
            #a. Update the overall Max
            overallMax = max(counterSum, overallMax);
            
            #b. Handle negative case of counterSum 
            if counterSum<0:
                counterSum = 0
        
        #3. return the overallMax value 
        return overallMax
        