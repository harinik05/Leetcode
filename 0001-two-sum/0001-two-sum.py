class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #1. Initialize hashmap 
        hashmap = {}
        
        #2. Loop through all of them and put in the indices
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        #3. Do the step with the complements
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in hashmap and hashmap[complement]!=j:
                return [j,hashmap[complement]]
        return