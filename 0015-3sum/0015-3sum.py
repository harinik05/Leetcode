class Solution:
    
    #1. constructor 
    def __init__(self):
        self.array = []
        
    #2. Helper function 
    def twoSumHelper(self, iVal, nums,lo,hi):
        #a. While loop
        while lo<hi:
            temp = iVal+nums[lo]+nums[hi]
            if temp<0:
                lo+=1
            if temp == 0:    
                self.array.append([iVal,nums[lo], nums[hi]])
                while(lo<hi and nums[lo]==nums[lo+1]):
                    lo+=1
                while(lo<hi and nums[hi] == nums[hi-1]):
                    hi-=1
                lo+=1
                hi-=1
                
            
            if temp>0:
                hi-=1
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #1. create a set 
        seen = set()
        nums.sort()
        
        #2. check if element in set
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                self.twoSumHelper(nums[i], nums, i+1, len(nums)-1)
                
        
        return self.array
        