class Solution:
    def reverse(self, nums, start, end):
        while start<end:
            nums[start], nums[end] = nums[end],nums[start]
            start+=1
            end-=1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        #1. reverse the entire thing
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        
       
        
        '''
        # First Solution - Not in place extra memory
        result = [0] * len(nums)  
        
        for i in range(len(nums)):
            indexToInsert = (i+k)%len(nums)
            result[indexToInsert] = nums[i]
        
        nums[:] = result
        '''
            
            
        
        