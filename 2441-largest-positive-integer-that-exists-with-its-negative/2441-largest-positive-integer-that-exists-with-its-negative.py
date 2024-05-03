class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        #1. Sort the array 
        nums.sort()
        
        #2. Get the max each time - backwards for loop
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>0:
                try:
                    index = nums.index(-1*nums[i])
                except ValueError:
                    index=-1
                if index!=-1:
                    return nums[i]
            else:
                break
        
        return -1