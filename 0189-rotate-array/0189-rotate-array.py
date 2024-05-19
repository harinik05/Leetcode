class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First Solution - Not in place extra memory
        result = [0] * len(nums)  
        
        for i in range(len(nums)):
            indexToInsert = (i+k)%len(nums)
            result[indexToInsert] = nums[i]
        
        nums[:] = result
            
            
        
        