class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #1. Base case 
        if len(nums) == 1:
            return nums[0]
        
        #2. Initialize the pointers for binary search 
        l = 0
        r = len(nums)-1
        
        # case 1 -> array is not rotated
        if nums[l] < nums[r]:
            return nums[l]
        
        #3. While loop 
        while l<r:
            mid = (l+r)//2
             #a. mid is too big?
            if nums[mid]>nums[0]:
                l = mid+1
            else:
                r = mid-1
            #b. compare the mid with the surrounding
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
             
           
            
          
            
        return nums[l]
                
            
            
            
        