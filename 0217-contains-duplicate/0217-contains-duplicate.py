class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #1. Create a set to store all the values
        seen = set()
        
        #2. loop through all elements and try to add to set
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False