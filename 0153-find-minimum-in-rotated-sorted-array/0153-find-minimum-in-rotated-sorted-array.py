class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #1. Initialize the setup of output
        outputMin = nums[0]
        
        #2. Loop through the whole thing
        for number in nums:
            outputMin = min(outputMin, number)
        
        return outputMin
        