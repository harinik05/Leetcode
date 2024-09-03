class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #1. Create a hashmap 
        hashmap = defaultdict(int)
        
        #2. Fill up with frequencies 
        for number in nums:
            hashmap[number]+=1
        
        #3. Find the maximum elemenet 
        maxValue = -float('inf')
        returnKey = 0
        for key, values in hashmap.items():
            if values > maxValue:
                maxValue = values
                returnKey = key
            
        
        return returnKey
            
        
        