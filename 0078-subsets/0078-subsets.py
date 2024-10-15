class Solution(object):
    
    def __init__(self):
        self.subsetsArr = []
    def backtrackingFunction(self, index, nums, currentSubset):
        #pass
        
        
        
        
        #b. put everything from the currentsubset into subsetsarr
        self.subsetsArr.append(currentSubset[:])
        
        #c. go through the rest of the elements 
        for i in range(index, len(nums)):
            #a. Put in the current subset 
            currentSubset.append(nums[i])
            
            #b. call the backtracking 
            self.backtrackingFunction(i+1, nums, currentSubset)
            
            #c. pop the elemtn 
            currentSubset.pop()
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #self.subsetsArr = []
        self.backtrackingFunction(0,nums,[])
        return self.subsetsArr
        