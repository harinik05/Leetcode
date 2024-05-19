class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1. Create a hashmap 
        hashmap = {}
        
        #2. Load up the keys with nums[i]
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        
        #3. Loop through the array again
        for j in range(len(nums)):
            complementSum = target-nums[j]
            if complementSum in hashmap.keys() and hashmap[complementSum]!=j:
                return [j,hashmap[complementSum]]
        return