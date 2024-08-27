class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #1. Determine the length of nums array 
        ans = []
        length = len(nums)
        
        #2. Append stuff
        for num in nums:
            ans.append(num)
        
        for num in nums:
            ans.append(num)
        
        
        return ans 
        
        
            
        