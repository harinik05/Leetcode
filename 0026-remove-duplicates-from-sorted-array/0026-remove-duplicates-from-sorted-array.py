class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #1. Insert index 
        insertIndex = 1
        
        #2. Check if the length of the list is empty, then return 0
        if len(nums) == 0:
            return 0
        
        #3. for loop to check for duplicates
        for i in range(0, len(nums)-1, 1):
            if nums[i]!=nums[i+1]:
                nums[insertIndex] = nums[i+1]
                insertIndex+=1
        
        return insertIndex